from .views import InvestidorListCreateAPIView 
from .views import InvestidorDetailAPIView
from .views import SituacaoDetailView
from .views import PerfilDetailView
from .views import SituacaoAllView
from .views import PerfilAllView
from .views import SituacaoView
from .views import PerfilView
from django.urls import path



app_name = 'analytics'

urlpatterns = [


    path('investidores/', InvestidorListCreateAPIView.as_view(), name='investidor-list-create'),
    path('investidores/<int:pk>/', InvestidorDetailAPIView.as_view(), name='investidor-detail'),       
    path('situacao/<str:pk>/detail/', SituacaoDetailView.as_view(), name='situacao-detail'),
    path('situacao/all/', SituacaoAllView.as_view(), name='situacao-list'),
    path('perfil/<str:pk>/detail/', PerfilDetailView.as_view(), name='perfil-detail'),     
    path('perfil/all/', PerfilAllView.as_view(), name='perfil-all'), 
    path('situacao/<str:pk>/', SituacaoView.as_view(), name='situacao'),
    path('perfil/<str:pk>/', PerfilView.as_view(), name='perfil'),
    
    

    path('perfil/', PerfilView.as_view(), name='perfil-list'),
  
]