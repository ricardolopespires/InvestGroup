#from binance import Client
#from secrets import api_key, api_secret
import json
import pandas as pd

#client = Client(api_key, api_secret)

#pegar informações da nossa conta

#info = client.get_account()


dados_binance = open("binance.json")

dados = json.dump(dados_binance, indent=4)

print(dados)
