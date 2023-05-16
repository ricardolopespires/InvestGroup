from django.urls import path
from . import views



app_name = 'acoes'




urlpatterns = [

    path('setores/mercado/',views.Setor_Templates_View.as_view(), name = 'setores'),
    path('ciclos/<setor_id>/detail', views.Setor_Detail_View.as_view(), name = 'setor_detail'),

    path('ativo/<ativo_id>/',views.Acao_Template_View.as_view(), name = 'ativo'),
]