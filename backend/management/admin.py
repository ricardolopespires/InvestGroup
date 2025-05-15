from django.contrib import admin
from .models import Asset, InvestorProfile, Investidor, InvestmentOperation, RiskAssessment


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('ticker', 'name', 'asset_type', 'currency', 'sector', 'volatility', 'created_at')
    list_filter = ('asset_type', 'currency', 'created_at')
    search_fields = ('ticker', 'name', 'sector')
    ordering = ('ticker',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')
    list_select_related = True


@admin.register(InvestorProfile)
class InvestorProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'risk_tolerance', 'max_exposure', 'fixed_income_allocation', 'variable_income_allocation')
    list_filter = ('risk_tolerance',)
    search_fields = ('name',)
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    list_select_related = True


@admin.register(Investidor)
class InvestidorAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'investor_profile', 'calcular_saude_financeira', 'tolerancia_risco', 'horizonte_tempo', 'objetivo')
    list_filter = ('tolerancia_risco', 'horizonte_tempo', 'objetivo', 'investor_profile')
    search_fields = ('usuario__username', 'usuario__email')
    readonly_fields = ('created_at', 'updated_at')
    autocomplete_fields = ['investor_profile']
    list_select_related = ('usuario', 'investor_profile')

    def calcular_saude_financeira(self, obj):
        return obj.calcular_saude_financeira()
    calcular_saude_financeira.short_description = "Saúde Financeira"


@admin.register(InvestmentOperation)
class InvestmentOperationAdmin(admin.ModelAdmin):
    list_display = ('asset', 'investidor', 'operation_type', 'quantity', 'unit_price', 'total_value', 'risk_score', 'operation_date')
    list_filter = ('operation_type', 'operation_date', 'asset__asset_type', 'investidor__investor_profile')
    search_fields = ('asset__ticker', 'asset__name', 'investidor__usuario__username')
    date_hierarchy = 'operation_date'
    readonly_fields = ('total_value', 'risk_score', 'created_at', 'updated_at')
    autocomplete_fields = ['asset', 'investidor']
    list_select_related = ('asset', 'investidor', 'investidor__investor_profile')


@admin.register(RiskAssessment)
class RiskAssessmentAdmin(admin.ModelAdmin):
    list_display = ('operation', 'risk_type', 'risk_level', 'assessment_date')
    list_filter = ('risk_type', 'risk_level', 'assessment_date')
    search_fields = ('operation__asset__ticker', 'operation__asset__name', 'operation__investidor__usuario__username')
    date_hierarchy = 'assessment_date'
    readonly_fields = ('assessment_date',)
    autocomplete_fields = ['operation']
    list_select_related = ('operation', 'operation__asset', 'operation__investidor')