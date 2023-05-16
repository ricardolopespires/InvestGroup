from django.urls import path
from . import views



app_name = 'quiz'





urlpatterns = [

    #------------------------------------------------------ Dashboard ----------------------------------------------------------
    path('profile/<usuario_id>/',views.Profile_View.as_view(), name = 'profile'),
    path('financial/perfil/',views.Profile_Perfil_Investor.as_view(), name = 'perfil_investidor'),
    path('financial/situation/',views.Profile_Financial_Situation.as_view(), name = 'financial_situation'),



    #------------------------------------------------------- Management -----------------------------------------------------------
   
    path('list/', views.List_Quiz_View.as_view(), name = 'list_quiz'),
    path('created/', views.Created_Quiz_View.as_view(), name = 'created_quiz'),
    path('<question_id>/updated/', views.Updated_Quiz_View.as_view(), name = 'updated_quiz'),
    path('<question_id>/delete/', views.Delete_Quiz_View.as_view(), name = 'delete_quiz'),


    path('<question_id>/question/list/',views.Question_List_View.as_view(), name = 'list_questions'),
    path('<question_id>/question/created/',views.Question_Created_View.as_view(), name = 'created_questions'),
     path('<question_id>/question/updated/',views.Question_Updated_View.as_view(), name = 'updated_questions'),
    path('<question_id>/question/delete/', views.Delete_Question_View.as_view(), name = 'delete_questions'),
    
    path('<pk>/answer/', views.Answer_List_View.as_view(), name = 'answer_list'),
    path('<question_id>/answer/created/', views.Answer_Created_View.as_view(), name = 'answer_created'),
    path('<question_id>/answer/updated/', views.Answer_Updated_View.as_view(), name = 'answer_updated'),
    path('<question_id>/answer/delete/', views.Answer_Delete_View.as_view(), name = 'answer_delete'),
    
 

 ]

