from unicodedata import name
from django.urls import path
from .views import (
        RegisterView,
        SecretGenerateAPIView,
        TwoFactorDetailView,       
        VerifyUserEmail,
        LoginUserView, 
        TestingAuthenticatedReq, 
        PasswordResetConfirm, 
        PasswordResetRequestView,SetNewPasswordView, LogoutApiView)


from .views import UserListView
from .views import UserDetailView
from .views import ChangePasswordView
from .views import ImageUploadView
from .views import TwoFactorView
from .views import VerifyTwoFactorView
from . views import UserStatusView
from rest_framework_simplejwt.views import (TokenRefreshView,)

urlpatterns = [
        path('list/<str:pk>/',UserListView.as_view(), name ="list"),
        path('user/status/<str:pk>/', UserStatusView.as_view(), name ="user-status"),     
        path('register/', RegisterView.as_view(), name='register'),
        path('verify-email/', VerifyUserEmail.as_view(), name='verify'),
        path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        path('login/', LoginUserView.as_view(), name='login-user'),
        path('get-something/', TestingAuthenticatedReq.as_view(), name='just-for-testing'),
        path('password-reset/', PasswordResetRequestView.as_view(), name='password-reset'),
        path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='reset-password-confirm'),
        path('set-new-password/', SetNewPasswordView.as_view(), name='set-new-password'),
        path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
        path('change-password/', ChangePasswordView.as_view(), name='change-password'),
        path('logout/', LogoutApiView.as_view(), name='logout'),
        path('user/details/<str:pk>/', UserDetailView.as_view(), name='users'),
        path('upload-image/', ImageUploadView.as_view(), name='image_upload'),      
        path('generate-secret/', SecretGenerateAPIView.as_view(), name='generate-secret'),
        path('two-factor/<pk>/', TwoFactorView.as_view(), name='two-factor'),
        path('twofactor/detail/<int:pk>/', TwoFactorDetailView.as_view(), name='twofactor-detail'),
        path('verify/two-factor/<pk>/', VerifyTwoFactorView.as_view(), name='verify-twofactor'),

    ]

