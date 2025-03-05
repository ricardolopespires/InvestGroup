import AxiosInstance from "@/services/AxiosInstance";
import { parseStringify } from "../utils";
import { UserGetStatus, UserUpdatedStatus } from "./actions.user";

// Interfaces para tipagem
interface PerfilInvestidor {
  id: number;
  minimo: number;
  maximo: number;
  investidor: string[];
}

interface ErrorResponse {
  status: number;
  message: string;
  timestamp?: string;
}

interface PerfilInvestidorProps {
  perfilId: number;
}

interface UpdatedPerfilInvestidorProps {
  perfilId: number;
  data: PerfilInvestidor;
}

interface UpdatePerfilProps {
  value: number;
  userId: string;
}

// Função para buscar todos os perfis
export const listPerfilInvestidor = async (): Promise<PerfilInvestidor[] | ErrorResponse> => {
  try {
    const res = await AxiosInstance.get('/api/v1/analytics/perfil/all/');
    return res.status === 200 
      ? res.data as PerfilInvestidor[]
      : parseStringify({
          status: res.status,
          message: res.data?.message || 'Erro ao buscar perfis',
        });
  } catch (error: any) {
    return parseStringify({
      status: error.response?.status || 500,
      message: error.response?.data?.message || 'Erro na requisição ao servidor',
      timestamp: new Date().toISOString(),
    });
  }
};

// Função para buscar um perfil específico
export const perfilInvestidor = async ({ perfilId }: PerfilInvestidorProps): Promise<PerfilInvestidor[] | ErrorResponse> => {
  try {
    const res = await AxiosInstance.get(`/api/v1/analytics/perfil/${perfilId}/`);
    return res.status === 200
      ? res.data
      : parseStringify({
          status: res.status,
          message: res.data?.message || 'Erro ao buscar perfil',
        });
  } catch (error: any) {
    return parseStringify({
      status: error.response?.status || 500,
      message: error.response?.data?.message || 'Erro na requisição do perfil',
      timestamp: new Date().toISOString(),
    });
  }
};

// Função para atualizar um perfil
export const updatedPerfilInvestidor = async ({ perfilId, data }: UpdatedPerfilInvestidorProps): Promise<PerfilInvestidor | ErrorResponse> => {
  try {
    const res = await AxiosInstance.put(`/api/v1/analytics/perfil/${perfilId}/detail/`, data);
    return res.status === 200
      ? res.data
      : parseStringify({
          status: res.status,
          message: res.data?.message || 'Erro ao atualizar perfil',
        });
  } catch (error: any) {
    return parseStringify({
      status: error.response?.status || 500,
      message: error.response?.data?.message || 'Erro na atualização do perfil',
      timestamp: new Date().toISOString(),
    });
  }
};

// Função para encontrar ID do perfil baseado no valor
export const encontrarPerfilId = async ({ valor }: { valor: number }): Promise<number | null | ErrorResponse> => {
  try {
    const perfisResponse = await listPerfilInvestidor();

    if ('status' in perfisResponse) {
      return perfisResponse;
    }

    const perfis = perfisResponse as PerfilInvestidor[];
    const perfil = perfis.find(p => valor >= p.minimo && valor <= p.maximo);
    
    return perfil?.id ?? null;
  } catch (error: any) {
    return parseStringify({
      status: 500,
      message: 'Erro ao processar busca de perfil',
      timestamp: new Date().toISOString(),
    });
  }
};

// Função principal de atualização de perfil
export const updatePerfil = async ({ value, userId }: UpdatePerfilProps): Promise<{
  status: 'success' | 'error';
  data?: any;
  message?: string;
  timestamp?: string;
}> => {
  try {
    // Validação dos parâmetros
    if (!value || !userId) {
      throw new Error('Value e userId são obrigatórios');
    }

    // Busca e validação do perfil
    const perfilId = await encontrarPerfilId({ valor: value });
    if (!perfilId || typeof perfilId !== 'number') {
      throw new Error('Perfil não encontrado ou inválido');
    }

    // Busca dos dados do investidor
    const investorData = await perfilInvestidor({ perfilId });
    if (!Array.isArray(investorData) || !investorData.length) {
      throw new Error('Dados do investidor não encontrados');
    }

    // Atualização imutável dos dados
    const updatedInvestorData: PerfilInvestidor = {
      ...investorData[0],
      investidor: [...new Set([...investorData[0].investidor, userId])] // Remove duplicatas
    };

    // Atualização do perfil
    const perfilResponse = await updatedPerfilInvestidor({ 
      perfilId, 
      data: updatedInvestorData 
    });

    if ('status' in perfilResponse) {
      throw new Error(perfilResponse.message);
    }

    // Atualização do status do usuário
    const userData = await UserGetStatus({ userId: userId });
    console.log(userData);

    if (!Array.isArray(userData) || !userData.length) {
      throw new Error('Usuário não encontrado');
    }

    const updatedUserStatus = {
      ...userData[0],
      perfil: true
    };
    

    const userResponse = await UserUpdatedStatus({ 
      userId: userId, 
      data: updatedUserStatus
    });

    console.log(userResponse.status);

    if (userResponse.status !== 200) {
      throw new Error(userResponse.data?.message || 'Erro ao atualizar status do usuário');
    }

    return parseStringify({
      status: 200,
      data: userResponse.data,
      timestamp: new Date().toISOString()
    });

  } catch (error: any) {
    const errorMessage = error.message || 'Erro desconhecido na atualização do perfil';
    console.error(`Erro em updatePerfil: ${errorMessage}`, {
      value,
      userId,
      stack: error.stack
    });

    return {
      status: 'error',
      message: errorMessage,
      timestamp: new Date().toISOString()
    };
  }
};