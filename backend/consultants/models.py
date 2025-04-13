from django.core.validators import MaxValueValidator, MinValueValidator 
from django.db import models

# Create your models here.

class Asset(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    asset_type = models.CharField(
        max_length=20,
        choices=[('stock', 'Ação'), ('bond', 'Título'), ('fund', 'Fundo'), ('other', 'Outro')],
        default='stock'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Advisor(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='advisors/', blank=True, null=True)
    description = models.TextField()
    assest = models.ManyToManyField(Asset, related_name='advisors') 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name



class Skill(models.Model):
    advisor = models.ForeignKey(Advisor, on_delete=models.CASCADE, related_name='skills')
    market = models.IntegerField(
        validators=[
            MinValueValidator(1), 
            MaxValueValidator(100)
            ])
    analytics = models.IntegerField(
        validators=[
            MinValueValidator(1), 
            MaxValueValidator(100)
            ])
    strategy = models.IntegerField(
        validators=[
            MinValueValidator(1), 
            MaxValueValidator(100)
            ])
    planning = models.IntegerField(
        validators=[
            MinValueValidator(1), 
            MaxValueValidator(100)
            ])
    risk = models.IntegerField(
        validators=[
            MinValueValidator(1), 
            MaxValueValidator(100)
            ])
    operations = models.IntegerField(
        validators=[
            MinValueValidator(1), 
            MaxValueValidator(100)
            ])
    report = models.IntegerField(
        validators=[
            MinValueValidator(1), 
            MaxValueValidator(100)
            ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.advisor
            
    


from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User  # Para vincular ao consultor, se desejar

# Modelos existentes (assumidos)
class Asset(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    asset_type = models.CharField(
        max_length=20,
        choices=[('stock', 'Ação'), ('bond', 'Título'), ('fund', 'Fundo'), ('other', 'Outro')],
        default='stock'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Advisor(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='advisors/', blank=True, null=True)
    description = models.TextField()
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='advisors', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Gerenciamento de Carteira
class Portfolio(models.Model):
    name = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255)  # Nome do cliente
    advisor = models.ForeignKey(Advisor, on_delete=models.CASCADE, related_name='portfolios')
    total_value = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def update_total_value(self):
        # Calcula o valor total baseado nos ativos da carteira
        total = sum(pa.current_value for pa in self.assets.all())
        self.total_value = total
        self.save()

    def __str__(self):
        return f"{self.name} - {self.client_name}"

class PortfolioAsset(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='assets')
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='portfolio_assets')
    quantity = models.DecimalField(max_digits=15, decimal_places=4)  # Quantidade do ativo
    purchase_price = models.DecimalField(max_digits=15, decimal_places=2)  # Preço de compra por unidade
    current_price = models.DecimalField(max_digits=15, decimal_places=2)  # Preço atual por unidade
    current_value = models.DecimalField(max_digits=15, decimal_places=2, editable=False)  # Valor total atual

    def save(self, *args, **kwargs):
        # Calcula o valor atual automaticamente
        self.current_value = self.quantity * self.current_price
        super().save(*args, **kwargs)
        # Atualiza o valor total da carteira
        self.portfolio.update_total_value()

    def __str__(self):
        return f"{self.asset.name} ({self.portfolio.name})"

# Gerenciamento de Risco
class RiskProfile(models.Model):
    client_name = models.CharField(max_length=255, unique=True)
    risk_level = models.CharField(
        max_length=20,
        choices=[('conservative', 'Conservador'), ('moderate', 'Moderado'), ('aggressive', 'Agressivo')],
        default='moderate'
    )
    max_loss_tolerance = models.DecimalField(
        max_digits=5, decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Tolerância máxima de perda em %"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.client_name} - {self.get_risk_level_display()}"

class RiskAssessment(models.Model):
    portfolio = models.OneToOneField(Portfolio, on_delete=models.CASCADE, related_name='risk_assessment')
    risk_profile = models.ForeignKey(RiskProfile, on_delete=models.SET_NULL, null=True, related_name='assessments')
    volatility = models.DecimalField(
        max_digits=5, decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Volatilidade estimada em %"
    )
    value_at_risk = models.DecimalField(
        max_digits=15, decimal_places=2,
        help_text="Valor em risco (VaR) estimado"
    )
    assessment_date = models.DateTimeField(auto_now=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Avaliação de Risco - {self.portfolio.name}"