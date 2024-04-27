from rest_framework import generics 
from rest_framework.response import Response 
from rest_framework.reverse import reverse 
from rest_framework.decorators import api_view 
from rest_framework import status 
from .models import Countrie
from .serializers import CountrieSerializer
from .manager import Economia





@api_view(['GET', 'POST']) 
def countries_list(request): 
    if request.method == 'GET': 
        countries = Countrie.objects.all()       
        countries_serializer = CountrieSerializer(countries, many=True) 
        return Response(countries_serializer.data) 
 
    elif request.method == 'POST': 
        data = request.data
        print(data['user_id'])
        economia = Economia()
        response = economia.criar_favorito(data)
        print(response)

        return Response({'msg':'País adicionado com sucesso'}, status=status.HTTP_200_OK)
    