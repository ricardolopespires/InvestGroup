from rest_framework import serializers
from .models import Quiz, Question, Answer,  UsersAnswer, QuizTaker





class QuestionListSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Question
        fields = ('__all__')



class UsersAnswerListSerializer(serializers.ModelSerializer): 

    class Meta:
        model = UsersAnswer
        fields = ('__all__')


class UsersAnsweraDetailSerializer(serializers.ModelSerializer):


    class Meta:
        model = UsersAnswer
        fields = ('__all__')
