import { parseStringify } from "../utils";
import AxiosInstance from "@/services/AxiosInstance"
import { getUserInfo } from "./actions.user";




export const getPositions = async({symbol, Assest, UserId})=>{

        try{
            const user = await getUserInfo({userId:UserId})
            const user_id = user[0].id
                
            const res = await AxiosInstance.get(`api/v1/history/positions/${symbol}/${Assest}/1d/${user_id}/`);           
            if(res.status === 200){        
                return res.data
            }else{
            return parseStringify({"status":400, "message":"Enviada com error"})
            }
        }catch{
            return parseStringify({"status":400, "message":"Enviada com error"})
        }

};
