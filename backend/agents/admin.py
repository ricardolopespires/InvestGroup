from django.contrib import admin
from .models import Asset, RiskProfile, Portfolio, PortfolioAllocation, InvestmentAgent, Transaction, AdvisorRecommendation

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'ticker', 'asset_type', 'price', 'volatility', 'created_at')
    search_fields = ('name', 'ticker')
    list_filter = ('asset_type', 'created_at')
    ordering = ('name',)

@admin.register(RiskProfile)
class RiskProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'risk_level', 'max_loss_tolerance', 'investment_horizon', 'created_at')
    search_fields = ('user__username',)
    list_filter = ('risk_level', 'created_at')
    ordering = ('user',)

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'total_value', 'risk_profile', 'created_at')
    search_fields = ('name', 'user__username')
    list_filter = ('created_at',)
    ordering = ('name',)

@admin.register(PortfolioAllocation)
class PortfolioAllocationAdmin(admin.ModelAdmin):
    list_display = ('portfolio', 'asset', 'quantity', 'allocation_percentage', 'created_at')
    search_fields = ('portfolio__name', 'asset__ticker')
    list_filter = ('created_at',)
    ordering = ('portfolio',)

@admin.register(InvestmentAgent)
class InvestmentAgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'strategy', 'asset' ,'specialty', 'model', 'langchain_model', 'langchain_tool',  'created_at')
    search_fields = ('name',)
    list_filter = ('strategy', 'langchain_model', 'created_at')
    filter_horizontal = ('users', 'portfolios')  # Widget para ManyToManyField
    ordering = ('name',)

    def get_users(self, obj):
        return ", ".join([user.username for user in obj.users.all()])
    get_users.short_description = 'Users'

    def get_portfolios(self, obj):
        return ", ".join([portfolio.name for portfolio in obj.portfolios.all()])
    get_portfolios.short_description = 'Portfolios'

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('portfolio', 'asset', 'transaction_type', 'quantity', 'price_per_unit', 'total_amount', 'executed_at')
    search_fields = ('portfolio__name', 'asset__ticker')
    list_filter = ('transaction_type', 'executed_at')
    ordering = ('-executed_at',)

@admin.register(AdvisorRecommendation)
class AdvisorRecommendationAdmin(admin.ModelAdmin):
    list_display = ('portfolio', 'agent', 'recommendation_text_summary', 'get_recommended_assets', 'created_at')
    search_fields = ('portfolio__name', 'agent__name', 'recommendation_text')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    filter_horizontal = ('recommended_assets',)

    def recommendation_text_summary(self, obj):
        return obj.recommendation_text[:50] + ('...' if len(obj.recommendation_text) > 50 else '')
    recommendation_text_summary.short_description = 'Recommendation Text'

    def get_recommended_assets(self, obj):
        return ", ".join([asset.ticker for asset in obj.recommended_assets.all()])
    get_recommended_assets.short_description = 'Recommended Assets'