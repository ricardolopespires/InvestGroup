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
import json

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
        self.connected = False

    def initialize_mt5(self):
        """Inicializa a conexão com o terminal MetaTrader5."""
        if not mt5.initialize():
            error_code = mt5.last_error()
            logger.error(f"Falha Visualização do MetaTrader5, código de erro: {error_code}")
            return False
        logger.info(f"MetaTrader5 versão: {mt5.version()}")
        self.connected = True
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

    def balance(self):
        """Retorna o saldo atual da conta."""
        account = mt5.account_info()
        return account.balance if account else None

    def set_interval(self, interval):
        """Define o intervalo de tempo (timeframe) para as operações."""
        timeframes = {
            '1m': mt5.TIMEFRAME_M1, '5m': mt5.TIMEFRAME_M5, '15m': mt5.TIMEFRAME_M15,
            '30m': mt5.TIMEFRAME_M30, '1h': mt5.TIMEFRAME_H1, '4h': mt5.TIMEFRAME_H4,
            '6h': mt5.TIMEFRAME_H6, '8h': mt5.TIMEFRAME_H8, '12h': mt5.TIMEFRAME_H12,
            '1d': mt5.TIMEFRAME_D1, '1wk': mt5.TIMEFRAME_W1, '1mn': mt5.TIMEFRAME_MN1
        }
        if interval and interval not in timeframes:
            logger.error(f"Intervalo inválido: {interval}")
            raise ValueError(f"Intervalo inválido: {interval}")
        self.interval = timeframes.get(interval)

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
        
        from scipy.signal import find_peaks
        
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
        self.dataset.drop(["tick_volume", "spread", "real_volume","atr","close_smooth"], axis=1, inplace=True)
        logger.info("Sinais de compra e venda calculados.")
        return signals
    
    def buy_order(self, volume, sl=None, tp=None, comment="Buy Order"):
        """Executa uma ordem de compra no MetaTrader5."""
        if not self.connected:
            raise ConnectionError("MT5 não inicializado.")
        if not self.symbol:
            raise ValueError("Símbolo não definido.")
        
        symbol_info = mt5.symbol_info(self.symbol)
        if symbol_info is None:
            logger.error(f"Símbolo {self.symbol} não encontrado.")
            return None
        
        point = symbol_info.point
        price = mt5.symbol_info_tick(self.symbol).ask
        
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": self.symbol,
            "volume": float(volume),
            "type": mt5.ORDER_TYPE_BUY,
            "price": price,
            "sl": sl if sl else 0.0,
            "tp": tp if tp else 0.0,
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_FOK,
            "comment": comment
        }
        
        result = mt5.order_send(request)
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            logger.error(f"Falha ao executar ordem de compra: {result.comment}, código: {result.retcode}")
            return None
        
        logger.info(f"Ordem de compra executada: ticket #{result.order}, preço: {price}, volume: {volume}")
        return result

    def sell_order(self, volume, sl=None, tp=None, comment="Sell Order"):
        """Executa uma ordem de venda no MetaTrader5."""
        if not self.connected:
            raise ConnectionError("MT5 não inicializado.")
        if not self.symbol:
            raise ValueError("Símbolo não definido.")
        
        symbol_info = mt5.symbol_info(self.symbol)
        if symbol_info is None:
            logger.error(f"Símbolo {self.symbol} não encontrado.")
            return None
        
        point = symbol_info.point
        price = mt5.symbol_info_tick(self.symbol).bid
        
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": self.symbol,
            "volume": float(volume),
            "type": mt5.ORDER_TYPE_SELL,
            "price": price,
            "sl": sl if sl else 0.0,
            "tp": tp if tp else 0.0,
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_FOK,
            "comment": comment
        }
        
        result = mt5.order_send(request)
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            logger.error(f"Falha ao executar ordem de venda: {result.comment}, código: {result.retcode}")
            return None
        
        logger.info(f"Ordem de venda executada: ticket #{result.order}, preço: {price}, volume: {volume}")
        return result

    def close_position(self, ticket, comment="Close Position"):
        """Fecha uma posição específica com base no ticket."""
        if not self.connected:
            raise ConnectionError("MT5 não inicializado.")
        
        position = mt5.positions_get(ticket=ticket)
        if not position:
            logger.error(f"Posição com ticket #{ticket} não encontrada.")
            return None
        
        position = position[0]
        symbol = position.symbol
        volume = position.volume
        position_type = position.type
        
        close_type = mt5.ORDER_TYPE_SELL if position_type == mt5.ORDER_TYPE_BUY else mt5.ORDER_TYPE_BUY
        price = mt5.symbol_info_tick(symbol).bid if close_type == mt5.ORDER_TYPE_SELL else mt5.symbol_info_tick(symbol).ask
        
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": float(volume),
            "type": close_type,
            "position": ticket,
            "price": price,
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_FOK,
            "comment": comment
        }
        
        result = mt5.order_send(request)
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            logger.error(f"Falha ao fechar posição #{ticket}: {result.comment}, código: {result.retcode}")
            return None
        
        logger.info(f"Posição #{ticket} fechada com sucesso.")
        return result
    

    def reverse_position(self, ticket, sl=None, tp=None, volume=None, comment="Reverse Position", max_retries=3, retry_delay=0.5):
        """
        Inverte uma posição existente, fechando-a e abrindo uma nova na direção oposta.
        
        Args:
            ticket (int): Ticket da posição a ser invertida.
            sl (float, optional): Stop Loss da nova posição. Usa o SL original se None.
            tp (float, optional): Take Profit da nova posição. Usa o TP original se None.
            volume (float, optional): Volume da nova posição. Usa o volume original se None.
            comment (str): Comentário para a nova ordem.
            max_retries (int): Número máximo de tentativas para confirmar fechamento.
            retry_delay (float): Tempo de espera entre tentativas (em segundos).
        
        Returns:
            dict: Resultado da nova ordem ou None em caso de falha.
        """
        import time
        
        if not self.connected:
            raise ConnectionError("MT5 não inicializado.")

        # Obtém informações da posição
        position = mt5.positions_get(ticket=ticket)
        print(position)
        if not position:
            logger.error(f"Posição com ticket #{ticket} não encontrada.")
            return None
        
        position = position[0]
        if position.symbol != self.symbol:
            logger.error(f"Símbolo da posição #{ticket} ({position.symbol}) não corresponde ao símbolo configurado ({self.symbol}).")
            return None

        # Coleta informações da posição
        symbol = position.symbol
        position_volume = position.volume
        position_type = position.type
        position_sl = position.sl if sl is None else sl
        position_tp = position.tp if tp is None else tp
        new_volume = float(volume) if volume is not None else position_volume

        # Valida informações do símbolo
        symbol_info = mt5.symbol_info(symbol)
        if symbol_info is None:
            logger.error(f"Símbolo {symbol} não encontrado.")
            return None
        if not symbol_info.trade_mode == mt5.SYMBOL_TRADE_MODE_FULL:
            logger.error(f"Mercado para {symbol} está fechado ou restrito.")
            return None

        # Fecha a posição existente
        close_result = self.close_position(ticket, comment="Close for Reverse")
        if not close_result:
            logger.error(f"Falha ao fechar posição #{ticket} para reversão.")
            return None

        # Aguarda confirmação de fechamento
        for attempt in range(max_retries):
            remaining_positions = mt5.positions_get(ticket=ticket)
            if not remaining_positions:
                break
            logger.warning(f"Posição #{ticket} ainda aberta, tentativa {attempt + 1}/{max_retries}.")
            time.sleep(retry_delay)
        else:
            logger.error(f"Posição # não foi fechada após {max_retries} tentativas.")
            return None

        # Determina o tipo da nova ordem
        new_order_type = "sell" if position_type == mt5.ORDER_TYPE_BUY else "buy"
        
        # Executa a nova ordem
        try:
            new_order = (
                self.sell_order(new_volume, position_sl, position_tp, comment)
                if new_order_type == "sell"
                else self.buy_order(new_volume, position_sl, position_tp, comment)
            )
        except Exception as e:
            logger.error(f"Erro ao abrir nova posição oposta para #{ticket}: {str(e)}")
            return None

        if not new_order:
            logger.error(f"Falha ao abrir nova posição oposta para #{ticket}.")
            return None

        logger.info(
            f"Posição #{ticket} invertida com sucesso: "
            f"nova ordem #{new_order.order}, tipo: {new_order_type}, "
            f"volume: {new_volume}, SL: {position_sl}, TP: {position_tp}"
        )
        return new_order

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
    
    def positions_get(self, symbol=None, type=None):
        """Retrieve all current open positions, optionally filtered by symbol."""
        if not self.connected:
            raise ConnectionError("MT5 não inicializado.")
        
        if type == "stock" and symbol:
            positions = mt5.positions_get(symbol="#" + symbol)
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

    def history_deals_get(self, start_date=None, end_date=None):
        """Retrieve historical deals for the account over a specified period."""
        if not self.connected:
            raise ConnectionError("MT5 not initialized.")
        
        from_date = start_date if start_date else datetime(2010, 1, 1)
        to_date = end_date if end_date else datetime.now()
                
        deals = mt5.history_deals_get(from_date, to_date)
        if not deals:
            logger.info(f"No historical deals found from {from_date} to {to_date}.")
            return pd.DataFrame()
        
        df = pd.DataFrame(list(deals), columns=deals[0]._asdict().keys())
        df['time'] = pd.to_datetime(df['time'], unit='s')
        df['type'] = df['type'].map({0: 'buy', 1: 'sell', 2: 'balance', 3: 'credit'})
        df['entry'] = df['entry'].map({0: 'in', 1: 'out', 2: 'in/out', 3: 'reversed'})
        return df[['ticket', 'time', 'type', 'entry', 'symbol', 'volume', 'price', 
                  'profit', 'swap', 'commission', 'comment']]

    def get_all_data(self):
        """Retorna todos os dados formatados."""
        if self.dataset is None:
            raise ValueError("Os dados ainda não foram baixados.")        
        return self.dataset.to_dict(orient="records")



    def calculate_performance_metrics_for_symbol(self, symbol, start_date, end_date, initial_capital=10000):
        """Calcula métricas de performance para um símbolo específico e retorna um DataFrame."""
        if not self.connected:
            raise ConnectionError("MT5 não inicializado.")

        # Obter histórico de deals para o símbolo
        deals_df = self.history_deals_get(start_date, end_date)
        if deals_df.empty:
            return pd.DataFrame({"error": [f"Nenhum deal encontrado para o símbolo {symbol} no período especificado"]})

        # Filtrar pelo símbolo
        deals_df = deals_df[deals_df['symbol'] == symbol]
        if deals_df.empty:
            return pd.DataFrame({"error": [f"Nenhum deal encontrado para o símbolo {symbol}"]})

        # Calcular métricas
        return self._calculate_metrics(deals_df, initial_capital)

    def calculate_performance_metrics_all(self, start_date, end_date, initial_capital=10000):
        """Calcula métricas de performance para todas as operações e retorna um DataFrame."""
        if not self.connected:
            raise ConnectionError("MT5 não inicializado.")

        # Obter histórico de deals
        deals_df = self.history_deals_get(start_date, end_date)
        if deals_df.empty:
            return pd.DataFrame({"error": ["Nenhum deal encontrado no período especificado"]})

        # Calcular métricas
        return self._calculate_metrics(deals_df, initial_capital)

    def _calculate_metrics(self, df, initial_capital):
        """Função auxiliar para calcular métricas de performance e retornar um DataFrame."""
        # Filtrar apenas deals de compra/venda
        df = df[df['type'].isin(['buy', 'sell'])].copy()
        if df.empty:
            return pd.DataFrame({"error": ["Nenhum deal de compra/venda encontrado"]})

        # Calcular custos totais (comissões + swaps)
        df['total_cost'] = df['commission'] + df['swap']

        # Classificar operações
        df['result'] = np.where(df['profit'] > 0, 'vencedora',
                                np.where(df['profit'] < 0, 'perdedora', 'zerada'))

        # Calcular métricas
        metrics = {}

        # Resultado Líquido Total
        metrics['Resultado_Liq_Tot'] = df['profit'].sum() + df['total_cost'].sum()

        # Resultado Total
        metrics['Resultado_Total'] = df['profit'].sum()

        # Lucro Bruto
        metrics['Lucro_Bruto'] = df[df['profit'] > 0]['profit'].sum()

        # Prejuízo Bruto
        metrics['Prejuizo_Bruto'] = abs(df[df['profit'] < 0]['profit'].sum())

        # Operações (total)
        metrics['Operacoes'] = len(df)

        # Operações Vencedoras
        metrics['Vencedoras'] = len(df[df['result'] == 'vencedora'])

        # Saldo Líquido Total
        metrics['Saldo_Liquido_Total'] = metrics['Resultado_Liq_Tot']

        # Fator de Lucro
        metrics['Fator_de_Lucro'] = metrics['Lucro_Bruto'] / metrics['Prejuizo_Bruto'] if metrics['Prejuizo_Bruto'] > 0 else float('inf')

        # Número Total de Operações
        metrics['Numero_Total_de_Operacoes'] = metrics['Operacoes']

        # Operações Zeradas
        metrics['Operacoes_Zeradas'] = len(df[df['result'] == 'zerada'])

        # Média de Lucro/Prejuízo
        metrics['Media_de_Lucro_Prejuizo'] = df['profit'].mean() if metrics['Operacoes'] > 0 else 0

        # Média de Operações Vencedoras
        metrics['Media_de_Operacoes_Vencedoras'] = df[df['result'] == 'vencedora']['profit'].mean() if metrics['Vencedoras'] > 0 else 0

        # Maior Operação Vencedora
        metrics['Maior_Operacao_Vencedora'] = df[df['result'] == 'vencedora']['profit'].max() if metrics['Vencedoras'] > 0 else 0

        # Maior Sequência Vencedora
        def calculate_streak(series, condition):
            max_streak = current_streak = 0
            for result in series:
                if result == condition:
                    current_streak += 1
                    max_streak = max(max_streak, current_streak)
                else:
                    current_streak = 0
            return max_streak
        metrics['Maior_Sequencia_Vencedora'] = calculate_streak(df['result'], 'vencedora')

        # Média de Tempo em Operações Vencedoras (minutos)
        df['time_diff'] = df['time'].diff().dt.total_seconds() / 60
        metrics['Media_de_Tempo_em_Op_Vencedoras_mins'] = df[df['result'] == 'vencedora']['time_diff'].mean() if metrics['Vencedoras'] > 0 else 0

        # Média de Tempo em Operações (minutos)
        metrics['Media_de_Tempo_em_Operacoes_mins'] = df['time_diff'].mean() if len(df) > 1 else 0

        # Saldo Total
        metrics['Saldo_Total'] = metrics['Resultado_Total']

        # Custos
        metrics['Custos'] = abs(df['total_cost'].sum())

        # Percentual de Operações Vencedoras
        metrics['Percentual_de_Operacoes_Vencedoras'] = (metrics['Vencedoras'] / metrics['Operacoes'] * 100) if metrics['Operacoes'] > 0 else 0

        # Operações Perdedoras
        metrics['Operacoes_Perdedoras'] = len(df[df['result'] == 'perdedora'])

        # Razão Média Lucro:Média Prejuízo
        avg_profit = metrics['Media_de_Operacoes_Vencedoras']
        avg_loss = abs(df[df['result'] == 'perdedora']['profit'].mean()) if metrics['Operacoes_Perdedoras'] > 0 else 0
        metrics['Razao_Media_Lucro_Media_Prejuizo'] = avg_profit / avg_loss if avg_loss > 0 else float('inf')

        # Média de Operações Perdedoras
        metrics['Media_de_Operacoes_Perdedoras'] = avg_loss

        # Maior Operação Perdedora
        metrics['Maior_Operacao_Perdedora'] = abs(df[df['result'] == 'perdedora']['profit'].min()) if metrics['Operacoes_Perdedoras'] > 0 else 0

        # Maior Sequência Perdedora
        metrics['Maior_Sequencia_Perdedora'] = calculate_streak(df['result'], 'perdedora')

        # Média de Tempo em Operações Perdedoras
        metrics['Media_de_Tempo_em_Op_Perdedoras'] = df[df['result'] == 'perdedora']['time_diff'].mean() if metrics['Operacoes_Perdedoras'] > 0 else 0

        # Patrimônio Necessário (Maior Operação)
        metrics['Patrimonio_Necessario_Maior_Operacao'] = abs(df['profit'].min()) if not df['profit'].empty else 0

        # Retorno no Capital Inicial
        metrics['Retorno_no_Capital_Inicial'] = (metrics['Saldo_Liquido_Total'] / initial_capital * 100) if initial_capital > 0 else 0

        # Patrimônio Máximo
        df['cumulative_profit'] = df['profit'].cumsum()
        metrics['Patrimonio_Maximo'] = df['cumulative_profit'].max() + initial_capital if not df['cumulative_profit'].empty else initial_capital

        # Converter métricas para DataFrame
        return pd.DataFrame([metrics])

    def shutdown(self):
        """Encerra a conexão com o MetaTrader5."""
        mt5.shutdown()
        self.connected = False
        logger.info("Conexão com MetaTrader5 encerrada.")

if __name__ == "__main__":
    pass