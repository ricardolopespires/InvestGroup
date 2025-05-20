from django.conf import settings
# Create your models here.
from django.db import models

from django.utils import timezone

class Categoria(models.Model):
    TIPO_CHOICES = (
        ('RECEITA', 'Receita'),
        ('DESPESA', 'Despesa'),
    )
    
    nome = models.CharField(max_length=100, unique=True)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    img = models.ImageField(upload_to='categorias/', null=True, blank=True)  
    criado_em = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return f"{self.nome} ({self.tipo})"

class Receita(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, limit_choices_to={'tipo': 'RECEITA'})
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField(default=timezone.now)
    descricao = models.TextField(blank=True)
    criado_em = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'

    def __str__(self):
        return f"{self.categoria} - {self.valor} ({self.data})"

class Despesa(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, limit_choices_to={'tipo': 'DESPESA'})
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField(default=timezone.now)
    descricao = models.TextField(blank=True)
    criado_em = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Despesa'
        verbose_name_plural = 'Despesas'

    def __str__(self):
        return f"{self.categoria} - {self.valor} ({self.data})"