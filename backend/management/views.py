from django.shortcuts import render
from .serializers import Perfil_Add_User_Serializer
from .serializers import PerfilUserSerializer
from .serializers import Situacao_Add_User_Serializer
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from .models import Perfil, Situacao
from rest_framework import status

# Create your views here.


@api_view(['GET', 'PUT']) 
def perfil_username(request, pk): 
    try: 
        perfil = Perfil.objects.get(id=pk) 
    except Perfil.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        perfil_serializer = Perfil_Add_User_Serializer(perfil) 
        return Response(perfil_serializer.data) 
 
    elif request.method == 'PUT': 
        perfil_serializer = Perfil_Add_User_Serializer(perfil, data=request.data) 
        print(perfil_serializer)
        if perfil_serializer.is_valid(): 
            perfil_serializer.save() 
            return Response(perfil_serializer.data) 
        return Response(perfil_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 



@api_view(['GET', 'PUT']) 
def situacao_username(request, pk): 
    try: 
        situacao = Situacao.objects.get(id=pk) 
    except situacao.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        situacao_serializer = Situacao_Add_User_Serializer(situacao) 
        return Response(situacao_serializer.data) 
 
    elif request.method == 'PUT': 
        situacao_serializer = Situacao_Add_User_Serializer(situacao, data=request.data) 
        print(situacao_serializer)
        if situacao_serializer.is_valid(): 
            situacao_serializer.save() 
            return Response(situacao_serializer.data) 
        return Response(situacao_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 




@api_view(['GET', 'PUT']) 
def perfil_detail(request, pk): 
    try: 
        perfil = Perfil.objects.get(usuario=pk) 
    except Perfil.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        perfil_serializer = PerfilUserSerializer(perfil) 
        return Response(perfil_serializer.data) 
 

 