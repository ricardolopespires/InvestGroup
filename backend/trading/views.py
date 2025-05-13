from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Currency, Stock, Commoditie, Index
from .serializers import CurrencySerializer, StockSerializer, CommoditieSerializer, IndexSerializer
from django.db.models import Avg, Count, Min, Sum, Q
from plataform.models import MT5API
import yfinance as yf
from history.services import MT5Connector
import logging


logger = logging.getLogger(__name__)

# Currency Views (already provided)
class CurrencyList(APIView):
    def get(self, request):
        currencies = Currency.objects.all()
        serializer = CurrencySerializer(currencies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CurrencySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CurrencyDetail(APIView):
    def get_object(self, pk):
        try:
            return Currency.objects.get(pk=pk)
        except Currency.DoesNotExist:
            return None

    def get(self, request, pk):
        currency = self.get_object(pk)
        if currency is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CurrencySerializer(currency)
        return Response(serializer.data)

    def put(self, request, pk):
        currency = self.get_object(pk)
        if currency is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CurrencySerializer(currency, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        currency = self.get_object(pk)
        if currency is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        currency.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Stock Views (already provided)
class StockList(APIView):
    def get(self, request, pk):
        # Busca a conta MT5 ativa do usuário
        api = MT5API.objects.filter(Q(user_id=pk), Q(is_active=True)).last()
        
        if not api:
            return Response(
                {'error': 'Conta MT5 não encontrada ou inativa'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        # Inicializa o MT5Connector com as credenciais do usuário
        mt5 = MT5Connector(
            account=api.account,
            password=api.password,
            server=api.server,
            interval="1d"  # Intervalo diário para dados consistentes
        )
        
        # Inicializa e faz login no MT5
        if not mt5.initialize_mt5():
            return Response(
                {'error': 'Falha ao inicializar o MetaTrader 5'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        if not mt5.login():
            return Response(
                {'error': 'Falha no login do MetaTrader 5'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        try:
            stocks = Stock.objects.all()
            if not stocks:
                return Response(
                    {"message": "Nenhuma currency encontrada"},
                    status=status.HTTP_404_NOT_FOUND
                )

            result_data = []
            
            for stock in stocks:
                try:
                    # Define o símbolo no MT5Connector
                    mt5.symbol = stock.symbol
                    # Baixa os dados do MT5 (últimos 5 dias)
                    data = mt5.download_data()
                    if data is None or len(data) < 2:
                        logger.warning(f"Dados insuficientes para {stock.symbol}")
                        continue

                    # Pré-processa os dados
                    data = mt5.preprocess_data()

                    # Obtém os preços de fechamento mais recentes
                    today_close = data['close'].iloc[-1]
                    yesterday_close = data['close'].iloc[-2]

                    # Calcula a variação percentual
                    percentage_change = ((today_close - yesterday_close) / yesterday_close) * 100

                    # Monta os dados do ticker
                    ticker_info = {
                        'id': stock.id,
                        'name': stock.name,
                        'image': f"http://localhost:8000/media/{stock.img}",
                        'symbol': stock.symbol,
                        'yahoo': stock.symbol,  # Mantido para compatibilidade
                        'current_price': round(today_close, 2),
                        'close_24h': round(yesterday_close, 2),
                        'price_change_percentage_24h': round(percentage_change, 2),
                        'total_volume': int(data['tick_volume'].iloc[-1]),  # Volume do MT5
                        'last_update': data.index[-1].strftime('%Y-%m-%d %H:%M:%S'),
                        'open_24h': round(data['open'].iloc[-1], 2),
                        'high_24h': round(data['high'].iloc[-1], 2),
                        'low_24h': round(data['low'].iloc[-1], 2),
                    }
                    
                    result_data.append(ticker_info)
                
                except Exception as e:
                    logger.error(f"Erro ao processar {stock.symbol}: {str(e)}")
                    continue

            # Desconecta do MT5 após processar todas as commodities
            mt5.shutdown()

            if not result_data:
                return Response(
                    {"message": "Nenhum dado de mercado disponível"},
                    status=status.HTTP_404_NOT_FOUND
                )

            return Response(result_data, status=status.HTTP_200_OK)

        except Exception as e:
            logger.error(f"Erro ao processar a requisição: {str(e)}")
            mt5.shutdownv()  # Garante desconexão em caso de erro
            return Response(
                {"error": f"Erro ao processar a requisição: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def post(self, request):
        serializer = CommoditieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StockDetail(APIView):
    def get_object(self, pk):
        try:
            return Stock.objects.get(pk=pk)
        except Stock.DoesNotExist:
            return None

    def get(self, request, pk):
        stock = self.get_object(pk)
        if stock is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = StockSerializer(stock)
        return Response(serializer.data)

    def put(self, request, pk):
        stock = self.get_object(pk)
        if stock is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = StockSerializer(stock, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        stock = self.get_object(pk)
        if stock is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        stock.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class CommoditieList(APIView):
    def get(self, request, pk):
        # Busca a conta MT5 ativa do usuário
        api = MT5API.objects.filter(Q(user_id=pk), Q(is_active=True)).last()
        
        if not api:
            return Response(
                {'error': 'Conta MT5 não encontrada ou inativa'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        # Inicializa o MT5Connector com as credenciais do usuário
        mt5 = MT5Connector(
            account=api.account,
            password=api.password,
            server=api.server,
            interval="1d"  # Intervalo diário para dados consistentes
        )
        
        # Inicializa e faz login no MT5
        if not mt5.initialize_mt5():
            return Response(
                {'error': 'Falha ao inicializar o MetaTrader 5'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        if not mt5.login():
            return Response(
                {'error': 'Falha no login do MetaTrader 5'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        try:
            commodities = Commoditie.objects.all()
            if not commodities:
                return Response(
                    {"message": "Nenhuma commoditie encontrada"},
                    status=status.HTTP_404_NOT_FOUND
                )

            result_data = []
            
            for commodity in commodities:
                try:
                    # Define o símbolo no MT5Connector
                    mt5.symbol = commodity.symbol
                    # Baixa os dados do MT5 (últimos 5 dias)
                    data = mt5.download_data()
                    if data is None or len(data) < 2:
                        logger.warning(f"Dados insuficientes para {commodity.symbol}")
                        continue

                    # Pré-processa os dados
                    data = mt5.preprocess_data()

                    # Obtém os preços de fechamento mais recentes
                    today_close = data['close'].iloc[-1]
                    yesterday_close = data['close'].iloc[-2]

                    # Calcula a variação percentual
                    percentage_change = ((today_close - yesterday_close) / yesterday_close) * 100

                    # Monta os dados do ticker
                    ticker_info = {
                        'id': commodity.id,
                        'name': commodity.name,
                        'image': f"http://localhost:8000/media/{commodity.img}",
                        'symbol': commodity.symbol,
                        'yahoo': commodity.yahoo,  # Mantido para compatibilidade
                        'current_price': round(today_close, 2),
                        'close_24h': round(yesterday_close, 2),
                        'price_change_percentage_24h': round(percentage_change, 2),
                        'total_volume': int(data['tick_volume'].iloc[-1]),  # Volume do MT5
                        'last_update': data.index[-1].strftime('%Y-%m-%d %H:%M:%S'),
                        'open_24h': round(data['open'].iloc[-1], 2),
                        'high_24h': round(data['high'].iloc[-1], 2),
                        'low_24h': round(data['low'].iloc[-1], 2),
                    }
                    
                    result_data.append(ticker_info)
                
                except Exception as e:
                    logger.error(f"Erro ao processar {commodity.symbol}: {str(e)}")
                    continue

            # Desconecta do MT5 após processar todas as commodities
            mt5.shutdown()

            if not result_data:
                return Response(
                    {"message": "Nenhum dado de mercado disponível"},
                    status=status.HTTP_404_NOT_FOUND
                )

            return Response(result_data, status=status.HTTP_200_OK)

        except Exception as e:
            logger.error(f"Erro ao processar a requisição: {str(e)}")
            mt5.shutdown() # Garante desconexão em caso de erro
            return Response(
                {"error": f"Erro ao processar a requisição: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def post(self, request):
        serializer = CommoditieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommoditieDetail(APIView):
    def get_object(self, pk):
        try:
            return Commoditie.objects.get(pk=pk)
        except Commoditie.DoesNotExist:
            return None

    def get(self, request, pk):
        commoditie = self.get_object(pk)
        if commoditie is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CommoditieSerializer(commoditie)
        return Response(serializer.data)

    def put(self, request, pk):
        commoditie = self.get_object(pk)
        if commoditie is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CommoditieSerializer(commoditie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        commoditie = self.get_object(pk)
        if commoditie is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        commoditie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Index Views
class IndexList(APIView):
    def get(self, request):
        indices = Index.objects.all()
        serializer = IndexSerializer(indices, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = IndexSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IndexDetail(APIView):
    def get_object(self, pk):
        try:
            return Index.objects.get(pk=pk)
        except Index.DoesNotExist:
            return None

    def get(self, request, pk):
        index = self.get_object(pk)
        if index is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = IndexSerializer(index)
        return Response(serializer.data)

    def put(self, request, pk):
        index = self.get_object(pk)
        if index is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = IndexSerializer(index, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        index = self.get_object(pk)
        if index is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        index.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



class CommoditieDetailView(APIView):
    def get_object(self, pk):
        try:
            return Commoditie.objects.get(pk=pk)
        except Commoditie.DoesNotExist:
            return None

    def get_ticker_data(self, ticker_symbol):
        """
        Obtém dados do ticker via yfinance e calcula a variação percentual
        """
        try:
            ticker = yf.Ticker(ticker_symbol)
            # Obtém dados históricos dos últimos 2 dias úteis
            history = ticker.history(period="5d")  # Pegamos 5 dias para garantir dados
            
            if history.empty:
                return None

            # Obtém os preços de fechamento mais recentes
            today_close = history['Close'].iloc[-1]
            yesterday_close = history['Close'].iloc[-2]

            # Calcula a variação percentual
            percentage_change = ((today_close - yesterday_close) / yesterday_close) * 100

            # Obtém informações adicionais do ticker
            ticker_info = {
                'current_price': round(today_close, 2),
                'previous_close': round(yesterday_close, 2),
                'percentage_change': round(percentage_change, 2),
                'volume': int(history['Volume'].iloc[-1]),
                'last_update': history.index[-1].strftime('%Y-%m-%d %H:%M:%S'),
                'open_price': round(history['Open'].iloc[-1], 2),
                'high_price': round(history['High'].iloc[-1], 2),
                'low_price': round(history['Low'].iloc[-1], 2),
            }
            return ticker_info

        except Exception as e:
            print(f"Erro ao obter dados do ticker {ticker_symbol}: {str(e)}")
            return None

    def get(self, request, pk):
        # Obtém o objeto Commoditie do banco de dados
        commoditie = self.get_object(pk)
        if commoditie is None:
            return Response(
                {"error": "Commoditie não encontrada"},
                status=status.HTTP_404_NOT_FOUND
            )

        # Serializa os dados básicos da commoditie
        serializer = CommoditieSerializer(commoditie)
        response_data = serializer.data

        # Adiciona os dados do mercado se houver um ticker_symbol
        if hasattr(commoditie, 'ticker_symbol') and commoditie.ticker_symbol:
            ticker_data = self.get_ticker_data(commoditie.ticker_symbol)
            if ticker_data:
                response_data['market_data'] = ticker_data
            else:
                response_data['market_data'] = {
                    "error": "Não foi possível obter dados de mercado para este ativo"
                }

        return Response(response_data, status=status.HTTP_200_OK)

# Exemplo de uso para múltiplos ativos
class CommoditieListView(APIView):
    def get(self, request):
        # Obtém todas as commodities
        commodities = Commoditie.objects.all()
        response_data = []

        for commoditie in commodities:
            # Serializa os dados básicos
            serializer = CommoditieSerializer(commoditie)
            commoditie_data = serializer.data
            print(commodities)

            # Adiciona os dados do mercado se houver ticker_symbol
            if hasattr(commoditie, 'ticker_symbol') and commoditie.ticker_symbol:
                ticker_data = CommoditieDetailView().get_ticker_data(commoditie.ticker_symbol)
                if ticker_data:
                    commoditie_data['market_data'] = ticker_data
                else:
                    commoditie_data['market_data'] = {
                        "error": "Não foi possível obter dados de mercado para este ativo"
                    }

            response_data.append(commoditie_data)

        return Response(response_data, status=status.HTTP_200_OK)
    





# Commoditie Views
class CurrencyList(APIView):
    def get(self, request, pk):
        # Busca a conta MT5 ativa do usuário
        api = MT5API.objects.filter(Q(user_id=pk), Q(is_active=True)).last()
        
        if not api:
            return Response(
                {'error': 'Conta MT5 não encontrada ou inativa'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        # Inicializa o MT5Connector com as credenciais do usuário
        mt5 = MT5Connector(
            account=api.account,
            password=api.password,
            server=api.server,
            interval="1d"  # Intervalo diário para dados consistentes
        )
        
        # Inicializa e faz login no MT5
        if not mt5.initialize_mt5():
            return Response(
                {'error': 'Falha ao inicializar o MetaTrader 5'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        if not mt5.login():
            return Response(
                {'error': 'Falha no login do MetaTrader 5'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        try:
            currencies = Currency.objects.all()
            if not currencies:
                return Response(
                    {"message": "Nenhuma currency encontrada"},
                    status=status.HTTP_404_NOT_FOUND
                )

            result_data = []
            
            for currency in currencies:
                try:
                    # Define o símbolo no MT5Connector
                    mt5.symbol = currency.symbol
                    # Baixa os dados do MT5 (últimos 5 dias)
                    data = mt5.download_data()
                    if data is None or len(data) < 2:
                        logger.warning(f"Dados insuficientes para {currency.symbol}")
                        continue

                    # Pré-processa os dados
                    data = mt5.preprocess_data()

                    # Obtém os preços de fechamento mais recentes
                    today_close = data['close'].iloc[-1]
                    yesterday_close = data['close'].iloc[-2]

                    # Calcula a variação percentual
                    percentage_change = ((today_close - yesterday_close) / yesterday_close) * 100

                    # Monta os dados do ticker
                    ticker_info = {
                        'id': currency.id,
                        'name': currency.name,
                        'image': f"http://localhost:8000/media/{currency.img}",
                        'symbol': currency.symbol,
                        'yahoo': currency.yahoo,  # Mantido para compatibilidade
                        'current_price': round(today_close, 2),
                        'close_24h': round(yesterday_close, 2),
                        'price_change_percentage_24h': round(percentage_change, 2),
                        'total_volume': int(data['tick_volume'].iloc[-1]),  # Volume do MT5
                        'last_update': data.index[-1].strftime('%Y-%m-%d %H:%M:%S'),
                        'open_24h': round(data['open'].iloc[-1], 2),
                        'high_24h': round(data['high'].iloc[-1], 2),
                        'low_24h': round(data['low'].iloc[-1], 2),
                    }
                    
                    result_data.append(ticker_info)
                
                except Exception as e:
                    logger.error(f"Erro ao processar {currency.symbol}: {str(e)}")
                    continue

            # Desconecta do MT5 após processar todas as commodities
            mt5.shutdown()

            if not result_data:
                return Response(
                    {"message": "Nenhum dado de mercado disponível"},
                    status=status.HTTP_404_NOT_FOUND
                )

            return Response(result_data, status=status.HTTP_200_OK)

        except Exception as e:
            logger.error(f"Erro ao processar a requisição: {str(e)}")
            mt5.shutdownv()  # Garante desconexão em caso de erro
            return Response(
                {"error": f"Erro ao processar a requisição: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def post(self, request):
        serializer = CommoditieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
