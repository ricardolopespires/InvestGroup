 from typing import Dict, Any, Optional
from .ai_agents import InvestmentAgentBase, ConsultantAgent, ManagerAgent
from .agent_config import AGENT_CONFIGS
from .agent_tools import TOOLS
from .models import InvestmentAgent
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

class AgentManager:
    _instance = None
    _agents: Dict[str, InvestmentAgentBase] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AgentManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self._load_agents()

    def _load_agents(self):
        """Carrega os agentes do banco de dados"""
        try:
            agents = InvestmentAgent.objects.filter(is_active=True)
            for agent in agents:
                self._create_agent(agent)
        except Exception as e:
            print(f"Erro ao carregar agentes: {str(e)}")

    def _create_agent(self, agent_model: InvestmentAgent) -> Optional[InvestmentAgentBase]:
        """Cria um novo agente baseado no modelo do banco de dados"""
        try:
            agent_type = agent_model.specialty
            if agent_type not in AGENT_CONFIGS:
                print(f"Tipo de agente não suportado: {agent_type}")
                return None

            if agent_type == "consultor":
                agent = ConsultantAgent()
            elif agent_type == "gestor":
                agent = ManagerAgent()
            else:
                print(f"Tipo de agente não implementado: {agent_type}")
                return None

            self._agents[str(agent_model.id)] = agent
            return agent
        except Exception as e:
            print(f"Erro ao criar agente: {str(e)}")
            return None

    def get_agent(self, agent_id: str) -> Optional[InvestmentAgentBase]:
        """Obtém um agente específico"""
        if agent_id not in self._agents:
            try:
                agent_model = InvestmentAgent.objects.get(id=agent_id)
                return self._create_agent(agent_model)
            except InvestmentAgent.DoesNotExist:
                return None
        return self._agents[agent_id]

    def create_agent(self, agent_data: Dict[str, Any]) -> Optional[InvestmentAgentBase]:
        """Cria um novo agente"""
        try:
            agent_model = InvestmentAgent.objects.create(**agent_data)
            return self._create_agent(agent_model)
        except Exception as e:
            print(f"Erro ao criar agente: {str(e)}")
            return None

    def update_agent(self, agent_id: str, agent_data: Dict[str, Any]) -> Optional[InvestmentAgentBase]:
        """Atualiza um agente existente"""
        try:
            agent_model = InvestmentAgent.objects.get(id=agent_id)
            for key, value in agent_data.items():
                setattr(agent_model, key, value)
            agent_model.save()
            
            # Recria o agente com as novas configurações
            if agent_id in self._agents:
                del self._agents[agent_id]
            return self._create_agent(agent_model)
        except InvestmentAgent.DoesNotExist:
            return None
        except Exception as e:
            print(f"Erro ao atualizar agente: {str(e)}")
            return None

    def delete_agent(self, agent_id: str) -> bool:
        """Remove um agente"""
        try:
            if agent_id in self._agents:
                del self._agents[agent_id]
            agent_model = InvestmentAgent.objects.get(id=agent_id)
            agent_model.delete()
            return True
        except InvestmentAgent.DoesNotExist:
            return False
        except Exception as e:
            print(f"Erro ao deletar agente: {str(e)}")
            return False

    def list_agents(self) -> Dict[str, Any]:
        """Lista todos os agentes disponíveis"""
        return {
            agent_id: {
                "type": agent.__class__.__name__,
                "config": agent.agent_config
            }
            for agent_id, agent in self._agents.items()
        }

# Singleton instance
agent_manager = AgentManager()