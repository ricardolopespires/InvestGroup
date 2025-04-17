import MetaTrader5 as mt5
from datetime import datetime
import pandas as pd
import time
import logging
import signal
import sys
import random
from crewai import Agent, Task, Crew
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Carrega variáveis de ambiente
load_dotenv()

# Configuração do logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler('trading_log_crewai.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Configuração do LLM com Google Gemini
api_key = os.getenv("GOOGLE_API_KEY")
model_name = os.getenv("MODEL", "gemini-pro")

default_llm = ChatGoogleGenerativeAI(
    google_api_key=api_key,
    model=model_name
)

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

# Função simulada para gerar sinais de mercado
def gerar_sinal_mercado(simbolo):
    """Gera um sinal de mercado simulado ('buy', 'sell', ou 'hold')."""
    # Simulação: escolhe aleatoriamente um sinal para demonstração
    sinais = ['buy', 'sell', 'hold']
    sinal = random.choice(sinais)
    logger.info(f"Sinal gerado para {simbolo}: {sinal}")
    return sinal

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
        mt5.shutdown()
        self.conectado = False
        logger.info("Desconectado do MT5")

    def reconectar(self):
        tentativas = 0
        while tentativas < self.max_tentativas_reconexao:
            logger.warning(f"Tentativa de reconexão {tentativas + 1}/{self.max_tentativas_reconexao}")
            if self.conectar():
                return True
            tentativas += 1
            time.sleep(5)
        logger.error("Falha ao reconectar após %d tentativas", self.max_tentativas_reconexao)
        return False

    def verificar_conexao(self):
        if not self.conectado or not mt5.account_info():
            logger.warning("Conexão perdida, tentando reconectar...")
            self.desconectar()
            return self.reconectar()
        return True

    def obter_saldo_conta(self):
        if not self.verificar_conexao():
            return None
        info_conta = mt5.account_info()
        if info_conta:
            return info_conta.balance
        else:
            logger.error(f"Erro ao obter informações da conta: {mt5.last_error()}")
            return None

    def obter_posicoes_abertas(self):
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
    def __init__(self, conector_mt5, risco_por_operacao=0.02, pontos_breakeven=200, risco_maximo_total=0.1):
        self.conector_mt5 = conector_mt5
        self.operacoes = {}
        self.risco_por_operacao = risco_por_operacao
        self.pontos_breakeven = pontos_breakeven
        self.risco_maximo_total = risco_maximo_total
        self.lucro_total = 0.0
        self.ativo = True

    def atualizar_portfolio(self):
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
                preco_novo=pos.price_open,
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
        self.lucro_total = sum(operacao.lucro for operacao in self.operacoes.values())

    def adicionar_operacao(self, simbolo, volume, tipo_op, stop_loss=0, take_profit=0):
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

    def fechar_operacao(self, ticket):
        """Fecha uma operação existente pelo ticket."""
        if not self.conector_mt5.verificar_conexao():
            logger.error("Não foi possível fechar operação devido a falha de conexão")
            return False

        operacao = self.operacoes.get(ticket)
        if not operacao:
            logger.error(f"Operação com ticket {ticket} não encontrada")
            return False

        info_simbolo = mt5.symbol_info(operacao.simbolo)
        if not info_simbolo:
            logger.error(f"Símbolo {operacao.simbolo} não encontrado")
            return False

        preco = mt5.symbol_info_tick(operacao.simbolo).bid if operacao.tipo_op == 0 else mt5.symbol_info_tick(operacao.simbolo).ask

        requisicao = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": operacao.simbolo,
            "volume": operacao.volume,
            "type": mt5.ORDER_TYPE_SELL if operacao.tipo_op == 0 else mt5.ORDER_TYPE_BUY,
            "position": ticket,
            "price": preco,
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }

        resultado = mt5.order_send(requisicao)
        if resultado.retcode != mt5.TRADE_RETCODE_DONE:
            logger.error(f"Erro ao fechar operação {ticket}: {resultado.comment}")
            return False

        logger.info(f"Operação fechada: {operacao}")
        del self.operacoes[ticket]
        return True

    def adicionar_multiplas_operacoes(self, operacoes):
        operacoes_adicionadas = []
        saldo = self.conector_mt5.obter_saldo_conta()
        if not saldo:
            logger.error("Não foi possível obter o saldo para abrir operações")
            return False

        risco_atual = self.calcular_risco_acumulado(saldo)
        if risco_atual >= self.risco_maximo_total:
            logger.warning("Risco acumulado excede o limite máximo (%s%%)", self.risco_maximo_total * 100)
            return False

        for op in operacoes:
            simbolo = op.get("simbolo")
            tipo_op = op.get("tipo_op", 0)
            volume = op.get("volume", 0)
            stop_loss = op.get("stop_loss", 0)
            take_profit = op.get("take_profit", 0)

            risco_operacao = self._calcular_risco_operacao(saldo, simbolo, volume, stop_loss)
            if risco_atual + risco_operacao > self.risco_maximo_total:
                logger.warning(f"Operação em {simbolo} não adicionada: risco acumulado excederia o limite")
                continue

            if self.adicionar_operacao(simbolo, volume, tipo_op, stop_loss, take_profit):
                operacoes_adicionadas.append(simbolo)
                risco_atual += risco_operacao
            else:
                logger.error(f"Falha ao adicionar operação em {simbolo}")

        return operacoes_adicionadas

    def _calcular_risco_operacao(self, saldo, simbolo, volume, stop_loss):
        if stop_loss == 0:
            return 0
        info_simbolo = mt5.symbol_info(simbolo)
        if not info_simbolo:
            return 0
        preco = mt5.symbol_info_tick(simbolo).ask
        ponto = info_simbolo.point
        valor_pip = info_simbolo.trade_tick_value
        distancia_pip = abs(preco - stop_loss) / ponto
        risco = (distancia_pip * valor_pip * volume) / saldo
        return risco

    def calcular_risco_acumulado(self, saldo):
        risco_total = 0
        for operacao in self.operacoes.values():
            risco_total += self._calcular_risco_operacao(saldo, operacao.simbolo, operacao.volume, operacao.stop_loss)
        return risco_total

    def obter_resumo_portfolio(self):
        self.atualizar_portfolio()
        resumo = f"Portfólio - Total de Operações: {len(self.operacoes)}, Lucro Total: {self.lucro_total:.2f}\n"
        for operacao in self.operacoes.values():
            resumo += str(operacao) + "\n"
        return resumo

    def monitorar_mercado(self, intervalo_atualizacao=1):
        logger.info("Iniciando monitoramento do mercado...")
        while self.ativo:
            try:
                self.atualizar_portfolio()
                logger.debug(self.obter_resumo_portfolio())
                time.sleep(intervalo_atualizacao)
            except Exception as e:
                logger.error(f"Erro durante monitoramento: {str(e)}")
                if not self.conector_mt5.reconectar():
                    logger.critical("Falha crítica de conexão, encerrando monitoramento")
                    self.ativo = False
            except KeyboardInterrupt:
                logger.info("Interrupção recebida, encerrando monitoramento...")
                self.ativo = False

    def processar_sinal(self, simbolo, sinal, gerenciador_risco):
        """Processa um sinal de mercado e toma decisões."""
        saldo = self.conector_mt5.obter_saldo_conta()
        if not saldo:
            logger.error("Não foi possível obter o saldo")
            return False

        # Verifica operações existentes para o símbolo
        operacoes_simbolo = [op for op in self.operacoes.values() if op.simbolo == simbolo]
        tipo_op_sinal = 0 if sinal == "buy" else 1 if sinal == "sell" else None

        if sinal == "hold":
            logger.info(f"Manter posições atuais para {simbolo}")
            return True

        if operacoes_simbolo:
            for op in operacoes_simbolo:
                if tipo_op_sinal is not None and op.tipo_op != tipo_op_sinal:
                    # Fecha a operação se o sinal for oposto
                    self.fechar_operacao(op.ticket)
                    logger.info(f"Operação oposta fechada para {simbolo}, Ticket: {op.ticket}")

        if tipo_op_sinal is not None:
            # Abre nova operação se não houver uma operação aberta ou se a anterior foi fechada
            tick = mt5.symbol_info_tick(simbolo)
            if not tick:
                logger.error(f"Erro ao obter tick para {simbolo}")
                return False
            preco_entrada = tick.ask if tipo_op_sinal == 0 else tick.bid

            stop_loss = gerenciador_risco.calcular_stop_loss(simbolo, preco_entrada, tipo_op_sinal)
            if stop_loss == 0:
                logger.error(f"Não foi possível calcular o stop-loss para {simbolo}")
                return False

            volume = gerenciador_risco.calcular_tamanho_posicao(saldo, preco_entrada, stop_loss, simbolo)
            if volume <= 0:
                logger.error(f"Tamanho da posição inválido para {simbolo}")
                return False

            take_profit = (preco_entrada + 2 * abs(preco_entrada - stop_loss) if tipo_op_sinal == 0
                           else preco_entrada - 2 * abs(preco_entrada - stop_loss))

            operacao = {
                "simbolo": simbolo,
                "tipo_op": tipo_op_sinal,
                "volume": volume,
                "stop_loss": stop_loss,
                "take_profit": take_profit
            }

            if self.adicionar_multiplas_operacoes([operacao]):
                logger.info(f"Nova operação aberta para {simbolo}: {sinal}")
                return True
            else:
                logger.error(f"Falha ao abrir nova operação para {simbolo}")
                return False

        return True

