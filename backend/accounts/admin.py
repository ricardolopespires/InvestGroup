from import_export.admin import ImportExportModelAdmin
from .models import User, OneTimePassword, TwoFactor
from django.contrib import admin
# Register your models here., 


@admin.register(User)
class AdminPerfil(ImportExportModelAdmin):

	list_display = ['id','email','is_verified','is_active','situation','perfil','two_factor']
	
@admin.register(TwoFactor)
class AdminPerfil(ImportExportModelAdmin):

	list_display = ['user','key']


admin.site.register(OneTimePassword)


