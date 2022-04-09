from .models import Categoria, Plataforma, Exchange, Cripto, Investimento, Movimentacao, Price_percentage_change, Historico
from .core import porcentagem, retornos_acumalados, price_percentage_change
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from .history import Gerenciamento_Dados_Historicos
from django.db.models import Avg, Count, Sum ,F, Q
from django.http import HttpResponseRedirect
from datetime import datetime, timedelta
from requests import Request, Session
from django.views.generic import View
from django.utils.text import slugify
from django.http import JsonResponse
from pycoingecko import CoinGeckoAPI
from django.contrib import messages
from googletrans import Translator
from binance.client import Client
from management.models import API
from accounts.models import User
from django.urls import reverse
from .forms import Cripto_Form
from .historicos import dados
from decimal import Decimal
from datetime import date
from uuid import uuid4
import requests
import json


translator = Translator()

from binance.client import Client

API_KEY = "vBzARifEmC125fFXYwtZtzriL5pdWgHG2m7t2kHXIGjS9MmGTwugXgMpEdBheicm"
API_SECRET = "4L8nNe7q1kaxiAhD2FDPHAt0XFlN0itHUkaSXBn0ksm1G4AGqt3tHnY4LVOc3eEF"

client = Client(API_KEY, API_SECRET)
#Gerando a data atual
data_atual = datetime.now()


#Crie suas visualizações aqui.

class Manager_Crypto_View(LoginRequiredMixin, View):

	def get(self, request):		

		API = CoinGeckoAPI()
		#Buscando a data atual
		month = data_atual.month

		"Pesquisa individual por moeda"
		query  = request.GET.get('search', None)

		print(query)	
		if query is not None:

			try:
				url = "https://api.coingecko.com/api/v3/coins/" + str(query).lower()
				response = requests.get(url)
				search_data = response.json()				
				

				#data_crypto = API.get_coins_markets(vs_currency = 'usd')
				return render(request, 'crypto/manager/index.html',{ 'month':month,'search_data':search_data, })

			except:
				
				if  Cripto.objects.filter( id = query).exists():
					search_data = API.get_coin_by_id(id = query)

				elif Cripto.objects.filter( name = query).exists():
					crypto = get_object_or_404(Cripto, name = query)
					search_data = API.get_coin_by_id(id = crypto.id)

				elif Cripto.objects.filter( symbol = query).exists():
					crypto = get_object_or_404(Cripto, symbol = query)
					search_data = API.get_coin_by_id(id = crypto.id)			

				else:				
					return HttpResponseRedirect(reverse('crypto:manager'))			

			
		url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=275&page=1&sparkline=false' 	

		response = requests.get(url)
		data_crypto = response.json()

		#data_crypto = API.get_coins_markets(vs_currency = 'usd')
		return render(request, 'crypto/manager/index.html',{ 'month':month,'data_crypto':data_crypto, })







			 
