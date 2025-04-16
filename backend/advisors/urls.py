from django.urls import path
from . import views


app_name = 'advisors'



urlpatterns = [

    path('robos/', views.RoboListCreateAPIView.as_view(), name='robo-list-create'),
    path('robos/<int:pk>/', views.RoboDetailAPIView.as_view(), name='robo-detail'),


    path('robos/level/<str:pk>/', views.RoboLevelAPIView.as_view(), name='robo-level'),
    
    

    
] 