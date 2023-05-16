from import_export.admin import ImportExportModelAdmin
from .models import Capital, Gerenciamento, Operacoe
from django.contrib import admin

# Register your models here.




@admin.register(Capital)
class AnswerAdmin(ImportExportModelAdmin):
	list_display = ['total']



@admin.register(Gerenciamento)
class AnswerAdmin(ImportExportModelAdmin):
	list_display = ['capital']
	
