from django.urls import path
from . import views





app_name = 'ações'



urlpatterns = [


    path('setores/', views.setores, name = 'setores'),
    path('setor/<int:pk>/empresa/', views.setor, name = 'setor'),
    path('acoes/search/',views.search, name = 'search'),
    path('acoes/<papel>/details/',views.details, name ='details'),

]