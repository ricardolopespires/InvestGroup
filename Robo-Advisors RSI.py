import MetaTrader5 as mt5
from datetime import datetime
import pandas as pd
pd.set_option('display.max_columns', 500) # número de colunas mostradas
pd.set_option('display.width', 1500)      # max. largura máxima da tabela exibida
# exibimos dados sobre o pacote MetaTrader5
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)
print()
# estabelecemos a conexão ao MetaTrader 5
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()
 
# obtemos o número de transações no histórico
from_date=datetime(2020,1,1)
to_date=datetime.now()

# obtemos transações cujos símbolos não contêm "EUR" nem "GBP"
deals = mt5.history_deals_get(from_date, to_date,)
if deals == None:
    print("No deals, error code={}".format(mt5.last_error()))
elif len(deals) > 0:
    print("history_deals_get(from_date, to_date, group=\"*,!*EUR*,!*GBP*\") =", len(deals))
    # exibimos todas as transações recebidos como estão
    for deal in deals:
        print("  ",deal)
    print()
    # exibimos essas transações como uma tabela usando pandas.DataFrame
    df=pd.DataFrame(list(deals),columns=deals[0]._asdict().keys())
    df['time'] = pd.to_datetime(df['time'], unit='s')
    print(df)
    df.to_excel('forex.xlsx', index = False)
print("")
 

 
# concluímos a conexão ao terminal MetaTrader 5
mt5.shutdown()

#Simbolos = ['AUDUSD', 'GBPUSD', 'EURUSD', 'NZDUSD', 'USDCAD', 'USDCHF', 'USDJPY', 'AUDCAD',  'EURCAD' 'EURGBP', 'EURJPY',  'EURMXN', 'USDMXN',   'XAGUSD', 'XAUUSD', ]
Simbolos = []

