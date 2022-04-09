import MetaTrader5 as mt5
import time




mt5.initialize()

ativo = "XAUUSD"



while True:
    time.sleep(2)
    print(mt5.symbol_info_tick(ativo).bid)
