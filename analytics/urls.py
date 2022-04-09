from django.urls import path
from . import views


app_name = 'analytics'



urlpatterns = [ 

    path('selic/', views.selic, name = 'selic'),
    path('selic/updated/',views.updated_selic, name = 'updated_selic'),



]