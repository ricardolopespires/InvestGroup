from .models import Categoria, Movimentacao, Periodo, Planejamento, Reserva, Plano
from .models import Quantia
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


@admin.register(Plano)
class MovimentacaoAdmin(ImportExportModelAdmin):
	list_display = ['id','user','nome','quantia','economia','percent','meta']


@admin.register(Quantia)
class MovimentacaoAdmin(ImportExportModelAdmin):
	list_display = ['id','plano','quantia','percent','meta']




@admin.register(Planejamento)
class AdminUser(admin.ModelAdmin):
	list_display = ['user','pms','pmr','pi','pnif']



@admin.register(Reserva)
class AdminReserva( ImportExportModelAdmin):
	list_display = ['id', 'status', 'inicial','rendimentos','total','referencia','complete_per']