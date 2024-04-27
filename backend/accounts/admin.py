from import_export.admin import ImportExportModelAdmin
from .models import User, OneTimePassword
from django.contrib import admin
# Register your models here.

admin.site.register(User)
admin.site.register(OneTimePassword)


