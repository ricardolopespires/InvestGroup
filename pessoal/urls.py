from django.urls import path
from . import views




app_name = 'pessoal'




urlpatterns = [

	path('planejamento/financeiro/usuario/',views.Usuario_View.as_view(), name = 'planejamento-usuario'),
	path('planejamento/financeiro/manager/',views.Manager_Pessoal_Financeiro.as_view(), name = 'manager'),
	path('planejamento/financeiro/mensal/',views.List_Pessoal_Financeiro.as_view(), name = 'list'),
	path('finanças/pessoal/adicionar/receitas/',views.Receitas_Mensal_View.as_view(), name = 'add_receitas'),
	path('finanças/pessoal/adicionar/despesas/',views.Despesas_Mensal_View.as_view(), name = 'add_despesas'),
	path('finanças/pessoal/fundo/reserva/',views.Reserva_Pessoal_View.as_view(), name = 'reserva'),

	


]