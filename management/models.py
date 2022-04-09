from django.core.files import File
from PIL import Image, ImageDraw
from django.conf import settings
from django.db import models
from io import BytesIO
import qrcode

# Create your models here.






class API(models.Model):


	STATUS_CHOICES = (

		('gratis','Gratis'),
		('paga','Paga'),

		)

	id = models.CharField(max_length = 150, primary_key = True, unique = True, help_text = 'codigo identificador da apis na plataforma')
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'api_usuario',  on_delete = models.CASCADE)
	nome = models.CharField( max_length = 150, unique = True, help_text = 'Nome da plataforma da api')
	descricao = models.TextField(help_text = 'Descricao da plataforma da api')
	status = models.CharField( max_length = 9 , choices = STATUS_CHOICES, default = 'gratis', help_text = 'Status da api')
	image = models.ImageField(upload_to = 'api')
	created = models.DateTimeField(auto_now_add = True, help_text = 'Data da criação da api')
	api_key = models.CharField(max_length = 400, unique = True, help_text = 'Chave de acesso da apis do usuário' ,)
	secret_key = models.CharField(max_length = 400, unique = True, help_text = 'Chave secreta de acesso da api do usuário')
	qr_code = models.ImageField(upload_to = 'Veiculo/qr_code', blank = True, help_text='QR code de autorização do veiculo')
	is_active = models.BooleanField('Está ativo?', blank=True, default = False)

	class Meta:
		ordering = ['nome']
		verbose_name = 'API'
		verbose_name_plural = 'APIs'



	def save(self, *args, **kwargs):
		qrcode_img = qrcode.make(self.secret_key)
		canvas = Image.new('RGB',(290, 290), 'white')
		draw = ImageDraw.Draw(canvas)
		canvas.paste(qrcode_img)
		fsecret_key = f'qr_code-{self.secret_key}'+'.png'
		buffer = BytesIO()
		canvas.save(buffer, 'PNG')
		self.qr_code.save(fsecret_key, File(buffer), save = False)
		canvas.close()
		super().save(*args, **kwargs)


	def __str__(self):
		return f'{self.nome}'