class Crypto_Detail_View(LoginRequiredMixin, View):


	def get(self, request, cripto_id, name_id):

		data_crypto = Cripto.objects.filter( id = cripto_id )	

		API = CoinGeckoAPI()

		url = "https://api.coingecko.com/api/v3/coins/" + str( cripto_id ).lower()
		response = requests.get(url)	

		crypto = response.json()	
		

		if crypto['description']['pt'] == "":
			descricao = "Essa exchange ainda não tem descricao definida"
		
		else:
			try:
				descricao = translator.translate( crypto['description']['pt'],dest='pt')
			except:
				descricao = "Essa exchange ainda não tem descricao definida"

		#print(json.dumps(crypto, indent=4, sort_keys=True))

		try:
			ft = int(porcentagem(crypto['market_data']['total_supply'], crypto['market_data']['total_supply']))

		except:
			ft = 0
		


		try:
			fc = int(porcentagem(crypto['market_data']['total_supply'], crypto['market_data']['circulating_supply']))
		except:
			fc = 0

		if len(str(fc)) > 3:
			fc = 100
		else:
			fc

		p_30 = int(
			porcentagem(
					
					crypto['market_data']['price_change_percentage_30d_in_currency']['btc'],
					crypto['market_data']['price_change_percentage_30d_in_currency']['usd'] 
				)
			)

		

		p_60 = int(
			porcentagem(
					
					crypto['market_data']['price_change_percentage_60d_in_currency']['btc'],
					crypto['market_data']['price_change_percentage_60d_in_currency']['usd'] 
				)
			)

	


		
		p_200 = int(
			porcentagem(
					
					crypto['market_data']['price_change_percentage_200d_in_currency']['btc'],
					crypto['market_data']['price_change_percentage_200d_in_currency']['usd'] 
				)
			)


		p_1 = int(
			porcentagem(
					
					crypto['market_data']['price_change_percentage_1y_in_currency']['btc'],
					crypto['market_data']['price_change_percentage_1y_in_currency']['usd'] 
					
				)
			)

				

		total_capital = crypto['market_data']['market_cap']['usd']
		capital_geral = sum(list( x['market_cap'] for x in API.get_coins_markets(vs_currency = 'usd')))

		pc = int(porcentagem(capital_geral, total_capital ))

		if pc > 0:
			pc 
		else:
			pc = 1


		valorizacao = int(porcentagem(crypto['market_data']['ath']['usd'], crypto['market_data']['current_price']['usd']))
		

		try:
			github = crypto['links']['repos_url']['github'][0]
		except:
			github = " "
			

		if Cripto.objects.filter(name = name_id).exists():

			our_db = True

			try:
				fully_diluted_valuation = crypto['market_data']['fully_diluted_valuation']['usd']
			except:
				fully_diluted_valuation = 0


			try:
				ROI = crypto['market_data']['roi']['percentage']

			except: 
				ROI = 0


			
			price_percentage_change(crypto['id'], datetime, timedelta )	

			
			Cripto.objects.filter( id = crypto['id']).update(

				
			    current_price = crypto['market_data']['current_price']['usd'],
			    market_cap = crypto['market_data']['market_cap']['usd'],
			    market_cap_rank= crypto['market_data']['market_cap_rank'],
			    fully_diluted_valuation = fully_diluted_valuation,
			    descricao = descricao,
			    total_volume = crypto['market_data']['total_volume']['usd'],
			    high_24h = crypto['market_data']['high_24h']['usd'],
			    low_24h = crypto['market_data']['low_24h']['usd'],
			    price_change_24h = crypto['market_data']['price_change_24h'],
			    price_change_percentage_24h = crypto['market_data']['price_change_percentage_24h'],
			    market_cap_change_24h = crypto['market_data']['market_cap_change_24h'],
			    market_cap_change_percentage_24h = crypto['market_data']['market_cap_change_percentage_24h'],
			    circulating_supply  = crypto['market_data']['circulating_supply'],
			    total_supply  = crypto['market_data']['total_supply'],
			    max_supply  = crypto['market_data']['max_supply'],
			    ath  = crypto['market_data']['ath']['usd'],
			    ath_change_percentage  = crypto['market_data']['ath_change_percentage']['usd'],
			    ath_date = crypto['market_data']['ath_date']['usd'], 
			    atl = crypto['market_data']['atl']['usd'],
			    atl_change_percentage = crypto['market_data']['atl_change_percentage']['usd'],
			    atl_date = crypto['market_data']['atl_date']['usd'],				
				facebook_username = 'https://pt-br.facebook.com/' + str(crypto['links']['facebook_username']),
				twitter_screen_name = 'https://twitter.com/' + str(crypto['links']['twitter_screen_name']),
				telegram_channel_identifier = crypto['links']['telegram_channel_identifier'],
				blockchain_site = crypto['links']['blockchain_site'],
				official_forum_url = crypto['links']['official_forum_url'][0],
				repos_url = github, 
			    roi = ROI,
			    last_updated = crypto['last_updated'],


				)
				
			categorias = Categoria.objects.filter(cryptos = crypto['id'] )


			

			return render(request, 'crypto/manager/detail.html', {
				'crypto':crypto, 'ft':ft, 'fc':fc, 'pc':pc, 'fully_diluted_valuation':fully_diluted_valuation,
				'data_crypto':data_crypto, 'valorizacao' :valorizacao, 'p_1':p_1, 'p_30':p_30, 'p_60':p_60, 'p_200':p_200,
				
				})


		else:


			try:
				ROI = crypto['market_data']['roi']['percentage']

			except: 
				ROI = 0


			try:
				categoria_objs = []			
				
				categoria_list = [ x for x in crypto['categories'] ]
				print( categoria_list )

				for categoria in categoria_list:
					a, created = Categoria.objects.get_or_create(name = categoria)
					categoria_objs.append(a)

			except:
				pass


			try:
				fully_diluted_valuation = crypto['market_data']['fully_diluted_valuation']['usd']
			except:
				fully_diluted_valuation = 0

			try:
				asset_platform_id  = crypto['asset_platform_id']

			except:
				asset_platform_id  = "Não trabalha com rede"
			

			m, created = Cripto.objects.get_or_create(


				id = crypto['id'],
				asset_platform_id  = asset_platform_id,
			    symbol = crypto['symbol'],
			    name = crypto['name'],
			    slug = slugify(crypto['name']),
			    image = crypto['image']['thumb'],
			    current_price = crypto['market_data']['current_price']['usd'],
			    market_cap = crypto['market_data']['market_cap']['usd'],
			    market_cap_rank= crypto['market_data']['market_cap_rank'],
			    fully_diluted_valuation = fully_diluted_valuation,
			    descricao = descricao,
			    total_volume = crypto['market_data']['total_volume']['usd'],
			    high_24h = crypto['market_data']['high_24h']['usd'],
			    low_24h = crypto['market_data']['low_24h']['usd'],
			    price_change_24h = crypto['market_data']['price_change_24h'],
			    price_change_percentage_24h = crypto['market_data']['price_change_percentage_24h'],
			    market_cap_change_24h = crypto['market_data']['market_cap_change_24h'],
			    market_cap_change_percentage_24h = crypto['market_data']['market_cap_change_percentage_24h'],
			    circulating_supply  = crypto['market_data']['circulating_supply'],
			    total_supply  = crypto['market_data']['total_supply'],
			    max_supply  = crypto['market_data']['max_supply'],
			    ath  = crypto['market_data']['ath']['usd'],
			    ath_change_percentage  = crypto['market_data']['ath_change_percentage']['usd'],
			    ath_date = crypto['market_data']['ath_date']['usd'], 
			    atl = crypto['market_data']['atl']['usd'],
			    atl_change_percentage = crypto['market_data']['atl_change_percentage']['usd'],
			    atl_date = crypto['market_data']['atl_date']['usd'],				
				facebook_username = crypto['links']['facebook_username'],
				twitter_screen_name = crypto['links']['twitter_screen_name'],
				telegram_channel_identifier = crypto['links']['telegram_channel_identifier'],
				blockchain_site = crypto['links']['blockchain_site'],
				official_forum_url = crypto['links']['official_forum_url'],
				repos_url = github, 
			    roi = ROI,
			    last_updated = crypto['last_updated'],

				)


			m.categoria.set(categoria_objs)



			for categoria in categoria_objs:
				categoria.cryptos.add(m)
				categoria.save()


			m.save()
			our_db = False

		

		return render(request, 'crypto/manager/detail.html', {

			'crypto':crypto, 'ft':ft, 'fc':fc, 'pc':pc, 'data_crypto':data_crypto,
			'p_1':p_1, 'p_30':p_30, 'p_60':p_60, 'p_200':p_200,


			})



