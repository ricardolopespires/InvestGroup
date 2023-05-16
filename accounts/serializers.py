from accounts.models import Perfil, Situacao, User
from rest_framework import serializers




#------------------------------ Serializers User -----------------------------------------------




class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('__all__')


class PerfilUserSerialiser(serializers.ModelSerializer):


    class Meta:
        model = Perfil
        fields = ['id','investor','minimum','maximum','usuario']



class SituacaoUserSerialiser(serializers.ModelSerializer):


    class Meta:
        model = Situacao
        fields = ['id','minimum','maximum','usuario']
        


class Situacao_User_Updated_Serialiser(serializers.ModelSerializer):


    class Meta:
        model = Situacao
        fields = ['id','usuario']
