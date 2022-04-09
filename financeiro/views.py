from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.db.models import Avg, Count, Sum ,F, Q
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from requests import Request, Session
from django.views.generic import View
from django.contrib import messages
from accounts.models import User
from django.urls import reverse
from datetime import datetime
from decimal import Decimal
from uuid import uuid4
import investpy
import json


#Gerando a data atual
data_atual = datetime.now()



# Create your views here.


class Manager_Capital_View(LoginRequiredMixin, View):

    def get(self, request):

        #Buscando a data atual
        month = data_atual.month

        instituicoes = investpy.stocks.get_stocks_dict(country='brazil', columns=None, as_json=False)
        print(instituicoes)

        return render(request, 'manager/index.html',{
        
            'month':month, 'instituicoes':instituicoes,
        
        })