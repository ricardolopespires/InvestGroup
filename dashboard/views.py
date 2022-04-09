from django.views.generic import View, ListView, TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg, Count, Sum ,F, Q
from django.shortcuts import render, get_object_or_404
from accounts.models import User
from .models import Acoes
from datetime import date


#Gerando o data atual
data_atual =  date.today()

#Gerando o mês atual
month = data_atual.month


# Create your views here.

class DashboadTemplateView(LoginRequiredMixin, View):


    def get(self, request,):

        usuario = get_object_or_404(User, id = request.user.id)

        return render (request, 'dashboard/investing/index.html',{

            'month':month, 'usuario':usuario, 


            })



