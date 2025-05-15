from django.urls import path
from .views import (
    AssetListCreateAPIView,
    AssetDetailAPIView,
    InvestorProfileListCreateAPIView,
    InvestorProfileDetailAPIView,
    InvestidorListCreateAPIView,
    InvestidorDetailAPIView,
    InvestmentOperationListCreateAPIView,
    InvestmentOperationDetailAPIView,
    RiskAssessmentListCreateAPIView,
    RiskAssessmentDetailAPIView,
)

app_name = 'analytics'

urlpatterns = [
    path('assets/', AssetListCreateAPIView.as_view(), name='asset-list-create'),
    path('assets/<uuid:pk>/', AssetDetailAPIView.as_view(), name='asset-detail'),
    path('investor-profiles/', InvestorProfileListCreateAPIView.as_view(), name='investor-profile-list-create'),
    path('investor-profiles/<uuid:pk>/', InvestorProfileDetailAPIView.as_view(), name='investor-profile-detail'),
    path('investidores/', InvestidorListCreateAPIView.as_view(), name='investidor-list-create'),
    path('investidores/<uuid:pk>/', InvestidorDetailAPIView.as_view(), name='investidor-detail'),
    path('investment-operations/', InvestmentOperationListCreateAPIView.as_view(), name='investment-operation-list-create'),
    path('investment-operations/<uuid:pk>/', InvestmentOperationDetailAPIView.as_view(), name='investment-operation-detail'),
    path('risk-assessments/', RiskAssessmentListCreateAPIView.as_view(), name='risk-assessment-list-create'),
    path('risk-assessments/<uuid:pk>/', RiskAssessmentDetailAPIView.as_view(), name='risk-assessment-detail'),
]