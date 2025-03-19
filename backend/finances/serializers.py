from rest_framework import serializers
from .models import Portfolio, Investment

class InvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investment
        fields = '__all__'

class PortfolioSerializer(serializers.ModelSerializer):
    investments = InvestmentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Portfolio
        fields = ['id', 'nome', 'descricao', 'data_criacao', 'investments']