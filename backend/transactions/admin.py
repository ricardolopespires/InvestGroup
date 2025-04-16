from django.contrib import admin
from .models import Operation


# Register your models here.


@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    list_display = ('id', 'magic', 'asset', 'user', 'date', 'type', 'volume', 'price_entry', 'sl', 'tp', 'price_departure', 'profit', 'stoploss', 'takeprofit', 'comment')
    list_filter = ('type', 'stoploss', 'takeprofit')

