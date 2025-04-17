import MetaTrader5 as mt5
from datetime import datetime
import pandas as pd
import time
import logging
import signal
import sys

"""
ConectorMT5:
    Conecta ao MetaTrader 5 usando as credenciais fornecidas.
    Obtém o saldo disponível da conta e as posições abertas.
    Lida com a inicialização, desconexão e reconexão do MT5.

OperacaoTrade:
    Armazena informações sobre uma operação (ticket, símbolo, volume, preço de abertura, tipo, etc.).
    Calcula o lucro com base no preço atual do mercado.
    Inclui status de breakeven para rastrear se foi acionado.

GerenciadorPortfolio:
    Gerencia todas as operações ativas, sincronizando com as posições abertas no MT5.
    Implementa a estratégia de breakeven quando o preço se move a favor da operação (ex.: 200 pontos).
    Monitora ticks em tempo real para atualizações contínuas.

GerenciadorRisco:
    Calcula o tamanho da posição com base no risco máximo por operação (ex.: 2% do saldo).
    Limita o tamanho da posição para não exceder uma porcentagem do saldo (ex.: 10%).
    Considera a distância do stop-loss em pips e o valor do pip do símbolo.
"""

# Configuração do logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler('trading_log.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Função auxiliar para calcular o ATR
def calcular_atr(simbolo, timeframe=mt5.TIMEFRAME_H1, periodo=14):
    """Calcula o Average True Range (ATR) para o símbolo e período especificados."""
    if not mt5.initialize():
        logger.error("Falha ao inicializar o MT5 para calcular ATR")
        return None

    rates = mt5.copy_rates_from_pos(simbolo, timeframe, 0, periodo + 1)
    if rates is None or len(rates) < periodo:
        logger.error(f"Erro ao obter dados para {simbolo}: {mt5.last_error()}")
        return None

    df = pd.DataFrame(rates)
    df['high_low'] = df['high'] - df['low']
    df['high_close'] = abs(df['high'] - df['close'].shift())
    df['low_close'] = abs(df['low'] - df['close'].shift())
    df['tr'] = df[['high_low', 'high_close', 'low_close']].max(axis=1)
    
    atr = df['tr'].rolling(window=periodo).mean().iloc[-1]
    return atr

# Classe para conexão com o MetaTrader 5
class ConectorMT5:
    def __init__(self, conta, senha, servidor, timeout=30, max_tentativas_reconexao=5):
        self.conta = conta
        self.senha = senha
        self.servidor = servidor
        self.timeout = timeout
        self.max_tentativas_reconexao = max_tentativas_reconexao
        self.conectado = False

    def conectar(self):
        """Estabelece conexão com o MetaTrader 5."""
        if not mt5.initialize():
            logger.error("Falha ao inicializar o MT5")
            return False
        if not mt5.login(self.conta, password=self.senha, server=self.servidor, timeout=self.timeout):
            logger.error(f"Erro ao fazer login: {mt5.last_error()}")
            return False
        self.conectado = True
        logger.info("Conexão com MT5 estabelecida!")
        return True

    def desconectar(self):
        """Encerra a conexão com o MetaTrader 5."""
        mt5.shutdown()
        self.conectado = False
        logger.info("Desconectado do MT5")

    def reconectar(self):
        """Tenta reconectar ao MetaTrader 5 em caso de falha."""
        tentativas = 0
        while tentativas < self.max_tentativas_reconexao:
            logger.warning(f"Tentativa de reconexão {tentativas + 1}/{self.max_tentativas_reconexao}")
            if self.conectar():
                return True
            tentativas += 1
            time.sleep(5)  # Aguarda antes de tentar novamente
        logger.error("Falha ao reconectar após %d tentativas", self.max_tentativas_reconexao)
        return False

    def verificar_conexao(self):
        """Verifica se a conexão com o MT5 está ativa."""
        if not self.conectado or not mt5.account_info():
            logger.warning("Conexão perdida, tentando reconectar...")
            self.desconectar()
            return self.reconectar()
        return True

    def obter_saldo_conta(self):
        """Retorna o saldo disponível da conta."""
        if not self.verificar_conexao():
            return None
        info_conta = mt5.account_info()
        if info_conta:
            return info_conta.balance
        else:
            logger.error(f"Erro ao obter informações da conta: {mt5.last_error()}")
            return None

    def obter_posicoes_abertas(self):
        """Retorna a lista de posições abertas no MetaTrader 5."""
        if not self.verificar_conexao():
            return []
        posicoes = mt5.positions_get()
        if posicoes is None:
            logger.error(f"Erro ao obter posições: {mt5.last_error()}")
            return []
        return posicoes

