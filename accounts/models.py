import re
from phone_field import PhoneField
from django.db import models
from django.core import validators
from django.utils import timezone 
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)
from django.conf import settings


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
    is_active = models.BooleanField('Está ativo?', blank=True, default=True)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=False)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)
    img = models.ImageField(upload_to = 'user')
    dinheiro = models.FloatField( default=0 , help_text = "Valor do capital em dinheiro")
    acoes = models.FloatField( default=0 , help_text = "Valor do capital em ações")
    crypto = models.FloatField( default=0 , help_text = "Valor do capital em crypto moedas")
    imobiliario = models.FloatField( default=0 , help_text = "Valor do capital em fundos imobiliario")
    investimento = models.FloatField( default=0 , help_text = "Valor do capital investido")
    retorno = models.FloatField( default=0 , help_text = "Valor do retorno em capital ")
    balanco = models.FloatField( default=0 , help_text = "Valor do balanço do capital ")
    capital = models.FloatField( default=0 , help_text = "Valor total do capital")

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

    def save(self, *args, **kwargs):
        self.capital = self.dinheiro + self.acoes + self.crypto + self.imobiliario 
        self.investimento = self.acoes + self.crypto + self.imobiliario
        super().save(*args, **kwargs)




 