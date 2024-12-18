from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Subscriber
from .serializers import SubscriberSerializer
from django.core.mail import send_mail
from django.conf import settings

import logging

# Criando um logger para a classe
logger = logging.getLogger(__name__)

class SubscribeView(APIView):

    def post(self, request):        
        # Instanciando o serializer com os dados da requisição
        email_serializer = SubscriberSerializer(data=request.data)

        # Usando logging em vez de print
        logger.debug(f"Dados recebidos para inscrição: {request.data}")

        # Verificando a validade dos dados do serializer
        if email_serializer.is_valid():
            # Salvando os dados se válidos
            email_serializer.save()
            return Response(email_serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Caso os dados não sejam válidos, retornando os erros
            logger.warning(f"Erro de validação: {email_serializer.errors}")
            return Response(email_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# API para cancelar a inscrição
class UnsubscribeView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        try:
            subscriber = Subscriber.objects.get(email=email)
            subscriber.subscribed = False
            subscriber.save()
            return Response({"message": "Você foi desinscrito com sucesso."}, status=status.HTTP_200_OK)
        except Subscriber.DoesNotExist:
            return Response({"error": "E-mail não encontrado."}, status=status.HTTP_404_NOT_FOUND)

# API para enviar a newsletter
class SendNewsletterView(APIView):
    def post(self, request, *args, **kwargs):
        subject = request.data.get('subject')
        message = request.data.get('message')
        subscribers = Subscriber.objects.filter(subscribed=True)
        recipient_list = [subscriber.email for subscriber in subscribers]
        if not recipient_list:
            return Response({"error": "Nenhum assinante encontrado."}, status=status.HTTP_400_BAD_REQUEST)

        send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
        return Response({"message": "Newsletter enviada com sucesso!"}, status=status.HTTP_200_OK)