#--------------------------------------------------------- Moedas em tendência --------------------------------------------

class Moedas_Tendencia_View(LoginRequiredMixin, View):

	def get(self, request):


		cryptos= []

		API = CoinGeckoAPI()
		tendencias = API.get_search_trending()
		data_crypto = API.get_coins_markets(vs_currency = 'usd')

		for tendencia in tendencias['coins']:			

			url = "https://api.coingecko.com/api/v3/coins/" + str( tendencia['item']['id'] ).lower()
		
			response = requests.get(url)
			crypto = response.json()

			try:
				print(json.dumps( crypto['market_data']['roi']['percentage'], indent=4, sort_keys=True))
			except:
				print("O Roi não devulgado")

			

			cryptos.append(crypto)

			#print(json.dumps( crypto, indent=4, sort_keys=True))
	
		return render(request, 'crypto/manager/tendencia.html',{
			
			'tendencias':tendencias, 'data_crypto':data_crypto,
			'cryptos':cryptos,
			
			})



#--------------------------------------------------------- Meus Investimento --------------------------------------------



class Meus_Investimento_View(LoginRequiredMixin, View):

	def get(self, request):

		investimentos = Investimento.objects.all()
	
		return render(request, 'crypto/investimento/index.html',{'investimentos':investimentos})



