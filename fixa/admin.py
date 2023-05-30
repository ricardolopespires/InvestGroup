from import_export.admin import ImportExportModelAdmin
from .models import Categoria, Renda
from django.contrib import admin

# Register your models here.




@admin.register(Categoria)
class CategoriaAdmin(ImportExportModelAdmin):
	list_display = ['id','status','nome']


@admin.register(Renda)
class FixaAdmin(ImportExportModelAdmin):
	list_display = ['id', 'nome']