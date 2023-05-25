from import_export.admin import ImportExportModelAdmin
from .models import Categoria, Movimentacao, Financeiro
from django.contrib import admin






@admin.register(Categoria)
class CalendarioAdmin(ImportExportModelAdmin):
	list_display = ['id','status','tipo','nome']


@admin.register(Movimentacao)
class MovimentacaoAdmin(ImportExportModelAdmin):
	list_display = ['id','status','categoria','valor']


@admin.register(Financeiro)
class MovimentacaoAdmin(ImportExportModelAdmin):
	list_display = ['id','receitas','despesas','cartao','investimento', 'total']