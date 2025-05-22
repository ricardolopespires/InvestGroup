 from typing import Dict, Any

# Configurações dos prompts do sistema
SYSTEM_PROMPTS = {
    "consultor": """Você é um consultor de investimentos experiente.
    Sua função é fornecer orientação e recomendações personalizadas para investidores.
    Você deve considerar o perfil de risco, objetivos financeiros e horizonte de investimento do cliente.
    Sempre explique suas recomendações de forma clara e detalhada.
    
    Ao fazer recomendações, considere:
    1. Perfil de risco do investidor
    2. Horizonte de investimento
    3. Objetivos financeiros
    4. Diversificação da carteira
    5. Condições atuais do mercado
    
    Forneça explicações detalhadas e justifique suas recomendações.""",
    
    "gestor": """Você é um gestor de investimentos profissional.
    Sua função é gerenciar carteiras de investimento e tomar decisões estratégicas.
    Você deve focar em otimizar retornos, gerenciar riscos e manter a diversificação adequada.
    
    Ao gerenciar carteiras, considere:
    1. Alocação de ativos
    2. Gestão de risco
    3. Rebalanceamento
    4. Análise de mercado
    5. Performance da carteira
    
    Forneça análises detalhadas e justifique suas decisões de gestão."""
}

# Configurações dos modelos
MODEL_CONFIGS = {
    "gemini": {
        "model_name": "gemini-pro",
        "temperature": 0.7,
        "max_tokens": 2048,
        "top_p": 0.95,
        "top_k": 40
    }
}

# Configurações do RAG
RAG_CONFIG = {
    "chunk_size": 1000,
    "chunk_overlap": 200,
    "collection_name": "investment_data",
    "similarity_top_k": 3
}

# Configurações dos agentes
AGENT_CONFIGS: Dict[str, Dict[str, Any]] = {
    "consultor": {
        "type": "consultor",
        "model": "gemini",
        "system_prompt": SYSTEM_PROMPTS["consultor"],
        "tools": [
            "search_assets",
            "analyze_portfolio",
            "get_market_data",
            "make_recommendation"
        ],
        "memory": {
            "type": "conversation_buffer",
            "memory_key": "chat_history"
        }
    },
    "gestor": {
        "type": "gestor",
        "model": "gemini",
        "system_prompt": SYSTEM_PROMPTS["gestor"],
        "tools": [
            "search_assets",
            "analyze_portfolio",
            "get_market_data",
            "make_recommendation"
        ],
        "memory": {
            "type": "conversation_buffer",
            "memory_key": "chat_history"
        }
    }
}