from crewai import Agent, Task, Crew
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai_tools import ScrapeWebsiteTool  # Caso precise futuramente
from dotenv import load_dotenv
import os

# Carrega variáveis de ambiente do .env
load_dotenv()

# Configuração do LLM com Google Gemini (via langchain-google-genai)
api_key = os.getenv("GOOGLE_API_KEY")  # Certifique-se de ter essa chave no seu .env
model_name = os.getenv("MODEL", "gemini-pro")  # 'gemini-pro' é o modelo mais comum

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
    tools=[],  # Nenhuma ferramenta usada neste exemplo
    llm=default_llm,
    backstory="Você é um trader experiente, especialista em executar estratégias automatizadas de negociação."
)

# Definindo a tarefa do trader
trader_task = Task(
    description="Monitore a operação a cada 5 minutos e tome decisões com base no sinal de mercado ('buy' ou 'sell').",
    expected_output="Executar ou manter operações de acordo com os sinais.",
    agent=trader
)

# Criando a equipe de execução
crew = Crew(
    agents=[trader],
    tasks=[trader_task]
)

# (Opcional) Executar a crew
# result = crew.run()
# print(result)
