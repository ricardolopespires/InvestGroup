# history/services.py
import yfinance as yf
import pandas as pd
import numpy as np
from scipy.signal import savgol_filter, find_peaks
import pandas_ta as ta

class FinancialDataAnalyzer:
    # Períodos e intervalos suportados pelo Yahoo Finance
    VALID_PERIODS = ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
    VALID_INTERVALS = ['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo']

    def __init__(self, symbol, period="5y", interval="1wk"):
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
        self.dataset = yf.download(self.symbol, period=self.period, interval=self.interval)
        
        if self.dataset.shape[0] == 0:
            raise Exception("Não há dados disponíveis para o símbolo fornecido com os parâmetros especificados.")

        # Padronizar nomes das colunas para minúsculas
        if isinstance(self.dataset.columns, pd.MultiIndex):
            self.dataset.columns = self.dataset.columns.get_level_values(0).str.lower()
        else:
            self.dataset.columns = self.dataset.columns.str.lower()

    def preprocess_data(self):
        """Pré-processa os dados, convertendo tipos e arredondando valores."""
        if self.dataset is None:
            raise Exception("Os dados ainda não foram baixados. Execute download_data primeiro.")

        # Converter colunas para float
        self.dataset['open'] = self.dataset.open.astype(float)
        self.dataset['high'] = self.dataset.high.astype(float)
        self.dataset['low'] = self.dataset.low.astype(float)
        self.dataset['close'] = self.dataset.close.astype(float)

        # Arredondar para duas casas decimais
        self.dataset = self.dataset.round(2)

    def calculate_indicators(self):
        """Calcula indicadores técnicos como ATR e suavização de preços."""
        if self.dataset is None:
            raise Exception("Os dados ainda não foram baixados. Execute download_data primeiro.")

        # Calcular o ATR
        self.dataset["atr"] = ta.atr(high=self.dataset.high, low=self.dataset.low, close=self.dataset.close)
        self.dataset["atr"] = self.dataset.atr.rolling(window=30).mean()

        # Suavizar os preços
        self.dataset["close_smooth"] = savgol_filter(self.dataset.close, 49, 5)

    def get_data_point(self, date):
        """Retorna os dados de uma data específica no formato solicitado."""
        if self.dataset is None:
            raise Exception("Os dados ainda não foram baixados. Execute download_data primeiro.")

        try:
            data_point = self.dataset.loc[date]
            # Converter a data para timestamp UNIX (em segundos)
            timestamp = int(pd.Timestamp(date).timestamp())
            return {
                "open": data_point["open"],
                "high": data_point["high"],
                "low": data_point["low"],
                "close": data_point["close"],
                "time": timestamp
            }
        except KeyError:
            raise Exception(f"Data {date} não encontrada no conjunto de dados.")

    def get_all_data(self):
        """Retorna todos os dados no formato solicitado."""
        if self.dataset is None:
            raise Exception("Os dados ainda não foram baixados. Execute download_data primeiro.")

        data_list = []
        for date, row in self.dataset.iterrows():
            # Converter a data para timestamp UNIX (em segundos)
            timestamp = int(pd.Timestamp(date).timestamp())
            data_list.append({
                "open": row["open"],
                "high": row["high"],
                "low": row["low"],
                "close": row["close"],
                "time": timestamp
            })
        return data_list