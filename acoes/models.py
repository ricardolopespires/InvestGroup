from django.db import models
from django.conf import settings


# Create your models here.


class Setore(models.Model):
    id = models.CharField(max_length = 100, primary_key =True, )
    nome = models.CharField(max_length = 150, blank = True)
    empresas_setor = models.ManyToManyField('acoes.Empresa', related_name= 'acoes_empresa')
    img = models.URLField(blank=True)


    def __str__(self):
        return self.nome


class SubSetore(models.Model):
    id = models.CharField(max_length = 100, primary_key =True,)
    nome = models.CharField(max_length = 150, blank = True)
    empresas_sub_setor = models.ManyToManyField('acoes.Empresa', related_name= 'subsetor_empresa')


    def __str__(self):
        return self.nome


class Empresa(models.Model):   
    id = models.CharField(max_length = 100, primary_key =True, unique = True)
    Tipo = models.CharField(max_length = 150, blank = True)
    Empresa = models.CharField(max_length = 150, blank = True)
    img = models.URLField(blank=True)
    Setor = models.ManyToManyField(Setore, blank = True)
    Sub_Setor = models.ManyToManyField(SubSetore, blank = True)
    Cotacao = models.FloatField( blank =True)
    Data_ult_cot = models.DateTimeField(auto_now_add = False, )
    Min_52_sem = models.FloatField( blank = True)
    Max_52_sem = models.FloatField( blank = True)
    Vol_med_2m  = models.IntegerField( blank  = True)
    Valor_de_mercado = models.IntegerField( blank = True)
    Valor_da_firma = models.IntegerField( blank = True)
    Ult_balanco_processado = models.DateTimeField(auto_now_add = False, )
    Nro_Acoes = models.IntegerField( blank = True)
    PL 	= models.IntegerField( blank = True)
    PVP = models.IntegerField( blank = True)
    PEBIT = models.IntegerField( blank = True)
    PSR = models.IntegerField( blank = True)
    PAtivos = models.IntegerField( blank = True)
    PCap_Giro = models.IntegerField( blank = True)
    PAtiv_Circ_Liq  = models.IntegerField( blank = True)
    Div_Yield = models.CharField(max_length = 150, blank = True)
    EV_EBITDA  = models.IntegerField( blank = True)
    EV_EBIT = models.IntegerField( blank = True)
    Cres_Rec_5a = models.CharField(max_length = 150, blank = True)
    LPA = models.IntegerField( blank = True)
    VPA = models.IntegerField( blank = True)
    Marg_Bruta = models.CharField(max_length = 150, blank = True) 
    Marg_EBIT = models.CharField(max_length = 150, blank = True)
    Marg_Liquida = models.CharField(max_length = 150, blank = True)
    EBIT_Ativo = models.CharField(max_length = 150, blank = True)
    ROIC = models.CharField(max_length = 150, blank = True)
    ROE =  models.CharField(max_length = 150, blank = True)
    Liquidez_Corr = models.IntegerField( blank = True)
    Div_Br_Patrim = models.IntegerField( blank = True)
    Giro_Ativos  = models.IntegerField( blank = True)
    Ativo = models.IntegerField( blank = True)
    Disponibilidades = models.IntegerField( blank = True)
    Ativo_Circulante = models.IntegerField( blank = True)
    Div_Bruta = models.IntegerField( blank = True)
    Div_Liquida = models.IntegerField( blank = True)
    Patrim_Liq = models.IntegerField( blank = True)
    Receita_Liquida_12m = models.IntegerField( blank = True)
    EBIT_12m = models.IntegerField( blank = True)
    Lucro_Liquido_12m = models.IntegerField( blank = True)
    Receita_Liquida_3m = models.IntegerField( blank = True)
    EBIT_3m = models.IntegerField( blank = True)
    Lucro_Liquido_3m = models.IntegerField( blank = True)
    

    def __str__(self):
        return self.Empresa


class Aluguel(models.Model):
    id = models.IntegerField(primary_key =True, unique = True)
    Empresa = models.ForeignKey(Empresa, related_name = 'aluguel_acoes', on_delete = models.CASCADE)
    nome = models.CharField(max_length = 150, blank = True)


class Dividendos(models.Model):
    id = models.IntegerField(primary_key =True, unique = True)
    Empresa = models.ForeignKey(Empresa, related_name = 'dividendos_acoes', on_delete = models.CASCADE)
    Data_com = models.DateTimeField(auto_now_add = True, blank = True)
    Pagamento = models.DateTimeField(auto_now_add = True, blank = True)
    valor = models.DecimalField(decimal_places=2, max_digits=10, blank=True)
