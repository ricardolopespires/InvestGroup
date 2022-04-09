from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from requests import Request, Session
from pycoingecko import CoinGeckoAPI
from googletrans import Translator
from uuid import uuid4
import pandas as pd
import sys, os
import pprint
import qrcode
import time
 

translator = Translator()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "investgroup.settings")

import django
django.setup()

from crypto.models import Plataforma, Cripto, Categoria
from django.utils.text import slugify
import requests
import json




cg = CoinGeckoAPI()

categorias = cg.get_coins_categories()

for categoria in categorias:
    time.sleep(1)
    print(categoria['name'])
    try:
        
        Categoria.objects.get_or_create(
            id =  categoria['id'],
            name = categoria['name'],
            content =  translator.translate(str(categoria['content']),dest='pt'),
            market_cap = categoria['market_cap'],
            market_cap_change_24h = categoria['market_cap_change_24h'],
            top_1 = categoria['top_3_coins'][0],
            top_2 = categoria['top_3_coins'][1],
            top_3 = categoria['top_3_coins'][2],
            updated_at = categoria['updated_at'],
            volume_24h = categoria['volume_24h'],
        )
    except:
        Categoria.objects.get_or_create(
            id =  categoria['id'],
            name = categoria['name'],
            content =  "Sem informações no momento",
            market_cap = categoria['market_cap'],
            market_cap_change_24h = categoria['market_cap_change_24h'],
            top_1 = categoria['top_3_coins'][0],
            top_2 = categoria['top_3_coins'][1],
            top_3 = categoria['top_3_coins'][2],
            updated_at = categoria['updated_at'],
            volume_24h = categoria['volume_24h'],
        )



historico = data = cg.get_coin_market_chart_by_id(id='bitcoin',vs_currency='usd',days='10')
days = 7
#print(json.dumps(historico, indent=4, sort_keys=True))

#dados = cg.get_coin_ohlc_by_id(id = 'cardano', vs_currency = 'brl', days = 4)

#print(json.dumps(dados, indent=4, sort_keys=True))



















