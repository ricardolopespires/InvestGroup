from import_export.admin import ImportExportModelAdmin
from .models import Perfil, Situacao, Planejamento
from .models import User, Financeiro
from django.contrib import admin



@admin.register(Planejamento)
class AdminUser(admin.ModelAdmin):
	list_display = ['user','pms','pmr','pi','pnif']




@admin.register(User)
class AdminUser(admin.ModelAdmin):
	list_display = ['username', 'is_staff','is_active','date_joined']




@admin.register(Financeiro)
class AdminFinanceiro(admin.ModelAdmin):
	list_display = ['user', 'dinheiro', 'acoes', 'crypto', 'imobiliario','retorno', 'capital']




@admin.register(Perfil)
class AdminPerfil(ImportExportModelAdmin):

	list_display = ['investor','risk_profile','minimum','maximum']



@admin.register(Situacao)
class AdminSituacao(ImportExportModelAdmin):

	list_display = ['condicao','minimum','maximum']