class Detail_Investimento_View(LoginRequiredMixin, View):

	def get(self, request, cripto_id, cripto_name):

		API = CoinGeckoAPI()


		investimento = get_object_or_404(Investimento, id = cripto_id)

		crypto = API.get_coin_by_id( id = investimento.crypto.id )

		movimentacoes = Movimentacao.objects.filter(crypto_id = crypto['id'])

		for cripto in  Movimentacao.objects.filter(crypto_id = crypto['id']):
			preco =  cripto.quantidade * crypto['market_data']['current_price']['brl']

			investimento.saldo =  preco - cripto.total
			investimento.preco = movimentacoes.aggregate(Avg('preco'))['preco__avg']
			investimento.save()

			porcento = porcentagem(cripto.total, preco)
			cripto.porcentagem = porcento
			cripto.retorno = porcento
			cripto.save()


		movimento = [ int(movimentacoes.total) for movimentacoes in movimentacoes ]

		try:
			porcento = porcentagem(cripto.total, preco)
		except:
			porcento = 0

		porcento = porcento	
		investimento.taxa_retorno = porcento
		investimento.save()

		for retorno in retornos_acumalados(movimentacoes):
			investimento.retorno = retorno
			investimento.save()
		


		return render (request, 'crypto/investimento/detail.html',{

		 'crypto':crypto, 'investimento':investimento,
		 'movimentacoes':movimentacoes,
		 'movimento':json.dumps(movimento),
		 

		 })


class Created_Investimento_View(LoginRequiredMixin, View):

	def get(self,request):
		cryptos = Cripto.objects.all().order_by('market_cap_rank')
		return render(request, 'crypto/investimento/created.html', {'cryptos':cryptos,})



	def post(self, request):



		if request.method == 'POST':

			crypto_id = request.POST.get('cripto')

			print(crypto_id)

			cripto = get_object_or_404(Cripto, id = crypto_id)

			#Gerando código do investimento
			codigo_id = str(uuid4()).split('-')[4]

							

			m, created = Investimento.objects.get_or_create(

				id = codigo_id,
				investidor = request.user,												
				crypto = cripto,
				deposito = 0,
				retirada = 0,
				preco = 0,
				quantidade = 0,
				media = 0,
				retorno = 0,				
				taxa_retorno = 0,
				rating = 0,				
				final = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
				total = 0,

				)

			messages.success(request, 'Parabéns, {}, você acabou de gerar um novo investimento, não esqueça de fazer os aportes'.format(request.user))
			return HttpResponseRedirect(reverse('crypto:investimento'))

		else:
			messages.error(request, 'Ops...., {}, os dados não estão corretos'.format(request.user))
			return HttpResponseRedirect(reverse('crypto:investimento'))




class Movimentacao_Cripto_View(LoginRequiredMixin, View):

	def get(self, request , investimento_id):
		investimento = get_object_or_404(Investimento, id = investimento_id)
		investidores = User.objects.filter( id = request.user.id )
		codigo_aporte = str(uuid4()).split('-')[4]
		exchanges = Exchange.objects.all()
		cryptos =  Cripto.objects.all()

		return render(request, 'crypto/investimento/aporte.html', {

			'investimento':investimento, 'investidores':investidores, 'codigo_aporte':codigo_aporte,
			'exchanges':exchanges, 'cryptos':cryptos,

			})


	def post(self, request, investimento_id):
		

		if request.method == 'POST':
			codigo_aporte = str(uuid4()).split('-')[4]
			investidor = request.POST.get('investidor')
			investimento = request.POST.get('investimento')
			data = request.POST.get('data')
			crypto = request.POST.get('crypto')
			exchange = request.POST.get('exchange')
			status = request.POST.get('status')
			valor = request.POST.get('valor')
			preco = request.POST.get('preco')
			quantidade = float(request.POST.get('quantidade'))
			investidor = request.POST.get('investidor')
			retorno = request.POST.get('retorno')
			total = float(request.POST.get('total'))

			print(type(quantidade))
			print(type(total))

			Movimentacao.objects.get_or_create(


				id = codigo_aporte,
			    investidor_id = investidor,
			    investimento_id = investimento,
			    crypto_id = crypto,
			    blockchain_id = exchange,
			    status = status,
			    data =  data,
			    valor = valor,       
			    quantidade = quantidade,
			    preco = preco,
			    retorno = retorno,      
			    total = total,
				)

			#gerando os dados na movimentação financeira do investidor
			investidor = get_object_or_404(User,id = request.user.id)
			investidor.crypto += total
			investidor.investimento += total
			investidor.save()


			#Gerando os dados do investimento
			investimento = get_object_or_404(Investimento, id = investimento_id)
			investimento.deposito += 1	
			investimento.total += total
			investimento.quantidade += quantidade
			investimento.save() 


			messages.success(request,'O seu aporte no valor R$ {} foi feito con sucesso'.format( total ))
			return HttpResponseRedirect(reverse('crypto:investimento_detail', args = [investimento.id, investimento.crypto.name]))

		else:
			messages.error(request, "Os dados não estão corretos, por favor verifica-lo")
			return HttpResponseRedirect(reverse('crypto:aporte'))


