from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Quiz, Question, Answer, UserAnswer
from .serializers import QuizSerializer, QuestionSerializer, AnswerSerializer, UserAnswerSerializer
from django.shortcuts import get_object_or_404

# Quiz API
class QuizListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        quizzes = Quiz.objects.all()
        serializer = QuizSerializer(quizzes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuizSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user.username)  # Define o autor como o usuário autenticado
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuizDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        quiz = get_object_or_404(Quiz, pk=pk)
        serializer = QuizSerializer(quiz)
        return Response(serializer.data)

    def put(self, request, pk):
        quiz = get_object_or_404(Quiz, pk=pk)
        serializer = QuizSerializer(quiz, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        quiz = get_object_or_404(Quiz, pk=pk)
        quiz.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Question API
class QuestionListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def put(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        serializer = QuestionSerializer(question, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Answer API
class AnswerListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        answers = Answer.objects.all()
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AnswerDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        answer = get_object_or_404(Answer, pk=pk)
        serializer = AnswerSerializer(answer)
        return Response(serializer.data)

    def put(self, request, pk):
        answer = get_object_or_404(Answer, pk=pk)
        serializer = AnswerSerializer(answer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        answer = get_object_or_404(Answer, pk=pk)
        answer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# UserAnswer API
class UserAnswerListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_answers = UserAnswer.objects.filter(user=request.user)
        serializer = UserAnswerSerializer(user_answers, many=True)
        return Response(serializer.data)

    def post(self, request):
        question_id = request.data.get('question')
        answer_id = request.data.get('selected_answer')

        if not question_id or not answer_id:
            return Response({"error": "Question and selected_answer are required."}, 
                          status=status.HTTP_400_BAD_REQUEST)

        user_answer, created = UserAnswer.objects.update_or_create(
            user=request.user,
            question_id=question_id,
            defaults={'selected_answer_id': answer_id}
        )
        serializer = UserAnswerSerializer(user_answer)
        return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)

class UserAnswerDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        user_answer = get_object_or_404(UserAnswer, pk=pk, user=request.user)
        serializer = UserAnswerSerializer(user_answer)
        return Response(serializer.data)

    def put(self, request, pk):
        user_answer = get_object_or_404(UserAnswer, pk=pk, user=request.user)
        serializer = UserAnswerSerializer(user_answer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user_answer = get_object_or_404(UserAnswer, pk=pk, user=request.user)
        user_answer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)