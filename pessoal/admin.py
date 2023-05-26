from .models import Categoria, Movimentacao, Financeiro, Planejamento, Reserva
from import_export.admin import ImportExportModelAdmin
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



@admin.register(Planejamento)
class AdminUser(admin.ModelAdmin):
	list_display = ['user','pms','pmr','pi','pnif']



@admin.register(Reserva)
class AdminReserva( ImportExportModelAdmin):
	list_display = ['id', 'status', 'inicial','rendimentos','total','referencia','complete_per']