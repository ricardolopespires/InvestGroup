from .models import Categoria, Movimentacao, Periodo, Planejamento, Reserva
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin




@admin.register(Categoria)
class CalendarioAdmin(ImportExportModelAdmin):
	list_display = ['id','nome','tipo','punctuation']


@admin.register(Movimentacao)
class MovimentacaoAdmin(ImportExportModelAdmin):
	list_display = ['id','status','categoria','total']


@admin.register(Periodo)
class MovimentacaoAdmin(ImportExportModelAdmin):
	list_display = ['id','user_id','expenses','revenues','percent', 'total']



@admin.register(Planejamento)
class AdminUser(admin.ModelAdmin):
	list_display = ['user','pms','pmr','pi','pnif']



@admin.register(Reserva)
class AdminReserva( ImportExportModelAdmin):
	list_display = ['id', 'status', 'inicial','rendimentos','total','referencia','complete_per']