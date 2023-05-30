from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Categoria, Renda
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








class CDI_View(LoginRequiredMixin,View):
	def get(self, request):
		return render(request, 'renda/fixa/cdb/list.html')




class LCA_View(LoginRequiredMixin,View):
	def get(self, request):
		return render(request, 'renda/fixa/lca/list.html')




class LCI_View(LoginRequiredMixin,View):
	def get(self, request):
		return render(request, 'renda/fixa/lci/list.html')



class Tesouro_Direto_View(LoginRequiredMixin,View):
	def get(self, request):
		return render(request, 'renda/fixa/tesouro/list.html')