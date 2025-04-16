from rest_framework import serializers
from .models import Categoria
from .models import Transacao
from .models import Operation

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'tipo', 'usuario']

class TransacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacao
        fields = ['id', 'usuario', 'categoria', 'valor', 'data', 'descricao', 'tipo']


class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = '__all__'
        read_only_fields = ['id', 'user', 'date', 'stoploss', 'takeprofit']