#--------------------------------------------------------- Análise Fundamentalista ---------------------------------------

class Analise_Fundamentalista_View(LoginRequiredMixin, View):

	def get(self, request):

		#Buscando a data atual
		month = data_atual.month

		API = CoinGeckoAPI()		

		"Pesquisa individual por moeda"
		query  = request.GET.get('search', None)
	
		print(query)	
		if query is not None:

			if  Cripto.objects.filter( id = query).exists():
				search_data = API.get_coin_by_id(id = query)

			elif Cripto.objects.filter( name = query).exists():
				crypto = get_object_or_404(Cripto, name = query)
				search_data = API.get_coin_by_id(id = cripto.id)

			elif Cripto.objects.filter( symbol = query).exists():
				crypto = get_object_or_404(Cripto, symbol = query)
				search_data = API.get_coin_by_id(id = crypto.id)			

			else:				
				return HttpResponseRedirect(reverse('crypto:fundamentalista'))
			

			print(json.dumps(search_data, indent=4, sort_keys=True))			
			
			total = User.objects.filter(id = request.user.id).aggregate(total = Sum(F('dinheiro') + F('crypto') + F('retorno')))['total']

			return render(request, 'crypto/manager/index.html',{ 'month':month,'search_data':search_data, 'total':total,})
		
		try:
			total = User.objects.filter(id = request.user.id).aggregate(total = Sum(F('dinheiro') + F('crypto') + F('retorno')))['total']
		except:
			total = 0

		print(total)

		data_crypto = API.get_coins_markets(vs_currency = 'usd')

		return render(request, 'crypto/analise/fundamentalista/index.html', {'data_crypto':data_crypto,})



#--------------------------------------------------------- Análise Têcnica --------------------------------------------------

class Analise_Tecnica_View(LoginRequiredMixin, View):	
		
		
	def get(self, request):

		#Buscando a data atual
		month = data_atual.month

		API = CoinGeckoAPI()		

		"Pesquisa individual por moeda"
		query  = request.GET.get('search', None)

		print(query)	
		if query is not None:

			if  Cripto.objects.filter( id = query).exists():
				search_data = API.get_coin_by_id(id = query)

			elif Cripto.objects.filter( name = query).exists():
				crypto = get_object_or_404(Cripto, name = query)
				search_data = API.get_coin_by_id(id = cripto.id)

			elif Cripto.objects.filter( symbol = query).exists():
				crypto = get_object_or_404(Cripto, symbol = query)
				search_data = API.get_coin_by_id(id = crypto.id)			

			else:				
				return HttpResponseRedirect(reverse('crypto:tecnica'))
		

			return render(request, 'crypto/analise/tecnica/index.html',{ 'search_data':search_data, })		
			
		data_crypto = API.get_coins_markets(vs_currency = 'usd')
		return render(request, 'crypto/analise/tecnica/index.html',{ 'data_crypto':data_crypto,})



