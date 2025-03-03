from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Investidor
from .serializers import InvestidorSerializer
from rest_framework.permissions import IsAuthenticated

class InvestidorListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Lista apenas os investidores do usuário autenticado
        investidores = Investidor.objects.filter(usuario=request.user)
        serializer = InvestidorSerializer(investidores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Cria um novo investidor vinculado ao usuário autenticado
        serializer = InvestidorSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InvestidorDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        try:
            # Garante que apenas o investidor do usuário autenticado seja acessado
            return Investidor.objects.get(pk=pk, usuario=user)
        except Investidor.DoesNotExist:
            return None

    def get(self, request, pk):
        investidor = self.get_object(pk, request.user)
        if investidor is None:
            return Response({"error": "Investidor não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        serializer = InvestidorSerializer(investidor)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        investidor = self.get_object(pk, request.user)
        if investidor is None:
            return Response({"error": "Investidor não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        serializer = InvestidorSerializer(investidor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        investidor = self.get_object(pk, request.user)
        if investidor is None:
            return Response({"error": "Investidor não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        investidor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)