from rest_framework import serializers
from .models import Asset, InvestorProfile, Investidor, InvestmentOperation, RiskAssessment
from django.contrib.auth import get_user_model

User = get_user_model()


class AssetSerializer(serializers.ModelSerializer):
    asset_type_display = serializers.CharField(source='get_asset_type_display', read_only=True)

    class Meta:
        model = Asset
        fields = ['id', 'name', 'ticker', 'asset_type', 'asset_type_display', 'currency', 'sector', 'volatility', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at', 'asset_type_display']


class InvestorProfileSerializer(serializers.ModelSerializer):
    risk_tolerance_display = serializers.CharField(source='get_risk_tolerance_display', read_only=True)

    class Meta:
        model = InvestorProfile
        fields = ['id', 'name', 'risk_tolerance', 'risk_tolerance_display', 'max_exposure', 
                  'fixed_income_allocation', 'variable_income_allocation', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at', 'risk_tolerance_display']


class InvestidorSerializer(serializers.ModelSerializer):
    usuario = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    investor_profile = InvestorProfileSerializer(read_only=True)
    saude_financeira = serializers.CharField(source='calcular_saude_financeira', read_only=True)
    tolerancia_risco_display = serializers.CharField(source='get_tolerancia_risco_display', read_only=True)
    horizonte_tempo_display = serializers.CharField(source='get_horizonte_tempo_display', read_only=True)
    objetivo_display = serializers.CharField(source='get_objetivo_display', read_only=True)

    class Meta:
        model = Investidor
        fields = ['id', 'usuario', 'renda_mensal', 'despesas_mensais', 'dividas', 'investimentos', 
                  'reserva_emergencia', 'tolerancia_risco', 'tolerancia_risco_display', 
                  'horizonte_tempo', 'horizonte_tempo_display', 'objetivo', 'objetivo_display', 
                  'investor_profile', 'saude_financeira', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at', 'saude_financeira', 
                            'tolerancia_risco_display', 'horizonte_tempo_display', 'objetivo_display']

    def validate(self, data):
        # Validação para garantir que os valores financeiros sejam positivos
        for field in ['renda_mensal', 'despesas_mensais', 'dividas', 'investimentos', 'reserva_emergencia']:
            if data.get(field, 0) < 0:
                raise serializers.ValidationError({field: "O valor não pode ser negativo."})
        return data


class InvestmentOperationSerializer(serializers.ModelSerializer):
    asset = AssetSerializer(read_only=True)
    asset_id = serializers.PrimaryKeyRelatedField(queryset=Asset.objects.all(), source='asset', write_only=True)
    investidor = InvestidorSerializer(read_only=True)
    investidor_id = serializers.PrimaryKeyRelatedField(queryset=Investidor.objects.all(), source='investidor', write_only=True)
    operation_type_display = serializers.CharField(source='get_operation_type_display', read_only=True)

    class Meta:
        model = InvestmentOperation
        fields = ['id', 'asset', 'asset_id', 'investidor', 'investidor_id', 'operation_type', 
                  'operation_type_display', 'quantity', 'unit_price', 'total_value', 'risk_score', 
                  'operation_date', 'created_at', 'updated_at']
        read_only_fields = ['id', 'total_value', 'risk_score', 'created_at', 'updated_at', 'operation_type_display']

    def validate(self, data):
        # Validação para garantir que a quantidade e o preço unitário sejam positivos
        if data.get('quantity', 0) <= 0:
            raise serializers.ValidationError({'quantity': "A quantidade deve ser maior que zero."})
        if data.get('unit_price', 0) <= 0:
            raise serializers.ValidationError({'unit_price': "O preço unitário deve ser maior que zero."})
        return data


class RiskAssessmentSerializer(serializers.ModelSerializer):
    operation = InvestmentOperationSerializer(read_only=True)
    operation_id = serializers.PrimaryKeyRelatedField(queryset=InvestmentOperation.objects.all(), source='operation', write_only=True)
    risk_type_display = serializers.CharField(source='get_risk_type_display', read_only=True)
    risk_level_display = serializers.CharField(source='get_risk_level_display', read_only=True)

    class Meta:
        model = RiskAssessment
        fields = ['id', 'operation', 'operation_id', 'risk_type', 'risk_type_display', 'risk_level', 
                  'risk_level_display', 'description', 'assessment_date', 'mitigation_strategy']
        read_only_fields = ['id', 'assessment_date', 'risk_type_display', 'risk_level_display']