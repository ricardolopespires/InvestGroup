from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Categoria, Receita, Despesa

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo',  'criado_em')
    list_filter = ('tipo', )
    search_fields = ('nome',)
    date_hierarchy = 'criado_em'

class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'valor', 'data', 'usuario', 'criado_em')
    list_filter = ('categoria', 'data', 'usuario')
    search_fields = ('descricao', 'categoria__nome')
    date_hierarchy = 'data'
    list_editable = ('valor', 'data')

class DespesaAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'valor', 'data', 'usuario', 'criado_em')
    list_filter = ('categoria', 'data', 'usuario')
    search_fields = ('descricao', 'categoria__nome')
    date_hierarchy = 'data'
    list_editable = ('valor', 'data')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Receita, ReceitaAdmin)
admin.site.register(Despesa, DespesaAdmin)