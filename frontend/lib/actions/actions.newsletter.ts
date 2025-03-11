
import AxiosInstance from "@/services/AxiosInstance";
import { parseStringify } from "../utils";








export const postSubscribed = async ({EmailData})=>{


    try{        
        const res = await AxiosInstance.post(`api/v1/newsletter/subscribe/`,EmailData);
        
        console.log(res)
        
        if(res.status === 201){            
            return parseStringify({"status": 201, "message": "Obrigado! por se escrever"})
        }
        else if(res.status === 400){            
                return parseStringify({"status": 400, "message": res.message})         
        }else{
            return parseStringify({"status": 404, "message": "Banco inválido"})
        }
    }catch(e){
        return parseStringify({"status": 500, "message": "Erro ao buscar dados do banco"})
    }

}