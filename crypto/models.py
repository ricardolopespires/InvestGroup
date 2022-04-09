
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.files import File
from django.utils import timezone
from django.conf import settings
from PIL import Image, ImageDraw
from datetime import timedelta
from django.db import models
from io import BytesIO
import qrcode


# Create your models here.




class Categoria(models.Model):
    id = models.CharField(primary_key = True, max_length = 150, unique = True, help_text = 'codigo de indentificação da categoria')
    name = models.CharField(max_length = 40, help_text = 'A modalidade do crypto ativo', blank = True, null = True)
    content = models.TextField(null = True)
    market_cap = models.FloatField(null = True)
    market_cap_change_24h = models.FloatField( null = True)
    top_1 = models.ImageField(upload_to = 'crypto/top_1')
    top_2 = models.ImageField(upload_to = 'crypto/top_2')
    top_3 = models.ImageField(upload_to = 'crypto/top_3')
    updated_at = models.DateTimeField(auto_now_add = False, null = True)
    volume_24h = models.FloatField( null = True)
    cryptos = models.ManyToManyField('crypto.Cripto',related_name='cripto_tags')
    
      
    def __str__(self):
        return f'{self.name}'


    class Meta:
         ordering = ['name']
         verbose_name = 'Categoria'
         verbose_name_plural = 'Categorias'


    

