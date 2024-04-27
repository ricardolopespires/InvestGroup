from django.urls import path

from .views import perfil_detail
from .views import perfil_username
from .views import situacao_username
 
urlpatterns = [ 


    path('perfil/<pk>',perfil_detail, name='perfil' ),
    path('perfil/<pk>/username/',perfil_username, name='perfil' ),
    path('situation/<pk>/username/',situacao_username, name='situation' ),

    
] 
