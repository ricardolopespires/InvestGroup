from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Perfil, Situacao

# Register your models here.



@admin.register(Perfil)
class AdminPerfil(ImportExportModelAdmin):

	list_display = ['investor','minimum','maximum']



@admin.register(Situacao)
class AdminSituacao(ImportExportModelAdmin):

	list_display = ['condicao',]