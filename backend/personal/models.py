from django.core.validators import MaxValueValidator, MinValueValidator
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.conf import settings
from datetime import timedelta
from django.db import models
from decimal import Decimal




class Categoria(models.Model):
	
	STATUS_CHOICES = (

		('Habitação','Habitação'),
		('Transporte','Transporte'),
		('Alimentação','Alimentação'),
		('Saúde','Saúde'),
		('Educação','Educação'),
		('Impostos','Impostos'),    
		('Cuidados pessoais','Cuidados pessoais'),
		('Manutenção/ prevenção','Manutenção/ prevenção'),
		('Transporte','Transporte'),
		('Vestuario','Vestuario'),
		('Lazer','Lazer'),
		('Outros','Outros'),
		

    )
	
	STATUS_MODELS = (

		('Fixa','Fixa'),
		('Variavel','Variavel'),
		('Extra','Extra'),
		('Adicionais','Adicionais'),
		

    )
	nome = models.CharField(max_length = 70, )
	tipo = models.CharField(max_length = 150,  choices = STATUS_CHOICES, default = 'receitas')
	status = models.CharField(max_length = 150,  choices = STATUS_MODELS, default = 'Fixas')
	punctuation = models.IntegerField(default = 0)


	class Meta:		
		verbose_name = 'Categoria'
		verbose_name_plural = 'Categorias'

	def __str__(self):
		return f'{self.nome }'




class Movimentacao(models.Model):


	STATUS_CHOICES = (

		('receitas','Receitas'),
		('despesas','Despesas'),
		)

	
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'user', on_delete = models.CASCADE)
	status = models.CharField(max_length = 19, choices = STATUS_CHOICES, default = 'receitas')
	categoria = models.ForeignKey(Categoria,  related_name = 'categorie', on_delete = models.CASCADE)	
	created = models.DateTimeField(auto_now_add = True,  blank=True)
	updated = models.DateTimeField(auto_now = True,  blank=True)
	descricao = RichTextField()	
	total = models.DecimalField(decimal_places = 2, max_digits = 10, default = 0, help_text = 'O valor Total do documento')



	class Meta:
		ordering =['-created']
		verbose_name = 'Movimentação'
		verbose_name_plural = 'Movimentações'

	def __str__(self):
		return f'{self.id}'


	def save(self, *args, **kwargs):		

		super().save(*args, **kwargs)




class Financeiro(models.Model):


	id = models.CharField(max_length = 90, primary_key = True)
	user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'financeiro_pessoal', blank=True)
	created = models.DateTimeField(auto_now_add = True,  blank=True)
	updated = models.DateTimeField(auto_now = True,  blank=True)		
	receitas = models.DecimalField(decimal_places = 2, max_digits = 10, default = 0, help_text = 'O valor das receitas')
	despesas = models.DecimalField(decimal_places = 2, max_digits = 10, default = 0, help_text = 'O valor das despesas')
	cartao = models.DecimalField(decimal_places = 2, max_digits = 10, default = 0, help_text = 'O valor das despesas')
	investimento = models.DecimalField(decimal_places = 2, max_digits = 10, default = 0, help_text = 'O valor dos investimento')
	total = models.DecimalField(decimal_places = 2, max_digits = 10, default = 0, help_text = 'O valor dos investimentos')


	class Meta:
		ordering =['-created']
		verbose_name = 'Financeiro'
		verbose_name_plural = 'Financeiros'

	def __str__(self):
		return f'{self.id}'


	
class Planejamento(models.Model):
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

	