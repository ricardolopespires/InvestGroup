#This example uses Python 2.7 and the python-request library.

from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from requests import Request, Session
from uuid import uuid4
import pandas as pd
import sys, os
import pprint
import qrcode
 


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "investgroup.settings")

import django
django.setup()

from crypto.models import Tag, Plataforma, Cripto
from django.utils.text import slugify
import requests
import json



'''
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'7',
  'limit':'1',
  'convert':'USD'
}

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'c773e9aa-0c9a-4420-8896-be97e954e7d9',
}

session = Session()
session.headers.update(headers)
'''



crypto_data = {'data': [{'circulating_supply': 42586164452.28444,
           'cmc_rank': 7,
           'date_added': '2018-10-08T00:00:00.000Z',
           'id': 3408,
           'last_updated': '2022-01-03T21:01:00.000Z',
           'max_supply': None,
           'name': 'USD Coin',
           'num_market_pairs': 2579,
           'platform': {'id': 1027,
                        'name': 'Ethereum',
                        'slug': 'ethereum',
                        'symbol': 'ETH',
                        'token_address': '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48'},
           'quote': {'USD': {'fully_diluted_market_cap': 42581891194.09,
                             'last_updated': '2022-01-03T21:01:00.000Z',
                             'market_cap': 42581891194.08534,
                             'market_cap_dominance': 1.9375,
                             'percent_change_1h': -0.01233014,
                             'percent_change_24h': 0.01193525,
                             'percent_change_30d': 0.0993317,
                             'percent_change_60d': -0.02628652,
                             'percent_change_7d': -0.01125363,
                             'percent_change_90d': 0.02361677,
                             'price': 0.9998996561851939,
                             'volume_24h': 2849502378.46,
                             'volume_change_24h': 15.4049}},
           'slug': 'usd-coin',
           'symbol': 'USDC',
           'tags': ['medium-of-exchange',
                    'stablecoin',
                    'asset-backed-stablecoin',
                    'binance-smart-chain',
                    'fantom-ecosystem'],
           'total_supply': 42586164452.28444}],
 'status': {'credit_count': 1,
            'elapsed': 17,
            'error_code': 0,
            'error_message': None,
            'notice': None,
            'timestamp': '2022-01-03T21:02:47.667Z',
            'total_count': 8759}}





try:
  #response = session.get(url, params=parameters)
  #crypto_data = response.json()

  tags_list = [x for x in crypto_data['data'][0]['tags']]


  tags_objs = []
  plataforma_objs = []

  
  #Para as Tags
  for tag in tags_list:
      codigo_id = str(uuid4()).split('-')[4]
      if Tag.objects.filter(nome = tag).exists():
          print('Ops.... Essa Tag já foi cadastrada')    
      else:
          a, created = Tag.objects.get_or_create(id = codigo_id , nome=tag)
          tags_objs.append(a)

  plataforma_list = crypto_data['data'][0]['platform']
  
  #Para as Plataformas
  for plataforma in plataforma_list:            
      if Plataforma.objects.filter(id = str(plataforma_list['id'])).exists():
          print('Ops.... Essa plataforma já foi cadastrada')    
      else:       
          a, created = Plataforma.objects.get_or_create(id = plataforma_list['id'], nome = plataforma_list['name'], slug = plataforma_list['slug'], simbolo = plataforma_list['symbol'], token_address = plataforma_list['token_address'])
          plataforma_objs.append(a)

  #Adicionando os dados da nova cryptomoeda
  for crypto in crypto_data['data']:
      #print(json.dumps(crypto, indent=2))
      
      codigo_id = str(uuid4()).split('-')[4]
            
      m, created = Cripto.objects.get_or_create(

          id  = codigo_id,
          logo = '',
          nome = crypto['name'],
          slug = crypto['slug'],
          codigo = crypto['id'],
          simbolo = crypto['symbol'],
          preco = crypto['quote']['USD']['price'],
          volume = '',
          capitalizacao = crypto['quote']['USD']['fully_diluted_market_cap'], 
          classificacao = crypto['cmc_rank'],
          circulacao = crypto['circulating_supply'],
          maximo = '',
          data_da_emissao = crypto['date_added'],
          preço_da_emissao = '',
          data_listagem = crypto['date_added'],
          updated = crypto['quote']['USD']['last_updated'],
          num_market_pairs = crypto['num_market_pairs'],
          last_updated = crypto['quote']['USD']['last_updated'],
          market_cap = crypto['quote']['USD']['market_cap'],
          market_cap_dominance = crypto['quote']['USD']['market_cap_dominance'],
          percent_change_1h = crypto['quote']['USD']['percent_change_1h'],
          percent_change_24h = crypto['quote']['USD']['percent_change_24h'],
          percent_change_30d = crypto['quote']['USD']['percent_change_30d'],
          percent_change_60d = crypto['quote']['USD']['percent_change_60d'],
          percent_change_7d = crypto['quote']['USD']['percent_change_7d'],
          percent_change_90d = crypto['quote']['USD']['percent_change_90d'],
          volume_24h = 0,
          volume_change_24h = 0,
          )
      m.plataforma.set(plataforma_objs)
      m.tags.set(tags_objs)

      m.save()
     
      


  print('Obrigado')
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)






























  
