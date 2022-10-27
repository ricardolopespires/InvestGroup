from django.urls import path
from . import views


app_name = 'dashboard'




urlpatterns = [


	path('manager/', views.Dashboard_Templates_View.as_view(), name = 'manager'),


]