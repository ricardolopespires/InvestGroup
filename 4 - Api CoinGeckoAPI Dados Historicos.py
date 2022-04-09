from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from datetime import date, datetime, timedelta
from requests import Request, Session
from pycoingecko import CoinGeckoAPI
from uuid import uuid4
import pandas as pd
import requests
import sys, os
import pprint
import qrcode
import time
 

cg = CoinGeckoAPI()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "investgroup.settings")

import django
django.setup()

from crypto.models import Plataforma, Cripto, Categoria, Historico
from django.db.models import Avg, Count, Sum ,F, Q
from django.utils.text import slugify
import requests
import json



def calculo_entre_data(inicial, final):
    # Data inicial
    d1 = datetime.strptime(str(inicial), '%Y-%m-%d')

    # Data final
    d2 = datetime.strptime(final, '%Y-%m-%d')

    # Calculo da quantidade de dias
    return abs((d1 - d2).days)


'''
datas = []


contador = calculo_entre_data(date.today(), '2021-03-29')


while True:
    if contador >= 0:
        dados =(date.today() - timedelta(days = contador )).strftime('%d-%m-%Y')
        dados = cg.get_coin_history_by_id('cardano',dados)
        print(dados)
        datas.append(dados)    
        contador -= 1
    else:
        break
    




for data in datas:
    url = "https://api.coingecko.com/api/v3/coins/cardano/history?date=" + str(datas)
    response = requests.get(url)
    history_data = response.json()
    print(json.dumps(history_data, indent=4, sort_keys=True))



'''





cripto = Historico.objects.filter(Q(name = 'cardano'),Q( data__gte=datetime.now()))





