from rest_framework import serializers 
from .models import Bank 
 
 
class BankSerializer(serializers.Serializer):    
    user = serializers.CharField(max_length=150) 
    number = serializers.IntegerField() 
    currency = serializers.CharField(max_length=9) 
    balance = serializers.DecimalField(decimal_places = 2, max_digits = 10) 

 
    def create(self, validated_data): 
        return Bank.objects.create(**validated_data) 
 
    def update(self, instance, validated_data): 
        instance.user = validated_data.get('user', instance.user)         
        instance.number = validated_data.get('number', instance.number) 
        instance.currency = validated_data.get('currency', instance.currency) 
        instance.balance = validated_data.get('balance', instance.balance) 
        
        instance.save() 
        return instance
    
