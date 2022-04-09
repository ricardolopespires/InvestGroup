from rest_framework import serializers
from .models import Cripto




# Cripto Serializer
class Cripto_Serializer( serializers.ModelSerializer ):

    class Meta:
        model = Cripto
        fields = ('__all__')