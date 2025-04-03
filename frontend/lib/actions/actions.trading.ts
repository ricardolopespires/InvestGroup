import { parseStringify, transformData } from "../utils"
import { Axios } from "axios"
import { getAssetCryptos } from "./actions.crypto"
import AxiosInstance from "@/services/AxiosInstance"
import { getAssetsCommodities } from "./actions.commodities"
import { getAssetsCurrencies } from "./actions.currency"
import { getAssetsStocks } from "./actions.stock"
import { getUserInfo } from "./actions.user"








export const getAssetList = async({CodeAsset}:getAssetListProps)=>{

    try{
        if (CodeAsset === "crypto"){
            const res = getAssetCryptos()
            return res
        }else if(CodeAsset === "commodities"){
            const res = await getAssetsCommodities()
            
            return res
        }else if(CodeAsset === "currency"){
            const res = await getAssetsCurrencies()
            return res
        }else if(CodeAsset === "stocks"){
            const res = await getAssetsStocks();
            console.log(res);
            return res
        };

    }catch{
        return parseStringify({"status":400, "message":"Enviada com error"})
    }

}

export const getAssetCryptosMT5 = async({symbol, period, UserId})=>{


    try{
        const res = await getUserInfo({userId:UserId})
        const user_id = res[0].id        
        const response = await AxiosInstance.get(`/api/v1/history/mt5/${symbol}/${period}/${user_id}/`)
        if(response.status === 200){
            return response.data
        }else{
            parseStringify({"status":400, "message":"Enviada com error"})
        };
    }catch{
        return parseStringify({"status":400, "message":"Enviada com error"})
    }   
}



export const getHistoryAssets = async({selected, period, CodeAsset, UserId})=>{
    try{
        
        if (CodeAsset === "crypto"){
            const res = await AxiosInstance.get(`/api/v1/history/data/${selected.symbol}-USD/${period}/`)
            if(res.status === 200){        
                return res.data
            }else{
            return parseStringify({"status":400, "message":"Enviada com error"})
            }   
        }else{
            const response = await getAssetCryptosMT5({symbol:selected.symbol, period:period, UserId:UserId})
            if(response.status === 200){
                return response
            }else{
                const res = await AxiosInstance.get(`/api/v1/history/data/${selected.yahoo}/${period}/`)
                return res
            }                
        };     

    }catch{
         return parseStringify({"status":400, "message":"Enviada com error"})
    }


    }
