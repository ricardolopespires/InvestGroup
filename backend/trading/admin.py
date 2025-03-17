from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Commoditie

# Register your models here.


@admin.register(Commoditie)
class CommoditieAdmin(ImportExportModelAdmin):
    list_display = ['name']