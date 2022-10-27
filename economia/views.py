from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.db.models import Avg, Count, Sum ,F, Q
from django.http import HttpResponseRedirect
from .core import calendario_economico
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
				official = translator.translate(dados[0]['name']['official'], dest = 'pt').text		
				area = dados[0]['area']
				try:
					borders = [x for x in dados[0]['borders']]
				except:
					borders = 'não adicionadas'
				capital = dados[0]['capital'][0]
				continents = translator.translate(dados[0]['subregion'] , dest = 'pt').text
				population = dados[0]['population']
				coatOfArms = dados[0]['coatOfArms']['png']
				idioma = [x for x in dados[0]['languages'].keys()][0]			
				languages =	dados[0]['languages'][idioma]
				moeda = [x for x in dados[0]['currencies'].keys()][0]			
				flags = dados[0]['flags']['png']



				if Continent.objects.filter(subregion = translator.translate(dados[0]['subregion'], dest = 'pt').text).exists():
					pass
				else:
					cont, created = Continent.objects.get_or_create(

						id = uuid4(),
						region = dados[0]['region'],
						subregion = translator.translate(dados[0]['subregion'], dest = 'pt').text,
						
						)

					
				

				continent = get_object_or_404(Continent, subregion = continents)

				

				


				if Countrie.objects.filter(name = translator.translate(name.title(), dest = 'pt').text).exists():
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

					
				

				if continents == 'América do Sul':
					return HttpResponseRedirect(reverse('economia:america_sul'))
				elif continents == 'Ásia Oriental':
					return HttpResponseRedirect(reverse('economia:asia'))
				elif continents == 'América do Norte':
					return HttpResponseRedirect(reverse('economia:america_norte'))
				elif continents == 'Sul da Europa':
					return HttpResponseRedirect(reverse('economia:europa'))
				elif continents == 'Europa Ocidental':
					return HttpResponseRedirect(reverse('economia:europa'))
				else:
					return HttpResponseRedirect(reverse('economia:create_countrie'))




		





		


class  Continents_America_Sul_View(LoginRequiredMixin, View):


	def get(self, request):


		paises = Countrie.objects.filter(continents = '9c3bd8ad-4e33-4ba8-a1c8-dbf470c86535')
		print(paises)

		return render(request, 'economia/continents/america_sul/index.html',{'paises':paises})



class  Continents_America_Sul_Detail(LoginRequiredMixin, View):


	def get(self, request, pais_id):


		pais = get_object_or_404(Countrie, id = pais_id)

		return render(request, 'economia/continents/america_sul/detail.html',{'pais':pais})
 

 


class  Continents_Asia_View(LoginRequiredMixin, View):


	def get(self, request):


		paises = Countrie.objects.filter(continents = '29a4d861-23bb-466c-ada5-f0d615ac1359')

		return render(request, 'economia/continents/asia/index.html',{'paises':paises})
 


class  Continents_America_Norte_View(LoginRequiredMixin, View):


	def get(self, request):


		paises = Countrie.objects.filter(continents = '1f09fcb2-536f-4c03-b06e-2c18eaf38ba4')

		return render(request, 'economia/continents/america_norte/index.html',{'paises':paises})
 



class  Continents_Europa_View(LoginRequiredMixin, View):


	def get(self, request):


		paises = Countrie.objects.filter(
			Q(continents = 'abbcd99c-fc5e-41f2-bdf6-e33a7fa18acd') | 
			Q(continents = '4b3e9897-e69b-4474-b2bc-99021b58edff')|
			Q(continents = 'e242fe60-7573-4993-8a6c-4b7e2ffa315f'))

		return render(request, 'economia/continents/europa/index.html',{'paises':paises})
 