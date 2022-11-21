from django.urls import path
from . import views



app_name = 'quiz'



urlpatterns = [

    #------------------------------------------------------ Dashboard ----------------------------------------------------------
    path('profile/<usuario_id>/',views.Profile_View.as_view(), name = 'profile'),
    path('profile/perfil/<usuario_id>/investidor/',views.Profile_Perfil_Investor.as_view(), name = 'perfil_investidor'),
    path('profile/<usuario_id>/financial/situation/',views.Profile_Financial_Situation.as_view(), name = 'financial_situation'),



    #------------------------------------------------------- Management -----------------------------------------------------------
   
    path('list/', views.List_Quiz_View.as_view(), name = 'list_quiz'),
    path('created/', views.Created_Quiz_View.as_view(), name = 'created_quiz'),
    path('<question_id>/updated/', views.Updated_Quiz_View.as_view(), name = 'updated_quiz'),
    path('<question_id>/delete/', views.Delete_Quiz_View.as_view(), name = 'delete_quiz'),


    path('<question_id>/question/list/',views.Question_List_View.as_view(), name = 'list_questions'),
    path('<question_id>/question/created/',views.Question_Created_View.as_view(), name = 'created_questions'),
    path('<quiz_id>/<question_id>/question/delete/', views.Delete_Question_View.as_view(), name = 'delete_question'),
    
    path('<question_id>/answer/', views.Answer_List_View.as_view(), name = 'answer_list'),
    path('<question_id>/answer/created/', views.Answer_Created_View.as_view(), name = 'answer_created'),
    
    #------------------------------------------------------- API -------------------------------------------------------------------
    path('api/questions/list/', views.Question_Api_List.as_view(), name="api_list"),
    path('api/situacao/',views.Situacao_Question_Api.as_view(), name = 'api_situacao'),


    path('api/user/answer/',views.UsersAnswerAPIView.as_view(), name = 'useranswer_list'),
    path('api/<pk>/user/answer/', views.UserAnswerRetrieveAPIView.as_view(), name="useranswer_detail"),
    path('api/create/user/answer/', views.UserAnswerCreateAPIView.as_view(), name="username_create"),




]


