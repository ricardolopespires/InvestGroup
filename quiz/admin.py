from import_export.admin import ImportExportModelAdmin
from .models import  Quiz, Question, Answer, QuizTaker, UsersAnswer
from django.contrib import admin
import nested_admin




@admin.register(Quiz)
class AnswerInline(ImportExportModelAdmin):
	list_display = ['name', 'topic', 'percentage','total']
	prepopulated_fields = {"slug": ("name",)}

	


@admin.register(Question)
class QuestionInline(ImportExportModelAdmin):
	list_display  = ['order','label','answers']



@admin.register(Answer)
class QuizAdmin(ImportExportModelAdmin):
	list_display = ['label','score']



@admin.register(QuizTaker)
class UsersAnswerInline(ImportExportModelAdmin):
	list_display = ['id']



@admin.register(UsersAnswer)
class QuizTakerAdmin(ImportExportModelAdmin):
	list_display = ['id']





