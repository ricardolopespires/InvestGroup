import os
from typing import List, Dict, Any
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools import Tool
from langchain.memory import ConversationBufferMemory
from langchain.embeddings import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader
from django.conf import settings
from .models import Asset, Portfolio, InvestmentAgent, Transaction, AdvisorRecommendation

# Carrega variáveis de ambiente
load_dotenv()

class InvestmentAgentBase:
    def __init__(self, agent_config: Dict[str, Any]):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-pro",
            temperature=0.7,
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )
        self.embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001",
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        self.agent_config = agent_config
        self.setup_vector_store()
        self.setup_tools()
        self.setup_agent()

    def setup_vector_store(self):
        """Configura o armazenamento vetorial para RAG"""
        # Carrega dados do banco de dados
        assets = Asset.objects.all()
        portfolios = Portfolio.objects.all()
        
        # Converte dados em texto para indexação
        documents = []
        for asset in assets:
            documents.append(f"Ativo: {asset.name} ({asset.ticker})\nTipo: {asset.asset_type}\nPreço: {asset.price}\nVolatilidade: {asset.volatility}")
        
        for portfolio in portfolios:
            documents.append(f"Portfólio: {portfolio.name}\nValor Total: {portfolio.total_value}\nPerfil de Risco: {portfolio.risk_profile.risk_level}")

        # Divide os documentos em chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        texts = text_splitter.split_text("\n".join(documents))

        # Cria o vector store
        self.vector_store = Chroma.from_texts(
            texts=texts,
            embedding=self.embeddings,
            collection_name="investment_data"
        )

    def setup_tools(self):
        """Configura as ferramentas disponíveis para o agente"""
        self.tools = [
            Tool(
                name="search_assets",
                func=self.search_assets,
                description="Busca informações sobre ativos financeiros"
            ),
            Tool(
                name="analyze_portfolio",
                func=self.analyze_portfolio,
                description="Analisa um portfólio de investimentos"
            ),
            Tool(
                name="get_market_data",
                func=self.get_market_data,
                description="Obtém dados atualizados do mercado"
            ),
            Tool(
                name="make_recommendation",
                func=self.make_recommendation,
                description="Faz recomendações de investimento"
            )
        ]

    def setup_agent(self):
        """Configura o agente com suas ferramentas e prompt"""
        prompt = ChatPromptTemplate.from_messages([
            ("system", self.agent_config.get("system_prompt", "Você é um assistente de investimentos.")),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ])

        self.agent = create_openai_functions_agent(
            llm=self.llm,
            tools=self.tools,
            prompt=prompt
        )

        self.agent_executor = AgentExecutor(
            agent=self.agent,
            tools=self.tools,
            memory=self.memory,
            verbose=True
        )

    def search_assets(self, query: str) -> str:
        """Busca informações sobre ativos usando RAG"""
        docs = self.vector_store.similarity_search(query)
        return "\n".join([doc.page_content for doc in docs])

    def analyze_portfolio(self, portfolio_id: str) -> str:
        """Analisa um portfólio específico"""
        try:
            portfolio = Portfolio.objects.get(id=portfolio_id)
            allocations = portfolio.allocations.all()
            
            analysis = f"Análise do Portfólio {portfolio.name}:\n"
            analysis += f"Valor Total: {portfolio.total_value}\n"
            analysis += f"Perfil de Risco: {portfolio.risk_profile.risk_level}\n\n"
            analysis += "Alocações:\n"
            
            for alloc in allocations:
                analysis += f"- {alloc.asset.name}: {alloc.allocation_percentage*100}%\n"
            
            return analysis
        except Portfolio.DoesNotExist:
            return "Portfólio não encontrado"

    def get_market_data(self, asset_ticker: str) -> str:
        """Obtém dados atualizados do mercado para um ativo"""
        try:
            asset = Asset.objects.get(ticker=asset_ticker)
            return f"Dados do ativo {asset.name} ({asset.ticker}):\nPreço: {asset.price}\nVolatilidade: {asset.volatility}"
        except Asset.DoesNotExist:
            return "Ativo não encontrado"

    def make_recommendation(self, portfolio_id: str) -> str:
        """Faz recomendações de investimento baseadas no portfólio"""
        try:
            portfolio = Portfolio.objects.get(id=portfolio_id)
            risk_profile = portfolio.risk_profile
            
            # Usa o LLM para gerar recomendações baseadas no perfil de risco
            prompt = f"""
            Analise o seguinte portfólio e faça recomendações de investimento:
            Nome: {portfolio.name}
            Valor Total: {portfolio.total_value}
            Perfil de Risco: {risk_profile.risk_level}
            Tolerância a Perdas: {risk_profile.max_loss_tolerance}
            Horizonte de Investimento: {risk_profile.investment_horizon} anos
            """
            
            response = self.llm.invoke(prompt)
            return response.content
        except Portfolio.DoesNotExist:
            return "Portfólio não encontrado"

    def run(self, input_text: str) -> str:
        """Executa o agente com uma entrada específica"""
        return self.agent_executor.invoke({"input": input_text})["output"]

class ConsultantAgent(InvestmentAgentBase):
    def __init__(self):
        super().__init__({
            "system_prompt": """Você é um consultor de investimentos experiente.
            Sua função é fornecer orientação e recomendações personalizadas para investidores.
            Você deve considerar o perfil de risco, objetivos financeiros e horizonte de investimento do cliente.
            Sempre explique suas recomendações de forma clara e detalhada."""
        })

class ManagerAgent(InvestmentAgentBase):
    def __init__(self):
        super().__init__({
            "system_prompt": """Você é um gestor de investimentos profissional.
            Sua função é gerenciar carteiras de investimento e tomar decisões estratégicas.
            Você deve focar em otimizar retornos, gerenciar riscos e manter a diversificação adequada.
            Forneça análises detalhadas e justifique suas decisões de gestão."""
        })

# Função para criar e retornar um agente específico
def create_agent(agent_type: str) -> InvestmentAgentBase:
    if agent_type == "consultor":
        return ConsultantAgent()
    elif agent_type == "gestor":
        return ManagerAgent()
    else:
        raise ValueError(f"Tipo de agente não suportado: {agent_type}")