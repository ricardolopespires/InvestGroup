from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)
from phone_field import PhoneField
from django.core import validators
from django.utils import timezone 
from django.conf import settings
from django.db import models
from decimal import Decimal
from .core import idade
import re





class User(AbstractBaseUser, PermissionsMixin):


    STATUS_CHOICES = (
                        ('ativos','Ativos'),
                        ('pendentes','Pendentes'),
                        ('inativos','Inativos'),
                     )

    username = models.CharField(
        'Nome de Usuário', max_length=30, unique=True, 
        validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
            'O nome de usuário só pode conter letras, digitos ou os '
            'seguintes caracteres: @/./+/-/_', 'invalid')]
    )
    email = models.EmailField('E-mail', unique=True)
    name = models.CharField('Nome', max_length=100, blank=True)
    address = models.CharField('Endereço', max_length = 190, blank = True)
    date_of_birth = models.DateTimeField(default=timezone.now) 
    state = models.CharField('Estado',  max_length = 100, blank = True)
    status = models.CharField(max_length = 100, choices = STATUS_CHOICES, default = 'projeto')
    city = models.CharField('Cidade', max_length = 190, blank = True)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    is_active = models.BooleanField('Está ativo?', blank=True, default=False)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=False)
    situation = models.BooleanField('Situação financeira', blank=True, default=False)
    perfil = models.BooleanField('Perfil do Investidor', blank=True, default=False)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)
    img = models.ImageField(upload_to = 'user')
    termos = models.BooleanField( default = False)
  
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name or self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    
 


class Planejamento(models.Model):
    id = models.CharField(max_length  = 110, primary_key = True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'usuário_planejamento', on_delete = models.CASCADE)   
    pms = models.DecimalField( max_digits = 10, decimal_places = 2, default=0 , help_text = "Patrimônio Mínimo de Sobrevivência")
    pmr = models.DecimalField( max_digits = 10, decimal_places = 2, default=0 , help_text = "Patrimônio Mínimo Recomendado para sua Segurança")
    pi = models.DecimalField( max_digits = 10, decimal_places = 2, default=0 , help_text = "Patrimônio Ideal para sua idade e situação de Consumo")
    pnif = models.DecimalField( max_digits = 10, decimal_places = 2, default=0 , help_text = "Patrimônio Necessário para a Independência Financeira")
    estabilidade = models.BooleanField(default = False, help_text = "O tipo de empregabilidade")

    class Meta:
        verbose_name = 'Planejamento'
        verbose_name_plural = 'Planejamentos'


    def save(self, *args, **kwargs):

        if self.estabilidade == True:
            self.pmr = ( 12 * self.pms )
        else:
            self.pmr = ( 20 * self.pms )

        self.pi = (( 12 * self.pms ) * idade(self.user.date_of_birth.year))
        self.pnif = ((12 * self.pms) / Decimal(0.08))
       


        super().save(*args, **kwargs)








class Financeiro(models.Model):

    id = models.CharField(max_length  = 110, primary_key = True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'usuário_financeiro', on_delete = models.CASCADE)   
    dinheiro = models.FloatField( default=0 , help_text = "Valor do capital em dinheiro")
    acoes = models.FloatField( default=0 , help_text = "Valor do capital em ações")
    crypto = models.FloatField( default=0 , help_text = "Valor do capital em crypto moedas")
    imobiliario = models.FloatField( default=0 , help_text = "Valor do capital em fundos imobiliario")
    forex = models.FloatField( default=0 , help_text = "Valor do capital em forex")   
    balanco = models.FloatField( default=0 , help_text = "Valor do balanço do capital ")
    capital = models.FloatField( default=0 , help_text = "Valor total do capital")
    retorno = models.FloatField( default=0 , help_text = "Valor do retorno em capital ")


    def __str__(self):
        return f'{self.user}'


    def save(self, *args, **kwargs):


        self.capital = self.acoes + self.crypto + self.imobiliario + self.forex 
        self.balanco =  self.dinheiro + self.capital
        self.retorno = ((self.capital - self.balanco) / self.balanco) 
        super().save(*args, **kwargs)






class Movimentacoes(models.Model):

    STATUS_CHOICES = (

        ('deposito', 'deposito'),
        ('retirada','retirada'),
        ('transferencia','transferencia'),
        )


    STATUS_TIPO = (

        ('acoes','acoes'),
        ('crypto','crypto'),
        ('imobiliario','investimento'),
        ('forex','forex'),
        ('movimentocao','movimetacao'),
        )

    id = models.CharField(max_length  = 110, primary_key = True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'movimetação_financeira', on_delete = models.CASCADE)
    operacao = models.CharField( max_length = 110, choices = STATUS_CHOICES, default ='deposito', help_text = 'transferência do capital')
    tipo = models.CharField(max_length = 110, choices = STATUS_TIPO, default = 'acoes', help_text = 'O tipo da movimento')
    data = models.DateTimeField(auto_now_add = False)
    descricao  = models.TextField(help_text = 'Descrição da movimentação')
    valor  = models.FloatField(help_text = 'O valor total do usuário')



    def __str__(self):
        return f'{self.operacao}'







class Perfil(models.Model):

    STATUS_CHOICES = (

        ('conservador','Conservador'),
        ('moderado','Moderado'),
        ('dinâmico','Dinâmico'),
        ('arrojado','Arrojado'),
        ('agressivo','Agressivo'),
        )

    id = models.CharField(max_length = 190, primary_key = True, unique = True)
    investor = models.CharField(max_length = 190, choices = STATUS_CHOICES, default = 'Conservador', blank = True, null = True)
    description = models.TextField()
    risk_profile = models.CharField(max_length = 150, null = True)
    minimum = models.IntegerField()
    maximum = models.IntegerField()
    usuario = models.ManyToManyField('accounts.User', related_name = 'perfil_investidor', blank=True)


    def __str__(self):
        return f'{self.investor}'






class Situacao(models.Model):

    STATUS_CHOICES = (

        ('investidor','Investidor'),
        ('equilibrado','Equilibrado'),
        ('endividado','Endividado'),
        
        )
    
    usuario = models.ManyToManyField('accounts.User', related_name = 'situacao_usuario', blank=True)
    condicao = models.CharField(max_length = 190, choices = STATUS_CHOICES, default = 'Conservador')
    description = models.TextField()    
    minimum = models.IntegerField()
    maximum = models.IntegerField()


    def __str__(self):
        return f'{self.condicao}'











