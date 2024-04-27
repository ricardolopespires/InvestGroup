from django.db import models
from accounts.models import User

# Create your models here.



class Continent(models.Model):
	id = models.CharField(max_length = 150, primary_key = True, unique = True)
	region = models.CharField(max_length = 150, help_text='O nome do Continente')
	subregion = models.CharField(max_length = 150, help_text='O nome do Continente')
	paises = models.ManyToManyField('economia.Countrie', related_name= 'paises')
	aberto = models.BooleanField(default = False)


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

	CHOICES_STATUS = (

		('primeiro','Primeiro'),
		('segundo','Segundo'),
		('terceiro','Terceiro'),

		)

	id = models.CharField(max_length = 150, primary_key = True, unique = True)
	name = models.CharField(max_length = 150, help_text='O nome do Pais')
	official = models.CharField( max_length = 400, help_text = 'Nome Oficial do país')
	status = models.CharField( max_length = 19, default = 'segundo', help_text = "Que tipo de país")
	area = models.FloatField(default = 0, help_text = 'A area do teritorial do pais')
	borders = models.CharField(max_length = 400, help_text = 'Pais vizinhos', blank = True, null = True)
	capital  = models.CharField(max_length = 400, help_text = 'Capital do Pais ')
	continents = models.ForeignKey(Continent, related_name = 'continente', on_delete = models.CASCADE)
	currencies = models.ManyToManyField(Currencie)
	population = models.IntegerField(default = 0)
	coatOfArms = models.URLField(max_length=200, )
	languages = models.CharField(max_length = 150)
	flags = models.URLField(max_length = 200)
	user = models.ManyToManyField("accounts.User", blank=True, related_name = 'user_favoritos')

	def __str__(self):
		return f'{self.name}'
