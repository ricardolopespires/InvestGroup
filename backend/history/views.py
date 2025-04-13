from .serializers import FinancialDataListSerializer
from django.db.models import Avg, Count, Min, Sum, Q
from .serializers import FinancialDataSerializer
from rest_framework.response import Response
from .services import FinancialDataAnalyzer
from rest_framework.views import APIView
from .serializers import SignalSerializer
from .serializers import MT5DataSerializer
from rest_framework import status
from plataform.models import MT5API
from .services import MT5Connector
import pandas as pd
import logging

logger = logging.getLogger(__name__)


class FinancialDataView(APIView):
    def get(self, request, symbol, interval):
        try:
            # Obter parâmetros opcionais de período, intervalo e outros
            period = request.query_params.get('period', '5y')          
            include_signals = request.query_params.get('include_signals', 'true').lower() == 'true'
            signal_distance = int(request.query_params.get('signal_distance', 15))
            signal_width = int(request.query_params.get('signal_width', 3))
            indicators = request.query_params.getlist('indicators', [])  # Lista de indicadores opcionais

            # Criar instância do analisador
            analyzer = FinancialDataAnalyzer(symbol=symbol, period=period, interval=interval)
            analyzer.download_data()
            analyzer.preprocess_data()
            analyzer.calculate_indicators(additional_indicators=indicators)

            # Calcular sinais de compra e venda, se solicitado
            signals = []
            if include_signals:
                signals = analyzer.calculate_signals(distance=signal_distance, width=signal_width)

            # Retornar todos os dados do período
            data_list = analyzer.get_all_data()
            serializer = FinancialDataListSerializer(data_list)  # Corrigido para usar o serializer correto

            # Preparar a resposta com preços e sinais
            response_data = {
                'prices': serializer.data,
                'signals': signals
            }

            # Adicionar indicadores técnicos, se solicitados
            if indicators:
                response_data['indicators'] = {}
                if 'rsi' in indicators and 'rsi' in analyzer.dataset.columns:
                    rsi_data = [
                        {'time': int(row.name.timestamp()), 'value': row['rsi']}
                        for row in analyzer.dataset.itertuples() if not pd.isna(row.rsi)
                    ]
                    response_data['indicators']['rsi'] = rsi_data
                if 'atr' in indicators and 'atr' in analyzer.dataset.columns:
                    atr_data = [
                        {'time': int(row.name.timestamp()), 'value': row['atr']}
                        for row in analyzer.dataset.itertuples() if not pd.isna(row.atr)
                    ]
                    response_data['indicators']['atr'] = atr_data
                if 'close_smooth' in indicators and 'close_smooth' in analyzer.dataset.columns:
                    smooth_data = [
                        {'time': int(row.name.timestamp()), 'value': row['close_smooth']}
                        for row in analyzer.dataset.itertuples() if not pd.isna(row.close_smooth)
                    ]
                    response_data['indicators']['close_smooth'] = smooth_data

            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        


