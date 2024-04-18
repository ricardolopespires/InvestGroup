from import_export.admin import ImportExportModelAdmin
from .models import User, OneTimePassword, Perfil, Situacao
from django.contrib import admin
# Register your models here.

admin.site.register(User)
admin.site.register(OneTimePassword)



@admin.register(Perfil)
class AdminPerfil(ImportExportModelAdmin):

	list_display = ['investor','risk_profile','minimum','maximum']



@admin.register(Situacao)
class AdminSituacao(ImportExportModelAdmin):

	list_display = ['condicao','minimum','maximum']


