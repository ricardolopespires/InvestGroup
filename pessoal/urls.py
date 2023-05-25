from django.urls import path
from . import views




app_name = 'pessoal'




urlpatterns = [

	path('planejamento/financeiro/usuario/',views.Usuario_View.as_view(), name = 'planejamento-usuario'),
	path('planejamento/financeiro/',views.List_Pessoal_Financeiro.as_view(), name = 'manager'),
	path('finanças/pessoal/adicionar/receitas/',views.Receitas_Mensal_View.as_view(), name = 'add_receitas'),
	path('finanças/pessoal/adicionar/despesas/',views.Despesas_Mensal_View.as_view(), name = 'add_despesas'),
	path('finanças/pessoal/fundo/reserva/',views.Reserva_Pessoal_View.as_view(), name = 'reserva'),


]