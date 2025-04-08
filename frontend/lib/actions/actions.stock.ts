


import { parseStringify } from "../utils";
import { getAssetCryptos } from "./actions.crypto"
import AxiosInstance from "@/services/AxiosInstance"
import { getUserInfo } from "./actions.user";






export const getAssetsStocks = async()=>{

        try{
    
            const res = await AxiosInstance.get(`/api/v1/trading/stocks/`)
            console.log(res)
            if(res.status === 200){        
                return res.data
            }else{
            return parseStringify({"status":400, "message":"Enviada com error"})
            }
        }catch{
            return parseStringify({"status":400, "message":"Enviada com error"})
        }

};




export const getTrendFollowingStocks = async({symbol, UserId})=>{


    try{
        const user = await getUserInfo({userId:UserId});
        const user_id = user[0].id

        const res = await AxiosInstance.get(`/api/v1/history/last-signal/${symbol}/stock/1d/${user_id}/`)  
        if(res.status === 200){        
            return res.data
        }else{
        return parseStringify({"status":400, "message":"Enviada com error"})
        }
    }catch{
        return parseStringify({"status":400, "message":"Enviada com error"})
    }

};