# Classe para operação de trading
class OperacaoTrade:
    def __init__(self, ticket, simbolo, volume, preco_abertura, tipo_op, stop_loss=0, take_profit=0):
        self.ticket = ticket
        self.simbolo = simbolo
        self.volume = volume
        self.preco_abertura = preco_abertura
        self.tipo_op = tipo_op
        self.stop_loss = stop_loss
        self.take_profit = take_profit
        self.hora_abertura = datetime.now()
        self.lucro = 0.0
        self.breakeven_acionado = False

    def atualizar_lucro(self, preco_atual):
        """Atualiza o lucro da operação com base no preço atual."""
        info_simbolo = mt5.symbol_info(self.simbolo)
        if not info_simbolo:
            logger.error(f"Símbolo {self.simbolo} não encontrado ao atualizar lucro")
            return
        if self.tipo_op == 0:  # Compra
            self.lucro = (preco_atual - self.preco_abertura) * self.volume * info_simbolo.point
        else:  # Venda
            self.lucro = (self.preco_abertura - preco_atual) * self.volume * info_simbolo.point

    def __str__(self):
        return (f"Operação: {self.simbolo}, Ticket: {self.ticket}, Volume: {self.volume}, "
                f"Tipo: {'Compra' if self.tipo_op == 0 else 'Venda'}, Lucro: {self.lucro:.2f}, "
                f"Breakeven: {'Acionado' if self.breakeven_acionado else 'Não acionado'}")

