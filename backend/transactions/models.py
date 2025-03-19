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