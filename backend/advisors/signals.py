import MetaTrader5 as mt5
import pandas as pd
import numpy as np
import talib as ta
from scipy.signal import find_peaks, savgol_filter
import logging
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

class Signals:
    def __init__(self, conta, senha, servidor, timeout=30):
        self.conta = conta
        self.senha = senha
        self.servidor = servidor
        self.timeout = timeout
        self.dataset = None
        self.symbol = None
        self.timeframe = None

    def initialize_mt5(self):
        """Inicializa a conexão com o MetaTrader 5."""
        if not mt5.initialize():
            logger.error("Falha ao inicializar o MT5")
            return False
        return True

    def login(self):
        """Realiza o login no MetaTrader 5."""
        if not mt5.login(self.conta, password=self.senha, server=self.servidor, timeout=self.timeout):
            logger.error(f"Erro ao fazer login: {mt5.last_error()}")
            return False
        logger.info("Login no MT5 realizado com sucesso")
        return True

    def set_interval(self, timeframe):
        """Configura o timeframe para download de dados."""
        timeframe_map = {
            '1wk': mt5.TIMEFRAME_W1,
            '1d': mt5.TIMEFRAME_D1,
            '4h': mt5.TIMEFRAME_H4,
            '1h': mt5.TIMEFRAME_H1,
            '15m': mt5.TIMEFRAME_M15,
            '5m': mt5.TIMEFRAME_M5,
            '1m': mt5.TIMEFRAME_M1
        }
        if timeframe not in timeframe_map:
            raise ValueError(f"Timeframe {timeframe} não suportado")
        self.timeframe = timeframe_map[timeframe]

    def download_data(self, bars=1000):
        """Baixa dados históricos do símbolo para o timeframe configurado."""
        if not self.symbol or not self.timeframe:
            raise ValueError("Símbolo ou timeframe não configurado")
        
        rates = mt5.copy_rates_from_pos(self.symbol, self.timeframe, 0, bars)
        if rates is None or len(rates) == 0:
            logger.error(f"Erro ao obter dados para {self.symbol}: {mt5.last_error()}")
            return
        
        self.dataset = pd.DataFrame(rates)
        self.dataset['time'] = pd.to_datetime(self.dataset['time'], unit='s')
        self.dataset.set_index('time', inplace=True)
        logger.info(f"Dados baixados para {self.symbol} no timeframe {self.timeframe}")

    def preprocess_data(self):
        """Pré-processa os dados, garantindo que estejam no formato correto."""
        if self.dataset is None:
            raise ValueError("Os dados ainda não foram baixados")
        
        required_columns = ['open', 'high', 'low', 'close', 'tick_volume', 'spread', 'real_volume']
        if not all(col in self.dataset.columns for col in required_columns):
            raise ValueError("Dados incompletos: colunas obrigatórias ausentes")
        
        self.dataset = self.dataset[required_columns]
        logger.info("Dados pré-processados com sucesso")

    def calculate_indicators(self, atr_period=14, atr_smoothing_window=30, smooth_window=49, smooth_polyorder=5):
        """Calcula indicadores técnicos como ATR e suavização de preços."""
        if self.dataset is None:
            raise ValueError("Os dados ainda não foram baixados.")
        
        self.dataset["atr"] = ta.ATR(self.dataset.high, self.dataset.low, self.dataset.close, timeperiod=atr_period)
        self.dataset["atr"] = self.dataset["atr"].rolling(window=atr_smoothing_window).mean()
        self.dataset["close_smooth"] = savgol_filter(self.dataset.close, smooth_window, smooth_polyorder)
        self.dataset['atr'] = self.dataset['atr'].fillna(0).astype(int)
        logger.info("Indicadores técnicos calculados.")
        
        return self.dataset

    def calculate_signals(self, distance=15, width=3):
        """Calcula sinais de compra e venda baseados em picos e vales."""
        if self.dataset is None or "close_smooth" not in self.dataset.columns:
            raise ValueError("Os indicadores ainda não foram calculados.")
        
        atr = self.dataset["atr"].iloc[-1] if not pd.isna(self.dataset["atr"].iloc[-1]) else 1.0
        peaks_idx, _ = find_peaks(self.dataset.close_smooth, distance=distance, width=width, prominence=atr)
        troughs_idx, _ = find_peaks(-self.dataset.close_smooth, distance=distance, width=width, prominence=atr)

        self.dataset['signal'] = np.nan
        self.dataset['signal'] = self.dataset['signal'].astype(object)

        self.dataset.loc[self.dataset.index[peaks_idx], 'signal'] = 'sell'
        self.dataset.loc[self.dataset.index[troughs_idx], 'signal'] = 'buy'

        signals = []
        for idx in peaks_idx:
            time = int(self.dataset.index[idx].timestamp())
            price = self.dataset.close.iloc[idx]
            signals.append({
                "time": time,
                "position": "aboveBar",
                "color": "#e91e63",
                "shape": "arrowDown",
                "text": f"Sell @ {price:.2f}",
                "type": "sell",
                "size": 2
            })

        for idx in troughs_idx:
            time = int(self.dataset.index[idx].timestamp())
            price = self.dataset.close.iloc[idx]
            signals.append({
                "time": time,
                "position": "belowBar",
                "color": "#2196F3",
                "shape": "arrowUp",
                "text": f"Buy @ {price:.2f}",
                "type": "buy",
                "size": 2
            })
        
        self.dataset["signal"] = self.dataset["signal"].fillna(0).astype("string")
        self.dataset.drop(["tick_volume", "spread", "real_volume", "atr", "close_smooth"], axis=1, inplace=True, errors='ignore')
        logger.info("Sinais de compra e venda calculados.")
        return signals
    
    def get_last_signal_by_timeframes(self, symbol, timeframes=['1wk', '1d', '4h'], type=None):
        """Obtém o último sinal de compra ou venda para os timeframes especificados."""
        if not self.initialize_mt5():
            raise ConnectionError("Não foi possível inicializar o MetaTrader5.")
        
        if not self.login():
            raise ConnectionError("Não foi possível realizar o login no MetaTrader5.")
        
        last_signals = []
        
        for timeframe in timeframes:
            if type == "stock":
                self.symbol = "#" + symbol
            else:
                self.symbol = symbol              
            self.set_interval(timeframe)
            
            self.download_data()
            self.preprocess_data()
            self.calculate_indicators()
            self.calculate_signals()
            
            signals_df = self.dataset[self.dataset['signal'].isin(['buy', 'sell'])].copy()
            
            if not signals_df.empty:
                last_signal = signals_df.tail(1).iloc[0]
                last_signals.append({
                    'timeframe': timeframe,
                    'time': last_signal.name,
                    'signal': last_signal['signal'],
                    'price': last_signal['close']
                })
            else:
                last_signals.append({
                    'timeframe': timeframe,
                    'time': None,
                    'signal': 'Nenhum sinal encontrado',
                    'price': None
                })
        
        result_df = pd.DataFrame(last_signals)
        logger.info("Últimos sinais calculados para os timeframes especificados.")
        return result_df