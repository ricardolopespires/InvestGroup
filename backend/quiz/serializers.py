from rest_framework import serializers
from .models import Quiz, Question, Answer, UserAnswer

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'answer_text', 'is_right', 'created_at', 'updated_at']

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'title', 'quiz', 'answers', 'created_at', 'updated_at']

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    question_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Quiz
        fields = ['id', 'author', 'title', 'questions', 'question_count', 'created_at']

class UserAnswerSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(read_only=True)
    selected_answer = AnswerSerializer(read_only=True)

    class Meta:
        model = UserAnswer
        fields = ['id', 'user', 'question', 'selected_answer', 'selected_at']
        read_only_fields = ['user']