# Classe para gerenciamento de risco
class GerenciadorRisco:
    def __init__(self, risco_maximo_percent=0.02, tamanho_maximo_posicao=0.1, multiplicador_atr=2.0):
        self.risco_maximo_percent = risco_maximo_percent
        self.tamanho_maximo_posicao = tamanho_maximo_posicao
        self.multiplicador_atr = multiplicador_atr

    def calcular_stop_loss(self, simbolo, preco_entrada, tipo_op, timeframe=mt5.TIMEFRAME_H1, periodo=14):
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

# Definindo o agente trader
trader = Agent(
    role="Trader",
    goal=(
        "Realizar operações de compra, venda ou manter posição em ativos financeiros. "
        "Utilize os sinais 'buy' e 'sell' para tomar decisões. "
        "Se a operação atual for diferente do sinal recebido, feche a posição e abra uma nova conforme o sinal. "
        "Caso o sinal seja igual à posição atual, mantenha a operação aberta."
    ),
    tools=[],
    llm=default_llm,
    backstory="Você é um trader experiente, especialista em executar estratégias automatizadas de negociação."
)

# Definindo a tarefa do trader
class TradingTask(Task):
    def __init__(self, portfolio, gerenciador_risco, simbolos, intervalo_minutos=5):
        super().__init__(
            description=(
                f"Monitore o mercado a cada {intervalo_minutos} minutos para os símbolos {simbolos}. "
                "Obtenha sinais de mercado ('buy', 'sell', ou 'hold') e tome decisões: "
                "abra novas posições, feche posições opostas, ou mantenha posições atuais."
            ),
            expected_output="Executar ou manter operações de acordo com os sinais.",
            agent=trader
        )
        self.portfolio = portfolio
        self.gerenciador_risco = gerenciador_risco
        self.simbolos = simbolos
        self.intervalo_minutos = intervalo_minutos

    def execute(self):
        """Executa a tarefa de monitoramento e decisão."""
        logger.info(f"Executando tarefa de trading para {self.simbolos}")
        for simbolo in self.simbolos:
            sinal = gerar_sinal_mercado(simbolo)  # Substitua por uma fonte real de sinais
            resultado = self.portfolio.processar_sinal(simbolo, sinal, self.gerenciador_risco)
            if not resultado:
                logger.error(f"Falha ao processar sinal para {simbolo}")
        return self.portfolio.obter_resumo_portfolio()

