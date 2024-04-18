from django.core.validators import MaxValueValidator, MinValueValidator
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.conf import settings
from datetime import timedelta
from django.db import models
from decimal import Decimal
from random import randint



class Bank(models.Model): 

	STATUS_CURRENCY = (
		('USD', 'USD'),
		('EUR', 'EUR'),
		('GBP', 'GBP'),
		('JPY', 'JPY'),
		('BRL', 'BRL'),
	)	
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'finance_personal', on_delete = models.CASCADE)
	number = models.IntegerField()
	created = models.DateTimeField(auto_now_add = True,  blank=True)
	updated = models.DateTimeField(auto_now = True,  blank=True)
	Transaction = models.ManyToManyField('finance.Transaction', related_name = 'finance_transaction', blank=True)
	currency = models.CharField(max_length = 9, choices = STATUS_CURRENCY , default = "USD")
	balance = models.DecimalField(decimal_places = 2, max_digits = 10, default = 0, help_text = 'O valor dos investimentos')
	


	class Meta:		
		verbose_name = 'Conta Bancaria'
		verbose_name_plural = 'Conta Bancarias'

	def __str__(self):
		return f'{self.number }'
	
    
	def save(self, *args, **kwargs):
		
		if self.id is None:
			self.number = randint(100000, 999999)
		

		super().save(*args, **kwargs)
	


class Category(models.Model):

	id = models.IntegerField(primary_key = True, editable = False, unique = True)
	name = models.CharField(max_length = 70, unique = True)
	type = models.CharField(max_length = 90, )
	icon = models.CharField(max_length = 90)
	iconColor = models.CharField(max_length = 90)
	Transaction = models.ManyToManyField('finance.Transaction', related_name = 'category_transaction')

	class Meta:		
		verbose_name = 'Categoria'
		verbose_name_plural = 'Categorias'

	def __str__(self):
		return f'{self.name }'
	

	def save(self, *args, **kwargs):
		
		if self.id is None:
			self.id = randint(10000000, 99999999)	
		super().save(*args, **kwargs)



class Transaction(models.Model):

	id = models.IntegerField(primary_key = True, editable = False, unique = True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'username', blank=True, on_delete = models.CASCADE)
	bank = models.ForeignKey(Bank, related_name = 'bank', blank=True, on_delete = models.CASCADE)		
	categoria = models.ForeignKey(Category,  related_name = 'categorie', on_delete = models.CASCADE)	
	date = models.DateTimeField(auto_now_add = False,  blank=True)	
	note = RichTextField()
	amount = models.DecimalField(decimal_places = 2, max_digits = 10, default = 0, help_text = 'O valor Total do documento')
	recipient = models.CharField(max_length = 90, )


	class Meta:
		ordering =['-date']
		verbose_name = 'Movimentação'
		verbose_name_plural = 'Movimentações'

	def __str__(self):
		return f'{self.id}'


	def save(self, *args, **kwargs):
		if self.id is None:
			self.id = randint(10000000, 99999999)
		super().save(*args, **kwargs)


'''
class Planejamento(models.Model):
    id = models.CharField(max_length  = 110, primary_key = True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'usuário_planejamento', on_delete = models.CASCADE)   
    pms = models.DecimalField( max_digits = 10, decimal_places = 2, default=0 , help_text = "Patrimônio Mínimo de Sobrevivência")
    pmr = models.DecimalField( max_digits = 10, decimal_places = 2, default=0 , help_text = "Patrimônio Mínimo Recomendado para sua Segurança")
    pi = models.DecimalField( max_digits = 10, decimal_places = 2, default=0 , help_text = "Patrimônio Ideal para sua idade e situação de Consumo")
    pnif = models.DecimalField( max_digits = 10, decimal_places = 2, default=0 , help_text = "Patrimônio Necessário para a Independência Financeira")
    estabilidade = models.BooleanField(default = False, help_text = "O tipo de empregabilidade")

    class Meta:
        verbose_name = 'Planejamento'
        verbose_name_plural = 'Planejamentos'


    def save(self, *args, **kwargs):

        if self.estabilidade == True:
            self.pmr = ( 12 * self.pms )
        else:
            self.pmr = ( 20 * self.pms )

        self.pi = (( 12 * self.pms ) * idade(self.user.date_of_birth.year))
        self.pnif = ((12 * self.pms) / Decimal(0.08))
        super().save(*args, **kwargs)





class Reserva(models.Model):


	STATUS_CHOICES = (

		('inicial','Inicial'),
		('executando','Executando'),
		('concluido','Concluido'),
		)

	id = models.CharField(max_length  = 110, primary_key = True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'usuário_reserva', on_delete = models.CASCADE) 
	inicial = models.DecimalField( max_digits = 10, decimal_places = 2, default=0 , help_text = "Patrimônio inicial")
	rendimentos = models.DecimalField(decimal_places = 2, max_digits = 10, default = 0, help_text = 'O valor redimentos')
	status = models.CharField(max_length = 90, choices = STATUS_CHOICES, default = 'inicial')		
	created = models.DateTimeField(auto_now_add = True,  blank=True)
	updated = models.DateTimeField(auto_now = True,  blank=True)
	descricao = RichTextField()	
	total = models.DecimalField(decimal_places = 2, max_digits = 10, default = 0, help_text = 'O valor Total fundo de emergência')
	referencia = models.DecimalField(decimal_places = 2, max_digits = 10, default = 0, help_text = 'O valor de referencia da reserva de emergência')
	complete_per = models.IntegerField( validators = [MinValueValidator(0), MaxValueValidator(100)], default=0)


	class Meta:
		verbose_name = 'Reserva'
		verbose_name_plural = 'Reservas'


	def __str__(self):
		return f'{self.inicial}'


	def save(self, *args, **kwargs):

		self.total = self.inicial + self.rendimentos

		if self.referencia > 0 or self.total > 0:			
			self.complete_per = int(self.total) / int(self.referencia)
		else:
			self.referencia = 0
			
		super().save(*args, **kwargs)

	
'''