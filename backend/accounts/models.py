from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .validators import validate_cpf
from rest_framework_simplejwt.tokens import RefreshToken
from phone_field import PhoneField
from django.core.files import File
from PIL import Image, ImageDraw
from django.utils import timezone 
from io import BytesIO
import pyotp
import qrcode


from accounts.managers import UserManager


def upload_image_user(instance, filename):
    return f'{instance.id_user}-{filename}'
# Create your models here.

AUTH_PROVIDERS ={'email':'email', 'google':'google', 'github':'github', 'linkedin':'linkedin'}

class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True, editable=False) 
    email = models.EmailField(
        max_length=255, verbose_name=_("Email Address"), unique=True
    )
    first_name = models.CharField(max_length=100, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=100, verbose_name=_("Last Name"))
    address = models.CharField('Endereço', max_length = 190, blank = True)
    date_of_birth = models.DateField(default=timezone.now) 
    state = models.CharField('Estado',  max_length = 100, blank = True) 
    city = models.CharField('Cidade', max_length = 190, blank = True)
    cpf = models.CharField(max_length= 11, default = 0, validators=[validate_cpf])
    phone = PhoneField(blank=True, help_text='Contact phone number')   
    img = models.ImageField(upload_to = "user", blank = True, null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified=models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    situation = models.BooleanField('Situação financeira', blank=True, default=False)
    perfil = models.BooleanField('Perfil do Investidor', blank=True, default=False)
    two_factor = models.BooleanField('Autenticação de dois fatores',  blank=True, default=False)
    auth_provider=models.CharField(max_length=50, blank=False, null=False, default=AUTH_PROVIDERS.get('email'))
   

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()

    def tokens(self):    
        refresh = RefreshToken.for_user(self)
        return {
            "refresh":str(refresh),
            "access":str(refresh.access_token)
        }


    def __str__(self):
        return self.email

    @property
    def get_full_name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"


class OneTimePassword(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    otp=models.CharField(max_length=6)


    def __str__(self):
        return f"{self.user.first_name} - otp code"
    

class TwoFactor(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      key = models.CharField(max_length=100, default=pyotp.random_base32)
      qr_code = models.ImageField(upload_to = 'TwoFactor/qr_code', blank = True, help_text='Autenticação de 2 Fatores', null = True)
      is_active = models.BooleanField(default=False)

      def __str__(self):
            return f'{self.user}'
      def save(self, *args, **kwargs):
        
            if not self.qr_code:
                uri = pyotp.totp.TOTP(self.key).provisioning_uri(name=str(self.user), issuer_name="InvestGroup")
                qr = qrcode.make(uri)
                buffer = BytesIO()
                qr.save(buffer, format="PNG")
                self.qr_code.save(f'{self.user.username}_qr.png', File(buffer), save=False)
            super().save(*args, **kwargs)
