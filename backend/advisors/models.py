from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User






class Asset(models.Model):
    """
    Modelo que representa um ativo financeiro.
    """
    name = models.CharField(max_length=255)
    alocation = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, default=0.00)
    advisor = models.ManyToManyField("advisors.Robo", related_name="assets", blank=True)

    class Meta:
        verbose_name = _("Ativo")
        verbose_name_plural = _("Ativos")

    def __str__(self):
        return self.name
        

class Robo(models.Model):
    """
    Modelo que representa um robô de trading.
    """
    name = models.CharField(
        max_length=255,
        verbose_name=_("Nome"),
        help_text=_("O nome do robô de trading.")
    )
    asset = models.ManyToManyField(
        'advisors.Asset',
        related_name='robots',       
        help_text=_("O ativo financeiro associado a este robô.")
    )
    user = models.ManyToManyField(
        'accounts.User',
        related_name='robots',
        blank=True,
        verbose_name=_("Usuários"),
        help_text=_("Usuários associados a este robô.")
    )
    description = models.TextField(
        blank=True,
        verbose_name=_("Descrição"),
        help_text=_("Descrição detalhada da estratégia do robô.")
    )   
    performance_fee = models.FloatField(
        default=0.0,
        verbose_name=_("Taxa de Performance"),
        help_text=_("Percentual da taxa de performance cobrada pelo robô.")
    )
    management_fee = models.FloatField(
        default=0.0,
        verbose_name=_("Taxa de Gestão"),
        help_text=_("Percentual da taxa de gestão cobrada pelo robô.")
    )
    rate = models.FloatField(
        default=0.0,
        verbose_name=_("Taxa de Retorno"),
        help_text=_("Taxa de retorno ou métrica de desempenho.")
    )
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00,
        verbose_name=_("Valor"),
        help_text=_("Valor total investido ou gerenciado.")
    )
    rebalancing = models.BooleanField(
        default=False,
        verbose_name=_("Rebalanceamento"),
        help_text=_("Indica se o robô suporta rebalanceamento automático.")
    )
    tax_inspection = models.BooleanField(
        default=False,
        verbose_name=_("Inspeção Tributária"),
        help_text=_("Indica se a inspeção tributária está habilitada para este robô.")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Criado em"),
        help_text=_("Data e hora em que o robô foi criado.")
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Atualizado em"),
        help_text=_("Data e hora da última atualização do robô.")
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Ativo"),
        help_text=_("Indica se o robô está atualmente ativo.")
    )

    class Meta:
        verbose_name = _("Robô")
        verbose_name_plural = _("Robôs")
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def get_summary(self):
        """
        Retorna um resumo das principais informações do robô.
        """
        return {
            'nome': self.name,
            'taxa_performance': f"{self.performance_fee:.2f}%",
            'taxa_gestao': f"{self.management_fee:.2f}%",
            'valor_gerenciado': f"R${self.amount:,.2f}",
            'ativo': "Sim" if self.is_active else "Não",
        }



class Level(models.Model):
    """
        Modelo que representa os níveis de risco do investidor,
    com perfil e alocação sugerida por classe de ativo.
    """
    RISK_CHOICES = (
        (1, "Conservador"),
        (3, "Moderado"),
        (2, "Agressivo"),
        (4, "Ultra Agressivo"),
    )
    advisor = models.ForeignKey(
        'advisors.robo',
        on_delete=models.CASCADE,
        related_name='levels',
        verbose_name=_("Orientador"),
        help_text=_("O orientador associado a este nível de risco.")
    )
    risk_level = models.IntegerField(choices=RISK_CHOICES, unique=True)     
    stock = models.IntegerField(default=0)
    crypto = models.IntegerField(default=0)
    forex = models.IntegerField(default=0) 
    commodities = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.advisor.name} - {self.get_risk_level_display()}"





