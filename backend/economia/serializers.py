from rest_framework import serializers 
from .models import Countrie
from accounts.serializers import UserSerializer


class CountrieSerializer(serializers.ModelSerializer):

    user = UserSerializer(many=True, read_only=True) 

    class Meta: 
        model = Countrie
        fields = ( 
            'user', 
            'name', 
            'official',
            'area',
            'borders',
            'capital',
            'continents',
            'currencies',
            'population',
            'coatOfArms',
            'languages',
            'flags',             
                ) 
