from django.db import models

# Create your models here.



class Perfil(models.Model):

    STATUS_CHOICES = (

        ('Conservador','Conservador'),
        ('Moderado','Moderado'),
        ('Dinâmico','Dinâmico'),
        ('Arrojado','Arrojado'),
        ('Agressivo','Agressivo'),
        )

    id = models.BigAutoField(primary_key=True, editable=False) 
    investor = models.CharField(max_length = 190, choices = STATUS_CHOICES, default = 'Conservador', blank = True, null = True)
    description = models.TextField()
    risk = models.ManyToManyField("management.Risk", related_name="risk_profile",  blank=True )    
    minimum = models.IntegerField(default=0)
    maximum = models.IntegerField(default=0)
    usuario = models.ManyToManyField('accounts.User', related_name = 'perfil_investidor', blank=True)
    color = models.CharField(max_length = 40, blank=True)
   


    def __str__(self):
        return f'{self.investor}'
    
    class Meta:
        ordering = ('id',)
        verbose_name = "Perfil do Investidor"
        verbose_name_plural = "Perfis do Investidor"


class Situacao(models.Model):

    STATUS_CHOICES = (

        ('investidor','Investidor'),
        ('equilibrado','Equilibrado'),
        ('endividado','Endividado'),
        
        )
    
    usuario = models.ManyToManyField('accounts.User', related_name = 'situacao_usuario', blank=True)
    condicao = models.CharField(max_length = 190, choices = STATUS_CHOICES, default = 'Conservador')
    strategic  = models.ManyToManyField("management.Strategy", related_name="estrategicas", help_text="Estrategias", blank=True)  
    minimum = models.IntegerField(default= 0)
    maximum = models.IntegerField(default=0)


    def __str__(self):
        return f'{self.condicao}'
    
    class Meta:
        ordering = ('id',)
        verbose_name = "Situacao Financeira"
        verbose_name_plural = "Situacoes Financeiras"


class Strategy(models.Model):

    situacao = models.ForeignKey(Situacao, verbose_name = "Situacao", on_delete= models.CASCADE)
    order = models.IntegerField(default = 0, blank  = True, null=True )
    name = models.CharField(max_length = 400)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        ordering = ('order',)
        verbose_name = "Estratégia"
        verbose_name_plural = "Estratégias"

   


class Risk(models.Model):
  
    idade = models.CharField(max_length =160)
    description = models.TextField()
    minimum = models.IntegerField( default=0)
    maximum = models.IntegerField(default=0)
    alto = models.BooleanField(default=False, help_text="Risk Alto")
    moderado = models.BooleanField(default=False, help_text="Risk Moderado")
    baixo = models.BooleanField(default=False, help_text="Baixo Risk")
    investimentos = models.ManyToManyField("management.Investimento", related_name = "portifolio_risk", help_text="Portfólio", blank=True)      

    def __str__(self):
        return f'{self.idade}'
    
    class Meta:
        ordering = ('id',)
        verbose_name = "Risco"
        verbose_name_plural = "Riscos"
        



class Investimento(models.Model):
    
    STATUS_CHOICES = (

        ("Fixa","Fixa"),
        ("Variável","Variável")
    )

    name = models.CharField(max_length= 400)
    description = models.TextField()
    tipo = models.CharField(max_length= 90, choices= STATUS_CHOICES, default = "Fixa" )
    tax = models.BooleanField(default=False, help_text="Imposto")

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        ordering = ('id',)
        verbose_name = "Investimento"
        verbose_name_plural = "Investimentos"



class Portfolio (models.Model):  

    name = models.CharField(max_length= 400)
    description = models.TextField()
    


   


