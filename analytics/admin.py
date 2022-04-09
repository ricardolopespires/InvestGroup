from django.contrib import admin
from  .models import Selic
from import_export.admin import ImportExportModelAdmin
# Register your models here.




@admin.register(Selic)
class SelicAdmin(ImportExportModelAdmin):
    list_display = ['data','taxa']