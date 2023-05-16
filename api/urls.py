from django.urls import path
from . import views


app_name = 'api'


urlpatterns = [


    #-------------------------------------- API User Situação ----------------------------------------------------
    path('quiz/situacao/questions/list/', views.Situacao_Api_List.as_view(), name="situacao_list"),
    path('quiz/financial/situation/list/', views.situacaoList, name = 'situacao-list'),
    path('quiz/financial/situacao/detail/<str:pk>/', views.situacaoDetail, name="situacao-detail"),
    path('quiz/financial/situation/create/', views.situacaoCreate, name = 'situacao-create'),
    path('quiz/financial/situation/update/<str:pk>/',views.situacaoUpdate, name = 'sutacao-update'),
   
    
    #------------------------------------------------------- api/perfil/questions/list/ ---------------------------
   
    path('api/perfil/questions/list/', views.Perfil_Api_List.as_view(), name="perfil_list"),
    path('quiz/financial/perfil/list/', views.perfilList, name = 'perfil-list'),
    path('quiz/financial/perfil/detail/<str:pk>/', views.perfilDetail, name="perfil-detail"),
    path('quiz/financial/perfil/create/', views.perfilCreate, name = 'perfil-create'),
    path('quiz/financial/perfil/update/<str:pk>/',views.perfilUpdate, name = 'perfil-update'),
    







    #-------------------------------------- API Quiz -----------------------------------------------------

    path('user/answer/list/', views.AnswerList, name = 'useranswer_list'),
    path('quiz/profile/financial/situation/user/answer/create/',views.AnswerCreate, name = 'useranswer_create'),



    #-------------------------------------- API Planejamento -----------------------------------------------------
    


  ]






