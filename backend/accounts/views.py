from ast import Expression
from multiprocessing import context
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics
from django.http import JsonResponse
from rest_framework.response import Response
from accounts.models import OneTimePassword
from .serializers import PasswordResetRequestSerializer
from .serializers import LogoutUserSerializer
from .serializers import  UserRegisterSerializer
from .serializers import LoginSerializer
from .serializers import SetNewPasswordSerializer
from .serializers import UserStatusSerializer
from .serializers import UserSerializer
from .serializers import ChangePasswordSerializer
from .serializers import UserUploadImage
from .serializers import TwofactorSerializer
from rest_framework import status
from .utils import send_generated_otp_to_email
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import smart_str, DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view 
from .models import User, TwoFactor
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
import pyotp
# Create your views here.




class UserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            # Filtrando o usuário pelo e-mail
            queryset = User.objects.filter(email=pk)
            
            # Verifica se existe algum usuário
            if not queryset.exists():
                raise NotFound(detail="Usuário não encontrado com o email fornecido.")

            # Serializando os dados encontrados
            serializer = UserSerializer(queryset, many=True)
            
            # Retorna a resposta com os dados dos usuários
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            # Caso haja algum erro inesperado
            return Response(
                {"detail": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    

class UserStatusView(APIView):
    def get(self, request, pk):
        queryset = User.objects.filter(id = pk)
        serializer = UserStatusSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        queryset = User.objects.get(id = pk)
        serializer = UserStatusSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        queryset = User.objects.get(id = pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    



class RegisterView(GenericAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        user_data = request.data  # Assuming request data contains user input
        print(user_data)
        serializer = self.serializer_class(data=user_data)
        
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            send_generated_otp_to_email(user.email, request)  # Assuming send_generated_otp_to_email function exists
            return Response({
                'data': serializer.data,
                'message': 'Obrigado por se inscrever. Um código foi enviado para verificar seu e-mail.'
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class VerifyUserEmail(APIView):
    def post(self, request):
        try:
            passcode = request.data.get('otp')
            user_pass_obj=OneTimePassword.objects.get(otp=passcode)
            user=user_pass_obj.user
            if not user.is_verified:
                user.is_verified=True
                user.save()
                return Response({
                    'message':'account email verified successfully'
                }, status=status.HTTP_200_OK)
            return Response({'message':'passcode is invalid user is already verified'}, status=status.HTTP_204_NO_CONTENT)
        except OneTimePassword.DoesNotExist as identifier:
            return Response({'message':'passcode not provided'}, status=status.HTTP_400_BAD_REQUEST)
        

class LoginUserView(GenericAPIView):
    serializer_class=LoginSerializer
    def post(self, request):
        serializer= self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PasswordResetRequestView(GenericAPIView):
    serializer_class=PasswordResetRequestSerializer

    def post(self, request):
        serializer=self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        return Response({'message':'enviamos a você um link para redefinir sua senha'}, status=status.HTTP_200_OK)
        # return Response({'message':'user with that email does not exist'}, status=status.HTTP_400_BAD_REQUEST)
    


class PasswordResetConfirm(GenericAPIView):

    def get(self, request, uidb64, token):
        try:
            user_id=smart_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(id=user_id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'message':'o token é inválido ou expirou'}, status=status.HTTP_401_UNAUTHORIZED)
            return Response({'success':True, 'message':'credenciais são válidas', 'uidb64':uidb64, 'token':token}, status=status.HTTP_200_OK)

        except DjangoUnicodeDecodeError as identifier:
            return Response({'message':'o token é inválido ou expirou'}, status=status.HTTP_401_UNAUTHORIZED)

class SetNewPasswordView(GenericAPIView):
    serializer_class=SetNewPasswordSerializer

    def patch(self, request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success':True, 'message':"A redefinição de senha foi bem-sucedida"}, status=status.HTTP_200_OK)


class TestingAuthenticatedReq(GenericAPIView):
    permission_classes=[IsAuthenticated]

    def get(self, request):

        data={
            'msg':'its works'
        }
        return Response(data, status=status.HTTP_200_OK)

class LogoutApiView(GenericAPIView):
    serializer_class=LogoutUserSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class QuizView(GenericAPIView):

    serializer_class= UserStatusSerializer

    def put(self, request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



class UserDetailView(APIView):
    
    def get(self, request, pk):
        try:
            user = User.objects.get(email=pk)
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            user = User.objects.get(email=pk)
            user_serializer = UserSerializer(user, data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
 


class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class ImageUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        images = User.objects.all()
        serializer = UserUploadImage(images, many=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        images_serializer = UserUploadImage(data=request.data)
        print(request.data)
        if images_serializer.is_valid():
            images_serializer.save()
            return Response(images_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', images_serializer.errors)
            return Response(images_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


class SecretGenerateAPIView(APIView):
    def get(self, request, format=None):
        secret = pyotp.random_base32()
        return Response({'secret': secret}, status=status.HTTP_200_OK)
    
    

class TwoFactorView(APIView):
    permission_classes = [IsAuthenticated]   

    def get(self, request, pk):
        twofactor = TwoFactor.objects.filter(user_id = pk)
        serializer = TwofactorSerializer(twofactor, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, pk):
        twofactor_serializer = TwofactorSerializer(data=request.data)
        if twofactor_serializer.is_valid():
            twofactor_serializer.save()
            return Response(twofactor_serializer.data, status=status.HTTP_201_CREATED)
        return Response(twofactor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



class TwoFactorDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        twofactor = TwoFactor.objects.filter(user_id=pk)
        serializer = TwofactorSerializer(twofactor, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        twofactor = TwoFactor.objects.get(user_id=pk)
        serializer = TwofactorSerializer(twofactor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        twofactor = TwoFactor.objects.get(user_id=pk)
        twofactor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



class VerifyTwoFactorView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        passcode = request.data.get("otp")
        
        if not passcode:
            return Response({'message': 'Código OTP não fornecido'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            towfactor = TwoFactor.objects.get(user_id=pk)
            user = towfactor.user
        except TwoFactor.DoesNotExist:
            return Response({'message': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        totp = pyotp.TOTP(towfactor.key)
        is_valid = totp.verify(passcode)
        
        if is_valid:
            user.two_factor = True
            user.save()
            return Response({'message': 'Código verificado com sucesso'}, status=status.HTTP_200_OK)
        
        return Response({'message': 'Código inválido, realize outro login'}, status=status.HTTP_401_UNAUTHORIZED)