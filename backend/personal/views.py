from rest_framework import generics 
from rest_framework.response import Response 
from rest_framework.reverse import reverse 
from rest_framework.decorators import api_view 
from rest_framework import status 
from .models import Movimentacao
from .models import Periodo
from .serializers import MovimentacaoCreatedSerializer
from .serializers import MovimentacaoListSerializer
from .serializers import PeriodoListSerializer
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
 
@api_view(['POST']) 
def movimentacao_created(request):   

    if request.method == 'POST': 
        data_serializer = MovimentacaoCreatedSerializer(data=request.data) 
        if data_serializer.is_valid(): 
            data_serializer.save() 
            return Response(data_serializer.data, status=status.HTTP_201_CREATED) 
        return Response(data_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    


@api_view(['GET', 'POST',  'PUT', 'DELETE']) 
def periodo_list(request, pk): 
    if request.method == 'GET': 
        periodos = Periodo.objects.filter(user_id = pk) 
        
        periodos_serializer = PeriodoListSerializer(periodos, many=True) 
        return Response(periodos_serializer.data) 
 
    elif request.method == 'POST': 
        periodo_serializer = PeriodoListSerializer(data=request.data) 
        if periodo_serializer.is_valid(): 
            periodo_serializer.save() 
            return Response(periodo_serializer.data, status=status.HTTP_201_CREATED) 
        return Response(periodo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT': 
        
        periodo_serializer = PeriodoListSerializer(periodo, data=request.data) 
        if periodo_serializer.is_valid(): 
            periodo_serializer.save() 
            return Response(periodo_serializer.data) 
        return Response(periodo_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        Periodo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  
 
 






@csrf_exempt 
def detail(request, pk): 
    try: 
        despesa = Despesas.objects.get(id=pk) 
    except Despesas.DoesNotExist: 
        return HttpResponse(status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        despesa_serializer = Lista_Despesas_Serializer(despesa) 
        return JSONResponse(despesa_serializer.data) 
 
    elif request.method == 'PUT': 
        despesa_data = JSONParser().parse(request) 
        despesa_serializer = Lista_Despesas_Serializer(despesa, data=despesa_data) 
        if despesa_serializer.is_valid(): 
            despesa_serializer.save() 
            return JSONResponse(despesa_serializer.data) 
        return JSONResponse(despesa_serializer.errors, \
            status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        despesa.delete() 
        return HttpResponse(status=status.HTTP_204_NO_CONTENT) 
