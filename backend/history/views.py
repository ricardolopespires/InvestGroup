# analyzer/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import FinancialDataAnalyzer
from .serializers import FinancialDataSerializer, FinancialDataListSerializer

class FinancialDataView(APIView):
    def get(self, request, symbol,):
        try:
            # Obter parâmetros opcionais de período e intervalo
            period = request.query_params.get('period', '5y')
            interval = request.query_params.get('interval', '1wk')

            # Criar instância do analisador
            analyzer = FinancialDataAnalyzer(symbol=symbol, period=period, interval=interval)
            analyzer.download_data()
            analyzer.preprocess_data()
            analyzer.calculate_indicators()

            # Retornar todos os dados do período
            data_list = analyzer.get_all_data()
            serializer = FinancialDataListSerializer(data_list)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)