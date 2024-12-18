from import_export.admin import ImportExportModelAdmin
from .models import Contact
from django.contrib import admin
# Register your models here., 


@admin.register(Contact)
class AdminPerfil(ImportExportModelAdmin):

	list_display = ['first_name','last_name','email','message', 'answers', 'time', 'created', 'updated']
	
