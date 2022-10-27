from django import forms
from .models import Questionnaire 




class Questionnaire_Form(forms.ModelForm):


	class Meta:
		model = Questionnaire
		fields = ('__all__')

