from django.urls import path
from . import views
from . import historicos


app_name = 'crypto'



urlpatterns = [


			path('manager/list/', views.Manager_Crypto_View.as_view(), name = 'manager'),
			path('<cripto_id>/<name_id>/detail',views.Crypto_Detail_View.as_view(), name = 'detail'),

			#------------------------------------- Tendências -----------------------------------------------------
			path('crypto/tendencias/',views.Moedas_Tendencia_View.as_view(), name = 'tendencias'),

			#------------------------------------- Meus Investimento -------------------------------------------------

			path('meus/investimento/',views.Meus_Investimento_View.as_view(), name = 'investimento'),
			path('meus/investimento/<cripto_id>/<cripto_name>/detail/',views.Detail_Investimento_View.as_view(), name = 'investimento_detail'),
			path('created/investimento/',views.Created_Investimento_View.as_view(), name = 'created'),
			path('aporte/investimento/<investimento_id>/cripto/',views.Movimentacao_Cripto_View.as_view(), name = 'aporte'),
			
			#------------------------------------- Analise Fundamentalista --------------------------------------------------------
			
			path('analytics/fundamentralista/',views.Analise_Fundamentalista_View.as_view(), name = 'fundamentalista'),


			#------------------------------------- Analise Têcnica  --------------------------------------------------------

			path('analytics/tecnica/', views.Analise_Tecnica_View.as_view(), name = 'tecnica'),
			path('analytics/tecnica/<cripto_id>/<name_id>/detail',views.Detail_Analise_Tecnica_View.as_view(), name = 'analise_tecnica_detail'),
			path('analytics/tecnica/dados/historicos', historicos.dados, name = 'dados_tecnicos_historicos'),

			#------------------------------------- Trading Manual de Crypto   --------------------------------------------------------

			path('trading/manual/plataformas/',views.Trading_Manual_Cripto_Plataforma_View.as_view(), name = 'trading_manual'),

			#------------------------------------- Trading Automatico de Crypto   --------------------------------------------------------

			path('trading/automatico/exchanges/',views.Trading_Automatic_Cripto_View.as_view(), name = 'trading_automatico' ),
			path('trading/automatica/exchange/<exchange_id>/detail/', views.Trading_Automatic_Cripto_Plataform_View.as_view(), name = 'trading_plataforma_automatico_detail'),
			path('trading/automatica/exchange/<exchange_id>/bots/', views.Trading_Automatic_Robos_View.as_view(), name = 'trading_bots_automiatico'),
			path('trading/automatico/operation/<exchange_id>/',views.Trading_Automatic_View.as_view(), name = 'trading_automatico_operation' ),
			path('trading/automatico/history/',views.Trading_Automatic_history_View.as_view(), name = 'history'),

			]


			