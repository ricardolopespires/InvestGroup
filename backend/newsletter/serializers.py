from rest_framework import serializers
from .models import Subscriber




from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import Subscriber  # Supondo que você tenha um modelo Subscriber

class SubscriberSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=254, required=True)

    class Meta:
        model = Subscriber  # Model de onde os dados são salvos
        fields = ['email']  # Apenas o campo 'email' será exposto pela API

    def validate_email(self, value):
        """
        Valida que o e-mail não esteja já registrado no banco de dados.
        """
        if Subscriber.objects.filter(email=value).exists():
            raise ValidationError("Este e-mail já está registrado.")
        return value


    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
    
