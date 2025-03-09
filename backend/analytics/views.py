from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Investidor
from .serializers import InvestidorSerializer
from rest_framework.permissions import IsAuthenticated
from .serializers import PerfilSerializer
from .serializers import SituacaoSerializer

from .models import Perfil
from .models import Situacao


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
    


class PerfilAllView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Lista apenas os perfis do usuário autenticado
        perfis = Perfil.objects.all()
        serializer = PerfilSerializer(perfis, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class PerfilView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        # Lista apenas os perfis do usuário autenticado
        perfis = Perfil.objects.filter(id = pk)
        serializer = PerfilSerializer(perfis, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        # Cria um novo perfil vinculado ao investidor do usuário autenticado
        serializer = PerfilSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PerfilDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        perfil = Perfil.objects.filter(id=pk).first()
        if not perfil:
            return Response({"error": "Perfil não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PerfilSerializer(perfil)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        perfil = Perfil.objects.filter(id=pk).first()
        if not perfil:
            return Response({"error": "Perfil não encontrado"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PerfilSerializer(perfil, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        perfil = Perfil.objects.filter(id=pk).first()
        if not perfil:
            return Response({"error": "Perfil não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        perfil.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class SituacaoAllView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Lista apenas as situações do usuário autenticado
        situacoes = Situacao.objects.all()
        serializer = SituacaoSerializer(situacoes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SituacaoView(APIView):
    permission_classes = [IsAuthenticated]
        
    def get(self, request, pk):
        situacao = Situacao.objects.filter(id=pk).first()
        if situacao is None:
            return Response({"error": "Situação não encontrada"}, status=status.HTTP_404_NOT_FOUND)
        
        # Adicione uma resposta quando a situação for encontrada
        serializer = SituacaoSerializer(situacao)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    
    def post(self, request):
        # Cria uma nova situação vinculada ao investidor do usuário autenticado
        serializer = SituacaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SituacaoDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        situacao = Situacao.objects.filter(id=pk).first()
        if situacao is None:
            return Response({"error": "Situação não encontrada"}, status=status.HTTP_404_NOT_FOUND)
        
        # Adicione uma resposta quando a situação for encontrada
        serializer = SituacaoSerializer(situacao)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        situacao = Situacao.objects.filter(id=pk).first()
        if situacao is None:
            return Response({"error": "Situação não encontrada"}, status=status.HTTP_404_NOT_FOUND)
        serializer = SituacaoSerializer(situacao, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        situacao = Situacao.objects.filter(id=pk).first()
        if situacao is None:
            return Response({"error": "Situação não encontrada"}, status=status.HTTP_404_NOT_FOUND)
        situacao.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
