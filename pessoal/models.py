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


	

	id = models.CharField(max_length = 90, primary_key = True)
	user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'user', blank=True)
	real = models.DecimalField(max_digits = 5, decimal_places = 2)
	categoria = models.ForeignKey(Categoria,  related_name = 'categorie', on_delete = models.CASCADE)	
	previsto = models.DecimalField(max_digits = 5, decimal_places = 2)
	atual = models.DecimalField(max_digits = 5, decimal_places = 2)
	diferenca = models.DecimalField(max_digits = 5, decimal_places = 2)
	created = models.DateTimeField(auto_now_add=True,  blank=True)
	updated = models.DateTimeField(auto_now=True,  blank=True)
	variacao = models.IntegerField( validators = [MinValueValidator(0), MaxValueValidator(100)], default=0)



	class Meta:
		ordering =['-created']
		verbose_name = 'Receita'
		verbose_name_plural = 'Receitas'

	def __str__(self):
		return f'{self.id}'


	def save(self, *args, **kwargs):

		self.diferenca = self.atual - self.previsto
		self.variacao = int((self.atual / self.previsto)*100)

		super().save(*args, **kwargs)











