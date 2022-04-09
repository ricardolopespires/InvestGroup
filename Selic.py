import io, datetime, time, codecs
import matplotlib.pyplot as plt
import urllib.request
import pandas as pd
import sys, os 





os.environ.setdefault("DJANGO_SETTINGS_MODULE", "investgroup.settings")

import django
django.setup()


from analytics.models import Selic





origem = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.1178/dados?formato=csv'
arquivo = 'selic_bcb_api.csv'

if(not os.path.isfile(arquivo)):
    print('Efetuando download do arquivo ' + arquivo)
    urllib.request.urlretrieve(origem, arquivo)
else:
    print('Arquivo ' + arquivo + ' já existe. Utilizando o já existente!')
  


df_selic = pd.read_csv('selic_bcb_api.csv', encoding = "utf-8", delimiter=';')


try:
    df_selic['data'] = df_selic['data'].str.replace('/', '-')+' 00:00:00'
    df_selic['valor'] = df_selic['valor'].str.replace(',', '.').astype(float)
    df_selic.to_excel('selic_bcb_api.xlsx')
    
except:
   pass
    
print(df_selic.head())

for selic in df_selic.itertuples():
    selic = Selic.objects.create(
            id = selic[0],            
            data = selic[1],
            taxa = selic[2],
        )

