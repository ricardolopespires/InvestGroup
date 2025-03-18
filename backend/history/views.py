from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import FinancialDataAnalyzer
from .serializers import FinancialDataSerializer, FinancialDataListSerializer

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
    def __init__(self):
        self.mt5 = MT5Connection(
            account=settings.MT5_ACCOUNT,
            password=settings.MT5_PASSWORD,
            server=settings.MT5_SERVER
        )

    def get(self, request):
        try:
            action = request.query_params.get('action', 'connect')
            
            if action == 'connect':
                result = self.mt5.connect()
            elif action == 'account_info':
                result = self.mt5.get_account_info()
            elif action == 'historical':
                symbol = request.query_params.get('symbol')
                timeframe = request.query_params.get('timeframe')
                start = datetime.fromisoformat(request.query_params.get('start'))
                end = datetime.fromisoformat(request.query_params.get('end'))
                result = self.mt5.get_historical_data(symbol, timeframe, start, end)
            elif action == 'disconnect':
                result = self.mt5.disconnect()
            else:
                return Response({"error": "Ação inválida"}, status=status.HTTP_400_BAD_REQUEST)
            
            return Response(result, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)