from django.urls import path
from . import views



app_name = 'economia'



urlpatterns = [	


	#-----------------------------------------  Calendario Economico ------------------------------------
	path('continents/countries/created/',views.Create_Countrie.as_view(), name =  'create_countrie'),
	path('continents/countries/america/sul/',views.Continents_America_Sul_View.as_view(), name = 'america_sul'),
	path('continents/countries/<paises_id>/america/sul/',views.Continents_America_Sul_Detail.as_view(), name = 'america_sul_detail'),

	path('continents/countries/america/norte/',views.Continents_America_Norte_View.as_view(), name = 'america_norte'),
	path('continents/countries/<paises_id>/america/norte/',views.Continents_America_Norte_Detail.as_view(), name = 'america_norte_detail'),
	
	path('continents/countries/europa/',views.Continents_Europa_View.as_view(), name = 'europa'),
	path('continents/countries/<paises_id>/europa/',views.Continents_Europa_Detail.as_view(), name = 'europa_detail'),
	path('continents/countries/asia/',views.Continents_Asia_View.as_view(), name = 'asia'),
	path('continents/countries/<paises_id>/asia/',views.Continents_Asia_Detail.as_view(), name = 'asia_detail'),

	#-----------------------------------------  Calendario Economico ------------------------------------

	#path('forex/calendario/economico/',views.Calendario_Economico_View.as_view(), name = 'calendario'),
	



]
