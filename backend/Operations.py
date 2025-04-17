import MetaTrader5 as mt5
import os
import sys
import django
import json  # Para lidar com o arquivo JSON
from datetime import datetime
import pandas as pd

# Definindo a variável de ambiente para as configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# Inicializando o Django
django.setup()

from transactions.models import Operation
from trading.models import Stock
 
# establish MetaTrader 5 connection to a specified trading account
if not mt5.initialize(login=6062572, server="LiteFinance-MT5-Demo",password="Rben290719rr@"):
    print("initialize() failed, error code =",mt5.last_error())
    quit()




for i in mt5.symbols_get():
    if "#" in i.name:
        ativo = i.name.replace("#","")
        if Stock.objects.filter(symbol = ativo).exists():
            pass
        else:
            symbol_info = mt5.symbol_info(i.name)
            
            Stock.objects.get_or_create(
                name = symbol_info.description,
                symbol = ativo,
                exchange = symbol_info.exchange,
                mt5 = symbol_info.name,
            )


'''
# get the number of deals in history
from_date=datetime(2020,1,1)
to_date=datetime.now()


# get deals for symbols whose names contain neither "EUR" nor "GBP"
deals = mt5.history_deals_get(from_date, to_date, group="*,!*EUR*,!*GBP*!*JPY*!*#AMZN*")
if deals == None:
    print("No deals, error code={}".format(mt5.last_error()))
elif len(deals) > 0:
    
    
    print()
    # display these deals as a table using pandas.DataFrame
    df=pd.DataFrame(list(deals),columns=deals[0]._asdict().keys())
    df['time'] = pd.to_datetime(df['time'], unit='s')
    dataset = df.to_dict(orient="records")
    for x in dataset:
                  
        Operation.objects.get_or_create(
            id = x['ticket'],
            magic = x['magic'],
            asset = x['symbol'],
            user_id = 2,
            date = x['time'],
            type = x['type'],
            volume = x['volume'],
            price_entry = x['price'],
            sl = 0,
            tp = 0,
            price_departure = 0,
            profit = x['profit'],
            stoploss = False,
            takeprofit = False,
            comment = x['comment']
            
            )
    
print("")
# shut down connection to the MetaTrader 5 terminal

'''
mt5.shutdown()
