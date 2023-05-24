from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Categoria, Movimentacao







@admin.register(Categoria)
class CalendarioAdmin(ImportExportModelAdmin):


	list_display = ['id','status','tipo','nome']


@admin.register(Movimentacao)
class MovimentacaoAdmin(ImportExportModelAdmin):


	list_display = ['id','status','categoria','valor']
