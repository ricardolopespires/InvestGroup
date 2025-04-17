import logging
import time
import signal
import sys
import threading
from crewai import Agent, Crew
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from connectors.mt5_connector import ConectorMT5
from managers.portfolio_manager import GerenciadorPortfolio
from managers.risk_manager import GerenciadorRisco
from tasks.trading_task import TradingTask
from signals.signals import Signals

# Configuração do logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler('trading_log_crewai.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Carrega variáveis de ambiente
load_dotenv()

# Configuração do LLM com Google Gemini
api_key = os.getenv("GOOGLE_API_KEY")
model_name = os.getenv("MODEL", "gemini-pro")

default_llm = ChatGoogleGenerativeAI(
    google_api_key=api_key,
    model=model_name
)

# Definindo o agente trader
trader = Agent(
    role="Trader",
    goal=(
        "Realizar operações de compra, venda ou manter posição em ativos financeiros. "
        "Utilize os sinais 'buy' e 'sell' para tomar decisões. "
        "Se a operação atual for diferente do sinal recebido, feche a posição e abra uma nova conforme o sinal. "
        "Caso o sinal seja igual à posição atual, mantenha a operação aberta."
    ),
    tools=[],
    llm=default_llm,
    backstory="Você é um trader experiente, especialista em executar estratégias automatizadas de negociação."
)

# Manipulador de sinal para interrupção segura
def sinal_handler(sig, frame):
    logger.info("Sinal de interrupção recebido, encerrando...")
    global portfolio
    portfolio.ativo = False
    portfolio.conector_mt5.desconectar()
    sys.exit(0)

if __name__ == "__main__":
    # Configura o manipulador de sinal
    signal.signal(signal.SIGINT, sinal_handler)

    # Configurações de conexão com o MT5
    conta = 123456  # Substitua pelo número da sua conta
    senha = "sua_senha"  # Substitua pela sua senha
    servidor = "sua_corretora"  # Substitua pelo servidor da sua corretora

    # Inicializa o conector MT5
    conector_mt5 = ConectorMT5(conta, senha, servidor)
    if not conector_mt5.conectar():
        logger.critical("Falha ao conectar ao MT5, encerrando...")
        sys.exit(1)

    # Inicializa o gerenciador de portfólio e risco
    portfolio = GerenciadorPortfolio(conector_mt5, risco_por_operacao=0.02, pontos_breakeven=200, risco_maximo_total=0.1)
    gerenciador_risco = GerenciadorRisco(risco_maximo_percent=0.02, tamanho_maximo_posicao=0.1, multiplicador_atr=2.0)

    # Inicializa o gerenciador de sinais
    signals = Signals(conta, senha, servidor)

    # Símbolos a serem monitorados
    simbolos = ["EURUSD", "GBPUSD", "USDJPY"]

    # Cria a tarefa de trading
    trader_task = TradingTask(portfolio, gerenciador_risco, signals, simbolos, intervalo_minutos=5)
    trader_task.agent = trader

    # Cria a equipe de execução
    crew = Crew(
        agents=[trader],
        tasks=[trader_task]
    )

    # Inicia o monitoramento em tempo real em uma thread separada
    monitoramento_thread = threading.Thread(target=portfolio.monitorar_mercado, args=(1,))
    monitoramento_thread.daemon = True
    monitoramento_thread.start()

    # Loop principal para executar a tarefa a cada 5 minutos
    logger.info("Iniciando loop principal de execução da tarefa...")
    while portfolio.ativo:
        try:
            resultado = crew.kickoff()
            logger.info(f"Resultado da tarefa:\n{resultado}")
            time.sleep(5 * 60)
        except Exception as e:
            logger.error(f"Erro durante execução da tarefa: {str(e)}")
            if not portfolio.conector_mt5.reconectar():
                logger.critical("Falha crítica de conexão, encerrando...")
                portfolio.ativo = False
        except KeyboardInterrupt:
            logger.info("Interrupção recebida, encerrando...")
            portfolio.ativo = False

    # Desconecta ao encerrar
    portfolio.conector_mt5.desconectar()