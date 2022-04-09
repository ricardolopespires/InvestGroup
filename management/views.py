from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.contrib import messages
from accounts.models import User
from django.urls import reverse
from .forms import API_Form
from .models import API
from uuid import uuid4



#Crie suas visualizações aqui.
class Settings_View(LoginRequiredMixin, View):

	def get(self, request):
		return render(request, 'management/settings.html')




#--------------------------------------------- Automação -----------------------------------------------

#Crie suas visualizações aqui.
class Settings_Api_View(LoginRequiredMixin, View):

	def get(self, request):
		apis = API.objects.filter( usuario = request.user)
		return render(request, 'management/automacao/api/index.html',{'apis':apis})



class Api_Detail_View(LoginRequiredMixin, View):

	def get(self, request, api_id):
		api = get_object_or_404(API, id = api_id)
		return render(request, 'management/automacao/api/detail.html',{'api':api,})


class Created_Api_View(LoginRequiredMixin, View):

	def get(self, request):

		codigo_api = 'API-' + str(uuid4()).split('-')[4]
		usuarios = User.objects.filter( name = request.user)

		print(codigo_api)

		return render(request, 'management/automacao/api/created.html',{'codigo_api':codigo_api,'usuarios':usuarios})


	def post(self, request):

		if request.method == 'POST':
			form = API_Form(request.POST or None, request.FILES or None)
			if form.is_valid():
				form.save( )
				messages.success(request, 'Sua nova API ja foi adicionada no sistema e liberada para uso')
				return HttpResponseRedirect(reverse('management:api'))

			else:
				print(form.errors)        
				messages.error(request, 'Os dados que foi preechido estão incorrentos')
				return HttpResponseRedirect(reverse('management:api'))