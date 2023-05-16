from .serializers import PerfilUserSerialiser, SituacaoUserSerialiser, UserSerializer, Situacao_User_Updated_Serialiser
from django.views.generic import View, ListView, TemplateView, DetailView
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg, Count, Sum ,F, Q
from django.shortcuts import redirect, reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from .forms import LoginForm, RegisterForm
from .models import User, Perfil, Situacao
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render
from datetime import date, datetime


# Create your views here.





def loggin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                if user.groups.filter(name='Administrador').exists() == True:
                    login(request,user)
                    #Redirect to success page.
                    form = LoginForm()
                    return redirect('management:manager')                
                else:
                    login(request,user)
                    #Redirect to success page.
                    form = LoginForm()
                    data = user.date_joined.strftime('%Y-%m-%d')
                    
                    if request.user.situation == False:
                        messages.info(request,'{}, Conheça mais sobre sua relação com o dinheiro e como pode fazer dele seu aliado!!!!'.format(user).title())
                        return HttpResponseRedirect(reverse('quiz:financial_situation'))

                    elif  str(data) == str(date.today()):
                        messages.info(request,'{}, sabia que ser fiel ao seu perfil de investidor (ou suitability) pode fazer a diferença na hora de ter sucesso em suas aplicações financeiras?'.format(user).title())
                        return HttpResponseRedirect(reverse('quiz:perfil_investidor'))

                    elif request.user.perfil == False:
                        messages.info(request,'{}, sabia que ser fiel ao seu perfil de investidor (ou suitability) pode fazer a diferença na hora de ter sucesso em suas aplicações financeiras?'.format(user).title())
                        return HttpResponseRedirect(reverse('quiz:perfil_investidor'))
                    else:
                        return redirect('dashboard:manager')
                    

    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


User = get_user_model()



class Register_User_View(View):


    def get(self, request):
        return render(request, 'registration/register.html')



    def post(self, request):
        if request.method == 'POST':

        
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('pass1')

            is_investidor = True
            is_active = True

            new_user = User.objects.create_user(username, email, password)
            messages.success(request,'O seu usuário foi criado com sucesso!!!!')
            return HttpResponseRedirect(reverse('login'))
        return render(request, 'registration/register.html',{'form':form})

   
def profile_users(request):
    profiles = User.objects.all()    
    
    return render(request, 'profile/profile.html',{'profiles':profiles})


def profile_details(request, pk):
    user_profile = get_object_or_404(User, id = pk)     

    return render(request, 'profile/details.html',{'user_profile':user_profile, })





class Perfil_Investor_View(LoginRequiredMixin, View):



    def get(self, request):

        return render(request, 'perfil/list.html')



#-------------------------------------- Api Perfil User ------------------------------------------------------




@api_view(['GET'])
def perfilList(request):
    perfis = Perfil.objects.all().order_by('-id')
    serializer = PerfilUserSerialiser(perfis, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def perfilDetail(request, pk):
    perfis = Perfil.objects.get(id = pk)
    serializer = PerfilUserSerialiser(perfis, many = False)
    return Response(serializer.data)


@api_view(['POST'])
def  perfilCreate(request):
    serializer = PerfilUserSerialiser(data = request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
    


@api_view(['POST'])
def perfilUpdate(request, pk):
    perfis = Perfil.objects.get(id = pk)    
    serializer = PerfilUserSerialiser(instance = perfis, data = request.data)    
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['DELETE'])
def perfilDelete(request, pk):
    perfis = Perfil.objects.get(id = pk)
    serializer = PerfilUserSerialiser(instance = perfis, data = request.data)

    if serializer.is_valid():
        serializer.delete()

    return Response({'message': 'O Perfil foi excluído com sucesso!'}, status = status.HTTP_204_NO_CONTENT)






#-------------------------------------- Api Situação User  ------------------------------------------------------




@api_view(['GET'])
def situacaoList(request):
    situacao = Situacao.objects.all().order_by('-id')
    serializer = SituacaoUserSerialiser(situacao, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def situacaoDetail(request, pk):
    situacao = Situacao.objects.get(id = pk)
    serializer = SituacaoUserSerialiser(situacao, many = False)
    return Response(serializer.data)


@api_view(['POST'])
def  situacaoCreate(request):
    serializer = SituacaoUserSerialiser(data = request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
    


@api_view(['POST'])
def situacaoUpdate(request, pk):
    situacao = Situacao.objects.get(id = pk)    
    serializer = Situacao_User_Updated_Serialiser(instance = situacao, data = request.data)    
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['DELETE'])
def situacaoDelete(request, pk):
    situacao = Situacao.objects.get(id = pk)
    serializer = SituacaoUserSerialiser(instance = situacao, data = request.data)

    if serializer.is_valid():
        serializer.delete()

    return Response({'message': 'O situacao foi excluído com sucesso!'}, status = status.HTTP_204_NO_CONTENT)


