import MetaTrader5 as mt5
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

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