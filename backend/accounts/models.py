from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.managers import UserManager
# Create your models here.

AUTH_PROVIDERS ={'email':'email', 'google':'google', 'github':'github', 'linkedin':'linkedin'}

class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True, editable=False) 
    email = models.EmailField(
        max_length=255, verbose_name=_("Email Address"), unique=True
    )
    first_name = models.CharField(max_length=100, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=100, verbose_name=_("Last Name"))
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified=models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    situation = models.BooleanField('Situação financeira', blank=True, default=False)
    perfil = models.BooleanField('Perfil do Investidor', blank=True, default=False)
    auth_provider=models.CharField(max_length=50, blank=False, null=False, default=AUTH_PROVIDERS.get('email'))

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()

    def tokens(self):    
        refresh = RefreshToken.for_user(self)
        return {
            "refresh":str(refresh),
            "access":str(refresh.access_token)
        }


    def __str__(self):
        return self.email

    @property
    def get_full_name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"


class OneTimePassword(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    otp=models.CharField(max_length=6)


    def __str__(self):
        return f"{self.user.first_name} - otp code"
    


class Perfil(models.Model):

    STATUS_CHOICES = (

        ('Conservador','Conservador'),
        ('Moderado','Moderado'),
        ('Dinâmico','Dinâmico'),
        ('Arrojado','Arrojado'),
        ('Agressivo','Agressivo'),
        )

    id = models.BigAutoField(primary_key=True, editable=False) 
    investor = models.CharField(max_length = 190, choices = STATUS_CHOICES, default = 'Conservador', blank = True, null = True)
    description = models.TextField()
    risk_profile = models.CharField(max_length = 150, null = True)
    minimum = models.IntegerField()
    maximum = models.IntegerField()
    usuario = models.ManyToManyField('accounts.User', related_name = 'perfil_investidor', blank=True)
    color = models.CharField(max_length = 40)
   


    def __str__(self):
        return f'{self.investor}'



class Portfolio (models.Model):
    name = models.CharField(max_length= 400)
    description = models.TextField()
    risk = models.IntegerField(default = 0)




class Situacao(models.Model):

    STATUS_CHOICES = (

        ('investidor','Investidor'),
        ('equilibrado','Equilibrado'),
        ('endividado','Endividado'),
        
        )
    
    usuario = models.ManyToManyField('accounts.User', related_name = 'situacao_usuario', blank=True)
    condicao = models.CharField(max_length = 190, choices = STATUS_CHOICES, default = 'Conservador')
    goals = models.TextField( help_text="Objetivos Financeiros")
    situation = models.TextField( help_text="Situação Financeira Atua")
    risk = models.TextField( help_text="Tolerância ao Risco")
    horizon = models.TextField( help_text="Horizonte de Investimento")
    portfolio = models.ManyToManyField("accounts.Portfolio", help_text="Diversificação do Portfólio", blank=True)
    strategy  = models.TextField( help_text="Estratégia Financeira", blank=True )
    minimum = models.IntegerField()
    maximum = models.IntegerField()


    def __str__(self):
        return f'{self.condicao}'












