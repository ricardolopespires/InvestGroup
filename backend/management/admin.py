from import_export.admin import ImportExportModelAdmin
from .models import  Perfil, Situacao, Strategy, Risk, Investimento
from django.contrib import admin


@admin.register(Perfil)
class AdminPerfil(ImportExportModelAdmin):

	list_display = ['id','investor','minimum','maximum','color']

@admin.register(Situacao)
class AdminSituacao(ImportExportModelAdmin):

	list_display = ['id','condicao','minimum','maximum']


@admin.register(Strategy)
class AdminSituacao(ImportExportModelAdmin):

	list_display = ['id','situacao','order','name']
	
@admin.register(Risk)
class AdminPerfil(ImportExportModelAdmin):

	list_display = ['id','idade','minimum','maximum','alto','moderado','baixo']


	
@admin.register(Investimento)
class AdminPerfil(ImportExportModelAdmin):

	list_display = ['id','name','tipo','tax',]