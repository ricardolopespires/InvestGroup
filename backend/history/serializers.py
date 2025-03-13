# analyzer/serializers.py
from rest_framework import serializers

class FinancialDataSerializer(serializers.Serializer):
    time = serializers.CharField()
    open = serializers.FloatField()
    high = serializers.FloatField()
    low = serializers.FloatField()
    close = serializers.FloatField()

class FinancialDataListSerializer(serializers.ListSerializer):
    child = FinancialDataSerializer()