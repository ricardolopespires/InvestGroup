from django.shortcuts import render 
from rest_framework import generics 
from rest_framework.response import Response 
from rest_framework.reverse import reverse 
from .models import Quiz, Question, Answer, UsersAnswer
from .serializers import QuizSerializer
from .serializers import QuestionSerializer
from .serializers import AnswerSerializer


class QuizList(generics.ListCreateAPIView): 
    queryset = Quiz.objects.all() 
    serializer_class = QuizSerializer
    name = 'quiz-list' 


class QuizDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Quiz.objects.all() 
    serializer_class = QuizSerializer 
    name = 'quiz-detail' 
 

class QuestionList(generics.ListCreateAPIView): 
    queryset = Question.objects.all() 
    serializer_class = QuestionSerializer 
    name = 'question-list' 
 
 
class QuestionDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Question.objects.all() 
    serializer_class = QuestionSerializer  
    name = 'question-detail' 




class AnswerList(generics.ListCreateAPIView): 
    queryset = Answer.objects.all() 
    serializer_class = AnswerSerializer 
    name = 'answer-list' 
 
 
class AnswerDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Answer.objects.all() 
    serializer_class = AnswerSerializer  
    name = 'answer-detail' 