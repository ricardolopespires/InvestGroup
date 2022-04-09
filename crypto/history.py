from django.db.models import Avg, Count, Sum ,F, Q
from dateutil.relativedelta import relativedelta
from django.shortcuts import get_object_or_404
from datetime import datetime, timedelta
from django.utils.text import slugify
from django.contrib import messages
from decimal import Decimal
from datetime import date
from uuid import uuid4
import requests





class Gerenciamento_Dados_Historicos:
    
    inicial = str(date.today().strftime('%d-%m-%Y') )
    relativedelta
    

    def __init__(self):
        self.datas = data
        self.inicial = inicial                                     
     

    def calculo_entre_data(self, final):
        # Data inicial
        d1 = datetime.strptime(str(self.inicial), '%Y-%m-%d')

        # Data final
        d2 = datetime.strptime(date.today() - timedelta(days = 365 ), '%Y-%m-%d')

        # Calculo da quantidade de dias
        return abs((d1 - d2).days)


    def generate_datas_history(self, data):

        url = "https://api.coingecko.com/api/v3/coins/"+str(self.cripto_id)+"/history?date=" + str(self.data)
        response = requests.get(url)
        return response.json()	
    

    def create_data_history(self, request, cripto_id, historico):

        datas = []
        
        contador = int(365)


        while True:
            if contador >= 0:
                
                datas.append((date.today() - timedelta(days = contador )).strftime('%d-%m-%Y'))                          

                contador -= 1
            else:
                break
                
        for data in datas:
            url = "https://api.coingecko.com/api/v3/coins/"+str(cripto_id)+"/history?date=" + str(data)
            response = requests.get(url)
            data_crypto = response.json()




            if data_crypto['developer_data']['pull_request_contributors'] == None:
                pull_request_contributors = 0
            else:
                try:
                    pull_request_contributors = data_crypto['developer_data']['pull_request_contributors']
                except:
                    pull_request_contributors = 0


            data_atual = datetime.strptime((data + str(" 00:00:00")), '%d-%m-%Y %H:%M:%S')

           


            historico.objects.get_or_create(

                id = str(uuid4()),
                symbol = data_crypto['symbol'],
                name = data_crypto['name'],
                slug = slugify(data_crypto['name']),
                data = data_atual,
                current_price = data_crypto['market_data']['current_price']['usd'],
                market_cap = data_crypto['market_data']['market_cap']['usd'],
                total_volume = data_crypto['market_data']['total_volume']['usd'],               
                facebook_likes = data_crypto['community_data']['facebook_likes'],
                twitter_followers = data_crypto['community_data']['twitter_followers'],
                reddit_average_posts_48h = data_crypto['community_data']['reddit_average_posts_48h'],
                reddit_average_comments_48h = data_crypto['community_data']['reddit_average_comments_48h'],
                reddit_subscribers = data_crypto['community_data']['reddit_subscribers'],
                reddit_accounts_active_48h = data_crypto['community_data']['reddit_accounts_active_48h'],
                forks = data_crypto['developer_data']['forks'],
                stars = data_crypto['developer_data']['stars'],
                subscribers = data_crypto['developer_data']['subscribers'],
                total_issues = data_crypto['developer_data']['total_issues'],
                closed_issues = data_crypto['developer_data']['closed_issues'],
                pull_requests_merged = data_crypto['developer_data']['pull_requests_merged'],
                pull_request_contributors = pull_request_contributors,
                views = 0,
                



            )

        messages.success(request, 'O total de dados atualizados com sucesso {}'.format(len(datas)))
        


    def upadte_date_history(self):
        pass