from rest_framework import serializers
import pandas as pd
import math

class FinancialDataSerializer(serializers.Serializer):
    time = serializers.IntegerField()
    open = serializers.FloatField()
    high = serializers.FloatField()
    low = serializers.FloatField()
    close = serializers.FloatField()
    close_smooth = serializers.FloatField(required=False, allow_null=True)  # Opcional
    signal = serializers.CharField(required=False, allow_null=True)  # Opcional, pode ser nulo

class FinancialDataListSerializer(serializers.ListSerializer):
    child = FinancialDataSerializer()




class SignalSerializer(serializers.Serializer):
    time = serializers.IntegerField()
    position = serializers.CharField()
    color = serializers.CharField()
    shape = serializers.CharField()
    text = serializers.CharField()
    type = serializers.CharField()
    size = serializers.IntegerField()






class PositionSerializer(serializers.Serializer):
    ticket = serializers.IntegerField()
    time = serializers.DateTimeField()
    time_update = serializers.DateTimeField()
    type = serializers.CharField()
    symbol = serializers.CharField()
    volume = serializers.FloatField()
    price_open = serializers.FloatField()
    price_current = serializers.FloatField()
    sl = serializers.FloatField()
    tp = serializers.FloatField()
    profit = serializers.FloatField()
    comment = serializers.CharField()

class DealSerializer(serializers.Serializer):
    ticket = serializers.IntegerField()
    time = serializers.DateTimeField()
    type = serializers.CharField()
    entry = serializers.CharField()
    symbol = serializers.CharField()
    volume = serializers.FloatField()
    price = serializers.FloatField()
    profit = serializers.FloatField()
    swap = serializers.FloatField()
    commission = serializers.FloatField()
    comment = serializers.CharField()

class MT5DataSerializer:
    @staticmethod
    def serialize_positions(df):
        if df.empty:
            return []
        return PositionSerializer(df.to_dict('records'), many=True).data

    @staticmethod
    def serialize_deals(df):
        if df.empty:
            return []
        return DealSerializer(df.to_dict('records'), many=True).data
    

    @staticmethod
    def serialize_positions(df):
        """
        Serializa um DataFrame de posições/signais em um formato JSON.

        Args:
            df (pd.DataFrame): DataFrame com colunas 'timeframe', 'time', 'signal', 'price'.

        Returns:
            list: Lista de dicionários serializados.
        """
        if df.empty:
            return []
        
        # Converte o DataFrame para uma lista de dicionários
        result = df.to_dict(orient='records')
        
        # Formata o timestamp e outros campos, se necessário
        for item in result:
            if item['time'] is not None:
                item['time'] = item['time'].isoformat()  # Converte para string ISO
            if pd.isna(item['price']):
                item['price'] = None  # Trata valores NaN
        return result
    

class PerformanceQuerySerializer(serializers.Serializer):
    """
    Serializer para validar parâmetros de consulta da API de desempenho.
    """
    start_date = serializers.DateField(format="%Y-%m-%d", input_formats=["%Y-%m-%d"])
    end_date = serializers.DateField(format="%Y-%m-%d", input_formats=["%Y-%m-%d"])
    initial_capital = serializers.FloatField(min_value=0.01, default=10000)

    def validate(self, data):
        """
        Valida que start_date é anterior a end_date.
        """
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError("Data inicial deve ser anterior à data final.")
        return data


class PerformanceMetricsSerializer(serializers.Serializer):
    """
    Serializer para métricas de desempenho retornadas pelo MT5Connector.
    """
    Resultado_Liq_Tot = serializers.FloatField(allow_null=True)
    Resultado_Total = serializers.FloatField(allow_null=True)
    Lucro_Bruto = serializers.FloatField(allow_null=True)
    Prejuizo_Bruto = serializers.FloatField(allow_null=True)
    Operacoes = serializers.IntegerField(allow_null=True)
    Vencedoras = serializers.IntegerField(allow_null=True)
    Saldo_Liquido_Total = serializers.FloatField(allow_null=True)
    Fator_de_Lucro = serializers.FloatField(allow_null=True)
    Numero_Total_de_Operacoes = serializers.IntegerField(allow_null=True)
    Operacoes_Zeradas = serializers.IntegerField(allow_null=True)
    Media_de_Lucro_Prejuizo = serializers.FloatField(allow_null=True)
    Media_de_Operacoes_Vencedoras = serializers.FloatField(allow_null=True)
    Maior_Operacao_Vencedora = serializers.FloatField(allow_null=True)
    Maior_Sequencia_Vencedora = serializers.IntegerField(allow_null=True)
    Media_de_Tempo_em_Op_Vencedoras_mins = serializers.FloatField(allow_null=True)
    Media_de_Tempo_em_Operacoes_mins = serializers.FloatField(allow_null=True)
    Saldo_Total = serializers.FloatField(allow_null=True)
    Custos = serializers.FloatField(allow_null=True)
    Percentual_de_Operacoes_Vencedoras = serializers.FloatField(allow_null=True)
    Operacoes_Perdedoras = serializers.IntegerField(allow_null=True)
    Razao_Media_Lucro_Media_Prejuizo = serializers.FloatField(allow_null=True)
    Media_de_Operacoes_Perdedoras = serializers.FloatField(allow_null=True)
    Maior_Operacao_Perdedora = serializers.FloatField(allow_null=True)
    Maior_Sequencia_Perdedora = serializers.IntegerField(allow_null=True)
    Media_de_Tempo_em_Op_Perdedoras = serializers.FloatField(allow_null=True)
    Patrimonio_Necessario_Maior_Operacao = serializers.FloatField(allow_null=True)
    Retorno_no_Capital_Inicial = serializers.FloatField(allow_null=True)
    Patrimonio_Maximo = serializers.FloatField(allow_null=True)

    def to_representation(self, instance):
        """
        Converte valores especiais (Infinity, NaN) para representação JSON.
        """
        representation = super().to_representation(instance)
        for key, value in representation.items():
            if value is not None and (math.isinf(value) or math.isnan(value)):
                representation[key] = None  # or str(value) for "Infinity"/"NaN"
        return representation