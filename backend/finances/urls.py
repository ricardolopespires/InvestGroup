# investments/urls.py
from django.urls import path
from .views import (
    PortfolioList, 
    PortfolioDetail, 
    InvestmentList, 
    InvestmentDetail
)

urlpatterns = [
    path('portfolios/', PortfolioList.as_view(), name='portfolio-list'),
    path('portfolios/<int:pk>/', PortfolioDetail.as_view(), name='portfolio-detail'),
    path('investments/', InvestmentList.as_view(), name='investment-list'),
    path('investments/<int:pk>/', InvestmentDetail.as_view(), name='investment-detail'),
]