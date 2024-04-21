from django.urls import path
from . import views 
 
urlpatterns = [ 

    path('list/despesas/<pk>/', views.movimentacoes_list, name="list_despesas"),
    path('created/despesas/', views.MovimentacaoList.as_view(), name="list_despesas"),   
] 
