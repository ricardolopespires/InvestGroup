import AxiosInstance from "@/services/AxiosInstance";
import { formatNumbers, parseStringify } from "../utils";
import { getUserInfo, UserGetStatus, UserUpdatedStatus } from "./actions.user";
import { get } from "http";

// Interfaces para tipagem
interface PerfilInvestidor {
  id: number;
  minimo: number;
  maximo: number;
  investidor: string[];
}

interface SituationInvestidor {
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
  data: PerfilInvestidor | SituationInvestidor;
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
      : {
          status: res.status,
          message: res.data?.message || 'Erro ao buscar perfis',
        };
  } catch (error: any) {
    return {
      status: error.response?.status || 500,
      message: error.response?.data?.message || 'Erro na requisição ao servidor',
      timestamp: new Date().toISOString(),
    };
  }
};

// Função para buscar um perfil específico
export const perfilInvestidor = async ({ perfilId }: PerfilInvestidorProps): Promise<PerfilInvestidor[] | ErrorResponse> => {
  try {
    const res = await AxiosInstance.get(`/api/v1/analytics/perfil/${perfilId}/`);
    return res.status === 200
      ? res.data as PerfilInvestidor[]
      : {
          status: res.status,
          message: res.data?.message || 'Erro ao buscar perfil',
        };
  } catch (error: any) {
    return {
      status: error.response?.status || 500,
      message: error.response?.data?.message || 'Erro na requisição do perfil',
      timestamp: new Date().toISOString(),
    };
  }
};

// Função para atualizar um perfil
export const updatedPerfilInvestidor = async ({ perfilId, data }: UpdatedPerfilInvestidorProps): Promise<PerfilInvestidor | ErrorResponse> => {
  try {
    const res = await AxiosInstance.put(`/api/v1/analytics/perfil/${perfilId}/detail/`, data);
    return res.status === 200
      ? res.data as PerfilInvestidor
      : {
          status: res.status,
          message: res.data?.message || 'Erro ao atualizar perfil',
        };
  } catch (error: any) {
    return {
      status: error.response?.status || 500,
      message: error.response?.data?.message || 'Erro na atualização do perfil',
      timestamp: new Date().toISOString(),
    };
  }
};

