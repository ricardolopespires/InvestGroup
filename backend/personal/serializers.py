from rest_framework import serializers 
from .models import Categoria, Movimentacao, Periodo
from .models import Quantia
 
 
class MovimentacaoCreatedSerializer(serializers.Serializer):    
    user_id = serializers.CharField(max_length=150) 
    status = serializers.CharField(max_length=150) 
    categoria_id = serializers.CharField(max_length=150) 
    descricao = serializers.CharField(max_length=400) 
    total = serializers.DecimalField(decimal_places = 2, max_digits = 10, default = 0, )
    
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
    created = serializers.DateTimeField()
    descricao = serializers.CharField(max_length=400) 
    total = serializers.DecimalField(decimal_places = 2, max_digits = 10, default = 0, )
        
    
class PeriodoListSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=150)
    revenues = serializers.DecimalField(decimal_places = 2, max_digits = 10, default = 0, )
    expenses = serializers.DecimalField(decimal_places = 2, max_digits = 10, default=0)
    last= serializers.DecimalField(decimal_places = 2, max_digits = 10, default = 0,)
    percent =  serializers.IntegerField( default=0)
    limit = serializers.IntegerField( )
    spending = serializers.DecimalField(decimal_places = 2, max_digits = 10, default = 0,)
    total = serializers.DecimalField(decimal_places = 2, max_digits = 10, default = 0, )
    

    def update(self, instance, validated_data): 
        instance.user_id = validated_data.get('user_id', instance.user_id)         
        instance.status = validated_data.get('status', instance.status) 
        instance.categoria_id = validated_data.get('categoria_id', instance.categoria_id) 
        instance.total = validated_data.get('total', instance.total) 
        
        instance.save() 
        return instance



class Periodo_Despesas_Serializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=150)
    revenues = serializers.DecimalField(decimal_places = 2, max_digits = 10, default = 0, )
    expenses = serializers.DecimalField(decimal_places = 2, max_digits = 10, default=0)
    last= serializers.DecimalField(decimal_places = 2, max_digits = 10, default = 0,)
    percent =  serializers.IntegerField( default=0)
    limit = serializers.IntegerField( )
    spending = serializers.DecimalField(decimal_places = 2, max_digits = 10, default = 0,)
    total = serializers.DecimalField(decimal_places = 2, max_digits = 10, default = 0, )

    def update (self, instance, validated_data):
        instance.revenues = validated_data.get('revenues', instance.revenues)
        instance.expenses = validated_data.get('expenses', instance.expenses)
        instance.last = validated_data.get('last', instance.last)
        instance.percent = validated_data.get('percent', instance.percent)
        instance.limit = validated_data.get('limit', instance.limit)
        instance.spending = validated_data.get('spending', instance.spending)
        instance.total = validated_data.get('total', instance.total)

        instance.save()
        return instance 
    


class PlanListSerializer(serializers.Serializer):
    id =  serializers.IntegerField( default=0)  
    user_id = serializers.CharField(max_length=150)
    icon = serializers.CharField(max_length=150)
    nome = serializers.CharField(max_length=150)
    economia = serializers.DecimalField(decimal_places = 2, max_digits = 10, default = 0,)    
    quantia = serializers.DecimalField(decimal_places = 2, max_digits = 10, default = 0,)
    percent =  serializers.IntegerField( default=0)  
    meta = serializers.DecimalField(decimal_places = 2, max_digits = 10, default = 0, )


    def update (self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.icon = validated_data.get('icon', instance.icon)
        instance.nome = validated_data.get('nome', instance.nome)
        instance.economia = validated_data.get('economia', instance.economia)
        instance.quantia = validated_data.get('quantia', instance.quantia)
        instance.percent = validated_data.get('percent', instance.percent)
        instance.meta = validated_data.get('meta', instance.meta)

        instance.save()
        return instance 
    


class QuantiaListSerializer(serializers.Serializer):
    id =  serializers.IntegerField( default=0)  
    plano_id = serializers.CharField(max_length=150) 
    plano = serializers.CharField(max_length=150)    
    quantia = serializers.DecimalField(decimal_places = 2, max_digits = 10, default = 0,)
    created = serializers.DateTimeField()
    percent =  serializers.IntegerField( default=0)  
    meta = serializers.DecimalField(decimal_places = 2, max_digits = 10, default = 0, )
    


class QuantiaCreatedSerializer(serializers.Serializer):  
    plano_id = serializers.CharField(max_length=150)   
    quantia = serializers.DecimalField(decimal_places = 2, max_digits = 10, default = 0,)    
    meta = serializers.DecimalField(decimal_places = 2, max_digits = 10, default = 0, )

    def create(self, validated_data): 
        return Quantia.objects.create(**validated_data) 