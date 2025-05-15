from django.urls import path
from .views import (
    CurrencyList, CurrencyDetail,
    StockList, StockDetail,
    CommoditieList, CommoditieDetail,
    IndexList, IndexDetail,
    RecommendationAPIView
)

urlpatterns = [
    # Currency endpoints
    path('currencies/<int:pk>/list/', CurrencyList.as_view(), name='currency-list'),
    path('currencies/<int:pk>/', CurrencyDetail.as_view(), name='currency-detail'),
    
    # Stock endpoints
    path('stocks/<int:pk>/list/', StockList.as_view(), name='stock-list'),
    path('stocks/<int:pk>/', StockDetail.as_view(), name='stock-detail'),
    
    # Commoditie endpoints
    path('commodities/<int:pk>/list/', CommoditieList.as_view(), name='commoditie-list'),
    path('commodities/<int:pk>/', CommoditieDetail.as_view(), name='commoditie-detail'),
    
    # Index endpoints
    path('indices/', IndexList.as_view(), name='index-list'),
    path('indices/<int:pk>/', IndexDetail.as_view(), name='index-detail'),

    # Recommendation endpoint
    path('recommendations/<int:pk>/<str:asset>/', RecommendationAPIView.as_view(), name='recommendations'),
]