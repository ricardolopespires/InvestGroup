from rest_framework import generics 
from rest_framework.response import Response 
from rest_framework.reverse import reverse 
from rest_framework.decorators import api_view 
from rest_framework import status 
from .models import Movimentacao
from .serializers import MovimentacaoCreatedSerializer
from .serializers import MovimentacaoListSerializer
from django.shortcuts import render

# Create your views here.




class MovimentacaoList(generics.ListCreateAPIView): 
    queryset = Movimentacao.objects.all() 
    serializer_class = MovimentacaoListSerializer
    name = 'movimentacao-list' 
 

@api_view(['GET']) 
def movimentacoes_list(request, pk): 
    if request.method == 'GET': 
        movimentacoes = Movimentacao.objects.filter(user_id = pk) 
        movimentacoes_serializer = MovimentacaoListSerializer(movimentacoes, many=True) 
        return Response(movimentacoes_serializer.data) 
    

 
    

class MovimentacaoCreated(generics.ListCreateAPIView): 
    queryset = Movimentacao.objects.all() 
    serializer_class = MovimentacaoCreatedSerializer
    name = 'movimentacao-created' 
 
