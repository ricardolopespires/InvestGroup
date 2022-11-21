from django.views.generic import View, ListView, TemplateView, DetailView
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg, Count, Sum ,F, Q
from django.shortcuts import redirect, reverse
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from django.http import HttpResponse
from django.contrib import messages
from datetime import date, datetime
from django.shortcuts import render
from rest_framework import generics
from django.http import JsonResponse
from accounts.models import User
from .models import Perfil
from uuid import uuid4








class Perfil_Investor_View(LoginRequiredMixin, View):



	def get(self, request):

		return render(request, 'perfil/list.html')







#--------------------------------------------- API  -----------------------------------------------------------------


class Api_Perfil_View(LoginRequiredMixin, View):

	def get(self, request):

		if request.method == "GET":

			a ={'conservador':{'max':" ",'min':" "},
				'moderado':{'max':" ",'min':" "},
				'arrojado':{'max':" ",'min':" "},
				'agressivo':{'max':" ",'min':" "},
				}

			try:

				investidor = []
				for perfil in Perfil.objects.all():					

					if perfil.investor == 'conservador':
						a['conservador']['max'] = perfil.maximum
						a['conservador']['min'] = perfil.minimum
						

					elif perfil.investor == 'moderado':
						a['moderado']['max'] = perfil.maximum
						a['moderado']['min'] = perfil.minimum

					elif perfil.investor == 'arrojado':
						a['arrojado']['max'] = perfil.maximum
						a['arrojado']['min'] = perfil.minimum

					elif perfil.investor == 'agressivo':
						a['agressivo']['max'] = perfil.maximum
						a['agressivo']['min'] = perfil.minimum

				
				investidor.append(a)


				return JsonResponse({"perfil": investidor})
			except:
				return JsonResponse({"status": 1})