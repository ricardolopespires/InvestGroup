from .models import Bandeira, Cartao, Fatura
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

# Register your models here.




@admin.register(Bandeira)
class BandeiraAdmin(ImportExportModelAdmin):
	list_display = ['id','nome',]


@admin.register(Cartao)
class CartaoAdmin(ImportExportModelAdmin):
	list_display = ['id','nome',]
