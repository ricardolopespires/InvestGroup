from django.contrib import admin
from .models import Investidor
from .models import Perfil
from .models import Situacao
# Register your models here.




admin.site.register(Investidor)
admin.site.register(Perfil) 
admin.site.register(Situacao)