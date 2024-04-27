from django.urls import path
from . import views 
 
urlpatterns = [ 

    path('list/countries/', views.countries_list, name="list_countries"),

  
   
] 
