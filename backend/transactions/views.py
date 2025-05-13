from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from plataform.models import MT5API
from history.services import MT5Connector
from .models import Categoria, Transacao
from .serializers import CategoriaSerializer, TransacaoSerializer
from django.db.models import Q
from .models import Operation
from .serializers import OperationSerializer
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.views import APIView

# Views para Categorias
class CategoriaListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        categorias = Categoria.objects.filter(usuario=request.user)
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(usuario=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoriaDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, usuario):
        try:
            return Categoria.objects.get(pk=pk, usuario=usuario)
        except Categoria.DoesNotExist:
            return None

    def get(self, request, pk):
        categoria = self.get_object(pk, request.user)
        if categoria is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)

    def put(self, request, pk):
        categoria = self.get_object(pk, request.user)
        if categoria is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        categoria = self.get_object(pk, request.user)
        if categoria is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Views para Transações
class TransacaoListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        transacoes = Transacao.objects.filter(usuario=request.user)
        serializer = TransacaoSerializer(transacoes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TransacaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(usuario=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransacaoDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, usuario):
        try:
            return Transacao.objects.get(pk=pk, usuario=usuario)
        except Transacao.DoesNotExist:
            return None

    def get(self, request, pk):
        transacao = self.get_object(pk, request.user)
        if transacao is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TransacaoSerializer(transacao)
        return Response(serializer.data)

    def put(self, request, pk):
        transacao = self.get_object(pk, request.user)
        if transacao is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TransacaoSerializer(transacao, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        transacao = self.get_object(pk, request.user)
        if transacao is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        transacao.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class OperationListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk, user_id):
        operations = Operation.objects.filter(
            Q(asset = pk.upper()),
            Q(user_id = user_id)
            )
        serializer = OperationSerializer(operations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OperationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OperationDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk, user):
        return get_object_or_404(Operation, pk=pk, user=user)

    def get(self, request, pk):
        operation = self.get_object(pk, request.user)
        serializer = OperationSerializer(operation)
        return Response(serializer.data)

    def put(self, request, pk):
        operation = self.get_object(pk, request.user)
        serializer = OperationSerializer(operation, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        operation = self.get_object(pk, request.user)
        operation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CloseOperationAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        ticket = request.data.get('ticket')

        # Validate ticket
        if not ticket:
            return Response(
                {"error": "É necessário fornecer o ticket da operação."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            ticket = int(ticket)  # Ensure ticket is an integer
        except ValueError:
            return Response(
                {"error": "O ticket deve ser um número inteiro válido."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Fetch the active MT5 API account for the user
        api = MT5API.objects.filter(Q(user_id=pk), Q(is_active=True)).last()
        
        if not api:
            return Response(
                {"error": "Conta MT5 não encontrada ou inativa"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        mt5 = None
        try:
            # Initialize MT5Connector
            mt5 = MT5Connector(
                account=api.account,
                password=api.password,
                server=api.server,
                interval="1d"  # Intervalo diário para dados consistentes
            )
            
            # Initialize MT5 connection
            if not mt5.initialize_mt5():
                return Response(
                    {"error": "Falha ao inicializar o MetaTrader 5"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
            
            # Login to MT5
            if not mt5.login():
                return Response(
                    {"error": "Falha no login do MetaTrader 5"},
                    status=status.HTTP_401_UNAUTHORIZED
                )
            
            # Attempt to close the position
            result = mt5.close_position(ticket, comment="Close Position")
            if not result:
                return Response(
                    {"error": "Falha ao fechar a posição"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

            return Response(
                {"message": "Operação concluída com sucesso."},
                status=status.HTTP_200_OK
            )
        
        except ConnectionError as e:
            return Response(
                {"error": f"Erro de conexão com MetaTrader 5: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        except Exception as e:
            return Response(
                {"error": f"Erro inesperado: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST
            )
        finally:
            # Ensure MT5 connection is closed
            if mt5 and mt5.connected:
                mt5.shutdown()






    
class ReverseOperationAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        ticket = request.data.get('ticket')

        # Validate ticket
        if not ticket:
            return Response(
                {"error": "É necessário fornecer o ticket da operação."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            ticket = int(ticket)  # Ensure ticket is an integer
        except ValueError:
            return Response(
                {"error": "O ticket deve ser um número inteiro válido."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Fetch the active MT5 API account for the user
        api = MT5API.objects.filter(Q(user_id=pk), Q(is_active=True)).last()
        
        if not api:
            return Response(
                {"error": "Conta MT5 não encontrada ou inativa"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        mt5 = None
        try:
            # Initialize MT5Connector
            mt5 = MT5Connector(
                account=api.account,
                password=api.password,
                server=api.server,
                interval="1d"  # Intervalo diário para dados consistentes
            )
            
            # Initialize MT5 connection
            if not mt5.initialize_mt5():
                return Response(
                    {"error": "Falha ao inicializar o MetaTrader 5"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
            
            # Login to MT5
            if not mt5.login():
                return Response(
                    {"error": "Falha no login do MetaTrader 5"},
                    status=status.HTTP_401_UNAUTHORIZED
                )
            
            print("Ticket:", ticket)
            
            # Attempt to close the position
            result = mt5.reverse_position(ticket, comment="Close Position")
            print("Result:", result)
            # Check if the result is valid
            if not result:
                return Response(
                    {"error": "Falha ao fechar a posição"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

            return Response(
                {"message": "Operação concluída com sucesso."},
                status=status.HTTP_200_OK
            )
        
        except ConnectionError as e:
            return Response(
                {"error": f"Erro de conexão com MetaTrader 5: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        except Exception as e:
            return Response(
                {"error": f"Erro inesperado: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST
            )
        finally:
            # Ensure MT5 connection is closed
            if mt5 and mt5.connected:
                mt5.shutdown()