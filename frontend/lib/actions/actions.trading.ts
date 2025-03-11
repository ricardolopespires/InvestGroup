import { parseStringify } from "../utils"
import { Axios } from "axios"
import { getAssetCryptos } from "./actions.crypto"




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