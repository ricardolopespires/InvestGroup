from rest_framework import serializers 
from .models import Categoria, Movimentacao
 
 
class MovimentacaoCreatedSerializer(serializers.Serializer):    
    user_id = serializers.CharField(max_length=150) 
    status = serializers.CharField(max_length=150) 
    categoria_id = serializers.CharField(max_length=150) 
    descricao = serializers.CharField(max_length=400) 
    total = serializers.IntegerField() 
    
    class Meta: 
        model = Movimentacao
        fields = ( 
            'user_id', 
            'status', 
            'categoria_id', 
            'descricao',  
            'total', 
                ) 

 
    def create(self, validated_data): 
        return Movimentacao.objects.create(**validated_data) 
 
    def update(self, instance, validated_data): 
        instance.user_id = validated_data.get('user_id', instance.user_id)         
        instance.status = validated_data.get('status', instance.status) 
        instance.categoria_id = validated_data.get('categoria_id', instance.categoria_id) 
        instance.total = validated_data.get('total', instance.total) 
        
        instance.save() 
        return instance
    

class MovimentacaoListSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=150) 
    status = serializers.CharField(max_length=150) 
    categoria = serializers.CharField(max_length=150)
    create = serializers.DateField()  
    descricao = serializers.CharField(max_length=400) 
    total = serializers.IntegerField() 
        
    
