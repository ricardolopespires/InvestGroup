import MetaTrader5 as mt5
from datetime import datetime
import pandas as pd

class MT5Connection:
    def __init__(self, account: int, password: str, server: str):
        self.account = account
        self.password = password
        self.server = server
        self.connected = False

    def connect(self):
        """Estabelece conexão com MT5"""
        if not mt5.initialize():
            raise Exception("Falha ao inicializar MT5")
        
        if not mt5.login(self.account, self.password, self.server):
            raise Exception("Falha no login")
        
        self.connected = True
        return {"status": "connected", "account": self.account}

    def disconnect(self):
        """Desconecta do MT5"""
        mt5.shutdown()
        self.connected = False
        return {"status": "disconnected"}

    def get_account_info(self):
        """Retorna informações da conta"""
        if not self.connected:
            raise Exception("Não conectado")
        
        account_info = mt5.account_info()
        if account_info is None:
            raise Exception("Falha ao obter info da conta")
        
        return {
            "balance": account_info.balance,
            "equity": account_info.equity,
            "margin": account_info.margin,
            "free_margin": account_info.margin_free
        }

    def get_historical_data(self, symbol: str, timeframe: str, start_date: datetime, end_date: datetime):
        """Obtém dados históricos"""
        if not self.connected:
            raise Exception("Não conectado")
        
        timeframe_dict = {
            "M1": mt5.TIMEFRAME_M1,
            "M5": mt5.TIMEFRAME_M5,
            "H1": mt5.TIMEFRAME_H1,
            "D1": mt5.TIMEFRAME_D1
        }
        
        rates = mt5.copy_rates_range(symbol, timeframe_dict.get(timeframe, mt5.TIMEFRAME_H1), 
                                   start_date, end_date)
        
        if rates is None:
            raise Exception("Falha ao obter dados históricos")
        
        df = pd.DataFrame(rates)
        df['time'] = pd.to_datetime(df['time'], unit='s')
        return df.to_dict(orient='records')