

from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from django.utils.text import slugify
from requests import Request, Session
from uuid import uuid4
import pandas as pd
import sys, os
import pprint
import qrcode
 


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "investgroup.settings")

import django
django.setup()

from crypto.models import Categoria, Plataforma, Cripto, Plataforma
from django.utils.text import slugify
from pycoingecko import CoinGeckoAPI
from uuid import uuid4
import requests
import json



dataset = CoinGeckoAPI()

'''
cg = CoinGeckoAPI()
cs = 'bitcoin'

start_dti = '1, 1, 2016'
end_dti = '1, 2, 2022'
#index = pd.date_range(start_dti, end_dti)


data = cg.get_coin_history_by_id(id='ethereum',date='10-11-2020', localization='false')


#print(json.dumps(data, indent=4, sort_keys=True))



import datetime

start = datetime.datetime.strptime("01-01-2022", "%d-%m-%Y")
end = datetime.datetime.strptime("22-01-2022", "%d-%m-%Y")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

for date in date_generated:
        dados = cg.get_coin_history_by_id(id='ethereum',date = (date.strftime("%d-%m-%Y")), localization='false')        
        for dado in dados:
                print(json.dumps(dado[1]['market_data'], indent=4, sort_keys=True))
'''

plataformas = dataset.get_asset_platforms()

plataforma_all = []

for plataforma in plataformas:    
        plataforma_all.append(plataforma['name'])
        

for plataforma in plataforma_all:
        print(plataforma)
        codigo_blockchain = str(uuid4()).split('-')[4]
        if Plataforma.objects.filter(nome = plataforma).exists():
                print("Essa Plataforma já foi cadastrada ")
        else:
                
                
                Plataforma.objects.get_or_create(

                        id = plataforma.lower(),
                        nome = plataforma.title(),
                        #symbol = plataforma.symbol,
                        slug = slugify(plataforma),


                        )

    

print(len(plataforma_all))       

#print(json.dumps(plataformas, indent=4, sort_keys=True))

