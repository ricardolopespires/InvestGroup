from rest_framework import serializers
from .models import Investidor

class InvestidorSerializer(serializers.ModelSerializer):
    saude_financeira = serializers.SerializerMethodField()
    perfil_investidor = serializers.SerializerMethodField()

    class Meta:
        model = Investidor
        fields = [
            'id', 'usuario', 'nome', 'renda_mensal', 'despesas_mensais', 'dividas',
            'investimentos', 'reserva_emergencia', 'tolerancia_risco', 'horizonte_tempo',
            'objetivo', 'saude_financeira', 'perfil_investidor'
        ]
        read_only_fields = ['usuario', 'saude_financeira', 'perfil_investidor']

    def get_saude_financeira(self, obj):
        return obj.calcular_saude_financeira()

    def get_perfil_investidor(self, obj):
        return obj.determinar_perfil()

    def create(self, validated_data):
        # Vincula o usuário autenticado ao investidor
        validated_data['usuario'] = self.context['request'].user
        return super().create(validated_data)