import MetaTrader5 as mt5
import pandas as pd





# estabelecemos a conexão ao MetaTrader 5
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()
else:
    authorized =  mt5.login(5406115 , password="r328294305r")
    if authorized:
        account_info=mt5.account_info()
        if account_info!=None:
            # exibimos os dados sobre a conta de negociação como estão
            print(account_info)

accounts = 44072542
password = 'r328294305r'

def authication(accounts, password):
    authorized = mt5.login(accounts, password=password)
    if authorized:
        pass
