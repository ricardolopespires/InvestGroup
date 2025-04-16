import AxiosInstance from "@/services/AxiosInstance";
import { parseStringify } from "../utils";
import { getUserInfo } from "./actions.user";





export const getTransactions = async({symbol, UserId})=>{
    try {
        const user = await getUserInfo({userId:UserId});
        const user_id = user[0].id
        
        const res = await AxiosInstance.get(`/api/v1/transactions/operations/list/${symbol}/${user_id}/`);        
        return res.data 
        } catch (error: any) {
        return {
            status: error.response?.status || 500,
        }
    }
}

