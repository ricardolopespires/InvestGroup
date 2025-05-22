 from typing import List, Dict, Any
from langchain.tools import BaseTool
from .models import Asset, Portfolio, PortfolioAllocation, Transaction, AdvisorRecommendation
from datetime import datetime, timedelta

class AssetSearchTool(BaseTool):
    name = "search_assets"
    description = "Busca informações sobre ativos financeiros"

    def _run(self, query: str) -> str:
        try:
            assets = Asset.objects.filter(
                name__icontains=query
            ) | Asset.objects.filter(
                ticker__icontains=query
            )
            
            if not assets.exists():
                return "Nenhum ativo encontrado com os critérios especificados."
            
            result = "Ativos encontrados:\n\n"
            for asset in assets:
                result += f"Nome: {asset.name}\n"
                result += f"Ticker: {asset.ticker}\n"
                result += f"Tipo: {asset.asset_type}\n"
                result += f"Preço: {asset.price}\n"
                result += f"Volatilidade: {asset.volatility}\n\n"
            
            return result
        except Exception as e:
            return f"Erro ao buscar ativos: {str(e)}"

class PortfolioAnalysisTool(BaseTool):
    name = "analyze_portfolio"
    description = "Analisa um portfólio de investimentos"

    def _run(self, portfolio_id: str) -> str:
        try:
            portfolio = Portfolio.objects.get(id=portfolio_id)
            allocations = PortfolioAllocation.objects.filter(portfolio=portfolio)
            
            # Análise básica
            analysis = f"Análise do Portfólio {portfolio.name}:\n\n"
            analysis += f"Valor Total: R$ {portfolio.total_value:,.2f}\n"
            analysis += f"Perfil de Risco: {portfolio.risk_profile.risk_level}\n\n"
            
            # Análise de alocação
            analysis += "Alocação de Ativos:\n"
            total_allocation = 0
            for alloc in allocations:
                percentage = alloc.allocation_percentage * 100
                total_allocation += percentage
                analysis += f"- {alloc.asset.name} ({alloc.asset.ticker}): {percentage:.2f}%\n"
            
            # Verificação de diversificação
            if len(allocations) < 3:
                analysis += "\nAlerta: Portfólio pouco diversificado. Considere adicionar mais ativos."
            
            # Verificação de alocação total
            if abs(total_allocation - 100) > 0.01:
                analysis += f"\nAlerta: Alocação total ({total_allocation:.2f}%) diferente de 100%"
            
            return analysis
        except Portfolio.DoesNotExist:
            return "Portfólio não encontrado"
        except Exception as e:
            return f"Erro ao analisar portfólio: {str(e)}"

class MarketDataTool(BaseTool):
    name = "get_market_data"
    description = "Obtém dados atualizados do mercado"

    def _run(self, asset_ticker: str) -> str:
        try:
            asset = Asset.objects.get(ticker=asset_ticker)
            
            # Busca transações recentes
            recent_transactions = Transaction.objects.filter(
                asset=asset,
                executed_at__gte=datetime.now() - timedelta(days=30)
            ).order_by('-executed_at')
            
            result = f"Dados do ativo {asset.name} ({asset.ticker}):\n\n"
            result += f"Preço Atual: R$ {asset.price:,.2f}\n"
            result += f"Volatilidade: {asset.volatility:.2%}\n"
            
            if recent_transactions.exists():
                result += "\nTransações Recentes:\n"
                for trans in recent_transactions[:5]:
                    result += f"- {trans.transaction_type.upper()}: {trans.quantity} @ R$ {trans.price_per_unit:,.2f}\n"
            
            return result
        except Asset.DoesNotExist:
            return "Ativo não encontrado"
        except Exception as e:
            return f"Erro ao obter dados do mercado: {str(e)}"

class RecommendationTool(BaseTool):
    name = "make_recommendation"
    description = "Faz recomendações de investimento"

    def _run(self, portfolio_id: str) -> str:
        try:
            portfolio = Portfolio.objects.get(id=portfolio_id)
            risk_profile = portfolio.risk_profile
            allocations = PortfolioAllocation.objects.filter(portfolio=portfolio)
            
            # Análise do perfil de risco
            risk_level = risk_profile.risk_level
            max_loss = risk_profile.max_loss_tolerance
            horizon = risk_profile.investment_horizon
            
            # Gera recomendações baseadas no perfil
            recommendations = []
            
            if risk_level == "conservador":
                recommendations.extend([
                    "Aumentar exposição a títulos públicos e CDBs",
                    "Considerar fundos imobiliários de baixa volatilidade",
                    "Manter posições em ações blue chips"
                ])
            elif risk_level == "moderado":
                recommendations.extend([
                    "Balancear entre renda fixa e variável",
                    "Considerar ETFs diversificados",
                    "Incluir ações de dividendos"
                ])
            else:  # agressivo
                recommendations.extend([
                    "Aumentar exposição a ações de crescimento",
                    "Considerar pequena exposição a criptomoedas",
                    "Incluir opções de alavancagem"
                ])
            
            # Verifica diversificação
            asset_types = set(alloc.asset.asset_type for alloc in allocations)
            if len(asset_types) < 3:
                recommendations.append("Aumentar diversificação entre diferentes tipos de ativos")
            
            # Monta o resultado
            result = f"Recomendações para o Portfólio {portfolio.name}:\n\n"
            result += f"Perfil de Risco: {risk_level}\n"
            result += f"Tolerância a Perdas: {max_loss:.1%}\n"
            result += f"Horizonte de Investimento: {horizon} anos\n\n"
            result += "Recomendações:\n"
            for i, rec in enumerate(recommendations, 1):
                result += f"{i}. {rec}\n"
            
            return result
        except Portfolio.DoesNotExist:
            return "Portfólio não encontrado"
        except Exception as e:
            return f"Erro ao gerar recomendações: {str(e)}"

# Dicionário de ferramentas disponíveis
TOOLS = {
    "search_assets": AssetSearchTool(),
    "analyze_portfolio": PortfolioAnalysisTool(),
    "get_market_data": MarketDataTool(),
    "make_recommendation": RecommendationTool()
}