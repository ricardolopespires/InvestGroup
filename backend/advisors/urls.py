from django.urls import path
from . import views


app_name = 'advisors'



urlpatterns = [

    path('robos/', views.RoboListCreateAPIView.as_view(), name='robo-list-create'),
    path('robo/<int:pk>/', views.RoboDetailAPIView.as_view(), name='robo-detail'),
    path('robo/level/<str:pk>/', views.RoboLevelAPIView.as_view(), name='robo-level'),
    path('risks/', views.RiskListCreateView.as_view(), name='risk-list-create'),
    path('risk/<int:pk>/', views.RiskDetailView.as_view(), name='risk-detail'),       

    
] 