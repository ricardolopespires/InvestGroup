from django.urls import path
from . import views



app_name = 'quiz'



urlpatterns = [

    #------------------------------------------------------ Dashboard ----------------------------------------------------------
	path('profile/<usuario_id>/',views.Profile_View.as_view(), name = 'profile'),
    path('profile/perfil/<usuario_id>/investidor/',views.Profile_Perfil_Investor.as_view(), name = 'perfil_investidor'),
    path('profile/<usuario_id>/financial/situation/',views.Profile_Financial_Situation.as_view(), name = 'financial_situation'),



    #------------------------------------------------------- Management -----------------------------------------------------------

    path('manager/', views.List_Quiz_View.as_view(), name = 'questionnaires'),
    path('<subject_id>/detail/', views.Detail_Quiz_View.as_view(), name = 'quiz_detail'),
    path('<subject_id>/question/created/', views.Created_Quiz_View.as_view(), name = 'created_quiz'),
    path('<question_id>/<subject_id>/question/updated/', views.Updated_Quiz_View.as_view(), name = 'updated_quiz'),
    path('<question_id>/<subject_id>/question/delete/', views.Delete_Quiz_View.as_view(), name = 'delete_quiz'),
    

]
