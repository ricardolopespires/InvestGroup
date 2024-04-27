from django.urls import path
from . import views 
 
urlpatterns = [ 

    path('list/despesas/<pk>/', views.movimentacoes_list, name="list_despesas"),
    path('created/despesas/', views.MovimentacaoCreated.as_view(), name="list_despesas"),
    path('list/periodos/<pk>/', views.periodo_list), 
    path('periodos/<pk>/', views.periodo_detail), 
    path('list/plan/<pk>/', views.plan_list), 
    path('plan/<pk>/', views.plan_detail), 
    path('quantias/list/<pk>/', views.quantias_list), 
    path('quantias/created/<pk>/', views.quantias_created),
    path('quantias/delete/<pk>/', views.quantias_delete),  
] 
