from django.db import models

# Create your models here.




class Calendario(models.Model):


	id = models.CharField(max_length = 90, primary_key = True)
	codigo = models.CharField(max_length = 28, )
	data = models.DateTimeField(auto_now_add = False)
	horario = models.CharField(max_length = 19)
	img = models.ImageField(upload_to = 'bandeiras', blank = True, null = True)
	pais = models.CharField(max_length = 19)
	moeda = models.CharField(max_length = 19)
	importancia = models.CharField(max_length = 19)
	evento = models.TextField()
	K = models.BooleanField(default = False)
	M = models.BooleanField(default = False)
	B = models.BooleanField(default = False)
	percent = models.BooleanField(default = False)
	actual = models.FloatField(max_length = 19)
	forecast = models.FloatField(max_length = 19)
	previous= models.FloatField(max_length = 19)


	def __str__(self):
		return f'{self.id}'


	class Meta:
		ordering = ['-data']

		verbose_name = 'Evento Economico'
		verbose_name_plural = 'Eventos Economico'



class Continent(models.Model):
	id = models.CharField(max_length = 150, primary_key = True, unique = True)
	region = models.CharField(max_length = 150, help_text='O nome do Continente')
	subregion = models.CharField(max_length = 150, help_text='O nome do Continente')
	paises = models.ManyToManyField('economia.Countrie', related_name= 'paises')


	def __str__(self):
		return f'{self.subregion}'
	


class Currencie(models.Model):
	id = models.CharField(max_length = 50, primary_key = True, )
	name = models.CharField(max_length = 50, help_text = 'nome da moeda' )
	symbol = models.CharField(max_length = 10, help_text ='Simbolo da moeda' )
	paises = models.ManyToManyField('economia.Countrie', related_name= 'moedas_paises')
	def __str__(self):
		return f'{self.name}'


class Countrie(models.Model):
	id = models.CharField(max_length = 150, primary_key = True, unique = True)
	name = models.CharField(max_length = 150, help_text='O nome do Pais')
	official = models.CharField( max_length = 400, help_text = 'Nome Oficial do país')
	area = models.FloatField(default = 0, help_text = 'A area do teritorial do pais')
	borders = models.CharField(max_length = 400, help_text = 'Pais vizinhos', blank = True, null = True)
	capital  = models.CharField(max_length = 400, help_text = 'Capital do Pais ')
	continents = models.ForeignKey(Continent, related_name = 'continente', on_delete = models.CASCADE)
	currencies = models.ManyToManyField(Currencie)
	population = models.IntegerField(default = 0)
	coatOfArms = models.URLField(max_length=200, )
	languages = models.CharField(max_length = 150)
	flags = models.URLField(max_length = 200)

	def __str__(self):
		return f'{self.name}'





class Indicators(models.Model):
	id = models.CharField(max_length = 150, primary_key = True, unique = True)
	pib = models.FloatField(default = 0, help_text = 'Produto Interno Bruto (PIB)')
	selic = models.FloatField(default = 0, help_text = 'taxa básica de juros da economia')
	ipca = models.FloatField(default = 0, help_text = 'Índice Nacional de Preços ao Consumidor Amplo (IPCA)')
	tr = models.FloatField(default = 0, help_text = 'Taxa Referencial')
