from .views import FinancialDataView
from .views import MT5APIView
from django.urls import path

app_name = 'history'

urlpatterns = [
      
       path('data/<str:symbol>/<str:interval>/', FinancialDataView.as_view(), name='financial_data'),
       path('mt5/', MT5APIView.as_view(), name='mt5-api'),

    ]

