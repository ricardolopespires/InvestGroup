from rest_framework import serializers
from .models import Asset
from .models import Robo
from .models import Level
from .models import Risk



class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'
        read_only_fields = ('id',)  # 'id' será somente leitura

class RoboSerializer(serializers.ModelSerializer):
    # Usando o SlugRelatedField para serializar o campo 'asset' com base no 'name'
    asset = serializers.SlugRelatedField(
        queryset=Asset.objects.all(),
        slug_field='name',
        many=True,  # Defina como True se for um relacionamento Many-to-Many, caso contrário False
   
    )

    class Meta:
        model = Robo
        fields = [
            'id','name', 'asset', 'user', 'description', 'performance_fee', 
            'management_fee', 'rate', 'amount', 'rebalancing', 'tax_inspection',
            'created_at', 'updated_at', 'is_active'
        ]
        read_only_fields = ('created_at', 'updated_at', 'is_active')  # Campos somente leitura

class RiskSerializer(serializers.ModelSerializer):
    advisor_name = serializers.CharField(source='advisor.name', read_only=True)

    class Meta:
        model = Risk
        fields = ['id', 'advisor', 'advisor_name', 'amount', 'level', 'breakeven']
        read_only_fields = ['advisor_name']




class RoboLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields ='__all__'



