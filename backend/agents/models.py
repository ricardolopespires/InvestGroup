from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import uuid

class Asset(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    ticker = models.CharField(max_length=10, unique=True)
    asset_type = models.CharField(max_length=50, choices=[
        ('ação', 'Ação'),
        ('título', 'Título'),
        ('fundo', 'Fundo'),
        ('cripto', 'Criptomoeda'),
        ('commodities', 'Commodities'),
        ('moeda', 'Moeda'),      
        ('index', 'Índice'),
        ('opção', 'Opção'),       
        ('etf', 'ETF'),
        ('bdr', 'BDR'),
        ('fii', 'FII'),
        ('debênture', 'Debênture'),
        ('cdb', 'CDB'),
        ('lci', 'LCI'),
        ('lca', 'LCA'),
        ('tesouro direto', 'Tesouro Direto'),
        ('previdência', 'Previdência'),
        ('poupança', 'Poupança'),
        ('fundos imobiliários', 'Fundos Imobiliários'),
       

    ])

    price = models.DecimalField(max_digits=15, decimal_places=2)
    volatility = models.FloatField(help_text="Annualized volatility (e.g., 0.2 for 20%)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['ticker']),
        ]

    def __str__(self):
        return f"{self.name} ({self.ticker})"

class RiskProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    risk_level = models.CharField(max_length=20, choices=[
        ('conservador', 'Conservador'),
        ('moderado', 'Moderado'),
        ('agressivo', 'Agressivo')
    ])
    max_loss_tolerance = models.FloatField(help_text="Max percentage loss tolerance (e.g., 0.1 for 10%)")
    investment_horizon = models.IntegerField(help_text="Investment horizon in years")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.risk_level}"

class Portfolio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="portfolio_user", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    risk_profile = models.ForeignKey(RiskProfile, on_delete=models.SET_NULL, null=True)
    total_value = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.name}"

class PortfolioAllocation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='allocations')
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=15, decimal_places=4)
    allocation_percentage = models.FloatField(help_text="Percentage of portfolio (e.g., 0.25 for 25%)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(allocation_percentage__gte=0.0) & 
                                 models.Q(allocation_percentage__lte=1.0), 
                                 name='valid_allocation_percentage')
        ]

    def __str__(self):
        return f"{self.portfolio.name} - {self.asset.ticker} ({self.allocation_percentage*100}%)"

class InvestmentAgent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='investment_agents', blank=True)
    specialty = models.CharField(max_length=100, choices=[
        ('ação', 'Ação'),
        ('título', 'Título'),
        ('fundo', 'Fundo'),
        ('cripto', 'Criptomoeda'),
        ('commodities', 'Commodities'),
        ('moeda', 'Moeda'),      
        ('index', 'Índice'),
        ('opção', 'Opção'),       
        ('etf', 'ETF'),
        ('bdr', 'BDR'),
        ('fii', 'FII'),
        ('debênture', 'Debênture'),
        ('cdb', 'CDB'),
        ('lci', 'LCI'),
        ('lca', 'LCA'),
        ('tesouro direto', 'Tesouro Direto'),      
        ('fundos imobiliários', 'Fundos Imobiliários'), 
    ])
    portfolios = models.ManyToManyField(Portfolio, related_name='investment_agents', blank=True)
    description = models.TextField(blank=True, null=True)
    avatar =  models.ImageField(upload_to='agents/images/', blank=True, null=True)
    rating = models.FloatField(blank=True, null=True, default=0.0, help_text="Rating from 0 to 5") 
    reviews = models.IntegerField(default=0, help_text="Number of reviews received")
    name = models.CharField(max_length=100)
    experience = models.IntegerField(default=0, help_text="Experience in years")
    langchain_model = models.CharField(max_length=100, default="gpt-4", help_text="Language model used by LangChain")
    strategy = models.CharField(max_length=50, choices=[
        
        ('avesso ao risco', 'Averso ao risco'), 
        ('equilibrado', 'Equilibrado'),
        ('crescimento', 'Crescimento')
    ])
    config = models.JSONField(default=dict, help_text="LangChain agent configuration")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.strategy})"

class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='transactions')
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=20, choices=[
        ('buy', 'Buy'),
        ('sell', 'Sell')
    ])
    quantity = models.DecimalField(max_digits=15, decimal_places=4)
    price_per_unit = models.DecimalField(max_digits=15, decimal_places=2)
    total_amount = models.DecimalField(max_digits=15, decimal_places=2)
    executed_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['portfolio', 'executed_at']),
        ]

    def __str__(self):
        return f"{self.transaction_type} {self.quantity} {self.asset.ticker} at {self.executed_at}"

class AdvisorRecommendation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    agent = models.ForeignKey(InvestmentAgent, on_delete=models.CASCADE)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    recommendation_text = models.TextField()
    recommended_assets = models.ManyToManyField(Asset, blank=True)
    risk_assessment = models.JSONField(default=dict, help_text="Risk analysis details")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recommendation for {self.portfolio.name} at {self.created_at}"