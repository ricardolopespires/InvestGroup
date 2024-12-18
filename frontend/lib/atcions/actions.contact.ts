import AxiosInstance from "@/services/AxiosInstance"
import { parseStringify } from "../utils"




export const createMassage = async ({data}:createMassageProps)=> {

    try{
        const res = await AxiosInstance.post('/api/v1/contact/',data)
        if(res.status === 201){
            return parseStringify({"status":res.status, "message":"Enviada com successo"})
        }else{
            return parseStringify({"status":res.status, "message":"Enviada com error"})
        }
    }catch(err){
        return parseStringify({"status":400, "message":"Enviada com error"})

    };
};
