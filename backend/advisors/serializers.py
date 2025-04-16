from rest_framework import serializers
from .models import Robo
from .models import Level












class RoboSerializer(serializers.ModelSerializer):
    class Meta:
        model = Robo
        fields = '__all__'


class RoboLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields ='__all__'