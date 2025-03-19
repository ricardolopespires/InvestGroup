from rest_framework import serializers
from .models import Categoria, Transacao

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'tipo', 'usuario']

class TransacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacao
        fields = ['id', 'usuario', 'categoria', 'valor', 'data', 'descricao', 'tipo']

