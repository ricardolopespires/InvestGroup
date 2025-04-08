from .views import FinancialDataView
from .views import LastSignalStockView
from .views import PositionsView
from .views import MT5APIView
from django.urls import path

app_name = 'history'

urlpatterns = [
      
       path('data/<str:symbol>/<str:interval>/', FinancialDataView.as_view(), name='financial_data'),
       path('mt5/<str:symbol>/<str:interval>/<str:pk>/', MT5APIView.as_view(), name='mt5-api'),
       path('positions/<str:symbol>/<str:type>/<str:interval>/<str:pk>/', PositionsView.as_view(), name='positions'),
       path('last-signal/<str:symbol>/<str:type>/<str:interval>/<str:pk>/', LastSignalStockView.as_view(), name='positions'),

    ]




