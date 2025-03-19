from django.urls import path
from .views import (
    CategoriaListCreateView, CategoriaDetailView,
    TransacaoListCreateView, TransacaoDetailView,
    
)
app_name = 'transactions'



urlpatterns = [
    # Endpoints para Categorias
    path('api/categorias/', CategoriaListCreateView.as_view(), name='categoria-list-create'),
    path('api/categorias/<int:pk>/', CategoriaDetailView.as_view(), name='categoria-detail'),
    
    # Endpoints para Transações
    path('api/transacoes/', TransacaoListCreateView.as_view(), name='transacao-list-create'),
    path('api/transacoes/<int:pk>/', TransacaoDetailView.as_view(), name='transacao-detail'),

]
