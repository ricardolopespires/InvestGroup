import yfinance as yf
import pandas as pd
import numpy as np
from scipy.signal import savgol_filter, find_peaks
import pandas_ta as ta

class FinancialDataAnalyzer:
    VALID_PERIODS = ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
    VALID_INTERVALS = ['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo']

    def __init__(self, symbol, period="5y", interval=""):
        """Inicializa o analisador de dados financeiros."""
        self.symbol = symbol
        self.set_period(period)
        self.set_interval(interval)
        self.dataset = None

    def set_period(self, period):
        """Valida e define o período."""
        if period not in self.VALID_PERIODS:
            raise ValueError(f"Período inválido. Períodos suportados: {', '.join(self.VALID_PERIODS)}")
        self.period = period

    def set_interval(self, interval):
        """Valida e define o intervalo."""
        if interval not in self.VALID_INTERVALS:
            raise ValueError(f"Intervalo inválido. Intervalos suportados: {', '.join(self.VALID_INTERVALS)}")
        self.interval = interval

    def download_data(self):
        """Baixa os dados do Yahoo Finance."""
        try:
            self.dataset = yf.download(self.symbol, period=self.period, interval=self.interval)
            if self.dataset.shape[0] == 0:
                raise ValueError(f"Não há dados disponíveis para o símbolo '{self.symbol}' com período '{self.period}' e intervalo '{self.interval}'.")
            if isinstance(self.dataset.columns, pd.MultiIndex):
                self.dataset.columns = self.dataset.columns.get_level_values(0).str.lower()
            else:
                self.dataset.columns = self.dataset.columns.str.lower()
        except Exception as e:
            raise Exception(f"Erro ao baixar dados do Yahoo Finance: {str(e)}")

    def preprocess_data(self, fill_method="ffill"):
        """Pré-processa os dados, convertendo tipos, arredondando valores e tratando dados ausentes."""
        if self.dataset is None:
            raise Exception("Os dados ainda não foram baixados. Execute download_data primeiro.")
        self.dataset['open'] = self.dataset.open.astype(float)
        self.dataset['high'] = self.dataset.high.astype(float)
        self.dataset['low'] = self.dataset.low.astype(float)
        self.dataset['close'] = self.dataset.close.astype(float)
        if fill_method == "ffill":
            self.dataset.fillna(method="ffill", inplace=True)
        elif fill_method == "drop":
            self.dataset.dropna(inplace=True)
        else:
            raise ValueError(f"Método de preenchimento '{fill_method}' não suportado. Use 'ffill' ou 'drop'.")
        self.dataset = self.dataset.round(2)

    def calculate_indicators(self, atr_period=14, atr_smoothing_window=30, smooth_window=49, smooth_polyorder=5, additional_indicators=None):
        """Calcula indicadores técnicos como ATR, suavização de preços e outros configuráveis."""
        if self.dataset is None:
            raise Exception("Os dados ainda não foram baixados. Execute download_data primeiro.")
        self.dataset["atr"] = ta.atr(high=self.dataset.high, low=self.dataset.low, close=self.dataset.close, length=atr_period)
        self.dataset["atr"] = self.dataset.atr.rolling(window=atr_smoothing_window).mean()
        self.dataset["close_smooth"] = savgol_filter(self.dataset.close, smooth_window, smooth_polyorder)
        if additional_indicators:
            for indicator in additional_indicators:
                if indicator.lower() == "rsi":
                    self.dataset["rsi"] = ta.rsi(self.dataset.close)

    def calculate_signals(self, distance=15, width=3):
        """Calcula sinais de compra e venda com base em picos e vales na série suavizada."""
        if self.dataset is None or "close_smooth" not in self.dataset.columns:
            raise Exception("Os indicadores ainda não foram calculados. Execute calculate_indicators primeiro.")
        atr = self.dataset["atr"].iloc[-1] if not pd.isna(self.dataset["atr"].iloc[-1]) else 1.0
        peaks_idx, _ = find_peaks(self.dataset.close_smooth, distance=distance, width=width, prominence=atr)
        troughs_idx, _ = find_peaks(-1 * self.dataset.close_smooth, distance=distance, width=width, prominence=atr)
        self.dataset['signal'] = np.nan
        self.dataset['signal'] = self.dataset['signal'].astype('object')
        self.dataset.loc[self.dataset.index[peaks_idx], 'signal'] = 'sell'
        self.dataset.loc[self.dataset.index[troughs_idx], 'signal'] = 'buy'
        self.dataset.index = pd.to_datetime(self.dataset.index)
        signals = []
        for idx in peaks_idx:
            signals.append({
                "time": int(self.dataset.index[idx].timestamp()),
                "position": "aboveBar",
                "color": "#e91e63",
                "shape": "arrowDown",
                "text": f"Sell @ {self.dataset['high'].iloc[idx] + 2:.2f}",
                "type": "sell",
                "size": 2
            })
        for idx in troughs_idx:
            signals.append({
                "time": int(self.dataset.index[idx].timestamp()),
                "position": "belowBar",
                "color": "#2196F3",
                "shape": "arrowUp",
                "text": f"Buy @ {self.dataset['low'].iloc[idx] - 2:.2f}",
                "type": "buy",
                "size": 2
            })
        return signals

    def get_all_data(self):
        """Retorna todos os dados no formato solicitado, incluindo close_smooth e signal."""
        if self.dataset is None:
            raise Exception("Os dados ainda não foram baixados. Execute download_data primeiro.")
        data_list = []
        for date, row in self.dataset.iterrows():
            timestamp = int(pd.Timestamp(date).timestamp())
            data_point = {
                "open": row["open"],
                "high": row["high"],
                "low": row["low"],
                "close": row["close"],
                "time": timestamp
            }
            if "close_smooth" in row and not pd.isna(row["close_smooth"]):
                data_point["close_smooth"] = row["close_smooth"]
            if "signal" in row and not pd.isna(row["signal"]):
                data_point["signal"] = row["signal"]
            data_list.append(data_point)
        return data_list