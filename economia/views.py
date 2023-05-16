from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.db.models import Avg, Count, Sum ,F, Q
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.contrib import messages
from django.shortcuts import render
from googletrans import Translator
from django.urls import reverse
from .models import Calendario, Continent, Currencie, Countrie
from datetime import date
from uuid import uuid4

import requests
import sys, os
import time
import json


data_atual = date.today()

translator = Translator()


# Create your views here.

class Calendario_Economico_View(LoginRequiredMixin, View):


	def get(self, request):

		

		calendario = Calendario.objects.filter( Q(data__day = data_atual.day), Q(data__month = data_atual.month), Q(data__year = data_atual.year))
		
		return render(request, 'economia/calendario/index.html',{'calendario':calendario})



class Create_Countrie(LoginRequiredMixin, View):

	def get(self, request):

		return render(request, 'economia/continents/created.html')

	def post(self, request):

		
		if request.method == 'POST':


			nome = request.POST.get('search')

			

			url = "https://restcountries.com/v3.1/name/"+str(nome)+"?fullText=true"
			#url = "https://restcountries.com/v3.1/all"

			resp = requests.get(url)
			status = str(requests.get(url))
		
			dados = resp.json()

			if resp.status_code == 404:
				messages.error(request, 'O Nome do país esta errado')
				return HttpResponseRedirect(reverse('economia:create_countrie'))
			else:

				#print(json.dumps(dados, indent=4, sort_keys=True, ensure_ascii=False))

				#qts  = len([x for x in dados[0]['borders']])

				id = uuid4()
				name = dados[0]['name']['common']			
				official = dados[0]['name']['official']	
				area = dados[0]['area']
				try:
					borders = [x for x in dados[0]['borders']]
				except:
					borders = 'não adicionadas'
				capital = dados[0]['capital'][0]
				continents = dados[0]['subregion'] 
				population = dados[0]['population']
				coatOfArms = dados[0]['coatOfArms']['png']
				idioma = [x for x in dados[0]['languages'].keys()][0]			
				languages =	dados[0]['languages'][idioma]
				moeda = [x for x in dados[0]['currencies'].keys()][0]			
				flags = dados[0]['flags']['png']



				if Continent.objects.filter(subregion = dados[0]['subregion']).exists():
					pass
				else:
					cont, created = Continent.objects.get_or_create(

						id = dados[0]['subregion'],
						region = dados[0]['region'],
						subregion = dados[0]['subregion']
						
						)

					
				

				continent = get_object_or_404(Continent, subregion = continents)

				

				


				if Countrie.objects.filter(name = name.title()).exists():
					pass
				else:			

					Countrie.objects.get_or_create(

						id = uuid4(),
						name = name,
						official = official,
						area = area,
						borders = borders,
						capital = capital,
						continents_id = continent.id,
						population = population,
						coatOfArms = coatOfArms,
						languages = languages,
						flags = flags,

						)

				moeda = [x for x in dados[0]['currencies'].keys()][0]	
				currencies = dados[0]['currencies'][moeda]

				

				if Currencie.objects.filter(name = currencies['name']).exists():

					currency = get_object_or_404(Currencie, name = currencies['name'])
					print(currency.paises)

				else :

					m, created =  Currencie.objects.get_or_create(

						id = moeda,
						name = currencies['name'],
						symbol = currencies['symbol'],

						)

					pais = get_object_or_404(Countrie, name = name)
					m.paises.add(pais)					
					m.save()

					moeda = get_object_or_404(Currencie, name = m)

					pais.currencies.add(moeda)
					pais.save()

					
				

				if continents == 'South America':
					return HttpResponseRedirect(reverse('economia:america_sul'))
				elif continents == 'Eastern Asia':
					return HttpResponseRedirect(reverse('economia:asia'))
				elif continents == 'North America':
					return HttpResponseRedirect(reverse('economia:america_norte'))
				elif continents == 'South Europe':
					return HttpResponseRedirect(reverse('economia:europa'))
				elif continents == 'Northern Europe':
					return HttpResponseRedirect(reverse('economia:europa'))
				elif continents == 'Western Europe':
					return HttpResponseRedirect(reverse('economia:europa'))
				else:
					return HttpResponseRedirect(reverse('economia:create_countrie'))




		


		
#--------------------------------------------- AMERICA DO SUL -----------------------------------------------------

class  Continents_America_Sul_View(LoginRequiredMixin, View):


	def get(self, request):
		paises = Countrie.objects.filter(continents = 'South America')
		print(paises)

		return render(request, 'economia/continents/america_sul/index.html',{'paises':paises})



class  Continents_America_Sul_Detail(LoginRequiredMixin, View):


	def get(self, request, paises_id):


		pais = get_object_or_404(Countrie, id = paises_id)

		return render(request, 'economia/continents/america_sul/detail.html',{'pais':pais})
 







#--------------------------------------------- ASIA ------------------------------------------------

class  Continents_Asia_View(LoginRequiredMixin, View):


	def get(self, request, ):


		paises = Countrie.objects.filter(continents = 'Eastern Asia')

		return render(request, 'economia/continents/asia/index.html',{'paises':paises})
 



class  Continents_Asia_Detail(LoginRequiredMixin, View):


	def get(self, request, paises_id):


		pais = get_object_or_404(Countrie, id = paises_id)

		return render(request, 'economia/continents/asia/detail.html',{'pais':pais})
 









#--------------------------------------------- AMERICA DO NORTE -----------------------------------------------------
class  Continents_America_Norte_View(LoginRequiredMixin, View):


	def get(self, request):


		paises = Countrie.objects.filter(continents = 'North America')

		return render(request, 'economia/continents/america_norte/index.html',{'paises':paises})
 


class  Continents_America_Norte_Detail(LoginRequiredMixin, View):


	def get(self, request, paises_id):


		pais = get_object_or_404(Countrie, id = paises_id)

		return render(request, 'economia/continents/america_norte/detail.html',{'pais':pais})
 



#--------------------------------------------- EUROPA ---------------------------------------------------------------

class  Continents_Europa_View(LoginRequiredMixin, View):


	def get(self, request):


		paises = Countrie.objects.filter(
			Q(continents = 'Northern Europe') | 
			Q(continents = 'Western Europe')|
			Q(continents = 'e242fe60-7573-4993-8a6c-4b7e2ffa315f'))

		return render(request, 'economia/continents/europa/index.html',{'paises':paises})
 

class  Continents_Europa_Detail(LoginRequiredMixin, View):


	def get(self, request, paises_id):


		pais = get_object_or_404(Countrie, id = paises_id)

		return render(request, 'economia/continents/europa/detail.html',{'pais':pais})
 
