from rest_framework import serializers
from .models import Asset, RiskProfile, Portfolio, PortfolioAllocation, InvestmentAgent, Transaction, AdvisorRecommendation
from django.contrib.auth.models import User

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['id', 'name', 'ticker', 'asset_type', 'price', 'volatility', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class RiskProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = RiskProfile
        fields = ['id', 'user', 'risk_level', 'max_loss_tolerance', 'investment_horizon', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

class PortfolioSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    risk_profile = serializers.PrimaryKeyRelatedField(queryset=RiskProfile.objects.all(), allow_null=True)

    class Meta:
        model = Portfolio
        fields = ['id', 'user', 'name', 'risk_profile', 'total_value', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

class PortfolioAllocationSerializer(serializers.ModelSerializer):
    portfolio = serializers.PrimaryKeyRelatedField(queryset=Portfolio.objects.all())
    asset = serializers.PrimaryKeyRelatedField(queryset=Asset.objects.all())

    class Meta:
        model = PortfolioAllocation
        fields = ['id', 'portfolio', 'asset', 'quantity', 'allocation_percentage', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class InvestmentAgentSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(read_only=True, many=True)  # A relação é ManyToMany, portanto deve ser 'many=True'
    portfolios = serializers.PrimaryKeyRelatedField(queryset=Portfolio.objects.all(), many=True)  # Também deve ser 'many=True', já que é uma ManyToManyField

    class Meta:
        model = InvestmentAgent
        fields = ['id', 'users', 'portfolios', 'name', 'avatar','specialty', 'rating', 'reviews', 'experience', 'langchain_model', 'strategy', 'config', 'created_at', 'updated_at']
        read_only_fields = ['id', 'users', 'created_at', 'updated_at']  # 'users' está como read-only, já que o relacionamento é ManyToMany


class TransactionSerializer(serializers.ModelSerializer):
    portfolio = serializers.PrimaryKeyRelatedField(queryset=Portfolio.objects.all())
    asset = serializers.PrimaryKeyRelatedField(queryset=Asset.objects.all())

    class Meta:
        model = Transaction
        fields = ['id', 'portfolio', 'asset', 'transaction_type', 'quantity', 'price_per_unit', 'total_amount', 'executed_at', 'created_at']
        read_only_fields = ['id', 'created_at']

class AdvisorRecommendationSerializer(serializers.ModelSerializer):
    agent = serializers.PrimaryKeyRelatedField(queryset=InvestmentAgent.objects.all())
    portfolio = serializers.PrimaryKeyRelatedField(queryset=Portfolio.objects.all())
    recommended_assets = serializers.PrimaryKeyRelatedField(many=True, queryset=Asset.objects.all())

    class Meta:
        model = AdvisorRecommendation
        fields = ['id', 'agent', 'portfolio', 'recommendation_text', 'recommended_assets', 'risk_assessment', 'created_at']
        read_only_fields = ['id', 'created_at']