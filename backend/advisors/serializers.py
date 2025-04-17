from rest_framework import serializers
from .models import Robo
from .models import Level
from .models import Risk








class RiskSerializer(serializers.ModelSerializer):
    advisor_name = serializers.CharField(source='advisor.name', read_only=True)

    class Meta:
        model = Risk
        fields = ['id', 'advisor', 'advisor_name', 'amount', 'level', 'breakeven']
        read_only_fields = ['advisor_name']



class RoboSerializer(serializers.ModelSerializer):
    class Meta:
        model = Robo
        fields = '__all__'


class RoboLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields ='__all__'



