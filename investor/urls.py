from django.urls import path
from . import views



app_name = 'investor'




urlpatterns = [

	
	path('perfil/list/',views.Perfil_Investor_View.as_view(), name = 'list'),
	path('perfil/api/', views.Api_Perfil_View.as_view(), name = 'api'),



]