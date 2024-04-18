from django.contrib import admin
from .models import Bank, Category, Transaction

# Register your models here.
admin.site.register(Bank)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display  = ['id','name']
	search_fields = ['name']

admin.site.register(Transaction)