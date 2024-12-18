
# Register your models here.
from import_export.admin import ImportExportModelAdmin
from .models import Subscriber
from django.contrib import admin

# Register your models here., 


@admin.register(Subscriber)
class AdminPerfil(ImportExportModelAdmin):

	list_display = ['email','time', 'created', 'updated','subscribed']
	
