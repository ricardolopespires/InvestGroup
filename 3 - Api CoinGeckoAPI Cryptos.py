

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






url = "https://api.coingecko.com/api/v3/coins/list"

result = requests.get(url)

data_list = result.json()

for cripto in data_list:
        print(cripto['name'])
        url = "https://api.coingecko.com/api/v3/coins/" + str(cripto['name'])
        response = requests.get(url)
        search_data = response.json()
        
with open('data-crypto.json', 'w') as fp:
    json.dump(search_data, fp) 

#print(json.dumps(plataformas, indent=4, sort_keys=True))

