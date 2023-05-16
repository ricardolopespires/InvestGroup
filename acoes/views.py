from .models import Categoria,Setor,SubSetor,Segmento,Empresa
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.db.models import Avg, Count, Sum ,F, Q
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.contrib import messages
from django.shortcuts import render
from googletrans import Translator
from django.urls import reverse
from datetime import date
from uuid import uuid4


# Create your views here.









class Setor_Templates_View(LoginRequiredMixin, View):
    
    def get(self, request):
        setores = Setor.objects.all()
        

        return render(request,'setores/index.html',{
            'setores':setores,
        })



class Setor_Detail_View(LoginRequiredMixin, View):
    def get(self, request, setor_id):
        
        setor = get_object_or_404(Setor, id = setor_id)
        empresas = Empresa.objects.filter(setor_id = setor.id)
        return render(request, 'setores/detail.html',{'setor':setor,'empresas':empresas,})



class Acao_Template_View(LoginRequiredMixin, View):

    def get(sekf, request, ativo_id):
        ativo = get_object_or_404(Empresa, id = ativo_id)       
        return render(request, 'acoes/index.html',{'ativo':ativo,})