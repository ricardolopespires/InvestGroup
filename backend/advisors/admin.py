from django.contrib import admin
from .models import Robo,  Level, Risk
from .models import Asset

# Register your models here.


@admin.register(Asset)
class AdminAsset(admin.ModelAdmin):
    list_display = ('name', 'alocation')
    list_filter = ('name', 'alocation')
    search_fields = ('name', 'alocation')



@admin.register(Robo)
class AdminRobo(admin.ModelAdmin):
    list_display = ('name',  'performance_fee', 'management_fee', 'rate', 'amount', 'rebalancing', 'tax_inspection', 'created_at', 'updated_at', 'is_active')
    list_filter = ('name',    )
    search_fields = ('name',     )
    ordering = ('name',    )
    readonly_fields = ('created_at', 'updated_at')
    

@admin.register(Level)
class AdminLevel(admin.ModelAdmin):
    list_display = ('advisor', 'risk_level', 'stock', 'crypto', 'forex', 'commodities')
    list_filter = ('advisor', 'risk_level')
    search_fields = ('advisor', 'risk_level')
    ordering = ('advisor', 'risk_level')
    readonly_fields = ()


@admin.register(Risk)
class AdminRisk(admin.ModelAdmin):
    list_display = ('advisor', 'amount', 'level', 'breakeven')
    list_filter = ('advisor', 'amount', 'level', 'breakeven')
    search_fields = ('advisor', 'amount', 'level', 'breakeven')