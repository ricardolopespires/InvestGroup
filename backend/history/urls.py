from .views import FinancialDataView
from .views import LastSignalStockView
from .views import PositionsView
from .views import MT5APIView
from .views import HistoryDealsView
from .views import PerformanceView 
from django.urls import path

app_name = 'history'

urlpatterns = [
      
       path('data/<str:symbol>/<str:interval>/', FinancialDataView.as_view(), name='financial_data'),
       path('mt5/<str:symbol>/<str:interval>/<str:pk>/', MT5APIView.as_view(), name='mt5-api'),
       
       # Endpoint to retrieve deal history for a specific user
      # Supports optional query parameters: ?from_date=YYYY-MM-DD&to_date=YYYY-MM-DD
      path('users/<str:pk>/history-deals/', HistoryDealsView.as_view(), name='history-deals'),

       # Endpoint to retrieve performance metrics for a specific user and symbol
      path('users/<str:pk>/performance/<str:symbol>/', PerformanceView.as_view(), name='performance'),

      path('positions/<str:symbol>/<str:type>/<str:interval>/<str:pk>/', PositionsView.as_view(), name='positions'),
      path('last-signal/<str:symbol>/<str:type>/<str:interval>/<str:pk>/', LastSignalStockView.as_view(), name='positions'),

    ]




