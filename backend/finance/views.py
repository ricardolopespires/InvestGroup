from django.shortcuts import render 
from rest_framework import status 
from .models import Bank 
from .serializers import BankSerializer
from rest_framework.decorators import api_view 
from rest_framework.response import Response 

 
 
@api_view(['GET', 'POST']) 
def bank_list(request, pk): 
    if request.method == 'GET': 
        bank = Bank.objects.filter(user = pk) 
        bank_serializer = BankSerializer(bank, many=True) 
        return Response(bank_serializer.data) 
 
    elif request.method == 'POST': 
        bank_serializer = BankSerializer(data=request.data) 
        if bank_serializer.is_valid(): 
            bank_serializer.save() 
            return Response(bank_serializer.data, status=status.HTTP_201_CREATED) 
        return Response(bank_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
 
@api_view(['GET', 'PUT', 'DELETE']) 
def bank_detail(request, pk): 
    try: 
        bank = Bank.objects.get(pk=pk) 
    except bank.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        bank_serializer = BankSerializer(Bank) 
        return Response(bank_serializer.data) 
 
    elif request.method == 'PUT': 
        bank_serializer = BankSerializer(Bank, data=request.data) 
        if bank_serializer.is_valid(): 
            bank_serializer.save() 
            return Response(bank_serializer.data) 
        return Response(bank_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        Bank.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  
