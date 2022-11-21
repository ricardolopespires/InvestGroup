from django.db import models
from accounts.models import User

# Create your models here.







class Perfil(models.Model):

    STATUS_CHOICES = (

        ('conservador','Conservador'),
        ('moderado','Moderado'),
        ('dinâmico','Dinâmico'),
        ('arrojado','Arrojado'),
        ('agressivo','Agressivo'),
        )

    id = models.CharField(max_length = 190, primary_key = True, unique = True)
    investor = models.CharField(max_length = 190, choices = STATUS_CHOICES, default = 'Conservador')
    description = models.TextField()
    risk_profile = models.CharField(max_length = 150,)
    minimum = models.IntegerField()
    maximum = models.IntegerField()
    usuarios = models.ManyToManyField('accounts.User', related_name = 'perfil_investidor')


    def __str__(self):
        return f'{self.investor}'






class Situacao(models.Model):

    STATUS_CHOICES = (

        ('investidor','Investidor'),
        ('equilibrado','Equilibrado'),
        ('endividado','Endividado'),
        
        )

    id = models.CharField(max_length = 190, primary_key = True, unique = True)
    condicao = models.CharField(max_length = 190, choices = STATUS_CHOICES, default = 'Conservador')
    description = models.TextField()    
    minimum = models.IntegerField()
    maximum = models.IntegerField()


    def __str__(self):
        return f'{self.condicao}'










