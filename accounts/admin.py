from django.contrib import admin
from .models import User, Financeiro
from import_export.admin import ImportExportModelAdmin
# Register your models here.



@admin.register(User)
class AdminUser(admin.ModelAdmin):
	list_display = ['username', 'is_staff','is_active','is_investidor','date_joined']




@admin.register(Financeiro)
class AdminFinanceiro(admin.ModelAdmin):
	list_display = ['user', 'dinheiro', 'acoes', 'crypto', 'imobiliario','retorno', 'capital']




