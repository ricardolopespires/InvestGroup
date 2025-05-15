import os
from django.db.models import Sum
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain.prompts import ChatPromptTemplate
from langchain.tools import tool
from .models import Asset, Investidor, InvestorProfile, InvestmentOperation, RiskAssessment
from django.contrib.auth import get_user_model

User = get_user_model()

class InvestmentAgent:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("GOOGLE_API_KEY não configurada")
        self.llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", api_key=self.api_key)
        self.prompt_template = ChatPromptTemplate.from_messages([
            ("system", "Você é um assistente financeiro especializado em gestão de risco e investimentos. "
                       "Use os dados fornecidos para responder perguntas ou realizar análises. "
                       "Forneça respostas claras, concisas e em português. "
                       "Se necessário, use os dados dos modelos Django para cálculos ou consultas."),
            ("human", "{input}"),
            ("assistant", "{output}")
        ])

    def _create_agent(self, tools):
        agent = create_tool_calling_agent(self.llm, tools, self.prompt_template)
        return AgentExecutor(agent=agent, tools=tools, verbose=True)


class InvestorProfileAnalysisAgent(InvestmentAgent):
    @tool
    def get_investidor_profile_data(self, username: str) -> dict:
        """Retorna os dados financeiros e de perfil de um investidor pelo username."""
        try:
            investidor = Investidor.objects.select_related('usuario', 'investor_profile').get(usuario__username=username)
            return {
                "username": investidor.usuario.username,
                "renda_mensal": float(investidor.renda_mensal),
                "despesas_mensais": float(investidor.despesas_mensais),
                "dividas": float(investidor.dividas),
                "investimentos": float(investidor.investimentos),
                "reserva_emergencia": float(investidor.reserva_emergencia),
                "tolerancia_risco": investidor.get_tolerancia_risco_display(),
                "horizonte_tempo": investidor.get_horizonte_tempo_display(),
                "objetivo": investidor.get_objetivo_display(),
                "saude_financeira": investidor.calcular_saude_financeira(),
                "perfil_risco": investidor.investor_profile.risk_tolerance if investidor.investor_profile else "N/A",
                "max_exposure": float(investidor.investor_profile.max_exposure) if investidor.investor_profile else 0,
                "fixed_income_allocation": investidor.investor_profile.fixed_income_allocation if investidor.investor_profile else 0,
                "variable_income_allocation": investidor.investor_profile.variable_income_allocation if investidor.investor_profile else 0
            }
        except Investidor.DoesNotExist:
            return {"error": "Investidor não encontrado"}

    @tool
    def get_available_asset_types(self) -> list:
        """Retorna os tipos de ativos disponíveis no sistema."""
        return [choice[1] for choice in Asset._meta.get_field('asset_type').choices]

    def __init__(self, api_key=None):
        super().__init__(api_key)
        tools = [self.get_investidor_profile_data, self.get_available_asset_types]
        self.agent_executor = self._create_agent(tools)

    def analyze_investor_profile(self, username: str):
        """Analisa o perfil do investidor e fornece recomendações."""
        prompt = (
            f"Analise o perfil do investidor com username '{username}'. "
            "Considere os dados financeiros (renda mensal, despesas, dívidas, investimentos, reserva de emergência), "
            "saúde financeira, tolerância ao risco, horizonte de tempo e objetivo. "
            "Valide se o perfil de risco atual ({'Conservador, Moderado ou Agressivo'}) é adequado ou sugira ajustes. "
            "Recomende uma alocação de ativos ideal entre os tipos disponíveis (Ação, Commodities, Criptomoedas, Currency/Forex, Index, Título, Fundo, ETF), "
            "explicando como cada tipo se alinha com o perfil do investidor. Forneça a resposta em português."
        )
        return self.agent_executor.invoke({"input": prompt})["output"]


