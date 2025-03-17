from rest_framework import serializers
from .models import Currency, Stock, Commoditie, Index

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['id', 'name', 'symbol', 'img', 'yahoo', 'tradingview']

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id', 'name', 'symbol', 'img', 'yahoo', 'tradingview']

class CommoditieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commoditie
        fields = ['id', 'name', 'symbol', 'img', 'yahoo', 'tradingview']

class IndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Index
        fields = ['id', 'name', 'symbol', 'img', 'yahoo', 'tradingview']