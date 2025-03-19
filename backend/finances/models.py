from django.conf import settings
from django.db import models



class Portfolio(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome



class Investment(models.Model):
    TIPO_INVESTIMENTO = (
        ('ACOES', 'Ações'),
        ('RENDA_FIXA', 'Renda Fixa'),
        ('FUNDOS', 'Fundos'),
        ('CRIPTO', 'Criptomoedas'),
    )
    
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_INVESTIMENTO)
    valor_investido = models.DecimalField(max_digits=12, decimal_places=2)
    data_compra = models.DateField()
    valor_atual = models.DecimalField(max_digits=12, decimal_places=2)
    
    def __str__(self):
        return f"{self.nome} - {self.tipo}"