from django.urls import path
from . import views



app_name = 'management'



urlpatterns = [

	path('administration/', views.Management_Templates_View.as_view(), name = 'manager')

]