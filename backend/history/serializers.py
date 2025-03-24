from rest_framework import serializers

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