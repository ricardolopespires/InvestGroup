
import AxiosInstance from "@/services/AxiosInstance";
import { parseStringify } from "../utils";
import { getUserInfo } from "./actions.user";


export const postBuyOperations = async (params: OperationParams) => {
    try {
      const { data } = await AxiosInstance.post('/operations/buy', params);
      return data;
    } catch (error) {
      console.error('Erro ao criar operação de compra:', error);
      throw new Error('Falha ao criar operação de compra.');
    }
  };
  
  export const postSellOperations = async (params: OperationParams) => {
    try {
      const { data } = await AxiosInstance.post('/operations/sell', params);
      return data;
    } catch (error) {
      console.error('Erro ao criar operação de venda:', error);
      throw new Error('Falha ao criar operação de venda.');
    }
  };
  
  export const postCloseOperations = async ({ticket, UserId}) => {

    const user = await getUserInfo({userId:UserId})    

    try {   
      const  res = await AxiosInstance.post(`/api/v1/transactions/operations/close/${user[0].id}/`, {"ticket":ticket});  
      return res;
    } catch (error) {
      console.error('Erro ao fechar operação:', error);
      throw new Error('Falha ao fechar operação.');
    }
  };


  export const postCreatedOperations = async (params: OperationParams) => {
    try {
      const { type, asset, quantity, price, userId } = params;
  
      // Validação dos dados
      if (!['BUY', 'SELL'].includes(type)) {
        throw new Error('Tipo de operação inválido. Use BUY ou SELL.');
      }
      if (!asset || quantity <= 0 || price <= 0 || !userId) {
        throw new Error('Dados da operação incompletos ou inválidos.');
      }
  
      // Escolher o endpoint com base no tipo
      const endpoint = type === 'BUY' ? '/operations/buy' : '/operations/sell';
      const { data } = await AxiosInstance.post(endpoint, params);
  
      return {
        success: true,
        operation: data,
        message: `Operação de ${type} criada com sucesso.`,
      };
    } catch (error) {
      console.error('Erro ao criar operação:', error);
      throw new Error('Falha ao criar operação. Tente novamente.');
    }
  };



  export const postInversorOperations = async ({ ticket, UserId }) => {
    if (!ticket || !UserId) {
      throw new Error('Ticket and UserId are required');
    }
  
    try {
      const user = await getUserInfo({ userId: UserId });
  
      if (!user || !user[0]?.id) {
        throw new Error('User not found or invalid');
      }
  
      const { data: currentOperation } = await AxiosInstance.post(
        `/api/v1/transactions/operations/reverse/${user[0].id}/`,
        { ticket }
      );
  
      return currentOperation;
    } catch (error) {
      console.error('Error in postInversorOperations:', error);
      throw new Error('Failed to process operation');
    }
  };