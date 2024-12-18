from .models import Contact
from rest_framework import serializers


    

class ContactSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)    
    email = serializers.CharField(max_length=100)
    message = serializers.CharField(max_length= 900)


    def create(self, validated_data):
        return Contact.objects.create(**validated_data) 