from django.conf import settings # Importando o modelo de usuário do Django

from django.db import models

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=[('RECEITA', 'Receita'), ('DESPESA', 'Despesa'), ('INVESTIMENTO', 'Investimento')])
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Transacao(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    descricao = models.TextField(blank=True)
    tipo = models.CharField(max_length=20, choices=[('RECEITA', 'Receita'), ('DESPESA', 'Despesa'), ('INVESTIMENTO', 'Investimento')])

    def __str__(self):
        return f"{self.descricao} - {self.valor}"



class Operation(models.Model):
    CHOICE_TYPE = (
        ('sell', 'sell'),
        ('buy', 'buy'),
    )
    id = models.IntegerField(primary_key=True)
    asset = models.CharField(max_length=60, )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    entry = models.DateTimeField(auto_now_add=True )
    type = models.CharField(max_length=20, choices=CHOICE_TYPE, default='buy')
    volume = models.FloatField()
    price_entry = models.DecimalField(max_digits=10, decimal_places=2)
    sl = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_departure = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    profit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    stoploss = models.BooleanField(default=False)
    takeprofit = models.BooleanField(default=False)

    

    def __str__(self):
        return f"{self.tipo} - {self.transacao.descricao}"