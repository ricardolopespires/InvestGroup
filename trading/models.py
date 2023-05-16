from django.db import models

# Create your models here.





class Capital(models.Model):
	
	operacoes = models.FloatField()
	loss = models.FloatField()
	profit = models.FloatField()
	total = models.FloatField()


	def __str__(self):
		return f'{self.total}'


	class Meta:
		ordering = ['total']
		verbose_name = 'Capital'
		verbose_name_plural = 'Capitais'


	def save(self, *args, **kwargs):

		self.total = self.operacoes + self.profit - self.loss
		super().save(*args, **kwargs)




class Gerenciamento(models.Model):

	STATUS_TIPO = (

		('indice','Indice'),
		('dolar','Dolar'),
		('ações', 'Ações'),
		('opções','Opções'),
		('americano','Americano')

		)

	capital = models.ForeignKey(Capital,  related_name = 'capital_gerencimento', on_delete = models.CASCADE)
	status = models.CharField( max_length = 150, choices = STATUS_TIPO, default = 'indice')
	inicial = models.DecimalField(decimal_places = 2, max_digits = 10, help_text = 'O valor inicial para operações')
	preco = models.DecimalField(decimal_places = 2, max_digits = 10, help_text = 'O Preço do contrato')
	porcent =  models.DecimalField(decimal_places = 2, max_digits = 10, help_text = 'A Porcentagem de perca por operações')
	ganho = models.DecimalField(decimal_places = 2, max_digits = 10, help_text = 'O Valor do ganho')
	pontos = models.IntegerField()
	contratos = models.IntegerField()
	perda = models.IntegerField()
	stop = models.FloatField()


	def __str__(self):
		return f'{self.capital}'


	class Meta:
		ordering = ['inicial']
		verbose_name = 'Gerenciamento'
		verbose_name_plural = 'Gerenciamentos'


	def save(self, *args, **kwargs):



		self.pontos = self.porcent * self.inicial
		self.perda = self.preco * self.pontos	
		super().save(*args, **kwargs)






class Operacoe(models.Model):


	STATUS_TIPO = (

		('compra','Compra'),
		('venda','venda'),

		)

	id = models.IntegerField(primary_key = True, help_text = "Numero indentificação da operação")
	ativo = models.CharField(max_length = 150, help_text = "O nome do ativo ")
	stoploss = models.BooleanField(help_text ='Stop Loss')
	takeprofit = models.BooleanField(help_text = "Take Profit")
	inicio = models.DateTimeField(auto_now_add = True, help_text = "Data da entreda da operação")
	tipo = models.CharField( max_length = 150, choices = STATUS_TIPO, default = 'compra', help_text = "Tipo de operação")
	volume = models.FloatField()
	entrada = models.FloatField()
	sl = models.FloatField()
	tp = models.FloatField()
	saida = models.FloatField()
	lucro = models.FloatField()


	def __str__(self):
		return f'{self.ativos}'


	class Meta:
		ordering = ['inicio']
		verbose_name = 'Operação'
		verbose_name_plural = 'Operações'
