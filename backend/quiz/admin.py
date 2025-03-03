from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import UserAnswer
from .models import Question
from .models import  Answer
from .models import Quiz


# Register your models here.


@admin.register(Quiz)
class QuizAdmin(ImportExportModelAdmin):
    list_display = ["title", "question_count", "created_at", "updated_at"]
    search_fields = ["title"]
    list_filter = ["created_at", "updated_at"]


@admin.register(Question)
class QuestionAdmin(ImportExportModelAdmin):
    list_display = ["title", "quiz", "created_at", "updated_at"]
    search_fields = ["title"]
    list_filter = ["created_at", "updated_at"]
    
    

@admin.register(Answer)
class AnswerAdmin(ImportExportModelAdmin):
    list_display = ["answer_text", "question", "score", "is_right"]
    search_fields = ["answer_text"]
    list_filter = ["created_at", "updated_at"]


@admin.register(UserAnswer)
class UserAnswerAdmin(ImportExportModelAdmin):
    list_display = [ "question", "created_at", "updated_at"]
    search_fields = ["answer_text"]
    list_filter = ["created_at", "updated_at"]
    