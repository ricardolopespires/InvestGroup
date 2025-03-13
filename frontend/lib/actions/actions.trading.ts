import { parseStringify, transformData } from "../utils"
import { Axios } from "axios"
import { getAssetCryptos } from "./actions.crypto"
import AxiosInstance from "@/services/AxiosInstance"




export const getAssetList = async({CodeAsset}:getAssetListProps)=>{


    try{
        if (CodeAsset === "crypto"){
            const res = getAssetCryptos()
            return res
        }

    }catch{
        return parseStringify({"status":400, "message":"Enviada com error"})
    }

}


export const getHistoryAssets = async({symbol, period})=>{
    try{
        const res = await AxiosInstance.get(`/api/v1/history/data/${symbol}-USD/`)
        if(res.status === 200){
            const data =  transformData(res.data)
            return data
        }else{
           return parseStringify({"status":400, "message":"Enviada com error"})
        }

    }catch{
         return parseStringify({"status":400, "message":"Enviada com error"})
    }


    }
