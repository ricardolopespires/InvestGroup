import { parseStringify, transformData } from "../utils"
import { Axios } from "axios"
import { getAssetCryptos } from "./actions.crypto"
import AxiosInstance from "@/services/AxiosInstance"
import { getAssetsCommodities } from "./actions.commodities"
import { getAssetsCurrencies } from "./actions.currency"
import { getAssetsStocks } from "./actions.stock"








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


export const getHistoryAssets = async({symbol, period, CodeAsset})=>{
    try{
        
        if (CodeAsset === "crypto"){
            const res = await AxiosInstance.get(`/api/v1/history/data/${symbol}-USD/${period}/`)
            if(res.status === 200){        
                return res.data
            }else{
            return parseStringify({"status":400, "message":"Enviada com error"})
            }   
        }else{
            const res = await AxiosInstance.get(`/api/v1/history/data/${symbol}/${period}/`)
            if(res.status === 200){        
                return res.data
            }else{
            return parseStringify({"status":400, "message":"Enviada com error"})
            } 
            
        }     

    }catch{
         return parseStringify({"status":400, "message":"Enviada com error"})
    }


    }
