from django import forms
from .models import Quiz, Subject






class Subject_Form(forms.ModelForm):


	class Meta:
		model = Subject
		fields = ('__all__')





class Quiz_Form(forms.ModelForm):


	class Meta:
		model = Quiz
		fields = ('__all__')

