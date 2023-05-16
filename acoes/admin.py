from .models import Categoria, Setor, SubSetor, Segmento, Empresa
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

# Register your models here.



@admin.register(Categoria)
class CalendarioAdmin(ImportExportModelAdmin):


	list_display = ['id','nome']
	


@admin.register(Setor)
class CalendarioAdmin(ImportExportModelAdmin):
	list_display = ['id','nome', 'status']
	


@admin.register(SubSetor)
class CalendarioAdmin(ImportExportModelAdmin):
	list_display = ['id','nome']
	



@admin.register(Segmento)
class CalendarioAdmin(ImportExportModelAdmin):
	list_display = ['id','nome']
	search_fields = ['nome']

	


@admin.register(Empresa)
class CalendarioAdmin(ImportExportModelAdmin):
	list_display = ['id','nome','segmento']