import AxiosInstance from "@/services/AxiosInstance";
import { getUserInfo } from "./actions.user";
import { parseStringify } from "../utils";









export const getTrendFollowing = async({symbol, Assest, UserId})=>{


    try{
        const user = await getUserInfo({userId:UserId});
        const user_id = user[0].id

        const res = await AxiosInstance.get(`/api/v1/history/last-signal/${symbol}/${Assest}/1d/${user_id}/`)  
        if(res.status === 200){                 
            return res.data            
        }else{
        return parseStringify({"status":400, "message":"Enviada com error"})
        }
    }catch{
        return parseStringify({"status":400, "message":"Enviada com error"})
    }

};

