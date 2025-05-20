import AxiosInstance from "@/services/AxiosInstance";
import { parseStringify } from "../utils";





export const getLevelAdvisors = async({AdvisorId})=>{

    try {
        const res = await AxiosInstance.get(`/api/v1/advisor/robo/level/${AdvisorId}/`);        
        return res.data 
        } catch (error: any) {
        return {
            status: error.response?.status || 500,
        }
    }
}


export const patchIsActiveAdvisors =  async ({AdvisorId, data})=>{
    try {
        const res = await AxiosInstance.patch(`/api/v1/advisor/robo/${AdvisorId}/`, data);
        return res
    } catch (error: any) {
        return {
            status: error.response?.status || 500,
        }
    }
}



export const getListAdvisors = async()=>{
    try {
        const res = await AxiosInstance.get(`/api/v1/advisor/robos/list/`);
        const ad = await getLevelAdvisors({AdvisorId:res.data[0].id})
        return res.data 

      } catch (error: any) {
        return {
          status: error.response?.status || 500,
          message: error.response?.data?.message || 'Erro na atualização do perfil',
          timestamp: new Date().toISOString(),
        };
      }
    };
    


export const getDetailAdvisors = async({AdvisorId})=>{
      try {
          const res = await AxiosInstance.get(`/api/v1/advisor/robo/${AdvisorId}/`);         
          return res.data   
        } catch (error: any) {
          return {
            status: error.response?.status || 500,
            message: error.response?.data?.message || 'Erro na atualização do perfil',
            timestamp: new Date().toISOString(),
          };
        }
      };
      



export const getRiskAdvisors =  async ({AdvisorId})=>{

      try{
        const res = await AxiosInstance.get(`/api/v1/advisor/risk/${AdvisorId}/`,);
        return res.data
      }catch(err){
        return parseStringify({"status":400, "message":"Enviada com error"})

      }

  };


export const patchRiskAdvisors =  async ({AdvisorId, data})=>{

  try{
    const res = await AxiosInstance.patch(`/api/v1/advisor/risk/${AdvisorId}/`, data);
    return res
  }catch(err){
    return parseStringify({"status":400, "message":"Enviada com error"})

  }

};