class PortfolioAnalysisAgent(InvestmentAgent):
    @tool
    def get_investidor_data(self, username: str) -> dict:
        """Retorna os dados financeiros e de perfil de um investidor pelo username."""
        try:
            investidor = Investidor.objects.select_related('usuario', 'investor_profile').get(usuario__username=username)
            return {
                "username": investidor.usuario.username,
                "renda_mensal": float(investidor.renda_mensal),
                "despesas_mensais": float(investidor.despesas_mensais),
                "dividas": float(investidor.dividas),
                "investimentos": float(investidor.investimentos),
                "reserva_emergencia": float(investidor.reserva_emergencia),
                "saude_financeira": investidor.calcular_saude_financeira(),
                "perfil_risco": investidor.investor_profile.risk_tolerance if investidor.investor_profile else "N/A",
                "max_exposure": float(investidor.investor_profile.max_exposure) if investidor.investor_profile else 0,
                "fixed_income_allocation": investidor.investor_profile.fixed_income_allocation if investidor.investor_profile else 0,
                "variable_income_allocation": investidor.investor_profile.variable_income_allocation if investidor.investor_profile else 0
            }
        except Investidor.DoesNotExist:
            return {"error": "Investidor não encontrado"}

    @tool
    def get_portfolio_summary(self, username: str) -> dict:
        """Retorna um resumo do portfólio de um investidor pelo username."""
        try:
            operations = InvestmentOperation.objects.filter(investidor__usuario__username=username).select_related('asset')
            total_value = operations.aggregate(total=Sum('total_value'))['total'] or 0
            asset_types = operations.values('asset__asset_type').annotate(total=Sum('total_value'))
            return {
                "username": username,
                "total_value": float(total_value),
                "asset_allocation": [
                    {"asset_type": item['asset__asset_type'], "total_value": float(item['total'])}
                    for item in asset_types
                ]
            }
        except Exception as e:
            return {"error": str(e)}

    def __init__(self, api_key=None):
        super().__init__(api_key)
        tools = [self.get_investidor_data, self.get_portfolio_summary]
        self.agent_executor = self._create_agent(tools)

    def analyze_portfolio(self, username: str):
        """Analisa o portfólio do investidor e sugere alocações."""
        prompt = (
            f"Analise o portfólio do investidor com username '{username}'. "
            "Use os dados financeiros e de perfil para sugerir uma alocação de ativos ideal, "
            "considerando os tipos de ativos disponíveis (Ação, Commodities, Criptomoedas, Currency/Forex, Index, Título, Fundo, ETF). "
            "Forneça uma explicação detalhada e recomendações específicas em português."
        )
        return self.agent_executor.invoke({"input": prompt})["output"]


class RiskAssessmentAgent(InvestmentAgent):
    @tool
    def get_operation_risks(self, operation_id: str) -> dict:
        """Retorna os riscos associados a uma operação de investimento pelo ID."""
        try:
            operation = InvestmentOperation.objects.select_related('asset', 'investidor').get(id=operation_id)
            risks = RiskAssessment.objects.filter(operation=operation)
            return {
                "operation_id": str(operation.id),
                "asset": operation.asset.ticker,
                "asset_type": operation.asset.get_asset_type_display(),
                "volatility": float(operation.asset.volatility),
                "risk_score": float(operation.risk_score),
                "risks": [
                    {
                        "risk_type": risk.get_risk_type_display(),
                        "risk_level": risk.get_risk_level_display(),
                        "description": risk.description,
                        "mitigation_strategy": risk.mitigation_strategy
                    }
                    for risk in risks
                ]
            }
        except InvestmentOperation.DoesNotExist:
            return {"error": "Operação não encontrada"}

    def __init__(self, api_key=None):
        super().__init__(api_key)
        tools = [self.get_operation_risks]
        self.agent_executor = self._create_agent(tools)

    def assess_operation_risk(self, operation_id: str):
        """Avalia os riscos de uma operação específica e sugere estratégias de mitigação."""
        prompt = (
            f"Avalie os riscos da operação de investimento com ID '{operation_id}'. "
            "Considere o tipo de ativo (Ação, Commodities, Criptomoedas, Currency/Forex, Index, Título, Fundo, ETF), "
            "a volatilidade e os riscos associados. Forneça uma análise detalhada e sugira estratégias de mitigação em português."
        )
        return self.agent_executor.invoke({"input": prompt})["output"]


class QueryAgent(InvestmentAgent):
    @tool
    def query_investidor(self, username: str) -> dict:
        """Consulta informações detalhadas de um investidor pelo username."""
        try:
            investidor = Investidor.objects.select_related('usuario', 'investor_profile').get(usuario__username=username)
            operations = InvestmentOperation.objects.filter(investidor=investidor).select_related('asset')
            return {
                "username": investidor.usuario.username,
                "saude_financeira": investidor.calcular_saude_financeira(),
                "perfil_risco": investidor.investor_profile.risk_tolerance if investidor.investor_profile else "N/A",
                "operations": [
                    {
                        "asset": op.asset.ticker,
                        "asset_type": op.asset.get_asset_type_display(),
                        "total_value": float(op.total_value),
                        "risk_score": float(op.risk_score)
                    }
                    for op in operations
                ]
            }
        except Investidor.DoesNotExist:
            return {"error": "Investidor não encontrado"}

    @tool
    def query_assets_by_type(self, asset_type: str) -> list:
        """Consulta ativos por tipo (ex.: CRYPTO, STOCK, CURRENCY)."""
        valid_types = [choice[0] for choice in Asset._meta.get_field('asset_type').choices]
        if asset_type not in valid_types:
            return {"error": f"Tipo de ativo inválido. Tipos válidos: {', '.join(valid_types)}"}
        assets = Asset.objects.filter(asset_type=asset_type)
        return [
            {
                "ticker": asset.ticker,
                "name": asset.name,
                "volatility": float(asset.volatility),
                "currency": asset.currency
            }
            for asset in assets
        ]

    def __init__(self, api_key=None):
        super().__init__(api_key)
        tools = [self.query_investidor, self.query_assets_by_type]
        self.agent_executor = self._create_agent(tools)

    def answer_query(self, query: str):
        """Responde a uma pergunta em linguagem natural sobre os dados de investimento."""
        return self.agent_executor.invoke({"input": query})["output"]