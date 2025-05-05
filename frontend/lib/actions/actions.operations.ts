
import AxiosInstance from "@/services/AxiosInstance";
import { parseStringify } from "../utils";


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
  
  export const postCloseOperations = async (params: { ticket: string }) => {
    // params: { ticket: string }

    console.log("params", params)
    try {
    const { data } = await AxiosInstance.post(`/api/v1/transactions/operations/close/${params.ticket}/`, params);
      return data;
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

export const postInversorOperations = async ({ticket, type}) => {

    console.log("ticket", ticket)
    console.log("type", type)
    try {
      // Buscar a operação pelo ID
      const { data: currentOperation } = await AxiosInstance.get(`/operations/${id}`);
  
      // Verificar se a operação existe e está aberta
      if (!currentOperation) {
        throw new Error('Operação não encontrada.');
      }
      if (currentOperation.status !== 'OPEN') {
        throw new Error('A operação já está fechada ou inválida.');
      }
  
      // Determinar o tipo oposto
      const oppositeType = currentOperation.type === 'buy' ? 'sell' : 'buy';
  
      // Criar uma nova operação oposta
      const newOperationParams: OperationParams = {
        userId: currentOperation.userId,
        asset: currentOperation.asset,
        quantity: currentOperation.quantity,
        price: currentOperation.price, // Ou obter preço atual do mercado, se necessário
        type: oppositeType,
      };
  
      const newOperation = await postCreatedOperations(newOperationParams);
  
      // Fechar a operação atual
      const closeParams = { operationId: id };
      await postCloseOperations(closeParams);
  
      return {
        success: true,
        newOperation: newOperation.operation,
        closedOperation: currentOperation,
        message: `Operação de ${currentOperation.type} fechada e nova operação de ${oppositeType} criada.`,
      };
    } catch (error) {
      console.error('Erro ao processar operação inversa:', error);
      throw new Error('Falha ao processar operação inversa. Tente novamente.');
    }
  };