// Função para encontrar ID do perfil baseado no valor
export const SearchPerfilId = async ({ valor }: { valor: number }): Promise<number | ErrorResponse> => {
  try {
    const perfisResponse = await listPerfilInvestidor();

    if ('status' in perfisResponse) {
      return perfisResponse;
    }

    const perfis = perfisResponse as PerfilInvestidor[];
    const perfil = perfis.find(p => valor >= p.minimo && valor <= p.maximo);
    
    return perfil?.id ?? { status: 404, message: 'Perfil não encontrado' };
  } catch (error: any) {
    return {
      status: 500,
      message: 'Erro ao processar busca de perfil',
      timestamp: new Date().toISOString(),
    };
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
    if (!value || !userId) {
      throw new Error('Value e userId são obrigatórios');
    }

    const perfilId = await SearchPerfilId({ valor: value });
  

    const investorData = await perfilInvestidor({ perfilId });
  
    const updatedInvestorData: PerfilInvestidor = {
      ...investorData[0],
      investidor: [...new Set([...investorData[0].investidor, userId])]
    };

    const perfilResponse = await updatedPerfilInvestidor({ 
      perfilId, 
      data: updatedInvestorData 
    });


    const userData = await UserGetStatus({ userId });
    if (!Array.isArray(userData) || !userData.length) {
      throw new Error('Usuário não encontrado');
    }

    const updatedUserStatus = {
      ...userData[0],
      perfil: true
    };

    const userResponse = await UserUpdatedStatus({ 
      userId, 
      data: updatedUserStatus
    });

    if (userResponse.status !== 200) {
      throw new Error(userResponse.data?.message || 'Erro ao atualizar status do usuário');
    }

    return {
      status: 'success',
      data: userResponse.data,
      timestamp: new Date().toISOString()
    };

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



// Função para buscar todos os perfis
export const listSituationInvestidor = async (): Promise<PerfilInvestidor[] | ErrorResponse> => {
  try {
    const res = await AxiosInstance.get('/api/v1/analytics/situacao/all/');
    return res.status === 200 
      ? res.data as PerfilInvestidor[]
      : {
          status: res.status,
          message: res.data?.message || 'Erro ao buscar perfis',
        };
  } catch (error: any) {
    return {
      status: error.response?.status || 500,
      message: error.response?.data?.message || 'Erro na requisição ao servidor',
      timestamp: new Date().toISOString(),
    };
  }
};


// Função para encontrar ID do perfil baseado no valor
export const SearchSituationId = async ({ valor }: { valor: number }): Promise<number | ErrorResponse> => {
  try {
    const perfisResponse = await listSituationInvestidor();

    const perfis = perfisResponse as PerfilInvestidor[];
    const perfil = perfis.find(p => valor >= p.minimo && valor <= p.maximo);
    
    return perfil?.id ?? { status: 404, message: 'Perfil não encontrado' };
  } catch (error: any) {
    return {
      status: 500,
      message: 'Erro ao processar busca de perfil',
      timestamp: new Date().toISOString(),
    };
  }
};

// Função para buscar situação do investidor
export const situationInvestidor = async ({ situationId }: SituationInvestidorProps) => {   
  try {
    const res = await AxiosInstance.get(`/api/v1/analytics/situacao/${situationId}/`); 
    return res.status === 200
      ? res.data as SituationInvestidor[]
      : {
          status: res.status,
          message: res.data?.message || 'Erro ao buscar perfil',
        };
  } catch (error: any) {
    return {
      status: error.response?.status || 500,
      message: error.response?.data?.message || 'Erro na requisição do perfil',
      timestamp: new Date().toISOString(),
    };
  }
};

// Função para atualizar situação do investidor
export const updatedSituationInvestidor = async ({ situationId, data }: UpdatedSituationInvestidorProps)=> {
  console.log(data);
  console.log(situationId);
  try {
    const res = await AxiosInstance.put(`/api/v1/analytics/situacao/${situationId}/detail/`, data);
    console.log(res.data);
    return res.status === 200
      ? res.data as SituationInvestidor
      : {
          status: res.status,
          message: res.data?.message || 'Erro ao atualizar perfil',
        };
  } catch (error: any) {
    return {
      status: error.response?.status || 500,
      message: error.response?.data?.message || 'Erro na atualização do perfil',
      timestamp: new Date().toISOString(),
    };
  }
};

// Função principal de atualização de situação
export const updateSituation = async ({ value, userId }: UpdatePerfilProps): Promise<{
  status: 'success' | 'error';
  data?: any;
  message?: string;
  timestamp?: string;
}> => {
  try {
    if (!value || !userId) {
      throw new Error('Value e userId são obrigatórios');
    }

   

    const situation = await SearchSituationId({ valor: value });  
    
    const investorData = await situationInvestidor({situationId:situation});

    const updatedInvestorData: SituationInvestidor = {
      ...investorData,
      investidor: [...new Set([...investorData.investidor, userId])]
    };

    const perfilResponse = await updatedSituationInvestidor({ 
      situationId:situation, 
      data: updatedInvestorData 
    });

 
    const userData = await UserGetStatus({ userId:userId });
    if (!Array.isArray(userData) || !userData.length) {
      throw new Error('Usuário não encontrado');
    }

    const updatedUserStatus = {
      ...userData[0],
      situation: true
    };

    const userResponse = await UserUpdatedStatus({ 
      userId: userId, 
      data: updatedUserStatus
    });

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
    console.error(`Erro em updateSituation: ${errorMessage}`, {
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





/**
 * Fetches performance metrics for a specific asset (symbol) for a user.
 * @param params - Parameters including userId, symbol, startDate, endDate, and optional initialCapital
 * @returns Performance metrics, message for empty results, or error response
 */
export const getPerformanceAsset = async ({
  userId,
  symbol,
  startDate,
  endDate,
  initialCapital,
}: PerformanceParams): Promise<ApiResponse> => {

  const user = await getUserInfo({userId:userId});
  if (!user) {
    return {
      status: 404,
      message: 'Usuário não encontrado',
      timestamp: new Date().toISOString(),
    };
  }

  try {
    const response = await AxiosInstance.get(`api/v1/history/users/${user[0].id}/performance/${symbol}/`, {
      params: {
        start_date: startDate,
        end_date: endDate,
        initial_capital: initialCapital,
      },
    });

    if (response.status === 200) {
  
      return {
        data: response.data.data || response.data, // Handle nested data if present
        message: response.data.message, // Message for empty results
      };
    }

    return {
      status: response.status,
      message: response.data?.error || 'Erro ao buscar métricas de desempenho',
      timestamp: new Date().toISOString(),
    };
  } catch (error: any) {
    return {
      status: error.response?.status || 500,
      message: error.response?.data?.error || error.message || 'Erro na requisição de métricas de desempenho',
      timestamp: new Date().toISOString(),
    };
  }
};

/**
 * Fetches performance metrics for all operations for a user.
 * @param params - Parameters including userId, startDate, endDate, and optional initialCapital
 * @returns Performance metrics, message for empty results, or error response
 */
export const getAllPerformance = async ({
  userId,
  startDate,
  endDate,
  initialCapital,
}: AllPerformanceParams): Promise<ApiResponse> => {
  try {
    const response = await AxiosInstance.get(`/users/${userId}/performance/`, {
      params: {
        start_date: startDate,
        end_date: endDate,
        initial_capital: initialCapital,
      },
    });
    const dadosFormatados = formatNumbers(response.data)
    
    if (response.status === 200) {
      return {
        data: dadosFormatados || dadosFormatados,
        message: response.data.message,
      };
    }

    return {
      status: response.status,
      message: response.data?.error || 'Erro ao buscar métricas de desempenho para todas as operações',
      timestamp: new Date().toISOString(),
    };
  } catch (error: any) {
    return {
      status: error.response?.status || 500,
      message: error.response?.data?.error || error.message || 'Erro na requisição de métricas de desempenho',
      timestamp: new Date().toISOString(),
    };
  }
};