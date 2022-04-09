from django.views.generic import View, ListView, TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render


# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username = cd['username'], password =  cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Autenticação com sucesso')
                else:
                    return HttpResponse('Essa conta está desativada')
            else:
                return HttpResponse('Login inválido')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html',{'form':form})



def register(request):    
    return render(request, 'registration/register.html')













#---------------------------------------- PROFILE ----------------------------------------------------


class Profile_View(LoginRequiredMixin, View):

    def get(self, request, usuario_id):
        return render(request, 'profile/index.html')