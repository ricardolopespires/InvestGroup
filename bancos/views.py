from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Bandeira, Cartao, Fatura
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg, Count, Sum ,F, Q
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse
from decimal import Decimal
from datetime import date
from uuid import uuid4
import math


data_atual = date.today()
month = data_atual.month

















#--------------------------------------- Cartão de Credito / Debito ---------------------------------------



class Cartao_Template_View(LoginRequiredMixin, View):

	def get(self, request):
		cartoes = Cartao.objects.all()
		return render(request, 'bancos/cartoes/list.html',{'cartoes':cartoes, })



class Cartao_Details_View(LoginRequiredMixin, View):

	def get(self, request, pk):

		cartao = get_object_or_404(Cartao, id = pk)
		
		return render(request, 'bancos/cartoes/detials.html',{'cartao':cartao})



class Cartao_Create_View(LoginRequiredMixin, View):

	def get(self, request):
		bandeiras = Bandeira.objects.all()
		return render(request, 'bancos/cartoes/form.html',{

			'bandeiras':bandeiras,

			})


	def post(self, request):
		if request.method == 'POST':
			nome = request.POST.get("nome")
			numero = request.POST.get("numero")
			instituicao = request.POST.get("instituicao")
			vencimento = request.POST.get("vencimento")
			limite = request.POST.get("limite")
			bandeiras = request.POST.getlist("bandeiras")

			print(bandeiras)


			Cartao.objects.get_or_create(

				numero = numero,
				user_id = request.user.id,
				instituicao = instituicao, 
				nome = nome,
				bandeira_id  = bandeiras[0],				
				vencimento = vencimento,
				limite = limite,

				)

			messages.success(request,"O novo cartão foi adicionado")
			return HttpResponseRedirect(reverse('bancos:cartao'))




