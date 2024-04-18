from django.urls import path 
from . import views 
 
 
urlpatterns = [ 
   
    path('list/',  
        views.QuizList.as_view(), 
        name=views.QuizList.name), 
    
     path('details/<pk>',  
        views.QuizDetail.as_view(), 
        name=views.QuizDetail.name), 


    path('question/list/',  
        views.QuestionList.as_view(), 
        name=views.QuestionList.name), 

    path('question/<pk>',  
        views.QuestionDetail.as_view(), 
        name=views.QuestionDetail.name),


     path('answer/list/',  
        views.AnswerList.as_view(), 
        name=views.AnswerList.name), 

    path('answer/<pk>',  
        views.AnswerDetail.as_view(), 
        name=views.AnswerDetail.name),  


]
