from django.urls import path
from . import views




app_name = 'pessoal'




urlpatterns = [

	path('planejamento/financeiro/usuario/',views.Usuario_View.as_view(), name = 'planejamento-usuario'),
	path('planejamento/financeiro/',views.Planejamento_Financeiro_View.as_view(), name = 'manager'),


]