class MT5APIView(APIView):
    def get(self, request, symbol, interval, pk):
        api = MT5API.objects.filter(Q(user_id=pk), Q(is_active=True)).last()
        
        if not api:
            return Response({'error': 'Conta MT5 não encontrada ou inativa'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            mt5 = MT5Connector(
                symbol=symbol,
                interval=interval,
                account=api.account,
                password=api.password,
                server=api.server
            )
            
            if not mt5.initialize_mt5():
                return Response({'error': 'Falha ao inicializar o MetaTrader 5'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            if not mt5.login():
                return Response({'error': 'Falha no login do MetaTrader 5'}, status=status.HTTP_401_UNAUTHORIZED)
            
            mt5.download_data()
            mt5.preprocess_data()
            mt5.calculate_indicators()
            signals = mt5.calculate_signals()
            
            response_data = {
                'prices': mt5.get_all_data(),
                'signals': signals,
                "status": 200
            }
            
            return Response(response_data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)




class PositionsView(APIView):
    def get(self, request, symbol, type, interval, pk):

        api = MT5API.objects.filter(Q(user_id=pk), Q(is_active=True)).last()
        
        if not api:
            return Response({'error': 'Conta MT5 não encontrada ou inativa'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            mt5 = MT5Connector(
                symbol=symbol,
                interval=interval,
                account=api.account,
                password=api.password,
                server=api.server
            )
            
            if not mt5.initialize_mt5():
                return Response({'error': 'Falha ao inicializar o MetaTrader 5'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            if not mt5.login():
                return Response({'error': 'Falha no login do MetaTrader 5'}, status=status.HTTP_401_UNAUTHORIZED)

            positions = mt5.positions_get(symbol=symbol, type=type)
            result = positions.to_dict('records')
            
            return Response( result, status=status.HTTP_200_OK)
            
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)




class LastSignalStockView(APIView):
    def get(self, request, symbol, interval, type, pk):
        """
        Retorna os últimos sinais de compra/venda para o símbolo especificado nos timeframes W1, D1 e H4.

        Args:
            request: Requisição HTTP.
            symbol (str): Símbolo do ativo (ex: 'EURUSD').
            type (str): Tipo de ativo (não usado diretamente aqui, mas passado na URL).
            pk (int): ID do usuário para buscar a conta MT5 associada.

        Returns:
            Response: Dados serializados dos últimos sinais ou mensagem de erro.
        """
        # Busca a última conta MT5 ativa do usuário
        api = MT5API.objects.filter(Q(user_id=pk) & Q(is_active=True)).last()
        
        if not api:
            return Response(
                {'error': 'Conta MT5 não encontrada ou inativa'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        try:
            # Instancia o MT5Connector com as credenciais da conta
            mt5 = MT5Connector(
                symbol=symbol,
                interval=interval,  # Intervalo será definido em get_last_signal_by_timeframes
                account=api.account,
                password=api.password,
                server=api.server
            )
            
            # Inicializa a conexão com o MetaTrader 5
            if not mt5.initialize_mt5():
                return Response(
                    {'error': 'Falha ao inicializar o MetaTrader 5'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
            
            # Realiza o login na conta
            if not mt5.login():
                return Response(
                    {'error': 'Falha no login do MetaTrader 5'},
                    status=status.HTTP_401_UNAUTHORIZED
                )

            # Obtém os últimos sinais para os timeframes padrão (W1, D1, H4)
            signals = mt5.get_last_signal_by_timeframes(symbol= symbol, type = type)

            result = signals.to_dict('records')
            print(result)
            
            # Serializa os dados e retorna a resposta
            return Response(
                result,
                status=status.HTTP_200_OK
            )
        
        except Exception as e:
            # Captura qualquer erro inesperado e retorna uma resposta genérica
            return Response(
                {'error': f'Erro ao processar a solicitação: {str(e)}'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        finally:
            # Garante que a conexão com o MT5 seja encerrada, mesmo em caso de erro
            try:
                mt5.shutdown()
            except:
                pass  # Ignora erros no shutdown para não sobrescrever a resposta principal



class HistoryDealsView(APIView):
    def get(self, request, pk, from_date=None, to_date=None): 
        """
        Retorna o histórico de negociações para o usuário especificado.

        Args:
            request: Requisição HTTP.
            pk (int): ID do usuário para buscar o histórico de negociações.

        Returns:
            Response: Dados serializados do histórico de negociações ou mensagem de erro.
        """
        # Busca a última conta MT5 ativa do usuário
        api = MT5API.objects.filter(Q(user_id=pk) & Q(is_active=True)).last()
        
        if not api:
            return Response(
                {'error': 'Conta MT5 não encontrada ou inativa'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        try:
            # Instancia o MT5Connector com as credenciais da conta
            mt5 = MT5Connector(
                account=api.account,
                password=api.password,
                server=api.server
            )
            
            # Inicializa a conexão com o MetaTrader 5
            if not mt5.initialize_mt5():
                return Response(
                    {'error': 'Falha ao inicializar o MetaTrader 5'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
            
            # Realiza o login na conta
            if not mt5.login():
                return Response(
                    {'error': 'Falha no login do MetaTrader 5'},
                    status=status.HTTP_401_UNAUTHORIZED
                )

            # Obtém o histórico de negociações
            history = mt5.get_history_deals(symbol, from_date=from_date, to_date=to_date)

            result = history.to_dict('records')
            
            # Serializa os dados e retorna a resposta
            return Response(
                result,
                status=status.HTTP_200_OK
            )
        
        except Exception as e:
            # Captura qualquer erro inesperado e retorna uma resposta genérica
            return Response(
                {'error': f'Erro ao processar a solicitação: {str(e)}'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        finally:
            # Garante que a conexão com o MT5 seja encerrada, mesmo em caso de erro
            try:
                mt5.shutdown()
            except:
                pass

