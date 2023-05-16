from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.



class Categoria(models.Model):

	id = models.CharField(max_length = 150, primary_key = True) 	
	nome = models.CharField(max_length = 150)
	img = models.CharField(max_length = 17,blank = True, null = True)
	slug = models.SlugField(blank = True, null = True)
	descricao = RichTextField(blank = True, null = True)	
	classificacao = models.CharField(max_length =  3, blank = True, null = True )
	average_rating = models.CharField(max_length=5, blank = True, null = True)
	average_count = models.CharField(max_length=100, blank = True, null = True)
	empresas = models.ManyToManyField('acoes.Empresa', related_name= 'empresa_categoria', blank = True)  	


	def __str__(self):
		return self.nome

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.nome)
		return super().save(*args, **kwargs)



class Setor(models.Model):

	STATUS_CHOICES =(

		('fundo','Fundo'),
		('alta','Alta'),
		('topo','Topo'),
		('baixa','Baixa'),
	)
	id = models.CharField(max_length = 150, primary_key = True)	
	nome = models.CharField(max_length = 150)
	icon = models.CharField(max_length = 40,blank = True, null = True)
	slug = models.SlugField(null=True)
	status = models.CharField(max_length = 150, choices = STATUS_CHOICES, default = 'fundo')
	descricao = RichTextField(blank = True, null = True)	
	classificacao = models.CharField(max_length =  3, blank = True )
	average_rating = models.CharField(max_length=5, blank=True)
	average_count = models.CharField(max_length=100, blank=True)
	empresas = models.ManyToManyField('acoes.Empresa', related_name= 'empresa_setor', blank = True)   	

	class Meta:

		verbose_name = 'Setor'
		verbose_name_plural = 'Setores'

	def __str__(self):
		return self.nome
		

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.nome)
		return super().save(*args, **kwargs)



class SubSetor(models.Model):
	id = models.CharField(max_length = 150, primary_key = True)
	setor = models.ForeignKey(Setor, related_name = 'subsetor_setor', on_delete = models.CASCADE) 
	nome = models.CharField(max_length = 150)
	img = models.URLField(blank = True, null = True)
	slug = models.SlugField(null=True)
	descricao = RichTextField(blank = True, null = True)	
	classificacao = models.CharField(max_length =  3, blank = True )
	average_rating = models.CharField(max_length=5, blank=True)
	average_count = models.CharField(max_length=100, blank=True)
	empresas = models.ManyToManyField('acoes.Empresa', related_name= 'empresa_subsetor', blank = True)


	class Meta:

		verbose_name = 'Sub-Setor'
		verbose_name_plural = 'Sub-Setores'   	


	def __str__(self):
		return self.nome

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.nome)
		return super().save(*args, **kwargs)


class Segmento(models.Model):
	id = models.CharField(max_length = 150, primary_key = True)
	subsetor = models.ForeignKey(SubSetor, related_name = 'segmento_subsetor', on_delete = models.CASCADE) 
	nome = models.CharField(max_length = 150)
	img = models.URLField(blank = True, null = True)
	slug = models.SlugField(null=True)
	descricao = RichTextField(blank = True, null = True)	
	classificacao = models.CharField(max_length =  3, blank = True )
	average_rating = models.CharField(max_length=5, blank=True)
	average_count = models.CharField(max_length=100, blank=True)
	empresas = models.ManyToManyField('acoes.Empresa', related_name= 'empresa_segmento', blank = True)

	class Meta:

		verbose_name = 'Segmento'
		verbose_name_plural = 'Segmentos'   	


	def __str__(self):
		return self.nome

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.nome)
		return super().save(*args, **kwargs)



class Empresa(models.Model):
	id = models.CharField(max_length = 150, primary_key = True)
	categoria = models.ForeignKey( Categoria, related_name = '_empresa_categoria', on_delete = models.CASCADE)
	setor = models.ForeignKey(Setor, related_name = 'empresa_setor', on_delete = models.CASCADE)
	subsetor = models.ForeignKey(SubSetor, related_name = 'empresa_subsetor', on_delete = models.CASCADE) 
	segmento = models.ForeignKey(Segmento, related_name = 'empresa_segmento', on_delete = models.CASCADE) 
	nome = models.CharField(max_length = 150)
	logo = models.URLField(blank = True, null = True)
	slug = models.SlugField(null=True)
	descricao = RichTextField(blank = True, null = True)
	valor = models.DecimalField(decimal_places = 2, max_digits = 10, help_text = "O valor atual da ação")
	minimo = models.DecimalField(decimal_places = 2, max_digits = 10, help_text = "O valor minimo já alcançado pela ação")
	maximo = models.DecimalField(decimal_places = 2, max_digits = 10, help_text = "O valor maximo já alcançado pela ação")	
	dividendo = models.BooleanField(help_text = 'A ação paga dividendos', default = False)
	bonificacao = models.BooleanField(help_text = 'A empresa paga bonificação', default = False)
	aluguel = models.BooleanField(help_text = 'A empresa tem ação aluguada ', default = False)
	valorizacao = models.DecimalField(decimal_places = 2, max_digits = 10, help_text = "A valorização no perido de 12 meses") 
	classificacao = models.CharField(max_length =  3, blank = True )
	average_rating = models.CharField(max_length=5, blank=True)
	average_count = models.CharField(max_length=100, blank=True)
	

	class Meta:

		verbose_name = 'Empresas'
		verbose_name_plural = 'Empresas'

	def __str__(self):
		return self.nome

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.nome)
		return super().save(*args, **kwargs)



class Dividendo(models.Model):
	pass
	   