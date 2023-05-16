from django.urls import path
from . import views




app_name = 'trading'




urlpatterns = [


	path('index/',views.Trading_Index_View.as_view(), name = 'manager'),





]