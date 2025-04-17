from django.db import models

# Create your models here.

class Currency(models.Model):
    
    STATUS_CHOICES = (
        ("Maior", "Maior"),
        ("Menor", "Menor"),        
        ("Exotico", "Exotico"),            
    )
    
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=10)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="Maior")
    img = models.ImageField(upload_to='Flags', blank=True, null=True)  # Corrigido: removido o '/'
    yahoo = models.CharField(max_length=255)
    tradingview = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class Stock(models.Model):

    SECTOR_CHOICES = (
        ("Tecnologia da Informação", "Tecnologia da Informação"),
        ("Saúde", "Saúde"),
        ("Financeiro", "Financeiro"),
        ("Consumo Discricionário", "Consumo Discricionário"),
        ("Consumo Básico", "Consumo Básico"),
        ("Indústria", "Indústria"),
        ("Energia", "Energia"),
        ("Materiais", "Materiais"),
        ("Serviços de Utilidade Pública", "Serviços de Utilidade Pública"),
        ("Imobiliário", "Imobiliário"),
        ("Comunicação", "Comunicação"),
    )

    
    name = models.CharField(max_length=255)
    category = models.CharField(
        max_length=50,
        choices=SECTOR_CHOICES,
        default="Tecnologia da Informação",
        verbose_name="Categoria"
    )
    symbol = models.CharField(max_length=10)
    img = models.ImageField(upload_to='logo', blank=True, null=True)  # Corrigido: removido o '/'
    exchange = models.CharField(max_length=255)
    mt5 = models.CharField(max_length=255)
    signal_4h = models.CharField(max_length=255, blank=True, null=True)
    signal_1d = models.CharField(max_length=255, blank=True, null=True)
    signal_1w = models.CharField(max_length=255, blank=True, null=True)
    
 
       
        
    def __str__(self):
        return f"{self.category} - {self.name}"

    class Meta:
        verbose_name = "Ação"
        verbose_name_plural = "Ações"


class Commoditie(models.Model):
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=10)
    img = models.ImageField(upload_to='image')  # Corrigido: removido o '/'
    yahoo = models.CharField(max_length=255)
    tradingview = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class Index(models.Model):
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=10)
    img = models.ImageField(upload_to='image/flags')  # Corrigido: removido o '/'
    yahoo = models.CharField(max_length=255)
    tradingview = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
