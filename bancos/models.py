from ckeditor.fields import RichTextField
from django.conf import settings
from django.db import models


# Create your models here.




class Bandeira(models.Model):
	
	nome = models.CharField(max_length = 70, help_text = "O nome da bandeira do cartão")
	logo = models.FileField(upload_to='bandeira de cartão %Y-%m-%d')


	class Meta:		
		verbose_name = 'Bandeira'
		verbose_name_plural = 'Bandeiras'

	def __str__(self):
		return f'{self.nome}'





class Cartao(models.Model):	
	
	numero = models.IntegerField( help_text = 'O numero do cartão')
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'nome_cartao', on_delete = models.CASCADE)
	instituicao = models.CharField(max_length = 70)
	nome = models.CharField(max_length = 70)
	bandeira  = models.ForeignKey(Bandeira, related_name = 'bandeira', on_delete = models.CASCADE)
	created = models.DateTimeField(auto_now_add = True,  blank=True)
	updated = models.DateTimeField(auto_now = True,  blank=True)
	vencimento = models.DateTimeField( auto_now_add = False,)
	limite = models.DecimalField(decimal_places = 2, max_digits = 10, default = 0, help_text = 'O Limite do cartões')




	class Meta:
		ordering =['-created']
		verbose_name = 'Cartão'
		verbose_name_plural = 'Cartões'

	def __str__(self):
		return f'{self.id}'




class Fatura(models.Model):


	STATUS_CHOICES = (

		('em dia','Em dia'),
		('atrasada','Atrasada'),
		)

	id = models.CharField(max_length = 90, primary_key = True)	
	cartao = models.ForeignKey(Cartao,  related_name = 'cartao', on_delete = models.CASCADE)	
	created = models.DateTimeField(auto_now_add = True,  blank=True)
	updated = models.DateTimeField(auto_now = True,  blank=True)
	descricao = RichTextField()
	valor = models.DecimalField( decimal_places = 2 , max_digits = 10, default = 0, help_text = "valor da compra")	
	quantidade = models.IntegerField(default = 0, null = True, help_text = "quantidade")
	total = models.DecimalField(decimal_places = 2, max_digits = 10, default = 0, help_text = 'O valor Total do documento')	
	parcela = models.BooleanField(default = False, help_text = "Foi parcelado")

	class Meta:
		ordering =['-created']
		verbose_name = 'Fatura'
		verbose_name_plural = 'Faturas'

	def __str__(self):
		return f'{self.id}'


