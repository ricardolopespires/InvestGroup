from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.

from datetime import date


data_atual = date.today()




class Usuario_View(LoginRequiredMixin, View):

    def get(self, request):



    	usuario =  [{'usuario':request.user.id} ]

    	try:
    		return JsonResponse({"id": usuario})
    	except:
    		return JsonResponse({"status": 1})




class Planejamento_Financeiro_View(LoginRequiredMixin, View):


	def get(self, request):

		month = data_atual.month
		
		return render(request, 'pessoal/planejamento/index.html',{'month':month,})





		