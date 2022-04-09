from django import forms
from .models import API






class API_Form(forms.ModelForm):


	class Meta:
		model = API
		fields = ('__all__')