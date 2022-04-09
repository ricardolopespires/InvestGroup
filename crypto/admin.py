from import_export.admin import ImportExportModelAdmin
from .models import Categoria, Plataforma, Exchange, Cripto, Investimento, Movimentacao, Historico
from django.contrib import admin

# Register your models here.





@admin.register(Categoria)
class TagAdmin(ImportExportModelAdmin):
	list_display = ['id','name']



@admin.register(Plataforma)
class PlataformaAdmin(ImportExportModelAdmin):
	list_display = ['id','nome', 'slug','simbolo']



@admin.register(Exchange)
class PlataformaAdmin(ImportExportModelAdmin):
	list_display = ['id','name', 'slug',]


@admin.register(Cripto)
class CriptoAdmin(ImportExportModelAdmin):
	list_display = ['id', 'market_cap_rank', 'name', 'slug']



@admin.register(Investimento)
class InvestimentoAdmin(ImportExportModelAdmin):
	list_display = ['crypto', 'quantidade', 'total']


@admin.register(Movimentacao)
class InvestimentoAdmin(ImportExportModelAdmin):
	list_display = ['id', 'crypto', 'total']



@admin.register(Historico)
class InvestimentoAdmin(ImportExportModelAdmin):
	list_display = ['id', 'symbol', 'data', 'views']



