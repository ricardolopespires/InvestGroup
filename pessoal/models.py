from django.core.validators import MaxValueValidator, MinValueValidator
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.conf import settings
from datetime import timedelta
from django.db import models
from decimal import Decimal




class Categoria(models.Model):
	STATUS_CHOICES = (

		('receitas','Receitas'),
		('despesas','Despesas'),

		)

	id = models.CharField(max_length = 90, primary_key = True)
	status = models.CharField(max_length = 150,  choices = STATUS_CHOICES, default = 'receitas')
	nome = models.CharField(max_length = 70, unique = True)
	tipo = models.CharField(max_length = 90, )
	descricao = RichTextField(blank = True, null = True)



	class Meta:		
		verbose_name = 'Categoria'
		verbose_name_plural = 'Categorias'

	def __str__(self):
		return f'{self.id}'







class Movimentacao(models.Model):


	STATUS_CHOICES = (

		('receitas','Receitas'),
		('despesas','Despesas'),
		)

	id = models.CharField(max_length = 90, primary_key = True)
	user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'user', blank=True)
	status = models.CharField(max_length = 19, choices = STATUS_CHOICES, default = 'receitas')
	valor = models.DecimalField(decimal_places = 2, max_digits = 10, default = 0, help_text = 'O valor Total do documento')
	categoria = models.ForeignKey(Categoria,  related_name = 'categorie', on_delete = models.CASCADE)
	moeda = models.CharField(max_length = 19, help_text = "A moeda para pelo serviço")
	created = models.DateTimeField(auto_now_add = False,  blank=True)
	updated = models.DateTimeField(auto_now = False,  blank=True)
	descricao = RichTextField()
	fixa = models.BooleanField(help_text ='A renda fixa', default = False)
	repetir = models.BooleanField(help_text ='Renda variavel', default = False)
	quantidade = models.IntegerField(default = 0, null = True, help_text = "quantidade")
	tempo = models.IntegerField(default = 0, null = True, help_text = "O tempo que receberá")




	class Meta:
		ordering =['-created']
		verbose_name = 'Receita'
		verbose_name_plural = 'Receitas'

	def __str__(self):
		return f'{self.id}'


	def save(self, *args, **kwargs):

		

		super().save(*args, **kwargs)











