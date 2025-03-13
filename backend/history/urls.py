from .views import FinancialDataView
from django.urls import path

app_name = 'history'

urlpatterns = [
      
        path('data/<str:symbol>/', FinancialDataView.as_view(), name='financial_data'),
    ]

