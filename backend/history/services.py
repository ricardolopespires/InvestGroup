from datetime import datetime, timedelta
import yfinance as yf
import pandas as pd
import numpy as np
from scipy.signal import savgol_filter, find_peaks
from typing import Dict, List, Optional, Union
import MetaTrader5 as mt5
import pandas_ta as ta
import logging
# import pytz module for working with time zone
import pytz

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


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
        print(self.dataset.head())
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
    



class MT5Connector:
    def __init__(self, symbol=None, interval=None, account=None, password=None, server=None):
        self.symbol = symbol
        self.interval = None
        self.set_interval(interval)
        self.account = account
        self.password = password
        self.server = server
        self.dataset = None

    def initialize_mt5(self):
        """Inicializa a conexão com o terminal MetaTrader5."""
        if not mt5.initialize():
            error_code = mt5.last_error()
            logger.error(f"Falha na inicialização do MetaTrader5, código de erro: {error_code}")
            return False
        logger.info(f"MetaTrader5 versão: {mt5.version()}")
        return True

    def login(self):
        """Realiza login na conta de trading."""
        if not self.account or not self.password or not self.server:
            logger.error("Credenciais de conta incompletas.")
            return False
        
        authorized = mt5.login(int(self.account), password=self.password, server=self.server)
        if authorized:
            logger.info(f"Login bem-sucedido para a conta #{self.account} no servidor {self.server}")
            return True
        else:
            error_code = mt5.last_error()
            logger.error(f"Falha ao conectar à conta #{self.account}, código de erro: {error_code}")
            return False

    def set_interval(self, interval):
        """Define o intervalo de tempo (timeframe) para as operações."""
        timeframes = {
            '1m': mt5.TIMEFRAME_M1, '5m': mt5.TIMEFRAME_M5, '15m': mt5.TIMEFRAME_M15,
            '30m': mt5.TIMEFRAME_M30, '1h': mt5.TIMEFRAME_H1, '4h': mt5.TIMEFRAME_H4,
            '6h': mt5.TIMEFRAME_H6, '8h': mt5.TIMEFRAME_H8, '12h': mt5.TIMEFRAME_H12,
            '1d': mt5.TIMEFRAME_D1, '1wk': mt5.TIMEFRAME_W1, '1mn': mt5.TIMEFRAME_MN1
        }
        if interval not in timeframes:
            logger.error(f"Intervalo inválido: {interval}")
            raise ValueError(f"Intervalo inválido: {interval}")
        self.interval = timeframes[interval]

    def download_data(self):
        """Baixa os dados de mercado do MetaTrader5."""
        if not self.symbol:
            raise ValueError("Símbolo não definido.")
        
       
        
        bars = self._convert_period_to_bars()
        rates = mt5.copy_rates_from(self.symbol, self.interval, datetime.now(), bars)            
            
        if rates is None:
            rates = mt5.copy_rates_from(("#" + self.symbol), self.interval, datetime.now(), bars)
        
        self.dataset = pd.DataFrame(rates)
        self.dataset['time'] = pd.to_datetime(self.dataset['time'], unit='s')
        self.dataset.set_index('time', inplace=True)
        logger.info(f"{len(self.dataset)} registros baixados para {self.symbol}.")
        return self.dataset

    def _convert_period_to_bars(self):
        """Converte o intervalo de tempo para um número de barras adequado."""
        return 1000  # Número padrão de barras

    def preprocess_data(self, fill_method="ffill"):
        """Pré-processa os dados, convertendo tipos e tratando valores ausentes."""
        if self.dataset is None:
            raise ValueError("Os dados ainda não foram baixados.")        
        self.dataset[['open', 'high', 'low', 'close']] = self.dataset[['open', 'high', 'low', 'close']].astype(float)       
        self.dataset = self.dataset.round(2)
        
        # Correção: Converter o índice timestamp para cada linha
        self.dataset["time"] = self.dataset.index.map(lambda x: int(x.timestamp()))
        
        logger.info("Dados pré-processados com sucesso.")
        return self.dataset

 
    def calculate_indicators(self, atr_period=14, atr_smoothing_window=30, smooth_window=49, smooth_polyorder=5):
        """Calcula indicadores técnicos como ATR e suavização de preços."""
        if self.dataset is None:
            raise ValueError("Os dados ainda não foram baixados.")
        
        self.dataset["atr"] = ta.atr(self.dataset.high, self.dataset.low, self.dataset.close, timeperiod=atr_period)
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

        self.dataset['signal'] = np.nan  # Inicializa como NaN (float)
        self.dataset['signal'] = self.dataset['signal'].astype(object)  # Converte para object

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
        self.dataset.drop(["tick_volume", "spread", "real_volume","atr","close_smooth"], axis=1, inplace=True)
        logger.info("Sinais de compra e venda calculados.")
        return signals
    
    def get_last_signal_by_timeframes(self, symbol, timeframes=['1wk', '1d', '4h'], type=None):
        """
        Obtém o último sinal de compra ou venda para os timeframes especificados (W1, D1, H4).
        
        Args:
            symbol (str): Símbolo do ativo (ex: 'EURUSD').
            timeframes (list): Lista de timeframes a serem analisados (padrão: ['1wk', '1d', '4h']).
        
        Returns:
            pd.DataFrame: DataFrame com o último sinal para cada timeframe.
        """
        if not self.initialize_mt5():
            raise ConnectionError("Não foi possível inicializar o MetaTrader5.")
        
        if not self.login():
            raise ConnectionError("Não foi possível realizar o login no MetaTrader5.")
        
        last_signals = []
        
        for timeframe in timeframes:
            # Configura o timeframe atual
            if type == "stock":
                self.symbol = "#" + symbol
            else:
                self.symbol = symbol              
            self.set_interval(timeframe)
            
            # Baixa e processa os dados
            self.download_data()
            self.preprocess_data()
            self.calculate_indicators()
            self.calculate_signals()
            
            # Filtra apenas os sinais válidos ('buy' ou 'sell')
            signals_df = self.dataset[self.dataset['signal'].isin(['buy', 'sell'])].copy()
            
            if not signals_df.empty:
                # Pega o último sinal
                last_signal = signals_df.tail(1).iloc[0]
                print(last_signal)
                # Adiciona o sinal ao resultado
                last_signals.append({
                    'timeframe': timeframe,
                    'time': last_signal.name,  # O índice é o timestamp
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
        
        # Cria o DataFrame final
        result_df = pd.DataFrame(last_signals)
        logger.info("Últimos sinais calculados para os timeframes especificados.")
        return result_df
    
    def positions_get(self, symbol=None, type=None):
        """Retrieve all current open positions, optionally filtered by symbol."""        
        
        if type == "stock":
            positions = mt5.positions_get(symbol= "#" + symbol)

        else:
            positions = mt5.positions_get(symbol=symbol) if symbol else mt5.positions_get()

        if not positions:
            logger.info("No open positions found.")
            return pd.DataFrame()
        
        df = pd.DataFrame(list(positions), columns=positions[0]._asdict().keys())
        df['time'] = pd.to_datetime(df['time'], unit='s')
        df['time_update'] = pd.to_datetime(df['time_update'], unit='s')
        df['type'] = df['type'].map({0: 'buy', 1: 'sell'})
        return df[['ticket', 'time', 'time_update', 'type', 'symbol', 'volume', 'price_open', 
                  'price_current', 'sl', 'tp', 'profit', 'comment']]
    

    def history_deals_get(self):
        """Retrieve historical deals for the account over a specified period."""
        if not self.connected:
            raise ConnectionError("MT5 not initialized.")
        
        # obtemos o número de transações no histórico
        from_date=datetime(2010,1,1)
        to_date=datetime.now()
                
        deals = mt5.history_deals_get(from_date, to_date, group="*,!*EUR*,!*GBP*")
        if not deals:
            logger.info(f"No historical deals found for the last {from_date.days} days.")
            return pd.DataFrame()
        
        df = pd.DataFrame(list(deals), columns=deals[0]._asdict().keys())
        df['time'] = pd.to_datetime(df['time'], unit='s')
        df['type'] = df['type'].map({0: 'buy', 1: 'sell', 2: 'balance', 3: 'credit'})
        df['entry'] = df['entry'].map({0: 'in', 1: 'out', 2: 'in/out', 3: 'reversed'})
        return df[['ticket', 'time', 'type', 'entry', 'symbol', 'volume', 'price', 
                  'profit', 'swap', 'commission', 'comment']]

    def get_all_data(self):
        """Retorna todos os dados formatados."""
        print(self.dataset.head())
        if self.dataset is None:
            raise ValueError("Os dados ainda não foram baixados.")        
        return self.dataset.to_dict(orient="records") 
    


    def shutdown(self):
        """Encerra a conexão com o MetaTrader5."""
        mt5.shutdown()
        logger.info("Conexão com MetaTrader5 encerrada.")

if __name__ == "__main__":
    pass