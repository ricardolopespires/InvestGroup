from django.core.validators import MaxValueValidator, MinValueValidator
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.conf import settings
from datetime import timedelta
from django.db import models
from decimal import Decimal







class Categoria(models.Model):


	STATUS_CHOICE = (

			('público', 'Público'),
			('privado','Privado')


		)

	id = models.CharField(primary_key =  True, max_length = 90)
	nome = models.CharField(max_length = 90, help_text = "Nome do Produto")
	status = models.CharField(max_length = 90, choices = STATUS_CHOICE, default = 'banco')
	descricao = RichTextField( help_text = "descrição do produto")
	percent = models.IntegerField(
                      validators=[MinValueValidator(0),
                                  MaxValueValidator(100)], default = 0)
	active = models.BooleanField()


	class Meta:		
		verbose_name = 'Categoria'
		verbose_name_plural = 'Categorias'

	def __str__(self):
		return f'{self.nome }'




class Renda(models.Model):

	STATUS_CHOICE = (

		('banco','Banco'),
		('corretora','Corretora'),
		)




	id = models.CharField(primary_key =  True, max_length = 90)
	nome = models.ForeignKey(Categoria,  related_name = 'categorie', on_delete = models.CASCADE)
	instituicao = models.CharField(max_length = 90, help_text = 'Nome da instituição financeira')	
	status = models.CharField(max_length = 90, choices = STATUS_CHOICE, default = 'banco')	
	moeda = models.CharField(max_length = 19, help_text = "A moeda do investimento")
	created = models.DateTimeField(auto_now_add = False,  blank=True)
	updated = models.DateTimeField(auto_now = False,  blank=True)
	carencia = models.IntegerField(default = 0, null = True, help_text = "O tempo que receberá")
	diaria = models.BooleanField(help_text ='Liquidez diária', default = False)
	imposto = models.BooleanField(help_text ='Imposto de renda ', default = False)
	taxa = models.BooleanField( help_text = "Taxas de administração", default = False)
	iof = models.BooleanField(help_text = "Imposto sobre Operações Financeiras (IOF)", default = False)
	fgc = models.BooleanField(help_text = "Garantia do Fundo Garantidor de Crédito (FGC)", default = False)
	rentabilidade = models.BooleanField(help_text = "Rentabilidade baixa", default = False)
	pre = models.BooleanField(help_text = "Taxa pré-fixada (fixada antes)", default = False)
	pos = models.BooleanField(help_text = "Rendimento é definido depois", default = False)
	minimo = models.DecimalField(decimal_places = 2, max_digits = 10, default = 0, help_text = 'O valor Minimo de deposito')
	percent = models.IntegerField(
                      validators=[MinValueValidator(0),
                                  MaxValueValidator(100)], default = 0)
	active = models.BooleanField()




	class Meta:		
		verbose_name = 'Renda Fixa'
		verbose_name_plural = 'Rendas Fixas'

	def __str__(self):
		return f'{self.nome }'