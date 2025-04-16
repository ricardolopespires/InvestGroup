import AxiosInstance from "@/services/AxiosInstance";
import { parseStringify } from "../utils";





export const getLevelAdvisors = async({AdvisorId})=>{
    try {
        const res = await AxiosInstance.get(`/api/v1/advisor/robos/level/${AdvisorId}/`);        
        return res.data 
        } catch (error: any) {
        return {
            status: error.response?.status || 500,
        }
    }
}




export const getListAdvisors = async()=>{
    try {
        const res = await AxiosInstance.get(`/api/v1/advisor/robos/`);
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
    


