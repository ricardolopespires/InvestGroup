from accounts.models import User
from rest_framework import serializers








class PerfilUserSerializer(serializers.Serializer):
     
    id = serializers.CharField(max_length = 190, ) 
    investor = serializers.CharField(max_length = 190, ) 
    minimum = serializers.IntegerField()
    maximum = serializers.IntegerField()
    usuario = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    color  = serializers.CharField(max_length = 40, ) 

    class Meta:
        model=User
        fields = ['id','minimum', 'maximum','usuario', 'color']


   
    
class Perfil_Add_User_Serializer(serializers.Serializer):
    id = serializers.CharField(max_length=190)
    usuario = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.save()

        usuarios = validated_data.get('usuario', [])
        instance.usuario.add(*usuarios)

        return instance
    


class SituacaoUserSerializer(serializers.Serializer):
     
    id = serializers.CharField(max_length = 190, ) 
    condicao = serializers.CharField(max_length = 190, ) 
    minimum = serializers.IntegerField()
    maximum = serializers.IntegerField()
    usuario = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
  

    class Meta:
        model=User
        fields = ['id','condicao','usuario', ]


class Situacao_Add_User_Serializer(serializers.Serializer):
    id = serializers.CharField(max_length=190)
    usuario = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.save()

        usuarios = validated_data.get('usuario', [])
        instance.usuario.add(*usuarios)

        return instance
    