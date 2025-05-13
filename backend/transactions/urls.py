from django.urls import path
from .views import (
    CategoriaListCreateView, CategoriaDetailView,
    TransacaoListCreateView, TransacaoDetailView,
    OperationListCreateAPIView, OperationDetailAPIView,
    CloseOperationAPIView, ReverseOperationAPIView
    
)
app_name = 'transactions'



urlpatterns = [
    # Endpoints para Categorias
    path('categorias/', CategoriaListCreateView.as_view(), name='categoria-list-create'),
    path('categorias/<int:pk>/', CategoriaDetailView.as_view(), name='categoria-detail'),
    
    # Endpoints para Transações
    path('transacoes/', TransacaoListCreateView.as_view(), name='transacao-list-create'),
    path('transacoes/<int:pk>/', TransacaoDetailView.as_view(), name='transacao-detail'),


    path('operations/list/<str:pk>/<str:user_id>/', OperationListCreateAPIView.as_view(), name='operation-list-create'),
    path('operations/<int:pk>/', OperationDetailAPIView.as_view(), name='operation-detail'),
    path('operations/close/<int:pk>/', CloseOperationAPIView.as_view(), name='close-operation'),  
    path('operations/reverse/<int:pk>/', ReverseOperationAPIView.as_view(), name='reverse-operation'),
    # path('operations/<int:pk>/', OperationDetailAPIView.as_view(), name='operation-detail'),  

]
