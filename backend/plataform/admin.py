from django.contrib import admin
from .models import MT5API
# Register your models here.



@admin.register(MT5API)
class MT5APIAdmin(admin.ModelAdmin):
    list_display = ('user', 'broker', 'account', 'server', 'created_at', 'updated_at')
    search_fields = ('user__username', 'broker', 'account')
    list_filter = ('broker', 'created_at')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')