class Detail_Analise_Tecnica_View(LoginRequiredMixin, View):

	def get(self, request, cripto_id, name_id):
		from binance.client import Client

		API_KEY = "vBzARifEmC125fFXYwtZtzriL5pdWgHG2m7t2kHXIGjS9MmGTwugXgMpEdBheicm"
		API_SECRET = "4L8nNe7q1kaxiAhD2FDPHAt0XFlN0itHUkaSXBn0ksm1G4AGqt3tHnY4LVOc3eEF"

		client = Client(API_KEY, API_SECRET)

		cripto_id = cripto_id
		cripto = str(name_id.upper()) + 'USDT'
		
		candlesticks = client.get_historical_klines(str(cripto), Client.KLINE_INTERVAL_5MINUTE, '1 Jan, 2021',)

		processend_clanlesticks = []
		
		for data in candlesticks:
			candlestick = {

				'time': data[0] / 1000,
				'open':data[1],
				'high':data[2],
				'low':data[3],
				'close':data[4]

				}
			processend_clanlesticks.append(candlestick)

		return render(request, 'crypto/analise/tecnica/detail.html',{
			'dados':JsonResponse(processend_clanlesticks, safe=False),
			'cripto':cripto,
			
			})

#--------------------------------------------------------- Trading Manualmente ------------------------------------------------

class Trading_Manual_Cripto_Plataforma_View(LoginRequiredMixin, View):

	def get (self, request):
		exchanges = Exchange.objects.all()		
		return render(request, 'crypto/trading/manual/plataforma.html',{'exchanges':exchanges, })



class Trading_Manual_Cripto_Negocicao_View(LoginRequiredMixin, View):

	def get (self, request):		
		return render(request, 'crypto/trading/manual/negociacao.html')

#--------------------------------------------------------- Trading Automatico ------------------------------------------------

class Trading_Automatic_Cripto_View(LoginRequiredMixin, View):

	def get (self, request):
		exchanges = Exchange.objects.all().order_by('trust_score_rank')	
		return render(request, 'crypto/trading/automatico/exchanges.html',{'exchanges':exchanges, })


class Trading_Automatic_Cripto_Plataform_View(LoginRequiredMixin, View):

	def get(self, request, exchange_id ):
		exchange = get_object_or_404(Exchange, id  = exchange_id)
		return render(request, 'crypto/trading/automatico/detail.html', {'exchange':exchange, })




class Trading_Automatic_Robos_View(LoginRequiredMixin, View):

	def get (self, request, exchange_id):
		exchange = get_object_or_404(Exchange, id  = exchange_id)	
		return render(request, 'crypto/trading/automatico/robos.html', {'exchange':exchange, })




class Trading_Automatic_View(LoginRequiredMixin, View):

	def get (self, request, exchange_id):
		exchange = get_object_or_404(Exchange, id  = exchange_id)
		from binance.client import Client

		API_KEY = "vBzARifEmC125fFXYwtZtzriL5pdWgHG2m7t2kHXIGjS9MmGTwugXgMpEdBheicm"
		API_SECRET = "4L8nNe7q1kaxiAhD2FDPHAt0XFlN0itHUkaSXBn0ksm1G4AGqt3tHnY4LVOc3eEF"

		client = Client(API_KEY, API_SECRET)
		candlesticks = client.get_klines(symbol='BNBBTC', interval=Client.KLINE_INTERVAL_15MINUTE)

		processend_clanlesticks = []

		for data in candlesticks:
			candlestick = {
				'time': data[0] / 1000,
				'open':data[1],
				'high':data[2],
				'low':data[3],
				'close':data[4]
			}
			processend_clanlesticks.append(candlestick)	
		

		return render(request, 'crypto/trading/automatico/trading.html', {
			'exchange':exchange, 'candlesticks':processend_clanlesticks, 
			
			})



class Trading_Automatic_history_View(LoginRequiredMixin, View):

	def get (self, request):
		api_key = "eiXlqiLwskSPqFuLgiShKAvXYN99xsi7k0gAMdELR1hu2e7Ah1DjZ9FRKcm7dzd5"
		api_secret = "VIFRVdvXd9eoKbwNtBMdEmvwNo6YRx6faczObnsva0gX3vywEdO7APvqtfKY4nfz"


		client = Client(api_key, api_secret)

		#candlesticks = client.get_historical_klines("CAKEUSDT", Client.KLINE_INTERVAL_5WEEK, "3 Mar, 2022")
		candlesticks = client.get_historical_klines('CAKEUSDT', Client.KLINE_INTERVAL_5MINUTE, '1 Jan, 2022',)

		processend_clanlesticks = []

		for data in candlesticks:
			candlestick = {
				'time': data[0] / 1000,
				'open':data[1],
				'high':data[2],
				'low':data[3],
				'close':data[4]

				}
			processend_clanlesticks.append(candlestick)

		return JsonResponse(processend_clanlesticks, safe=False)
