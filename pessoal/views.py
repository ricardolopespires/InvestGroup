from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg, Count, Sum ,F, Q
from django.http import HttpResponseRedirect
from .models import Categoria, Movimentacao
from django.views.generic import View
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse
from decimal import Decimal
from datetime import date
from uuid import uuid4



data_atual = date.today()




class Usuario_View(LoginRequiredMixin, View):

    def get(self, request):



    	usuario =  [{'usuario':request.user.id} ]

    	try:
    		return JsonResponse({"id": usuario})
    	except:
    		return JsonResponse({"status": 1})





class Receitas_Mensal_View(LoginRequiredMixin, View):

	def get(self, request):
		categorias = Categoria.objects.filter( status = 'receitas')
		return render(request, 'pessoal/manager/receitas/form.html',{'categorias':categorias})


	def post(self, request):
		if request.method == 'POST':

			valor = request.POST.get('valor')
			data = request.POST.get('data')
			descricao = request.POST.get('descricao')
			categoria = request.POST.get('categoria')
			observacao = request.POST.get('observacao')
			option  = request.POST.get('option')
			moeda = request.POST.get('moeda')

		

			if option == '1':
				fixa = True
				repetir = False
				quantidade = 0
				tempo = 0

			elif option =='2':
				fixa = False
				repetir = True
				quantidade = request.POST.get('quantidade')
				tempo = request.POST.get('tempo')

			else:
				messages.error(request,'Você esqueceu de dizer se sua renda e fixa ou variável')
				return HttpResponseRedirect(reverse('pessoal:add_receitas'))

			


			
			m , create = Movimentacao.objects.get_or_create(


				id = str(uuid4())[:9],				
				status = "receitas",
				valor = Decimal(valor),
				categoria_id = categoria,
				moeda = moeda,
				created = data,
				updated = data,
				descricao = descricao,
				fixa = fixa,
				repetir = repetir,
				quantidade = quantidade,
				tempo = tempo,

				)

			m.user.add(request.user.id)
			
			messages.success(request, "A sua Receita no valor {} foi adicionada com sucesso".format(valor))
			return HttpResponseRedirect(reverse('pessoal:manager'))








class List_Pessoal_Financeiro(LoginRequiredMixin, View):


	def get(self, request):

		month = data_atual.month
		movimentos = Movimentacao.objects.filter(Q(created__month = data_atual.month),Q(created__year = data_atual.year))

		print(movimentos)
		
		return render(request, 'pessoal/list.html',{

			'month':month,
			'movimentos':movimentos,


			})





		