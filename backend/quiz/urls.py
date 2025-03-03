from django.urls import path
from .views import (
    QuizListCreateAPIView, QuizDetailAPIView,
    QuestionListCreateAPIView, QuestionDetailAPIView,
    AnswerListCreateAPIView, AnswerDetailAPIView,
    UserAnswerListCreateAPIView, UserAnswerDetailAPIView
)

urlpatterns = [
    # Quiz URLs
    path('quizzes/', QuizListCreateAPIView.as_view(), name='quiz-list-create'),
    path('quizzes/<int:pk>/', QuizDetailAPIView.as_view(), name='quiz-detail'),

    # Question URLs
    path('questions/', QuestionListCreateAPIView.as_view(), name='question-list-create'),
    path('questions/<int:pk>/', QuestionDetailAPIView.as_view(), name='question-detail'),

    # Answer URLs
    path('answers/', AnswerListCreateAPIView.as_view(), name='answer-list-create'),
    path('answers/<int:pk>/', AnswerDetailAPIView.as_view(), name='answer-detail'),

    # UserAnswer URLs
    path('user-answers/', UserAnswerListCreateAPIView.as_view(), name='user-answer-list-create'),
    path('user-answers/<int:pk>/', UserAnswerDetailAPIView.as_view(), name='user-answer-detail'),
]