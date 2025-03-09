import AxiosInstance from "@/services/AxiosInstance";
import { parseStringify } from "../utils";
import { getUserInfo } from "./actions.user";
import { updatePerfil, updateSituation } from "./actions.analytics";



export const quizPerfil = async () => {
    try {
        const res = await AxiosInstance.get(`/api/v1/quiz/1/`);

        if (res.status === 200) {
            return res.data;
        }

        return parseStringify({
            status: res.status,
            message: res.data?.message || "Erro desconhecido",
        });

    } catch (error) {
        return parseStringify({
            status: error.response?.status || 500,
            message: error.response?.data?.message || "Erro ao buscar dados",
        });
    }
};





export const quizUserAnswers = async ({UserId, QuestionId, AnwserId, }) => {

   
    try {
        const user = await getUserInfo({ userId: UserId });
        if (!user || user.length === 0) {
            throw new Error("Usuário não encontrado.");
        }

        const user_id = user[0].id;
        const res = await AxiosInstance.post(`/api/v1/quiz/user-answers/`, {          
                user_id: user_id, 
                question: QuestionId, 
                selected_answer: AnwserId, 
            });

        return {
            status: res.status,
            message: res.status === 200 ? "Enviada com sucesso" : "Erro ao enviar"
        };

    } catch (error) {
        console.error("Erro ao enviar respostas do quiz:", error);
        return {
            status: 500,
            message: "Erro ao processar a solicitação"
        };
    }
};




  // Função para atualizar o quiz do perfil
  export const updatedQuizPerfil = async ({ ValueId, userId }: UpdateQuizParams): Promise<QuizResponse> => {
    try {
      // Validação inicial dos parâmetros
      if (!ValueId || !userId) {
        throw new Error('ValueId e userId são obrigatórios');
      }
  
      // Busca das informações do usuário
      const userResponse = await getUserInfo({ userId:userId });
      if (!Array.isArray(userResponse) || userResponse.length === 0) {
        throw new Error('Usuário não encontrado');
      }
  
      const user: UserInfo = userResponse[0];
      const validatedUserId = user.id;
  
      // Atualização do perfil com os dados do usuário
      const perfilData = await updatePerfil({ 
        value: ValueId, 
        userId: validatedUserId.toString()
      });
  
      // Verificação do resultado da atualização
      if (perfilData.status === 'error') {
        throw new Error(perfilData.message || 'Erro ao atualizar perfil');
      }
  
      return parseStringify({
        status: 200,
        data: perfilData.data,
        timestamp: new Date().toISOString()
      });
  
    } catch (error) {
      const errorMessage = error instanceof Error 
        ? error.message 
        : 'Erro desconhecido ao atualizar quiz do perfil';
      
      console.error(`Erro em updatedQuizPerfil: ${errorMessage}`, {
        ValueId,
        userId,
        stack: error instanceof Error ? error.stack : undefined
      });
  
      return {
        status: 'error',
        message: errorMessage,
        timestamp: new Date().toISOString()
      };
    }
  };




  
export const quizSituation = async () => {
  try {
      const res = await AxiosInstance.get(`/api/v1/quiz/2/`);

      if (res.status === 200) {
          return res.data;
      }

      return parseStringify({
          status: res.status,
          message: res.data?.message || "Erro desconhecido",
      });

  } catch (error) {
      return parseStringify({
          status: error.response?.status || 500,
          message: error.response?.data?.message || "Erro ao buscar dados",
      });
  }
};




  // Função para atualizar o quiz do perfil
  export const updatedQuizSituation = async ({ ValueId, userId }: UpdateQuizParams): Promise<QuizResponse> => {
    try {
      // Validação inicial dos parâmetros
      if (!ValueId || !userId) {
        throw new Error('ValueId e userId são obrigatórios');
      }
  
      // Busca das informações do usuário
      const userResponse = await getUserInfo({ userId:userId });
      if (!Array.isArray(userResponse) || userResponse.length === 0) {
        throw new Error('Usuário não encontrado');
      }
  
      const user: UserInfo = userResponse[0];
      const validatedUserId = user.id;
  
      // Atualização do perfil com os dados do usuário
      const perfilData = await updateSituation({ 
        value: ValueId, 
        userId: validatedUserId.toString()
      });
  
      // Verificação do resultado da atualização
      if (perfilData.status === 'error') {
        throw new Error(perfilData.message || 'Erro ao atualizar perfil');
      }
  
      return parseStringify({
        status: 200,
        data: perfilData.data,
        timestamp: new Date().toISOString()
      });
  
    } catch (error) {
      const errorMessage = error instanceof Error 
        ? error.message 
        : 'Erro desconhecido ao atualizar quiz do perfil';
      
      console.error(`Erro em updatedQuizPerfil: ${errorMessage}`, {
        ValueId,
        userId,
        stack: error instanceof Error ? error.stack : undefined
      });
  
      return {
        status: 'error',
        message: errorMessage,
        timestamp: new Date().toISOString()
      };
    }
  };
