import { parseStringify } from "../utils";
import AxiosInstance from "@/services/AxiosInstance"
import { getUserInfo } from "./actions.user";




export const getStockPositions = async({symbol, UserId})=>{

        try{
            const user = await getUserInfo({userId:UserId})
            const user_id = user[0].id
                
            const res = await AxiosInstance.get(`api/v1/history/positions/${symbol}/stock/1d/${user_id}/`)
            console.log(res.data.positions)
            if(res.status === 200){        
                return res.data.positions
            }else{
            return parseStringify({"status":400, "message":"Enviada com error"})
            }
        }catch{
            return parseStringify({"status":400, "message":"Enviada com error"})
        }

}