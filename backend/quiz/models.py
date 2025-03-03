from django.utils.translation import gettext_lazy as _
from django.db import models
from django.conf import settings # Importando o modelo de usuário do Django

from autoslug import AutoSlugField

# Modelo Quiz (sem alterações)
class Quiz(models.Model):      
    
    title = models.CharField(
        _("Quiz Title"), max_length=255, unique=True, default=_("New Quiz")
    ) 
    icone = models.CharField( max_length=50, default="fas fa-question", help_text="Font Awesome icon class") 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def question_count(self):   
        return self.questions.count()

    class Meta:     
        verbose_name = _("Quiz")      
        verbose_name_plural = _("Quizzes")   
        ordering = ["id"]

    def __str__(self):
        return self.title

# Modelo Question (sem alterações)
class Question(models.Model):
    id = models.IntegerField(primary_key=True)
    quiz = models.ForeignKey(Quiz, related_name="questions", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default="")
    created_at = models.DateTimeField(auto_now_add=True)    
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Question")   
        verbose_name_plural = _("Questions")
        ordering = ["id"]

    def __str__(self):
        return self.title

# Modelo Answer (sem alterações)
class Answer(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.ForeignKey(
        Question, related_name="answers", on_delete=models.CASCADE
    )
    answer_text = models.CharField(max_length=255, null=True, blank=True)  
    is_right = models.BooleanField(default=False, null=True, blank=True)
    score = models.IntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:     
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ["id"]

    def __str__(self):
        return self.answer_text

# Novo modelo UserAnswer para rastrear as respostas selecionadas pelo usuário
class UserAnswer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="user_answers")
    selected_answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name="selected_by_users")
    selected_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("User Answer")
        verbose_name_plural = _("User Answers")
        unique_together = (("user", "question"),)  # Garante que um usuário só responda uma vez por pergunta
        ordering = ["selected_at"]

    def __str__(self):
        return f"{self.user.username} - {self.question.title} - {self.selected_answer.answer_text}"