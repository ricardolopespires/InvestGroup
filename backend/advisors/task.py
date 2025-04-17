from celery import shared_task
import logging
from ..tasks.trading_task import TradingTask
from ..signals.signals import Signals
from ..managers.portfolio_manager import GerenciadorPortfolio
from ..managers.risk_manager import GerenciadorRisco
from ..connectors.mt5_connector import ConectorMT5
import os

logger = logging.getLogger(__name__)

@shared_task
def monitorar_mercado():
    conector_mt5 = ConectorMT5(
        conta=int(os.getenv('MT5_ACCOUNT')),
        senha=os.getenv('MT5_PASSWORD'),
        servidor=os.getenv('MT5_SERVER')
    )
    if not conector_mt5.conectar():
        logger.critical("Falha ao conectar ao MT5")
        return
    
    portfolio = GerenciadorPortfolio(conector_mt5, risco_por_operacao=0.02, pontos_breakeven=200, risco_maximo_total=0.1)
    portfolio.monitorar_mercado()

@shared_task
def executar_tarefa_trading():
    conector_mt5 = ConectorMT5(
        conta=int(os.getenv('MT5_ACCOUNT')),
        senha=os.getenv('MT5_PASSWORD'),
        servidor=os.getenv('MT5_SERVER')
    )
    if not conector_mt5.conectar():
        logger.critical("Falha ao conectar ao MT5")
        return
    
    portfolio = GerenciadorPortfolio(conector_mt5, risco_por_operacao=0.02, pontos_breakeven=200, risco_maximo_total=0.1)
    gerenciador_risco = GerenciadorRisco(risco_maximo_percent=0.02, tamanho_maximo_posicao=0.1, multiplicador_atr=2.0)
    signals = Signals(
        conta=int(os.getenv('MT5_ACCOUNT')),
        senha=os.getenv('MT5_PASSWORD'),
        servidor=os.getenv('MT5_SERVER')
    )
    simbolos = ["EURUSD", "GBPUSD", "USDJPY"]
    
    trader_task = TradingTask(portfolio, gerenciador_risco, signals, simbolos, intervalo_minutos=5)
    result = trader_task.execute()
    logger.info(f"Resultado da tarefa de trading:\n{result}")