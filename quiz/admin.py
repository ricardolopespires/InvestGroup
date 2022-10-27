from import_export.admin import ImportExportModelAdmin
from .models import Subject, Questionnaire, Questions, Perfil
from django.contrib import admin






# Register your models here.

@admin.register(Subject)
class AdminQuestions(ImportExportModelAdmin):
	list_display = ['title', 'percentage', 'total']
	list_filter = ['title', 'percentage', 'total']

@admin.register(Questionnaire)
class AdminQuestionnaire(ImportExportModelAdmin):
	list_display = ['title']


@admin.register(Questions)
class AdminQuestions(ImportExportModelAdmin):
	list_display = ['questionnaire', 'valor']
	list_filter = ['questionnaire', 'valor']


@admin.register(Perfil)
class AdminPerfil(ImportExportModelAdmin):
	list_display = ['investor','risk_profile', 'minimum', 'maximum']
