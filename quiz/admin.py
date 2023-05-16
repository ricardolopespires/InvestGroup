from import_export.admin import ImportExportModelAdmin
from .models import  Quiz, Question, Answer, QuizTaker, UsersAnswer
from django.contrib import admin
import nested_admin




@admin.register(Quiz)
class AnswerAdmin(ImportExportModelAdmin):
	list_display = ['id','name', 'topic', 'percentage','total']
	prepopulated_fields = {"slug": ("name",)}

	


@admin.register(Question)
class QuestionAmin(ImportExportModelAdmin):
	list_display  = ['id','order','label','answers']
	search_fields = ['label']



@admin.register(Answer)
class QuizAdmin(ImportExportModelAdmin):
	list_display = ['id','question','label','score']
	list_filter = ['question']
	search_fields = ['label']



@admin.register(QuizTaker)
class UsersAnswerAdmin(ImportExportModelAdmin):
	list_display = ['id',]



@admin.register(UsersAnswer)
class QuizTakerAdmin(ImportExportModelAdmin):
	list_display = ['id']





