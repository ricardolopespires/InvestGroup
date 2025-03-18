import { parseStringify } from "../utils";
import { getAssetCryptos } from "./actions.crypto"
import AxiosInstance from "@/services/AxiosInstance"






export const getAssetsCurrencies = async()=>{

        try{
    
            const res = await AxiosInstance.get(`/api/v1/trading/currencies/`)
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