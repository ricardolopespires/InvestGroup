from .views import InvestidorListCreateAPIView 
from .views import InvestidorDetailAPIView
from django.urls import path

urlpatterns = [


    path('api/investidores/', InvestidorListCreateAPIView.as_view(), name='investidor-list-create'),
    path('api/investidores/<int:pk>/', InvestidorDetailAPIView.as_view(), name='investidor-detail'),
  
]