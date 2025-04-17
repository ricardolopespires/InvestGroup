import MetaTrader5 as mt5
import logging
from ..models.trade_operation import OperacaoTrade

logger = logging.getLogger(__name__)

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
        saldo = self.conector_mt5.obter_saldo_conta()
        if not saldo:
            logger.error("Não foi possível obter o saldo")
            return False

        operacoes_simbolo = [op for op in self.operacoes.values() if op.simbolo == simbolo]
        tipo_op_sinal = 0 if sinal == "buy" else 1 if sinal == "sell" else None

        if sinal == "hold":
            logger.info(f"Manter posições atuais para {simbolo}")
            return True

        if operacoes_simbolo:
            for op in operacoes_simbolo:
                if tipo_op_sinal is not None and op.tipo_op != tipo_op_sinal:
                    self.fechar_operacao(op.ticket)
                    logger.info(f"Operação oposta fechada para {simbolo}, Ticket: {op.ticket}")

        if tipo_op_sinal is not None:
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