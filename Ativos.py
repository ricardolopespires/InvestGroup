from bs4 import BeautifulSoup
import pandas as pd
import unicodedata
import unidecode
import requests
import sys, os 
import json
import re


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "investgroup.settings")

import django
django.setup()


from forex.models import Ativos

import MetaTrader5 as mt5


# estabelecemos a conexão ao MetaTrader 5
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()


    
# obtemos símbolos cujos nomes contêm RU
ru_symbols=mt5.symbols_get()
for s in ru_symbols:
    Ativos.objects.get_or_create(
        id =  s.name,
        pares = s.name,
        status = 'moedas',
        images_1 = "",
        images_2 = "",

        )
    print(s.name)

 
mt5.shutdown()