# Classe para gerenciamento do portfólio
class GerenciadorPortfolio:
    def __init__(self, conector_mt5, risco_por_operacao=0.02, pontos_breakeven=200):
        self.conector_mt5 = conector_mt5
        self.operacoes = {}
        self.risco_por_operacao = risco_por_operacao
        self.lucro_total = 0.0
        self.pontos_breakeven = pontos_breakeven
        self.ativo = True  # Controla o loop de monitoramento

    def atualizar_portfolio(self):
        """Sincroniza as operações ativas e verifica/aplica o breakeven."""
        if not self.conector_mt5.verificar_conexao():
            logger.error("Não foi possível atualizar portfólio devido a falha de conexão")
            return

        posicoes = self.conector_mt5.obter_posicoes_abertas()
        self.operacoes.clear()
        for pos in posicoes:
            operacao = OperacaoTrade(
                ticket=pos.ticket,
                simbolo=pos.symbol,
                volume=pos.volume,
                preco_abertura=pos.price_open,
                tipo_op=pos.type,
                stop_loss=pos.sl,
                take_profit=pos.tp
            )
            tick = mt5.symbol_info_tick(pos.symbol)
            if not tick:
                logger.error(f"Erro ao obter tick para {pos.symbol}")
                continue
            preco_atual = tick.bid
            operacao.atualizar_lucro(preco_atual)
            self.operacoes[pos.ticket] = operacao
            self._verificar_breakeven(operacao, preco_atual)
        self._calcular_lucro_total()

    def _verificar_breakeven(self, operacao, preco_atual):
        """Verifica se o breakeven deve ser acionado e ajusta o stop-loss."""
        if operacao.breakeven_acionado:
            return

        info_simbolo = mt5.symbol_info(operacao.simbolo)
        if not info_simbolo:
            logger.error(f"Símbolo {operacao.simbolo} não encontrado")
            return

        ponto = info_simbolo.point
        movimento_pontos = 0
        if operacao.tipo_op == 0:  # Compra
            movimento_pontos = (preco_atual - operacao.preco_abertura) / ponto
        else:  # Venda
            movimento_pontos = (operacao.preco_abertura - preco_atual) / ponto

        if movimento_pontos >= self.pontos_breakeven:
            novo_stop_loss = operacao.preco_abertura
            self._ajustar_stop_loss(operacao, novo_stop_loss)
            operacao.breakeven_acionado = True
            logger.info(f"Breakeven acionado para {operacao.simbolo}, Ticket: {operacao.ticket}, Novo SL: {novo_stop_loss}")

    def _ajustar_stop_loss(self, operacao, novo_stop_loss):
        """Ajusta o stop-loss da operação no MetaTrader 5."""
        info_simbolo = mt5.symbol_info(operacao.simbolo)
        if not info_simbolo:
            logger.error(f"Símbolo {operacao.simbolo} não encontrado")
            return

        requisicao = {
            "action": mt5.TRADE_ACTION_SLTP,
            "position": operacao.ticket,
            "symbol": operacao.simbolo,
            "sl": round(novo_stop_loss, info_simbolo.digits),
            "tp": operacao.take_profit
        }

        resultado = mt5.order_send(requisicao)
        if resultado.retcode != mt5.TRADE_RETCODE_DONE:
            logger.error(f"Erro ao ajustar stop-loss para {operacao.simbolo}, Ticket: {operacao.ticket}: {resultado.comment}")
        else:
            operacao.stop_loss = novo_stop_loss
            logger.info(f"Stop-loss ajustado para {operacao.simbolo}, Ticket: {operacao.ticket}, Novo SL: {novo_stop_loss}")

    def _calcular_lucro_total(self):
        """Calcula o lucro total das operações ativas."""
        self.lucro_total = sum(operacao.lucro for operacao in self.operacoes.values())

    def adicionar_operacao(self, simbolo, volume, tipo_op, stop_loss=0, take_profit=0):
        """Adiciona uma nova operação ao portfólio."""
        if not self.conector_mt5.verificar_conexao():
            logger.error("Não foi possível adicionar operação devido a falha de conexão")
            return False

        saldo = self.conector_mt5.obter_saldo_conta()
        if not saldo:
            logger.error("Não foi possível obter o saldo para abrir a operação")
            return False

        info_simbolo = mt5.symbol_info(simbolo)
        if not info_simbolo:
            logger.error(f"Símbolo {simbolo} não encontrado")
            return False

        preco = mt5.symbol_info_tick(simbolo).ask if tipo_op == 0 else mt5.symbol_info_tick(simbolo).bid

        requisicao = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": simbolo,
            "volume": volume,
            "type": mt5.ORDER_TYPE_BUY if tipo_op == 0 else mt5.ORDER_TYPE_SELL,
            "price": preco,
            "sl": stop_loss,
            "tp": take_profit,
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }

        resultado = mt5.order_send(requisicao)
        if resultado.retcode != mt5.TRADE_RETCODE_DONE:
            logger.error(f"Erro ao enviar ordem para {simbolo}: {resultado.comment}")
            return False

        operacao = OperacaoTrade(resultado.deal, simbolo, volume, preco, tipo_op, stop_loss, take_profit)
        self.operacoes[resultado.deal] = operacao
        logger.info(f"Operação adicionada: {operacao}")
        return True

    def obter_resumo_portfolio(self):
        """Retorna um resumo do portfólio."""
        self.atualizar_portfolio()
        resumo = f"Portfólio - Total de Operações: {len(self.operacoes)}, Lucro Total: {self.lucro_total:.2f}\n"
        for operacao in self.operacoes.values():
            resumo += str(operacao) + "\n"
        return resumo

    def monitorar_mercado(self, intervalo_atualizacao=1):
        """Monitora o mercado em tempo real e atualiza o portfólio."""
        logger.info("Iniciando monitoramento do mercado...")
        while self.ativo:
            try:
                self.atualizar_portfolio()
                logger.debug(self.obter_resumo_portfolio())
                time.sleep(intervalo_atualizacao)  # Controla a frequência de atualização
            except Exception as e:
                logger.error(f"Erro durante monitoramento: {str(e)}")
                if not self.conector_mt5.reconectar():
                    logger.critical("Falha crítica de conexão, encerrando monitoramento")
                    self.ativo = False
            except KeyboardInterrupt:
                logger.info("Interrupção recebida, encerrando monitoramento...")
                self.ativo = False

