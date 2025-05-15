from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Commoditie, Currency, Stock

# Register your models here.


@admin.register(Commoditie)
class CommoditieAdmin(ImportExportModelAdmin):
    list_display = ['name','symbol','yahoo','tradingview']




@admin.register(Currency)
class CurrencyAdmin(ImportExportModelAdmin):
    list_display = ['name', 'status']



@admin.register(Stock)
class StockAdmin(ImportExportModelAdmin):
    list_display = ['name', "img",  'exchange', 'category', 'symbol']
    search_fields = ['name', 'symbol']