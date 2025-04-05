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
            
            return Response({
                'positions': MT5DataSerializer.serialize_positions(positions),                
            }, status=status.HTTP_200_OK)
            
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
