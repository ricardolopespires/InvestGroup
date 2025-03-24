import MetaTrader5 as mt5
import pandas as pd
import numpy as np
from scipy.signal import savgol_filter, find_peaks
import pandas_ta as ta
from datetime import datetime
from typing import Dict, List, Optional, Union
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class FinancialMT5Analyzer:
    """A class to analyze financial data using MetaTrader5 platform."""
    
    VALID_TIMEFRAMES: Dict[str, int] = {
        '1m': mt5.TIMEFRAME_M1, '5m': mt5.TIMEFRAME_M5, '15m': mt5.TIMEFRAME_M15,
        '30m': mt5.TIMEFRAME_M30, '1h': mt5.TIMEFRAME_H1, '4h': mt5.TIMEFRAME_H4,
        '1d': mt5.TIMEFRAME_D1, '1wk': mt5.TIMEFRAME_W1, '1mo': mt5.TIMEFRAME_MN1
    }

    def __init__(self, symbol: str, period: str, interval: str, account: int, 
                 password: str, server: str) -> None:
        """
        Initialize the MT5 financial data analyzer.
        
        Args:
            symbol: Trading symbol (e.g., 'EURUSD')
            period: Data period (e.g., '1d', '1mo', 'max')
            interval: Timeframe interval
            account: MT5 account number
            password: MT5 account password
            server: MT5 server address
        """
        self.symbol = symbol.upper()
        self.period = period
        self.account = account
        self.password = password
        self.server = server
        self.dataset: Optional[pd.DataFrame] = None
        
        self._setup_mt5_connection()
        self.set_interval(interval)

    def _setup_mt5_connection(self) -> None:
        """Initialize and authenticate MT5 connection."""
        try:
            if not mt5.initialize():
                raise ConnectionError(f"MT5 initialization failed: {mt5.last_error()}")
            
            logger.info(f"MetaTrader5 version: {mt5.version()}")
            if not mt5.login(self.account, password=self.password, server=self.server):
                raise ConnectionError(f"MT5 login failed for account #{self.account}: {mt5.last_error()}")
            
            logger.info(f"Successfully connected to account #{self.account}")
            account_info = mt5.account_info()
            if account_info:
                logger.info(f"Account balance: {account_info.balance}")
        except Exception as e:
            logger.error(f"Connection setup failed: {str(e)}")
            raise

    def set_interval(self, interval: str) -> None:
        """Validate and set the timeframe."""
        if interval not in self.VALID_TIMEFRAMES:
            raise ValueError(f"Invalid interval. Supported: {', '.join(self.VALID_TIMEFRAMES.keys())}")
        self.interval = self.VALID_TIMEFRAMES[interval]

    def _convert_period_to_bars(self) -> int:
        """Convert period string to number of bars based on interval."""
        period_map = {
            '1d': 1, '5d': 5, '1mo': 21, '3mo': 63, '6mo': 126,
            '1y': 252, '2y': 504, '5y': 1260, '10y': 2520, 'max': 10000
        }
        
        if self.period not in period_map:
            raise ValueError(f"Invalid period. Supported: {', '.join(period_map.keys())}")
        
        timeframe_minutes = {
            mt5.TIMEFRAME_M1: 1, mt5.TIMEFRAME_M5: 5, mt5.TIMEFRAME_M15: 15,
            mt5.TIMEFRAME_M30: 30, mt5.TIMEFRAME_H1: 60, mt5.TIMEFRAME_H4: 240,
            mt5.TIMEFRAME_D1: 1440, mt5.TIMEFRAME_W1: 10080, mt5.TIMEFRAME_MN1: 43200
        }
        daily_bars = period_map[self.period]
        return int(daily_bars * (1440 / timeframe_minutes[self.interval]))

    def download_data(self) -> None:
        """Download market data from MetaTrader5."""
        try:
            if not mt5.symbol_select(self.symbol, True):
                raise ValueError(f"Symbol {self.symbol} not available")
            
            bars = self._convert_period_to_bars()
            rates = mt5.copy_rates_from(self.symbol, self.interval, datetime.now(), bars)
            
            if not rates or len(rates) == 0:
                raise ValueError(f"No data for {self.symbol} at timeframe {self.interval}")
            
            self.dataset = pd.DataFrame(rates)
            self.dataset['time'] = pd.to_datetime(self.dataset['time'], unit='s')
            self.dataset.set_index('time', inplace=True)
            logger.info(f"Downloaded {len(self.dataset)} bars for {self.symbol}")
        except Exception as e:
            logger.error(f"Data download failed: {str(e)}")
            raise

    def preprocess_data(self, fill_method: str = "ffill") -> None:
        """Pre-process the downloaded data."""
        if self.dataset is None:
            raise RuntimeError("No data available. Run download_data first.")
        
        try:
            for col in ['open', 'high', 'low', 'close']:
                self.dataset[col] = self.dataset[col].astype(float)
            
            if fill_method == "ffill":
                self.dataset.fillna(method="ffill", inplace=True)
            elif fill_method == "drop":
                self.dataset.dropna(inplace=True)
            else:
                raise ValueError(f"Unsupported fill method: {fill_method}")
            
            self.dataset = self.dataset.round(2)
            logger.info("Data preprocessing completed")
        except Exception as e:
            logger.error(f"Data preprocessing failed: {str(e)}")
            raise

    def calculate_indicators(self, atr_period: int = 14, atr_smoothing_window: int = 30,
                           smooth_window: int = 49, smooth_polyorder: int = 5,
                           additional_indicators: Optional[List[str]] = None) -> None:
        """Calculate technical indicators."""
        if self.dataset is None:
            raise RuntimeError("No data available. Run download_data first.")
        
        try:
            self.dataset["atr"] = ta.atr(
                high=self.dataset.high, 
                low=self.dataset.low, 
                close=self.dataset.close, 
                length=atr_period
            )
            self.dataset["atr"] = self.dataset.atr.rolling(window=atr_smoothing_window).mean()
            self.dataset["close_smooth"] = savgol_filter(
                self.dataset.close, smooth_window, smooth_polyorder
            )
            
            if additional_indicators:
                for indicator in additional_indicators:
                    if indicator.lower() == "rsi":
                        self.dataset["rsi"] = ta.rsi(self.dataset.close)
            logger.info("Technical indicators calculated")
        except Exception as e:
            logger.error(f"Indicator calculation failed: {str(e)}")
            raise

    def calculate_signals(self, distance: int = 15, width: int = 3) -> List[Dict]:
        """Calculate buy/sell signals."""
        if self.dataset is None or "close_smooth" not in self.dataset.columns:
            raise RuntimeError("Indicators not calculated. Run calculate_indicators first.")
        
        try:
            atr = self.dataset["atr"].iloc[-1] if not pd.isna(self.dataset["atr"].iloc[-1]) else 1.0
            peaks_idx, _ = find_peaks(self.dataset.close_smooth, distance=distance, 
                                    width=width, prominence=atr)
            troughs_idx, _ = find_peaks(-self.dataset.close_smooth, distance=distance, 
                                      width=width, prominence=atr)
            
            self.dataset['signal'] = np.nan
            self.dataset['signal'] = self.dataset['signal'].astype('object')
            self.dataset.iloc[peaks_idx, self.dataset.columns.get_loc('signal')] = 'sell'
            self.dataset.iloc[troughs_idx, self.dataset.columns.get_loc('signal')] = 'buy'
            
            signals = [
                {
                    "time": int(self.dataset.index[idx].timestamp()),
                    "position": "aboveBar",
                    "color": "#e91e63",
                    "shape": "arrowDown",
                    "text": f"Sell @ {self.dataset['high'].iloc[idx] + 2:.2f}",
                    "type": "sell",
                    "size": 2
                } for idx in peaks_idx
            ] + [
                {
                    "time": int(self.dataset.index[idx].timestamp()),
                    "position": "belowBar",
                    "color": "#2196F3",
                    "shape": "arrowUp",
                    "text": f"Buy @ {self.dataset['low'].iloc[idx] - 2:.2f}",
                    "type": "buy",
                    "size": 2
                } for idx in troughs_idx
            ]
            
            logger.info(f"Generated {len(signals)} trading signals")
            return signals
        except Exception as e:
            logger.error(f"Signal calculation failed: {str(e)}")
            raise

    def get_all_data(self) -> List[Dict]:
        """Return all processed data."""
        if self.dataset is None:
            raise RuntimeError("No data available. Run download_data first.")
        
        try:
            data_list = [
                {
                    "open": row["open"],
                    "high": row["high"],
                    "low": row["low"],
                    "close": row["close"],
                    "time": int(date.timestamp()),
                    **({"close_smooth": row["close_smooth"]} 
                       if "close_smooth" in row and not pd.isna(row["close_smooth"]) else {}),
                    **({"signal": row["signal"]} 
                       if "signal" in row and not pd.isna(row["signal"]) else {})
                }
                for date, row in self.dataset.iterrows()
            ]
            return data_list
        except Exception as e:
            logger.error(f"Data retrieval failed: {str(e)}")
            raise

    def __del__(self) -> None:
        """Cleanup MT5 connection on object destruction."""
        mt5.shutdown()
        logger.info("MT5 connection shutdown")

