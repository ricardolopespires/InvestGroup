from django.conf import settings
from django.db import models
from decimal import Decimal
# Create your models here.







class Financeiro(models.Model):

    usuario = models.ForeignKey( settings.AUTH_USER_MODEL, verbose_name='Usuário', related_name='resets', on_delete = models.CASCADE)
    dinheiro = models.DecimalField(decimal_places=2, max_digits=10, default=0 , help_text = "Valor do capital em dinheiro")
    acoes = models.DecimalField(decimal_places=2, max_digits=10, default=0 , help_text = "Valor do capital em ações")
    crypto = models.DecimalField(decimal_places=2, max_digits=10, default=0 , help_text = "Valor do capital em crypto moedas")
    imobiliario = models.DecimalField(decimal_places=2, max_digits=10, default=0 , help_text = "Valor do capital em fundos imobiliario")
    capital = models.DecimalField(decimal_places=2, max_digits=10, default=0 , help_text = "Valor total do capital")
    updated = models.DateTimeField('Data da ultima atualização do Financeiro', auto_now_add = True, blank = True, )

    def __str__(self):
        return f'{self.usuario}'


    def save(self, *args, **kwargs):
        self.capital = self.dinheiro + self.acoes + self.crypto + self.imobiliario
        self.updated = timezone.localtime(timezone.now())
        
        super().save(*args, **kwargs)





class Movimentacao(models.Model):
    
    
    STATUS_TIPO =(
 
        ('-','-'),
        ('D','Debito'),
        ('C','Cretido')
    )

    STATUS_MODELO = (

    	('-','-'),
    	('dinheiro','Dinheiro'),
    	('ações','Ações'),
    	('crypto','Crypto'),
    	('imobiliario','Imobiliario'),

    	)

    id = models.CharField(primary_key = True, max_length = 150, help_text = "Numero indentificador da movimentação")
    username = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'sindico_movimentação', on_delete = models.CASCADE)
    institucao = models.CharField(max_length = 400, blank = True, help_text = 'A pessoa que faz o pagamento')
    data = models.DateTimeField(auto_now_add = False, help_text = "A data do movimento")
    descricao = models.TextField(help_text = "Descrição do movimento")
    tipo = models.CharField(max_length = 150, choices = STATUS_TIPO, default = '-', help_text = "O tipo do movimento bancario")
    modelo = models.CharField(max_length = 150, choices = STATUS_MODELO, default = '-', help_text = "O tipo do movimento bancario")
    valor = models.DecimalField(max_digits = 10, decimal_places = 2 ,help_text = "O valor do movimento")
    saldo = models.DecimalField(max_digits = 10, decimal_places = 2,  help_text = "O valor que ficou de saldo na conta")


    class Meta:

        ordering = ['valor']
        verbose_name = 'Movimentação'
        verbose_name_plural = 'Movimentações'


 

    def __str__(self):
        return f"{self.conta}"



