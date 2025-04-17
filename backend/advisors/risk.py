import MetaTrader5 as mt5
import pandas as pd
import logging

logger = logging.getLogger(__name__)

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