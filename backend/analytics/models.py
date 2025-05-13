from django.conf  import settings
from django.db import models
from accounts.models import User

class Investidor(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="investidores")   
    renda_mensal = models.DecimalField(max_digits=10, decimal_places=2)
    despesas_mensais = models.DecimalField(max_digits=10, decimal_places=2)
    dividas = models.DecimalField(max_digits=10, decimal_places=2)
    investimentos = models.DecimalField(max_digits=10, decimal_places=2)
    reserva_emergencia = models.DecimalField(max_digits=10, decimal_places=2)
    tolerancia_risco = models.IntegerField(choices=((1, 'Baixa'), (2, 'Média'), (3, 'Alta')), default=1)
    horizonte_tempo = models.IntegerField(choices=((1, 'Curto prazo'), (2, 'Médio prazo'), (3, 'Longo prazo')), default=1)
    objetivo = models.CharField(max_length=50, choices=(('seguranca', 'Segurança'), ('crescimento', 'Crescimento'), ('especulacao', 'Especulação')), default='seguranca')

    def __str__(self):
        return f"{self.nome} ({self.usuario.username})"

    def calcular_saude_financeira(self):
        renda_liquida = self.renda_mensal - self.despesas_mensais
        razao_divida_renda = self.dividas / self.renda_mensal if self.renda_mensal > 0 else 0
        cobertura_emergencia = self.reserva_emergencia / self.despesas_mensais if self.despesas_mensais > 0 else 0
        if razao_divida_renda > 0.4 or cobertura_emergencia < 3:
            return "Saúde financeira fraca"
        elif razao_divida_renda <= 0.2 and cobertura_emergencia >= 6:
            return "Saúde financeira forte"
        else:
            return "Saúde financeira moderada"

    def determinar_perfil(self):
        pontuacao = self.tolerancia_risco + self.horizonte_tempo
        if self.objetivo == 'seguranca':
            pontuacao -= 1
        elif self.objetivo == 'especulacao':
            pontuacao += 1
        if pontuacao <= 3:
            return "Conservador"
        elif pontuacao <= 5:
            return "Moderado"
        else:
            return "Agressivo"
        



class Perfil(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    objective = models.CharField(max_length=500, )
    time_horizon = models.CharField(max_length=500, )
    risk_tolerance = models.CharField(max_length=500, )
    preference = models.CharField(max_length=500, )
    sentence = models.CharField(max_length=500, )
    minimo = models.IntegerField( default = 0)
    maximo = models.IntegerField( default = 0)
    investidor = models.ManyToManyField(User, related_name="perfis", blank=True)
    fixa = models.IntegerField( default = 0)
    variável = models.IntegerField( default = 0)

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"

    def __str__(self):
        return f"Perfil de {self.nome}"
    

    

class Situacao(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    objective = models.CharField(max_length=500, )
    time_horizon = models.CharField(max_length=500, )
    risk_tolerance = models.CharField(max_length=500, )
    preference = models.CharField(max_length=500, )
    sentence = models.CharField(max_length=500, )    
    minimo = models.IntegerField( default = 0)
    maximo = models.IntegerField( default = 0)
    investidor = models.ManyToManyField(User, related_name="situaçao", blank=True)

    class Meta:
        verbose_name = "Situação"
        verbose_name_plural = "Situações"

    def __str__(self):
        return f"Situacao {self.nome}"