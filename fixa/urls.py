from django.urls import path
from . import views



app_name = "fixa"




urlpatterns = [

	path('renda/fixa/cdi/',views.CDI_View.as_view(), name = 'cdb'),

	path('renda/fixa/lca/',views.LCA_View.as_view(), name = 'lca'),

	path('renda/fixa/lci/',views.LCI_View.as_view(), name = 'lci'),

	path('renda/fixa/tesouro/direto/',views.Tesouro_Direto_View.as_view(), name = 'tesouro'),


]