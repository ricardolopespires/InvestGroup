
from rest_framework import serializers 
from .models import Quiz, Question, Answer



class AnswerSerializer(serializers.HyperlinkedModelSerializer):    
  
    class Meta: 
        model = Answer
        fields = (
            "id",       
            "name",           
            'score',
                  )

    
class QuestionSerializer(serializers.HyperlinkedModelSerializer):    
    answers = AnswerSerializer(many=True, read_only=True)   
    class Meta: 
        model = Question
        fields = (
            "id",     
            "name",
            'answers',           
                   
        )


class QuizSerializer(serializers.HyperlinkedModelSerializer):
     
    questions =  QuestionSerializer(many=True, read_only=True)   
    class Meta: 
        model = Quiz
        fields = ( 
            "id",             
            "url" ,    
            "name",         
            "percentage", 
            "total", 
            "active",
            'questions',
            "timestamp",
        )
