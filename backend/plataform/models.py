from django.conf import settings
from django.db import models

# Create your models here.


class CryptoAPI(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Ex.: "binance"
    api_key = models.CharField(max_length=255)
    api_secret = models.CharField(max_length=255, blank=True, null=True)
    endpoint = models.URLField(blank=True, null=True)
    broker_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.broker_name}"
    


class Account(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"

    def __str__(self):
        return self.nome      


    

class Broker(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=255)
    account = models.ManyToManyField(Account)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Broker"
        verbose_name_plural = "Brokers"
        

    def __str__(self):
        return self.name
        

     



class MT5API(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    broker = models.CharField(max_length=100)
    image = models.CharField(max_length=255)
    account = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    server = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    


    class Meta:
        verbose_name = "MT5 API"
        verbose_name_plural = "MT5 APIs"
        

    def __str__(self):
        return f"{self.broker} - {self.password}"