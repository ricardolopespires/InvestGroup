import React, {useEffect} from 'react'
import { useRouter } from 'next/navigation'
import { toast } from 'react-toastify';
import AxiosInstance from "@/services/AxiosInstance";
import { FaSignInAlt, FaRegUserCircle } from "react-icons/fa";


const refresh=JSON.parse(localStorage.getItem('refresh_token'))

const Logout = () => {
    const router = useRouter();
    const handleLogout = async ()=>{

        const res = await AxiosInstance.post('/api/v1/auth/logout/', {'refresh_token':refresh})
    
        if (res.status === 204) {
             localStorage.removeItem('token')
             localStorage.removeItem('refresh_token')
             localStorage.removeItem('user')
             router.push('/auth/Sign-In')
             toast.warn("logout bem-sucedido")
        }
      }
    
  return (    
    <button onClick={handleLogout}  className="hover:text-green-500 text-2xl"><FaSignInAlt/></button>
  )
}

export default Logout