class Plataforma (models.Model):
    id = models.CharField(primary_key = True, max_length = 150, unique = True, help_text = 'codigo de indentificação da plataforma')
    nome = models.CharField(max_length = 40, help_text = 'O nome da rede')
    slug = models.SlugField()
    simbolo = models.CharField(max_length = 90, help_text = 'O simbolo da rede')
    token_address = models.CharField(max_length = 90, help_text = 'Endereço do token', blank = True, null = True)
    qr_code = models.ImageField(upload_to = 'token_address/qr_code', blank = True, null = True, help_text='QR code de autorização do veiculo')
    cryptos = models.ManyToManyField('crypto.Cripto',related_name='cripto_plataforma')



    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.token_address)
        canvas = Image.new('RGB',(350, 350), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        ftoken_address = f'qr_code-{self.token_address}'+'.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(ftoken_address, File(buffer), save = False)
        canvas.close()
        super().save(*args, **kwargs)


    def __str__(self):
        return self.nome


    class Meta:
         ordering = ['nome']
         verbose_name = 'Plataforma'
         verbose_name_plural = 'Plataformas'



class Exchange (models.Model):
    id = models.CharField(primary_key = True, max_length = 150, unique = True, help_text = 'codigo de indentificação da plataforma')    
    country = models.CharField(max_length = 40, help_text = 'Código indetificador da rede', blank = True, null = True)
    description = models.TextField(help_text = 'Descrição d Exchange ', blank = True, null = True)
    has_trading_incentive = models.BooleanField( help_text = 'tem incentivo comercial', )
    image = models.ImageField(upload_to = 'blockchain/', help_text = 'O simbolo da rede', blank = True, null = True)
    name = models.CharField(max_length = 40, help_text = 'O nome da rede')
    slug = models.SlugField(help_text = 'Slug')
    trade_volume_24h_btc  = models.FloatField()
    trade_volume_24h_btc_normalized = models.FloatField()
    trust_score = models.IntegerField()
    trust_score_rank = models.IntegerField()
    url = models.URLField()
    fee = models.FloatField( help_text = 'Taxa de transação da exchange', default = 0, blank = True, null = True)
    year_established = models.CharField(max_length = 150, help_text = 'Data de inicio da operações da ', null = True)     
    cryptos = models.ManyToManyField('crypto.Cripto',related_name='cripto_blockchain')
    

    def __str__(self):
        return f'{self.name}'


    class Meta:
         ordering = ['name']
         verbose_name = 'Exchange'
         verbose_name_plural = 'Exchanges'



   
class Cripto(models.Model):

    id = models.CharField(primary_key = True, max_length = 150, unique = True, help_text = 'codigo de indentificação do ativo')
    asset_platform_id = models.CharField(max_length = 14, help_text = "plataforma da cripto ativo", blank = True, null = True)
    categoria = models.ManyToManyField(Categoria, help_text = "As categoria do ativo ")
    symbol = models.CharField(max_length = 14, help_text = "Simbolo do cripto ativo")
    name = models.CharField(max_length = 14, help_text = "Nome do cripto ativo")
    slug = models.SlugField()
    image = models.URLField(help_text = "Image do cripto ativo")
    descricao = models.TextField( help_text ='Descrição do ativo')
    current_price = models.FloatField( help_text = 'Valor do Ativo',default = 0, blank = True, null = True)
    market_cap = models.FloatField( help_text = 'valor de mercado', default = 0, blank = True, null = True)
    market_cap_rank= models.IntegerField( help_text = 'A Classificação do crypto ativo no mercado', default = 0, blank = True, null = True)
    fully_diluted_valuation = models.FloatField( help_text = 'Total ativos deluido no mercado',default = 0, blank = True, null = True)
    total_volume = models.FloatField( help_text = 'Fornecimento total',default = 0,blank = True, null = True)
    high_24h = models.FloatField( help_text = 'Valor maximo em 24 horas',default = 0, blank = True, null = True)
    low_24h = models.FloatField( help_text = 'Valor Minimo em 24 horas',default = 0, blank = True, null = True)
    price_change_24h = models.FloatField( help_text = 'Variação do preço de mercado nas 25hr',default = 0, blank = True, null = True)
    price_change_percentage_24h = models.FloatField( help_text = 'Percentual do preço de mercado 24hr',default = 0, blank = True, null = True)
    market_cap_change_24h = models.FloatField( help_text = 'Variação do valor de mercado em 24hr',default = 0, blank = True, null = True)
    market_cap_change_percentage_24h = models.FloatField( help_text = 'Percentual variação do valor mercado 24hr',default = 0, blank = True, null = True)
    circulating_supply  = models.FloatField( help_text = 'Ativo em Circulação', default = 0, blank = True, null = True)
    total_supply  = models.FloatField( help_text = 'O total de ativos', default = 0, blank = True, null = True)
    max_supply  = models.FloatField( help_text = 'O maximo de ativos', default = 0, blank = True, null = True)
    ath  = models.FloatField( help_text = 'O valor mais alto do alcançado pelo ativo', default = 0, blank = True, null = True)
    ath_change_percentage  = models.FloatField( help_text = 'porcentagem', default = 0, blank = True, null = True)
    ath_date = models.DateTimeField(auto_now_add = False, help_text = 'Data da listagem ativo', blank = True, null = True) 
    atl = models.FloatField( help_text = 'O preço inicial do ativo', default = 0, blank = True, null = True)
    atl_change_percentage = models.FloatField( help_text = 'O porcetagem mais alto', default = 0, blank = True, null = True)
    atl_date = models.DateTimeField(auto_now_add = False, help_text = 'Data inicial ativo', blank = True, null = True) 
    roi = models.FloatField( help_text = 'Retorno sobre Investimento', default = 0, blank = True, null = True)
    last_updated = models.DateTimeField(auto_now_add = False, help_text = 'A ultima atualização no ativo', blank = True, null = True)
    contract_address = models.CharField(max_length = 14, help_text = "Endereço do Contrato")
    facebook_username = models.CharField(max_length = 400, help_text = 'Página no Facebook')
    twitter_screen_name = models.CharField(max_length = 90, help_text = 'Página no Twitter' )
    telegram_channel_identifier = models.CharField(max_length = 190, help_text = 'Página no Telegram')
    blockchain_site = models.CharField(max_length = 400, help_text = 'Página Oficial na Web ')
    official_forum_url = models.CharField(max_length = 400, help_text = 'Página Oficial do forum')
    repos_url = models.CharField(max_length = 150, help_text = 'Repositório no GitHub')
    qr_code = models.ImageField(upload_to = 'Veiculo/qr_code', blank = True, help_text='QR do endereço do contrato ')

    def __str__(self):
        return f'{self.name}'


    class Meta:
         ordering = ['market_cap_rank']
         verbose_name = 'Ativo'
         verbose_name_plural = 'Ativos'

    
    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.contract_address)
        canvas = Image.new('RGB',(290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fcontrato = f'qr_code-{self.contract_address}'+'.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fcontrato, File(buffer), save = False)
        canvas.close()
        super().save(*args, **kwargs)



class Price_percentage_change(models.Model):
    id = models.CharField(primary_key = True, max_length = 150, unique = True, help_text = 'codigo de indentificação do ativo')
    periodo = models.DateTimeField(auto_now_add = False)
    data = models.DateTimeField(auto_now_add = False)
    p_30 = models.FloatField( help_text = "Porcetagem do periodo de 30 dias")
    p_90 = models.FloatField( help_text = "Porcetagem do periodo de 90 dias")
    p_180 = models.FloatField( help_text = "Porcetagem do periodo de 180 dias")
    p_1 = models.FloatField( help_text = "Porcetagem do periodo de 1 Ano")

    class Meta:
        ordering = ['-data']

    def __str__(self):
        return f'{self.id }'



class Roi(models.Model):
    id = models.CharField(primary_key = True, max_length = 150, unique = True, help_text = 'codigo de indentificação do ativo')
    symbol = models.CharField(max_length = 14, help_text = "Simbolo do cripto ativo")
    name = models.CharField(max_length = 14, help_text = "Nome do cripto ativo")
    slug = models.SlugField()
    current_price = models.FloatField( help_text = 'Valor do Ativo',default = 0, blank = True, null = True)
    market_cap = models.FloatField( help_text = 'valor de mercado', default = 0, blank = True, null = True)
    data = models.DateTimeField( auto_now_add = 'True', help_text = 'A data historica')


class Historico(models.Model):
    id = models.CharField(primary_key = True, max_length = 150, unique = False, help_text = 'codigo de indentificação do ativo')
    symbol = models.CharField(max_length = 14, help_text = "Simbolo do cripto ativo")
    name = models.CharField(max_length = 14, help_text = "Nome do cripto ativo")
    slug = models.SlugField()
    current_price = models.FloatField( help_text = 'Valor do Ativo',default = 0, blank = True, null = True)
    market_cap = models.FloatField( help_text = 'valor de mercado', default = 0, blank = True, null = True)
    total_volume = models.FloatField( help_text = 'volume', default = 0, blank = True, null = True)
    data = models.DateTimeField( auto_now_add = False , help_text = 'A data historicas')
    facebook_likes = models.FloatField( help_text = 'Likes dno facebook', default = 0, blank = True, null = True)
    twitter_followers = models.FloatField( help_text = ' followrs tiwtter', default = 0, blank = True, null = True)
    reddit_average_posts_48h = models.FloatField( help_text = 'reddit average post em 48', default = 0, blank = True, null = True)
    reddit_average_comments_48h = models.FloatField( help_text = 'reddit average comentario em 48', default = 0, blank = True, null = True)
    reddit_subscribers = models.FloatField( help_text = 'inscrito na comunidade', default = 0, blank = True, null = True)
    reddit_accounts_active_48h = models.FloatField( help_text = 'contas ativas', default = 0, blank = True, null = True)
    forks = models.IntegerField(help_text = 'copia de sistema', blank = True, default = 0, null = True)
    stars = models.IntegerField(help_text = 'estrelas', blank = True, default = 0, null = True)
    subscribers = models.IntegerField(help_text = 'assinantes', blank = True, default = 0, null = True)
    total_issues = models.IntegerField(help_text = 'questões totais', blank = True, default = 0, null = True)
    closed_issues = models.IntegerField(help_text = 'questões encerradas"', blank = True, default = 0, null = True)
    pull_requests_merged = models.IntegerField(help_text = 'solicitações pull mescladas', blank = True, default = 0, null = True)
    pull_request_contributors = models.IntegerField(help_text = 'solicitação dos contribuidores', blank = True, default = 0, null = True)
    views = models.IntegerField(help_text = 'Quantidade de atualização diaria ', default = 0, null = True)
    


    class Meta:
         ordering = ['-data']
         verbose_name = 'Historico'
         verbose_name_plural = 'Históricos'  


    def __str__(self):
        return f'{self.name}'

  
    

class Investimento(models.Model):

    id = models.CharField(max_length = 150, primary_key = True, unique = True, help_text = 'Código do investimento')
    investidor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'user_investimento',  on_delete = models.CASCADE)        
    crypto = models.ForeignKey(Cripto, related_name = 'crypto', on_delete = models.CASCADE, help_text = "A moeda do investimento")
    deposito = models.IntegerField( default = 0, help_text = 'Quantidade de deposito', blank = True, null = True)
    retirada = models.IntegerField( default = 0, help_text = 'Quantidade de retirada', blank = True, null = True)
    preco = models.FloatField( default = 0, help_text = 'O preço pago por unidade', blank = True, null = True)
    quantidade = models.FloatField(  default = 0, help_text = 'Quantidade de moeda', blank = True, null = True)
    media = models.FloatField(  default = 0, help_text = 'Media do valor pago', blank = True, null = True)
    retorno = models.FloatField( default = 0, help_text = 'O valor do retorno', blank = True, null = True)    
    taxa_retorno = models.FloatField( default = 0, help_text = 'O valor da porcentagem do investimento', blank = True, null = True) 
    rating = models.IntegerField( validators = [MinValueValidator(0), MaxValueValidator(100)], blank = True, null = True)
    inicio =  models.DateTimeField(auto_now_add = True, help_text = 'A data do inicio do investimento' )
    final = models.DateTimeField( auto_now_add = False,  help_text = 'A data final do investimento', blank = True, null = True)
    duracao_total = models.DurationField( default=timedelta(seconds=0), blank = True, null = True )
    total = models.FloatField( default = 0, help_text = 'O valor total do investimento', blank = True, null = True) 


    class Meta:
         ordering = ['-inicio']
         verbose_name = 'Investimento'
         verbose_name_plural = 'Investimentos'  


    def __str__(self):
        return f'{self.investidor}'



class Movimentacao(models.Model):


    STATUS_CHOICES = (

        ('ótimo','Ótimo'),
        ('bom', 'Bom'),
        ('regular','Regular'),
        ('péssimo','Péssimo'),

        )

    STATUS_TYPE = (

        ('deposito','Deposito'),
        ('retirada','Retirada')
        )

    id = models.CharField(max_length = 150, primary_key = True, unique = True, help_text = 'Código do retorno movimentação')
    investidor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'user_aporte',  on_delete = models.CASCADE)
    investimento = models.ForeignKey(Investimento, related_name = 'aporte_movimentação', on_delete = models.CASCADE )
    crypto = models.ForeignKey(Cripto, related_name = 'aporte_crypto', on_delete = models.CASCADE, help_text = "A moeda do investimento")
    exchange = models.ForeignKey(Exchange, related_name = 'aporte_blockchain', on_delete = models.CASCADE)
    tipo = models.CharField(max_length = 90, choices = STATUS_CHOICES, default = 'bom', help_text = 'Status da movimentação')
    status = models.CharField(max_length = 90, choices = STATUS_TYPE, default = 'deposito', help_text = 'O tipo de movimentação')
    data =  models.DateTimeField(auto_now_add = False,  help_text = 'A data do valor do retorno' )
    valor = models.FloatField( default = 0, help_text = 'O valor do movimentação')       
    quantidade = models.FloatField( default = 0,  help_text = 'Quantidade de moeda')
    preco = models.FloatField( default = 0, help_text = 'O preço pago por unidade')
    retorno = models.FloatField( default = 0, help_text = 'O valor do retorno')
    porcentagem = models.FloatField( default = 0, help_text = 'Porcetagem do investimento')
    total = models.FloatField(  default = 0, help_text = 'O valor total do retorno do movimentação') 
    saldo = models.FloatField(  default = 0, help_text = 'Saldo do retorno do movimentação') 


    def __str__(self):
        return f'{self.investidor}'


    class Meta:
        ordering = ['-data']
        verbose_name = 'Movimentação'
        verbose_name_plural = 'Movimentações'





  