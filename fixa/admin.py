from .models import Categoria
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

# Register your models here.








@admin.register(Categoria)
class CategoriaAdmin(ImportExportModelAdmin):
	list_display = ['id','status','nome']