# Manipulador de sinal para interrupção segura
def sinal_handler(sig, frame):
    logger.info("Sinal de interrupção recebido, encerrando...")
    global portfolio
    portfolio.ativo = False
    portfolio.conector_mt5.desconectar()
    sys.exit(0)

# Exemplo de uso com CrewAI
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
    portfolio = GerenciadorPortfolio(conector_mt5, risco_por_operacao=0.02, pontos_breakeven=200, risco_maximo_total=0.1)
    gerenciador_risco = GerenciadorRisco(risco_maximo_percent=0.02, tamanho_maximo_posicao=0.1, multiplicador_atr=2.0)

    # Símbolos a serem monitorados
    simbolos = ["EURUSD", "GBPUSD", "USDJPY"]

    # Cria a tarefa de trading
    trader_task = TradingTask(portfolio, gerenciador_risco, simbolos, intervalo_minutos=5)

    # Cria a equipe de execução
    crew = Crew(
        agents=[trader],
        tasks=[trader_task]
    )

    # Inicia o monitoramento em tempo real em uma thread separada
    import threading
    monitoramento_thread = threading.Thread(target=portfolio.monitorar_mercado, args=(1,))
    monitoramento_thread.daemon = True
    monitoramento_thread.start()

    # Loop principal para executar a tarefa a cada 5 minutos
    logger.info("Iniciando loop principal de execução da tarefa...")
    while portfolio.ativo:
        try:
            resultado = crew.kickoff()  # Executa a tarefa
            logger.info(f"Resultado da tarefa:\n{resultado}")
            time.sleep(5 * 60)  # Aguarda 5 minutos
        except Exception as e:
            logger.error(f"Erro durante execução da tarefa: {str(e)}")
            if not portfolio.conector_mt5.reconectar():
                logger.critical("Falha crítica de conexão, encerrando...")
                portfolio.ativo = False
        except KeyboardInterrupt:
            logger.info("Interrupção recebida, encerrando...")
            portfolio.ativo = False

    # Desconecta ao encerrar
    portfolio.conector_mt5.desconectar()