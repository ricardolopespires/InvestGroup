from django.db import models

# Create your models here.

class Currency(models.Model):
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=10)
    img = models.ImageField(upload_to='Flags')  # Corrigido: removido o '/'
    yahoo = models.CharField(max_length=255)
    tradingview = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class Stock(models.Model):
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=10)
    img = models.ImageField(upload_to='logo')  # Corrigido: removido o '/'
    yahoo = models.CharField(max_length=255)
    tradingview = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


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
