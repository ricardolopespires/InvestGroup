from .models import Categoria, Plataforma, Cripto, Investimento, Movimentacao
from django import forms





class Categoria_Form(forms.ModelForm):

	class Meta:
		model = Categoria
		fields = ('__all__')



class Plataforma_Form(forms.ModelForm):

	class Meta:
		model = Plataforma
		fields = ('__all__')




class Cripto_Form(forms.ModelForm):

	class Meta:
		model = Cripto
		fields = ('__all__')




class Investimento_Form(forms.ModelForm):

	class Meta:
		model = Investimento
		fields = ('__all__')




class Aporte_Form(forms.ModelForm):

	class Meta:
		model = Movimentacao
		fields = ('__all__')

