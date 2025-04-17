from django.contrib import admin
from .models import Investidor
from .models import Perfil
from .models import Situacao
# Register your models here.




admin.site.register(Investidor)
@admin.register(Perfil)
class AdminPerfil(admin.ModelAdmin):
    list_display = ('id','nome','objective', 'time_horizon', 'minimo', 'maximo', "fixa", "variável")
    list_filter = ('nome', 'fixa', 'variável')
    search_fields = ('nome', "fixa","variável")
    ordering = ('nome',)
    readonly_fields = ()

admin.site.register(Situacao)