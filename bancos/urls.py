from django.urls import path
from . import views




app_name = 'bancos'




urlpatterns = [


	path('bancos/finanças/pessoal/cartao/',views.Cartao_Template_View.as_view(), name = 'cartao'),
	path('bancos/finanças/pessoal/cartao/<int:pk>/details/',views.Cartao_Details_View.as_view(), name = 'details'),
	path('bancos/finanças/pessoal/cartao/create/',views.Cartao_Create_View.as_view(), name = 'create'),



]