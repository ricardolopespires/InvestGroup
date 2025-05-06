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
from datetime import datetime, timedelta
from django.utils import timezone
import pandas as pd
import logging
import re

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
    """
    API View para recuperar o histórico de negociações de um usuário no MetaTrader 5.
    """

    def get(self, request, pk, from_date=None, to_date=None):
        """
        Retorna o histórico de negociações para o usuário especificado.
        
        Args:
            pk: ID do usuário
            from_date: Data inicial (formato: YYYY-MM-DD), opcional
            to_date: Data final (formato: YYYY-MM-DD), opcional
            
        Returns:
            Response com lista de negociações ou mensagem de erro
        """
        try:
            # Validação e parsing das datas
            from_date = self._parse_date(from_date, default=datetime(2000, 1, 1))
            to_date = self._parse_date(to_date, default=datetime.now())

            # Validação do intervalo de datas
            if from_date > to_date:
                return Response(
                    {'error': 'Data inicial deve ser anterior à data final'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Busca conta MT5 ativa
            mt5_api = MT5API.objects.filter(user_id=pk, is_active=True).last()
            if not mt5_api:
                return Response(
                    {'error': 'Conta MT5 não encontrada ou inativa'},
                    status=status.HTTP_404_NOT_FOUND
                )

            # Inicialização e conexão com MT5
            mt5 = MT5Connector(
                account=mt5_api.account,
                password=mt5_api.password,
                server=mt5_api.server
            )

            try:
                if not mt5.initialize_mt5():
                    return Response(
                        {'error': 'Falha ao inicializar o MetaTrader 5'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR
                    )

                if not mt5.login():
                    return Response(
                        {'error': 'Falha na autenticação do MetaTrader 5'},
                        status=status.HTTP_401_UNAUTHORIZED
                    )

                # Recuperação do histórico com tratamento para parâmetros de data
                try:
                    history = mt5.history_deals_get(from_date=from_date, to_date=to_date)
                except TypeError as te:
                    # Fallback para caso o método não aceite from_date/to_date
                    if "unexpected keyword argument 'from_date'" in str(te):
                        history = mt5.history_deals_get()  # Tenta sem parâmetros de data
                    else:
                        raise
                        
                result = history.to_dict('records') if history is not None else []

                return Response(result, status=status.HTTP_200_OK)

            finally:
                mt5.shutdown()

        except ValueError as ve:
            return Response(
                {'error': f'Formato de data inválido: {str(ve)}'},
                status=status.HTTP_400_BAD_REQUEST
            )
        except TypeError as te:
            return Response(
                {'error': f'Erro na configuração do conector MT5: {str(te)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        except Exception as e:
            return Response(
                {'error': f'Erro ao processar a solicitação: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def _parse_date(self, date_str, default):
        """
        Converte string de data para objeto datetime ou retorna data padrão.
        
        Args:
            date_str: String de data no formato YYYY-MM-DD
            default: Valor padrão se date_str for None
            
        Returns:
            Objeto datetime
        """
        if date_str is None:
            return default
        return datetime.strptime(date_str, "%Y-%m-%d")
    

class PerformanceView(APIView):
    """
    API View para recuperar métricas de desempenho de um usuário no MetaTrader 5.
    """

    def _parse_date(self, date_str, default):
        """Converte string de data para objeto datetime."""
        if not date_str:
            return default
        try:
            return datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Formato de data inválido. Use AAAA-MM-DD")

    def _validate_inputs(self, symbol, initial_capital, from_date, to_date):
        """Valida todas as entradas da requisição."""
        # Validar símbolo
        symbol = symbol.strip().upper()
        if not re.match(r'^[A-Z0-9./]+$', symbol):
            raise ValueError('Símbolo inválido. Use apenas letras, números, pontos ou barras.')

        # Validar capital inicial
        try:
            initial_capital = float(initial_capital)
            if initial_capital <= 0:
                raise ValueError("Capital inicial deve ser maior que zero.")
        except ValueError as ve:
            raise ValueError(f'Capital inicial inválido: {str(ve)}')

        # Validar intervalo de datas
        if from_date > to_date:
            raise ValueError('Data inicial deve ser anterior à data final')

        return symbol, initial_capital

    def _initialize_mt5(self, pk):
        """Inicializa e autentica a conexão com o MetaTrader 5."""
        mt5_api = MT5API.objects.filter(user_id=pk, is_active=True).last()
        if not mt5_api:
            raise ValueError('Conta MT5 não encontrada ou inativa')

        mt5 = MT5Connector(
            account=mt5_api.account,
            password=mt5_api.password,
            server=mt5_api.server
        )

        if not mt5.initialize_mt5():
            raise ConnectionError('Falha ao inicializar o MetaTrader 5')

        if not mt5.login():
            raise ConnectionError('Falha na autenticação do MetaTrader 5')

        return mt5

    def get(self, request, pk, symbol):
        """
        Retorna métricas de desempenho para usuário e símbolo especificados como DataFrame.

        Args:
            pk: ID do usuário
            symbol: Símbolo do instrumento (e.g., EURUSD)

        Query Parameters:
            initial_capital: Capital inicial (float, default: 10000)
            from_date: Data inicial (formato: AAAA-MM-DD)
            to_date: Data final (formato: AAAA-MM-DD)

        Returns:
            Response com DataFrame de métricas ou mensagem de erro
        """
        try:
            # Parse e validação das entradas
            from_date = self._parse_date(request.query_params.get('from_date'), default=datetime(2000, 1, 1))
            to_date = self._parse_date(request.query_params.get('to_date'), default=datetime.now())
            initial_capital = request.query_params.get('initial_capital', '10000')

            symbol, initial_capital = self._validate_inputs(
                symbol, initial_capital, from_date, to_date
            )

            # Inicialização do MT5
            mt5 = self._initialize_mt5(pk)
            try:
                # Calcula métricas
                logger.info(f"Calculando métricas para usuário {pk}, símbolo {symbol}")
                performance = mt5.calculate_performance_metrics_for_symbol(
                    symbol=symbol,
                    start_date=from_date,
                    end_date=to_date,
                    initial_capital=initial_capital
                )

                if performance.empty or 'error' in performance.columns:
                    logger.info(f"Nenhuma métrica encontrada para {symbol}")
                    return Response(
                        {'message': f'Nenhuma métrica encontrada para {symbol}'},
                        status=status.HTTP_200_OK
                    )

                logger.info(f"Métricas calculadas com sucesso para {symbol}")
                return Response(performance.to_dict(orient='records'), status=status.HTTP_200_OK)

            finally:
                mt5.shutdown()

        except ValueError as ve:
            logger.error(f"Erro de validação: {str(ve)}")
            return Response(
                {'error': f'Erro de validação: {str(ve)}'},
                status=status.HTTP_400_BAD_REQUEST
            )
        except ConnectionError as ce:
            logger.error(f"Erro de conexão com MT5: {str(ce)}")
            return Response(
                {'error': f'Erro de conexão com MT5: {str(ce)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        except Exception as e:
            logger.error(f"Erro inesperado: {str(e)}")
            return Response(
                {'error': f'Erro inesperado: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )