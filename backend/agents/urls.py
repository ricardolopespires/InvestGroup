
from django.urls import path
from .views import (
    AssetListCreateView, AssetDetailView,
    RiskProfileListCreateView, RiskProfileDetailView,
    PortfolioListCreateView, PortfolioDetailView,
    PortfolioAllocationListCreateView, PortfolioAllocationDetailView,
    InvestmentAgentListCreateView, InvestmentAgentDetailView,
    TransactionListCreateView, TransactionDetailView,
    AdvisorRecommendationListCreateView, AdvisorRecommendationDetailView
)
app_name = 'agents'




urlpatterns = [
    path('assets/', AssetListCreateView.as_view(), name='asset-list-create'),
    path('assets/<uuid:id>/', AssetDetailView.as_view(), name='asset-detail'),
    path('risk-profiles/', RiskProfileListCreateView.as_view(), name='risk-profile-list-create'),
    path('risk-profiles/<uuid:id>/', RiskProfileDetailView.as_view(), name='risk-profile-detail'),
    path('portfolios/', PortfolioListCreateView.as_view(), name='portfolio-list-create'),
    path('portfolios/<uuid:id>/', PortfolioDetailView.as_view(), name='portfolio-detail'),
    path('portfolio-allocations/', PortfolioAllocationListCreateView.as_view(), name='portfolio-allocation-list-create'),
    path('portfolio-allocations/<uuid:id>/', PortfolioAllocationDetailView.as_view(), name='portfolio-allocation-detail'),
    path('investment-agents/', InvestmentAgentListCreateView.as_view(), name='investment-agent-list-create'),
    path('investment-agents/<uuid:id>/', InvestmentAgentDetailView.as_view(), name='investment-agent-detail'),
    path('transactions/', TransactionListCreateView.as_view(), name='transaction-list-create'),
    path('transactions/<uuid:id>/', TransactionDetailView.as_view(), name='transaction-detail'),
    path('advisor-recommendations/', AdvisorRecommendationListCreateView.as_view(), name='advisor-recommendation-list-create'),
    path('advisor-recommendations/<uuid:id>/', AdvisorRecommendationDetailView.as_view(), name='advisor-recommendation-detail'),
]