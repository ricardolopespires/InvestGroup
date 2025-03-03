import { toast } from "react-toastify";
import { encryptId, extractCustomerIdFromUrl, parseStringify } from "../utils";
import AxiosInstance from "@/services/AxiosInstance";
import { useRouter } from "next/navigation";
import axios from "axios";
import { userResetPasswordProp } from "@/types";


export const getUserInfo = async ({ userId }: getUserInfoProps) => {
    try {
      // Faça a solicitação HTTP para a API
      const response = await AxiosInstance.get(`/api/v1/auth/user/${userId}/`);
       // Verifique se a resposta contém os dados esperados
      if (response.data) {
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

  
  console.log(data)
 
    try {
      
      const res = await AxiosInstance.post('/api/v1/auth/login/', { email:data.email, password:data.password });
      const response = res.data;
      console.log(res.status);
  
      if (res.status === 200) {
        const userData = {
          user_id: response.user_id,
          full_name: response.full_name,
          email: response.email,
        };
  
        localStorage.setItem('token', JSON.stringify(response.access_token));
        localStorage.setItem('refresh_token', JSON.stringify(response.refresh_token));
        localStorage.setItem('user', JSON.stringify(userData)); 
  
  
        const user = await getUserInfo({ userId: userData.email });
        localStorage.setItem('perfil', JSON.stringify(user[0].perfil));
        localStorage.setItem('situacao', JSON.stringify(user[0].situation));       
        
        return parseStringify(res);
      } else {
        toast.error('Algo deu errado');
      }
    } catch (error) {
      console.error('Error during login:', error);
      toast.error('Ocorreu um erro durante o login');
    }
  };


  

  // Função para registrar um novo usuário
  export const signUp = async ({ data }: SignUpParams): Promise<ApiResponse> => {

    console.log(data)
    try {
      // Verifica se o email já está cadastrado
      const user = await getUserInfo({ userId: data.email });
  
      if (user.email === data.email) {
        return {
          status: 409, // Código 409 (Conflict) para conflitos de recursos
          message: "O email já está cadastrado. Por favor, utilize um email diferente.",
        };
      }
  
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
      return null;
    }
  }



  export const UserStatusManagement = async ({userId}:UserStatusManagementProps) => {

    try {
      // Faça a solicitação HTTP para a API
      const response = await AxiosInstance.get(`/api/v1/auth/user/management/status/${userId}/`);
       // Verifique se a resposta contém os dados esperados
        if (response.data) {
          // Processar os dados, se necessário
          return response.data; // Não é necessário chamar parseStringify aqui, a menos que seja necessário outro processamento específico
        } else {
          throw new Error('Usuário não encontrado');
        }
  
      } catch (error) {
        console.error('Erro ao obter informações do usuário:', error);
        throw error; // Rejeita o erro para que o chamador também possa lidar com ele, se necessário
      }  
  }
  