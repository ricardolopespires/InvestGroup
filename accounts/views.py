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

# Create your views here.
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.db.models.query_utils import Q
from .tokens import account_activation_token




def loggin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username = username, password = password)

            try:
                user = User.objects.filter(user = user).last()
            except:
                pass

            if user.is_active == True:
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
                messages.info(request,'{}, O seu perfil de usuário ainda não está ativo, verifique a ativação no seu email'.format(usuario).title())
                return HttpResponseRedirect(reverse('login'))

                    

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
            termo = request.POST.get('termo')

            new_user = User.objects.create_user(username, email, password)

            if termo == 'on':
                new_user.termos = True
                new_user.save()

         
            mail_subject = "Ative sua conta de usuário."

            message = render_to_string("registration/activate_account.html", {

                'user': new_user,
                'domain': get_current_site(request).domain,
                'uid': urlsafe_base64_encode(force_bytes(new_user.pk)),
                'token': account_activation_token.make_token(new_user),
                "protocol": 'https' if request.is_secure() else 'http'
                })

          
            email = EmailMessage(mail_subject, message, to=[email])
            
            if email.send():
                messages.success(request, f'Prezado <b>{ new_user.username }</b>, vá até a caixa de entrada do seu e-mail <b>{email}</b> e clique no link de ativação recebido para confirmar e concluir o registro. <b>Observação:</b> Verifique sua pasta de spam.')
                return HttpResponseRedirect(reverse('login'))
                
            else:
                messages.error(request, f'Problema ao enviar e-mail para {email}, verifique se digitou corretamente.')
                return HttpResponseRedirect(reverse('login'))

          
        return render(request, 'registration/register.html')



class User_Activate_Email(View):

    def get(self, request, uidb64, token):
        
        User = get_user_model()
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except:
            user = None
        
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()

            messages.success(request, "Obrigado pela sua confirmação por e-mail. Agora você pode acessar sua conta.")
            return HttpResponseRedirect(reverse('login'))
        else:
            messages.error(request, "O link de ativação é inválido!")
            return HttpResponseRedirect(reverse('index'))
        
        return redirect('index')

        


class Password_Reset_View(View):

    def get(self, request):
        form = PasswordResetForm()
        return render(request, 'registration/password_reset.html',{'form':form,})
    
    def post(self, request):

        if request.method == 'POST':
            
            form = PasswordResetForm(request.POST)
            if form.is_valid():
                user_email = form.cleaned_data['email']
                associated_user = get_user_model().objects.filter(Q(email=user_email)).first()
               
                if associated_user:
                    subject = "Password Reset request"
                    message = render_to_string("registration/template_reset_password.html", {
                        
                        'user': associated_user,
                        'domain': get_current_site(request).domain,
                        'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
                        'token': account_activation_token.make_token(associated_user),
                        "protocol": 'https' if request.is_secure() else 'http'
                        
                        })
                    email = EmailMessage(subject, message, to=[associated_user.email])                    
                    return HttpResponseRedirect(reverse('index'))

                    if email.send():
                        messages.success(request,
                                         """
                                         <h2>Redefinição de senha enviada</h2><hr>
                                         <p>
                                            Enviamos um e-mail com instruções para definir sua senha, caso exista uma conta com o e-mail inserido.
                                            Você deve recebê-los em breve.<br>Se você não receber um e-mail, certifique-se de inserir o endereço com o qual você se registrou e verifique sua pasta de spam.
                                         </p>
                                         """
                                         )
                    else:
                        messages.error(request, "Problema ao enviar e-mail de redefinição de senha, <b>PROBLEMA DO SERVIDOR</b>")
                        return HttpResponseRedirect(reverse('index'))
                
                for key, error in list(form.errors.items()):
                    if key == 'captcha' and error[0] == 'Este campo é obrigatório.':
                        messages.error(request, "Você deve passar no teste reCAPTCHA")
                        continue
                    return HttpResponseRedirect(reverse('index'))
            
            else:
              
                messages.error(request, "Problema ao enviar e-mail de redefinição de senha, <b>PROBLEMA DO SERVIDOR</b>")
                return HttpResponseRedirect(reverse('index'))
            
        else:
                print()
                messages.error(request, "Problema ao enviar e-mail de redefinição de senha, <b>PROBLEMA DO SERVIDOR</b>")
                return HttpResponseRedirect(reverse('index'))















   
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


