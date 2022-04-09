import MetaTrader5 as mt5
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
 
# exibimos informações sobre ordens ativas do símbolo GBPUSD
orders=mt5.orders_get(symbol="GBPUSD")
if orders is None:
    print("No orders on GBPUSD, error code={}".format(mt5.last_error()))
else:
    print("Total orders on GBPUSD:",len(orders))
    # exibimos todas as ordens ativas
    for order in orders:
        print(order)
print()
 
# obtemos uma lista de ordens com base em símbolos cujos nomes contenham "*GBP*"
gbp_orders=mt5.orders_get(group="*GBP*")
if gbp_orders is None:
    print("No orders with group=\"*GBP*\", error code={}".format(mt5.last_error()))
else:
    print("orders_get(group=\"*GBP*\")={}".format(len(gbp_orders)))
    # exibimos essas posições como uma tabela usando pandas.DataFrame
    df=pd.DataFrame(list(gbp_orders),columns=gbp_orders[0]._asdict().keys())
    df.drop(['time_done', 'time_done_msc', 'position_id', 'position_by_id', 'reason', 'volume_initial', 'price_stoplimit'], axis=1, inplace=True)
    df['time_setup'] = pd.to_datetime(df['time_setup'], unit='s')
    print(df)
 
# concluímos a conexão ao terminal MetaTrader 5
mt5.shutdown()
 