# Classe para gerenciamento de risco
class GerenciadorRisco:
    def __init__(self, risco_maximo_percent=0.02, tamanho_maximo_posicao=0.1, multiplicador_atr=2.0):
        self.risco_maximo_percent = risco_maximo_percent
        self.tamanho_maximo_posicao = tamanho_maximo_posicao
        self.multiplicador_atr = multiplicador_atr

    def calcular_stop_loss(self, simbolo, preco_entrada, tipo_op, timeframe=mt5.TIMEFRAME_H1, periodo=14):
        """Calcula o stop-loss com base no ATR."""
        atr = calcular_atr(simbolo, timeframe, periodo)
        if atr is None:
            logger.error("Não foi possível calcular o ATR")
            return 0

        info_simbolo = mt5.symbol_info(simbolo)
        if not info_simbolo:
            logger.error(f"Símbolo {simbolo} não encontrado")
            return 0

        if tipo_op == 0:  # Compra
            stop_loss = preco_entrada - (self.multiplicador_atr * atr)
        else:  # Venda
            stop_loss = preco_entrada + (self.multiplicador_atr * atr)

        stop_loss = round(stop_loss, info_simbolo.digits)
        return stop_loss

    def calcular_tamanho_posicao(self, saldo, preco_entrada, stop_loss, simbolo):
        """Calcula o tamanho da posição com base no risco."""
        if stop_loss == 0:
            logger.error("Stop-loss não definido")
            return 0

        info_simbolo = mt5.symbol_info(simbolo)
        if not info_simbolo:
            logger.error(f"Símbolo {simbolo} não encontrado")
            return 0

        ponto = info_simbolo.point
        valor_risco = saldo * self.risco_maximo_percent
        valor_pip = info_simbolo.trade_tick_value
        distancia_pip = abs(preco_entrada - stop_loss) / ponto
        if distancia_pip == 0:
            logger.error("Distância do stop-loss inválida")
            return 0

        volume = valor_risco / (distancia_pip * valor_pip)
        volume_maximo = (saldo * self.tamanho_maximo_posicao) / (preco_entrada * valor_pip)
        return min(volume, volume_maximo)

# Manipulador de sinal para interrupção segura
def sinal_handler(sig, frame):
    logger.info("Sinal de interrupção recebido, encerrando...")
    global portfolio
    portfolio.ativo = False
    portfolio.conector_mt5.desconectar()
    sys.exit(0)

# Exemplo de uso em ambiente real
if __name__ == "__main__":
    # Configura o manipulador de sinal
    signal.signal(signal.SIGINT, sinal_handler)

    # Configurações de conexão com o MT5
    conta = 123456  # Substitua pelo número da sua conta
    senha = "sua_senha"  # Substitua pela sua senha
    servidor = "sua_corretora"  # Substitua pelo servidor da sua corretora

    # Inicializa o conector MT5
    conector_mt5 = ConectorMT5(conta, senha, servidor)
    if not conector_mt5.conectar():
        logger.critical("Falha ao conectar ao MT5, encerrando...")
        sys.exit(1)

    # Inicializa o gerenciador de portfólio e risco
    portfolio = GerenciadorPortfolio(conector_mt5, risco_por_operacao=0.02, pontos_breakeven=200)
    gerenciador_risco = GerenciadorRisco(risco_maximo_percent=0.02, tamanho_maximo_posicao=0.1, multiplicador_atr=2.0)

    # Exemplo: Abre uma operação
    saldo = conector_mt5.obter_saldo_conta()
    if not saldo:
        logger.critical("Não foi possível obter o saldo, encerrando...")
        conector_mt5.desconectar()
        sys.exit(1)

    simbolo = "EURUSD"
    tipo_op = 0  # Compra
    preco_entrada = mt5.symbol_info_tick(simbolo).ask

    stop_loss = gerenciador_risco.calcular_stop_loss(simbolo, preco_entrada, tipo_op)
    if stop_loss == 0:
        logger.error("Não foi possível calcular o stop-loss")
        conector_mt5.desconectar()
        sys.exit(1)

    volume = gerenciador_risco.calcular_tamanho_posicao(saldo, preco_entrada, stop_loss, simbolo)
    if volume <= 0:
        logger.error("Tamanho da posição inválido")
        conector_mt5.desconectar()
        sys.exit(1)

    take_profit = preco_entrada + 2 * abs(preco_entrada - stop_loss) if tipo_op == 0 else preco_entrada - 2 * abs(preco_entrada - stop_loss)

    if portfolio.adicionar_operacao(simbolo, volume, tipo_op, stop_loss, take_profit):
        logger.info("Operação aberta com sucesso, iniciando monitoramento...")
        print(portfolio.obter_resumo_portfolio())
    else:
        logger.error("Falha ao abrir operação, encerrando...")
        conector_mt5.desconectar()
        sys.exit(1)

    # Inicia o monitoramento do mercado
    portfolio.monitorar_mercado(intervalo_atualizacao=1)

    # Desconecta ao encerrar
    conector_mt5.desconectar()