from rest_framework import serializers
import pandas as pd

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