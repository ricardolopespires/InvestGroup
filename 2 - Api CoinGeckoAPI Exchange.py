# Ian Annase
# Mastering The CoinMarketCap API with Python3

import os
import json
import requests
from datetime import datetime
from prettytable import PrettyTable
from colorama import Fore, Back, Style
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

from crypto.models import Plataforma, Cripto, Categoria, Exchange
from django.utils.text import slugify
import requests
import json



exchanges_url = 'https://api.coingecko.com/api/v3/exchanges'


request = requests.get(exchanges_url)
results = request.json()


#print(json.dumps(results, indent=4, sort_keys=True))


for exchange in results:
    time.sleep(1)
    print(exchange['name'])
    if exchange['description'] == "":
         descricao = "Essa exchange ainda não tem descricao definida"
    else:
        try:
            descricao = translator.translate( exchange['description'],dest='pt')
        except:
            descricao = "Essa exchange ainda não tem descricao definida"
        

   

    print('Cadastrando a exchange {}, nom sistema InvestGroup'.format(exchange['name']))
    Exchange.objects.get_or_create(


      country   = exchange['country'],
      description  =  descricao ,
      has_trading_incentive = False,
      id   = exchange['id'],
      image = exchange['image'],
      name = exchange['name'],
      slug  = slugify(exchange['name']),
      trade_volume_24h_btc = exchange['trade_volume_24h_btc'],
      trade_volume_24h_btc_normalized = exchange[ 'trade_volume_24h_btc_normalized' ],
      trust_score = exchange[ 'trust_score' ],
      trust_score_rank  = exchange[ 'trust_score_rank' ],
      url = exchange[ 'url'],
      year_established = exchange[ 'year_established' ]
    )
    print(' A exchange {}, foi cadastrada co sucesso....'.format(exchange['name']))
    print('\t\t')
        