class Performance(models.Model):
    """
    Modelo que representa métricas detalhadas de desempenho de um robô de trading.
    Registra indicadores financeiros para fornecer insights sobre o desempenho do robô.
    """
    robo = models.ForeignKey(
        'Robo',
        on_delete=models.CASCADE,
        related_name='performances',
        verbose_name=_("Robô"),
        help_text=_("O robô de trading associado a este registro de desempenho.")
    )
    date = models.DateField(
        verbose_name=_("Data"),
        help_text=_("Data do registro de desempenho.")
    )
    cumulative_return = models.FloatField(
        validators=[MinValueValidator(-100.0)],
        verbose_name=_("Retorno Cumulativo (%)"),
        help_text=_("Percentual de retorno acumulado desde o início.")
    )
    daily_return = models.FloatField(
        validators=[MinValueValidator(-100.0)],
        verbose_name=_("Retorno Diário (%)"),
        help_text=_("Percentual de retorno para este dia específico.")
    )
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00,
        verbose_name=_("Valor da Carteira"),
        help_text=_("Valor total da carteira gerenciada pelo robô nesta data.")
    )
    drawdown = models.FloatField(
        validators=[MinValueValidator(0.0)],
        verbose_name=_("Drawdown Atual (%)"),
        help_text=_("Percentual de drawdown atual em relação ao pico.")
    )
    max_drawdown = models.FloatField(
        validators=[MinValueValidator(0.0)],
        verbose_name=_("Drawdown Máximo (%)"),
        help_text=_("Maior percentual de drawdown observado até esta data.")
    )
    max_drawdown_duration = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        verbose_name=_("Duração do Drawdown Máximo (Dias)"),
        help_text=_("Maior duração do drawdown, em dias.")
    )
    sharpe_ratio = models.FloatField(
        null=True,
        blank=True,
        verbose_name=_("Índice Sharpe"),
        help_text=_("Métrica de retorno ajustado ao risco (maior é melhor).")
    )
    sortino_ratio = models.FloatField(
        null=True,
        blank=True,
        verbose_name=_("Índice Sortino"),
        help_text=_("Métrica de retorno ajustada ao risco de queda.")
    )
    volatility = models.FloatField(
        validators=[MinValueValidator(0.0)],
        verbose_name=_("Volatilidade Anualizada (%)"),
        help_text=_("Volatilidade dos retornos, em base anual.")
    )
    profit_factor = models.FloatField(
        validators=[MinValueValidator(0.0)],
        verbose_name=_("Fator de Lucro"),
        help_text=_("Relação entre lucros brutos e perdas brutas.")
    )
    win_rate = models.FloatField(
        validators=[MinValueValidator(0.0), MinValueValidator(100.0)],
        verbose_name=_("Taxa de Vitórias (%)"),
        help_text=_("Percentual de trades vencedores.")
    )
    trade_count = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        verbose_name=_("Número de Trades"),
        help_text=_("Quantidade de trades realizados nesta data.")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Criado em"),
        help_text=_("Data e hora em que o registro foi criado.")
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Atualizado em"),
        help_text=_("Data e hora da última atualização do registro.")
    )

    class Meta:
        verbose_name = _("Desempenho")
        verbose_name_plural = _("Desempenhos")
        ordering = ['robo__name', '-date']
        constraints = [
            models.UniqueConstraint(
                fields=['robo', 'date'],
                name='unique_robo_date'
            )
        ]
        indexes = [
            models.Index(fields=['robo', 'date']),
            models.Index(fields=['date']),
        ]

    def __str__(self):
        return f"{self.robo.name} - {self.date}"

    def get_risk_reward_ratio(self):
        """
        Calcula a relação risco-retorno com base no fator de lucro e na taxa de vitórias.
        Retorna None se os dados forem insuficientes.
        """
        if self.profit_factor > 0 and self.win_rate > 0:
            return self.profit_factor * (self.win_rate / 100)
        return None

    def get_performance_summary(self):
        """
        Retorna um resumo formatado das principais métricas de desempenho para exibição ao usuário.
        """
        return {
            'data': self.date,
            'retorno_cumulativo': f"{self.cumulative_return:.2f}%",
            'retorno_diario': f"{self.daily_return:.2f}%",
            'valor_carteira': f"R${self.amount:,.2f}",
            'drawdown_maximo': f"{self.max_drawdown:.2f}%",
            'indice_sharpe': f"{self.sharpe_ratio:.2f}" if self.sharpe_ratio else "N/D",
            'indice_sortino': f"{self.sortino_ratio:.2f}" if self.sortino_ratio else "N/D",
            'volatilidade': f"{self.volatility:.2f}%",
            'taxa_vitorias': f"{self.win_rate:.2f}%",
            'numero_trades': self.trade_count,
        }

    def is_profitable(self):
        """
        Retorna True se o retorno diário for positivo, False caso contrário.
        """
        return self.daily_return > 0
    




class Risk(models.Model):
    advisor = models.ForeignKey(
        'advisors.Robo',
        on_delete=models.CASCADE,
        related_name='risks',
        help_text="Robô responsável pela operação."
    )
    amount = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        help_text="Quantidade de operações ou contratos."
    )
    level = models.FloatField(
        default=0.00,
        validators=[MinValueValidator(0.0), MaxValueValidator(1.0)],
        help_text="Percentual de risco por operação (0.0 a 1.0)."
    )
    breakeven = models.IntegerField(
        default=0,
        help_text="Ponto de equilíbrio da operação em pontos ou unidades específicas."
    )

    def __str__(self):
        return f"{self.advisor.name} - Quantidade: {self.amount} | Risco: {self.level:.2%}"

    class Meta:
        verbose_name = "Configuração de Risco"
        verbose_name_plural = "Configurações de Risco"
        ordering = ['advisor']