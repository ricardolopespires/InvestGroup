import { toast } from "react-toastify";
import { parseStringify } from "../utils";
import AxiosInstance from "@/services/AxiosInstance";
import { useRouter } from "next/navigation";
import axios from "axios";



export const getUserInfo = async ({ userId }: getUserInfoProps) => {


    try {
      // Faça a solicitação HTTP para a API
      const response = await AxiosInstance.get(`/api/v1/auth/list/${userId}/`);
       // Verifique se a resposta contém os dados esperados
      if (response.status === 200) {
        // Processar os dados, se necessário
        return response.data; // Não é necessário chamar parseStringify aqui, a menos que seja necessário outro processamento específico
      } else {
        throw new Error('Usuário não encontrado');
      }
    } catch (error) {
      console.error('Erro ao obter informações do usuário:', error);
      throw error; // Rejeita o erro para que o chamador também possa lidar com ele, se necessário
    }
  };
  


 export const userResetPassword = async({data}:userResetPasswordProp)=>{

    try{
        const res = await AxiosInstance.post('/api/v1/account/resetpassword/',data)
        console.log(res.status)
        if(res.status === 200){
            return parseStringify({"status":res.status, "message":"Enviada com successo"})
        }else{
            return parseStringify({"status":res.status, "message":"Enviada com error"})
        }
        
    }catch(err){
        return parseStringify({"message": "Informaões incorretas"})
    }
}



export const SignIn = async ({ data }:SignInParams) => {
  

 
    try {
      
      const res = await AxiosInstance.post('/api/v1/auth/login/', { email:data.email, password:data.password });
      const response = res.data;
 
  
      if (res.status === 200) {
        
        
        const userData = {
          user_id: response.user_id,
          full_name: response.full_name,
          email: response.email,
        };
  
        localStorage.setItem('token', JSON.stringify(response.access_token));
        localStorage.setItem('refresh_token', JSON.stringify(response.refresh_token));
        localStorage.setItem('user', JSON.stringify(userData));   
        
        
        return parseStringify(res);
      } else {
        return parseStringify({
          status: res.status,
          message: res.data?.message || 'Erro desconhecido',
        });
      }
    } catch (error) {
      return parseStringify({
        status: 500,
        message: 'Erro inesperado ao fazer login.',
      });
    }
  };


  

  // Função para registrar um novo usuário
  export const signUp = async ({ data }: SignUpParams): Promise<ApiResponse> => {

    console.log(data)
    try {
      // Verifica se o email já está cadastrado
    
  
      // Verifica se as senhas coincidem
      if (data.password !== data.password2) {
        return {
          status: 400, // Código 400 (Bad Request) para dados inválidos
          message: "As senhas não coincidem. Por favor, tente novamente.",
        };
      }
  
      // Envia a solicitação para registrar o usuário
      const response = await AxiosInstance.post('/api/v1/auth/register/', data);
  
      return {
        status: response.status,
        data: response.data,
      };
    } catch (error) {
      // Tratar erros de forma apropriada
      if (axios.isAxiosError(error)) {
        return {
          status: error.response?.status || 500,
          message: error.response?.data?.message || 'Erro inesperado ao registrar o usuário.',
        };
      }
  
      return {
        status: 500,
        message: 'Erro inesperado ao registrar o usuário.',
      };
    }
  };
  
  
  
  export const logoutAccount = async () => {
    
    try {
      const refresh=JSON.parse(localStorage.getItem('refresh_token'))
      const router = useRouter();
      const res = await AxiosInstance.post('/api/v1/auth/logout/', {'refresh_token':refresh})
      
      if (res.status === 204) {
           localStorage.removeItem('token')
           localStorage.removeItem('refresh_token')
           localStorage.removeItem('user')
           router.push('/auth/Sign-In')
           toast.warn("logout bem-sucedido")
      }
  
    } catch (error) {
      return parseStringify({
        status: 500,
        message: 'Erro inesperado ao registrar o usuário.',
      });
    }
  }


export const UserGetStatus = async ({userId}:UserIdProps) => {
  try {
    const user = await getUserInfo({ userId: userId }); 

    // Faça a solicitação HTTP para a API
    const response = await AxiosInstance.get(`/api/v1/auth/user/status/${user[0].id}/`,);
    console.log(response.status)
     // Verifique se a resposta contém os dados esperados
    if (response.status === 200) {
        // Processar os dados, se necessário
        // Não é necessário chamar parseStringify aqui, a menos que seja necessário outro processamento específico             
        localStorage.setItem('perfil', JSON.stringify(user[0].perfil));
        localStorage.setItem('situacao', JSON.stringify(user[0].situation));
        
        return response.data;

      } else {
        throw new Error('Usuário não encontrado');
      }

    } catch (error) {
      return parseStringify({
        status: 500,
        message: 'Erro inesperado ao registrar o usuário.',
      });
    } 

};


  export const UserUpdatedStatus = async ({userId, data}:UserStatusProps) => {
    try {

      // Faça a solicitação HTTP para a API
      const response = await AxiosInstance.put(`/api/v1/auth/user/status/${userId}/`, data);
       // Verifique se a resposta contém os dados esperados
        if (response.status === 200) {
          // Processar os dados, se necessário
          return parseStringify(response); // Não é necessário chamar parseStringify aqui, a menos que seja necessário outro processamento específico
        } else {
          throw new Error('Usuário não encontrado');
        }
  
      } catch (error) {
        return parseStringify({
          status: 500,
          message: 'Erro inesperado ao registrar o usuário.',
        });
      }  
  }
  