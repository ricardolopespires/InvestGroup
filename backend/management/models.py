from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
import uuid


class Asset(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, verbose_name="Nome do Ativo")
    ticker = models.CharField(max_length=20, unique=True, verbose_name="Ticker")
    img = models.ImageField(upload_to="asset/images", verbose_name="Imagem do Ativo")
    asset_type = models.CharField(
        max_length=50,
        choices=[
            ('STOCK', 'Ação'),
            ('COMMODITY', 'Commodity'),
            ('CRYPTO', 'Criptomoeda'),
            ('CURRENCY', 'Moeda (Forex)'),
            ('INDEX', 'Índice'),
            ('BOND', 'Título'),
            ('FUND', 'Fundo'),
            ('ETF', 'ETF'),
        ],
        verbose_name="Tipo de Ativo"
    )
    currency = models.CharField(
        max_length=5,
        choices=[
            ('USD', 'Dólar Americano'),
            ('BRL', 'Real Brasileiro'),
            ('EUR', 'Euro'),
            ('JPY', 'Iene Japonês'),
            ('GBP', 'Libra Esterlina'),
            ('OTHER', 'Outra')
        ],
        default='USD',
        verbose_name="Moeda"
    )
    sector = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Setor",
        help_text="Setor do ativo (ex.: Tecnologia, Energia, Financeiro), aplicável para Ações e ETFs"
    )
    volatility = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name="Volatilidade (%)",
        help_text="Volatilidade histórica do ativo em percentual"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        verbose_name = "Ativo"
        verbose_name_plural = "Ativos"

    def __str__(self):
        return f"{self.ticker} - {self.name} ({self.get_asset_type_display()})"


class InvestorProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, verbose_name="Nome do Perfil")
    risk_tolerance = models.CharField(
        max_length=20,
        choices=[
            ('CONSERVATIVE', 'Conservador'),
            ('MODERATE', 'Moderado'),
            ('AGGRESSIVE', 'Agressivo')
        ],
        verbose_name="Tolerância ao Risco"
    )
    max_exposure = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name="Exposição Máxima (%)",
        help_text="Percentual máximo do portfólio para um único ativo"
    )
    fixed_income_allocation = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name="Alocação em Renda Fixa (%)"
    )
    variable_income_allocation = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name="Alocação em Renda Variável (%)"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        verbose_name = "Perfil de Investidor"
        verbose_name_plural = "Perfis de Investidor"

    def __str__(self):
        return f"{self.name} ({self.get_risk_tolerance_display()})"


class Investidor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="investidor")
    renda_mensal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Renda Mensal")
    despesas_mensais = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Despesas Mensais")
    dividas = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Dívidas")
    investimentos = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Investimentos")
    reserva_emergencia = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Reserva de Emergência")
    tolerancia_risco = models.IntegerField(
        choices=((1, 'Baixa'), (2, 'Média'), (3, 'Alta')),
        default=1,
        verbose_name="Tolerância ao Risco"
    )
    horizonte_tempo = models.IntegerField(
        choices=((1, 'Curto prazo'), (2, 'Médio prazo'), (3, 'Longo prazo')),
        default=1,
        verbose_name="Horizonte de Tempo"
    )
    objetivo = models.CharField(
        max_length=50,
        choices=(('seguranca', 'Segurança'), ('crescimento', 'Crescimento'), ('especulacao', 'Especulação')),
        default='seguranca',
        verbose_name="Objetivo"
    )
    investor_profile = models.ForeignKey(
        InvestorProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Perfil de Investidor"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        verbose_name = "Investidor"
        verbose_name_plural = "Investidores"

    def __str__(self):
        return f"{self.usuario} - "

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
            return 'CONSERVATIVE'
        elif pontuacao <= 5:
            return 'MODERATE'
        else:
            return 'AGGRESSIVE'

    def save(self, *args, **kwargs):
        perfil_nome = self.determinar_perfil()
        profile, created = InvestorProfile.objects.get_or_create(
            risk_tolerance=perfil_nome,
            defaults={
                'name': perfil_nome.capitalize(),
                'max_exposure': 30 if perfil_nome == 'CONSERVATIVE' else 50 if perfil_nome == 'MODERATE' else 70,
                'fixed_income_allocation': 70 if perfil_nome == 'CONSERVATIVE' else 50 if perfil_nome == 'MODERATE' else 30,
                'variable_income_allocation': 30 if perfil_nome == 'CONSERVATIVE' else 50 if perfil_nome == 'MODERATE' else 70,
            }
        )
        self.investor_profile = profile
        super().save(*args, **kwargs)


class InvestmentOperation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, verbose_name="Ativo")
    investidor = models.ForeignKey(Investidor, on_delete=models.CASCADE, verbose_name="Investidor")
    operation_type = models.CharField(
        max_length=20,
        choices=[
            ('BUY', 'Compra'),
            ('SELL', 'Venda')
        ],
        verbose_name="Tipo de Operação"
    )
    quantity = models.PositiveIntegerField(verbose_name="Quantidade")
    unit_price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Preço Unitário")
    operation_date = models.DateTimeField(verbose_name="Data da Operação")
    total_value = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Valor Total", editable=False)
    risk_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name="Pontuação de Risco",
        help_text="Pontuação de risco calculada para a operação"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        verbose_name = "Operação de Investimento"
        verbose_name_plural = "Operações de Investimento"

    def save(self, *args, **kwargs):
        self.total_value = self.quantity * self.unit_price
        # Ajuste simples no risk_score com base no tipo de ativo
        base_risk = self.asset.volatility
        if self.asset.asset_type in ['CRYPTO', 'CURRENCY']:
            base_risk *= 1.5  # Aumenta risco para cripto e forex
        elif self.asset.asset_type == 'BOND':
            base_risk *= 0.5  # Reduz risco para títulos
        self.risk_score = min(base_risk, 100)  # Limita a 100
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.get_operation_type_display()} {self.asset.ticker} - {self.investidor.usuario.username} - {self.operation_date}"


class RiskAssessment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    operation = models.ForeignKey(InvestmentOperation, on_delete=models.CASCADE, verbose_name="Operação")
    risk_type = models.CharField(
        max_length=50,
        choices=[
            ('MARKET', 'Risco de Mercado'),
            ('CREDIT', 'Risco de Crédito'),
            ('LIQUIDITY', 'Risco de Liquidez'),
            ('OPERATIONAL', 'Risco Operacional'),
            ('CURRENCY', 'Risco Cambial'),
            ('COMMODITY', 'Risco de Commodity'),
        ],
        verbose_name="Tipo de Risco"
    )
    risk_level = models.CharField(
        max_length=20,
        choices=[
            ('LOW', 'Baixo'),
            ('MEDIUM', 'Médio'),
            ('HIGH', 'Alto')
        ],
        verbose_name="Nível de Risco"
    )
    description = models.TextField(verbose_name="Descrição", blank=True)
    assessment_date = models.DateTimeField(auto_now_add=True, verbose_name="Data da Avaliação")
    mitigation_strategy = models.TextField(verbose_name="Estratégia de Mitigação", blank=True)

    class Meta:
        verbose_name = "Avaliação de Risco"
        verbose_name_plural = "Avaliações de Risco"

    def __str__(self):
        return f"{self.get_risk_type_display()} - {self.operation}"