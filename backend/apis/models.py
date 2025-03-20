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
    broker_name = models.CharField(max_length=100)
    image = models.CharField(max_length=255)
    account = models.CharField(max_length=255)
    login = models.IntegerField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    server = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.broker_name} - {self.login}"