from django.contrib import admin
from .models import  Empresa, Setore, SubSetore
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(Setore)
class SetorAdmin(ImportExportModelAdmin):
    list_display = ['nome']


@admin.register(SubSetore)
class SetorAdmin(ImportExportModelAdmin):
    list_display = ['nome']




@admin.register(Empresa)
class AcoesAdmin(ImportExportModelAdmin):
    list_display = ['id','Empresa', 'Cotacao']
