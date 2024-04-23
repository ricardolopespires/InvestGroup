from ast import Expression
from multiprocessing import context
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from accounts.models import OneTimePassword
from .serializers import PasswordResetRequestSerializer
from .serializers import LogoutUserSerializer
from .serializers import  UserRegisterSerializer
from .serializers import LoginSerializer
from .serializers import SetNewPasswordSerializer
from .serializers import UserSerializers
from .serializers import PerfilUserSerializer
from .serializers import Perfil_Add_User_Serializer
from .serializers import SituacaoUserSerializer
from .serializers import UserSerializer
from .serializers import Situacao_Add_User_Serializer
from rest_framework import status
from .utils import send_generated_otp_to_email
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import smart_str, DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view 
from .models import User, Perfil, Situacao
from rest_framework.views import APIView
# Create your views here.




class UserListView(APIView):    
    permission_classes = [IsAuthenticated]   

    def get(self, request, pk):
        queryset = User.objects.filter(email = pk)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RegisterView(GenericAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        user = request.data
        serializer=self.serializer_class(data=user)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user_data=serializer.data
            send_generated_otp_to_email(user_data['email'], request)
            return Response({
                'data':user_data,
                'message':'obrigado por se inscrever, uma senha foi enviada para verificar seu e-mail"'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class VerifyUserEmail(GenericAPIView):
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
        return Response({'message':'we have sent you a link to reset your password'}, status=status.HTTP_200_OK)
        # return Response({'message':'user with that email does not exist'}, status=status.HTTP_400_BAD_REQUEST)
    



class PasswordResetConfirm(GenericAPIView):

    def get(self, request, uidb64, token):
        try:
            user_id=smart_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(id=user_id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'message':'token is invalid or has expired'}, status=status.HTTP_401_UNAUTHORIZED)
            return Response({'success':True, 'message':'credentials is valid', 'uidb64':uidb64, 'token':token}, status=status.HTTP_200_OK)

        except DjangoUnicodeDecodeError as identifier:
            return Response({'message':'token is invalid or has expired'}, status=status.HTTP_401_UNAUTHORIZED)

class SetNewPasswordView(GenericAPIView):
    serializer_class=SetNewPasswordSerializer

    def patch(self, request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success':True, 'message':"password reset is succesful"}, status=status.HTTP_200_OK)


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

    serializer_class= UserSerializers

    def put(self, request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


@api_view(['GET', 'PUT']) 
def user_detail(request, pk): 
    try: 
        user = User.objects.get(email=pk) 
    except User.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        user_serializer = UserSerializers(user) 
        return Response(user_serializer.data) 
 
    elif request.method == 'PUT': 
        user_serializer = UserSerializers(user, data=request.data) 
        if user_serializer.is_valid(): 
            user_serializer.save() 
            return Response(user_serializer.data) 
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 



@api_view(['GET', 'PUT']) 
def perfil_detail(request, pk): 
    try: 
        perfil = Perfil.objects.get(usuario=pk) 
    except Perfil.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        perfil_serializer = PerfilUserSerializer(perfil) 
        return Response(perfil_serializer.data) 
 

 

@api_view(['GET', 'PUT']) 
def perfil_username(request, pk): 
    try: 
        perfil = Perfil.objects.get(id=pk) 
    except Perfil.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        perfil_serializer = Perfil_Add_User_Serializer(perfil) 
        return Response(perfil_serializer.data) 
 
    elif request.method == 'PUT': 
        perfil_serializer = Perfil_Add_User_Serializer(perfil, data=request.data) 
        print(perfil_serializer)
        if perfil_serializer.is_valid(): 
            perfil_serializer.save() 
            return Response(perfil_serializer.data) 
        return Response(perfil_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 



@api_view(['GET', 'PUT']) 
def situacao_username(request, pk): 
    try: 
        situacao = Situacao.objects.get(id=pk) 
    except situacao.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        situacao_serializer = Situacao_Add_User_Serializer(situacao) 
        return Response(situacao_serializer.data) 
 
    elif request.method == 'PUT': 
        situacao_serializer = Situacao_Add_User_Serializer(situacao, data=request.data) 
        print(situacao_serializer)
        if situacao_serializer.is_valid(): 
            situacao_serializer.save() 
            return Response(situacao_serializer.data) 
        return Response(situacao_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
