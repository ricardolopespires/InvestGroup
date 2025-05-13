import { parseStringify } from "../utils";
import { getAssetCryptos } from "./actions.crypto"
import AxiosInstance from "@/services/AxiosInstance"
import { getUserInfo } from "./actions.user";
import { get } from "http";






export const getAssetsCommodities = async({UserId}:{UserId:string})=>{

        try{
            const user = await getUserInfo({userId:UserId})            
    
            const res = await AxiosInstance.get(`/api/v1/trading/commodities/${user[0].id}/list/`)
            if(res.status === 200){        
                return res.data
            }else{
            return parseStringify({"status":400, "message":"Enviada com error"})
            }
        }catch{
            return parseStringify({"status":400, "message":"Enviada com error"})
        }

};

