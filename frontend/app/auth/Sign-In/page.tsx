"use client"

import { FaSignInAlt,  FaAddressCard  } from "react-icons/fa";
import { useRouter } from 'next/navigation';
import { handleLogin } from "@/lib/actions";
import apiService from "@/services/apiService";
import AxiosInstance from "@/services/AxiosInstance";
import { useState } from "react";
import { toast } from 'react-toastify';
import Image from 'next/image'




const page = () => {
    
    const router = useRouter();
    const [errors, setErrors] = useState<string[]>([]);
    const[formdata, setFormdata] = useState({

        email:"",    
        password:"",
        
    })

    const handleOnchange = (e)=>{

        setFormdata({...formdata, [e.target.name]:e.target.value})
        
    }

    const handleSubmit = async(e)=>{
        e.preventDefault()
        if (formdata) {
             const res = await AxiosInstance.post('/api/v1/auth/login/', formdata)
             const response= res.data
             console.log(response)
             const user={
                'full_name':response.full_name,
                'email':response.email,
                'situation':response.situation,
                'perfil':response.perfil
             }
               

             if (res.status === 200) {
                 localStorage.setItem('token', JSON.stringify(response.access_token))
                 localStorage.setItem('refresh_token', JSON.stringify(response.refresh_token))
                 localStorage.setItem('user', JSON.stringify(user))
                 await router.push('/dashboard')
                 toast.success('login successful')
             }else{
                toast.error('something went wrong')
             }
        }
    }

  return (
    
    <section className='flex h-screen justify-center items-center'>
        <div className='flex flex-col shadow-2xl bg-white rounded min-w-96 p-4'>
           <div className='flex items-center justify-center mb-4 cursor-pointer'>
                <a href="/">
                <Image src={"/images/logo.png"} width={160} height={160} alt='logotipo'/>
                </a>
            </div>
            <hr />
            <div className='p-4 space-y-6'>
            <div className=' space-y-2'>
                <div className="flex items-center w-full space-x-2 ">                
                <span className='text-lg'>Login</span>
                </div>
                <p className='font-light text-sm bg-red-600 text-white p-4 rounded'>
                    Entre com as informações para fazer seu login no
                    <span className='font-semibold'> InvestGroup</span>
                </p>
            </div>
            <form action="" onSubmit={handleSubmit} className="space-y-6 w-full">
            <div className='flex flex-col'>
                 <label htmlFor="" className="text-sm font-semibold">Email:</label>
                 <input type="text"
                  className='border rounded py-2 text-xs px-2' 
                  name="email" 
                  value={formdata.email}  
                  onChange={handleOnchange} />
               </div>       
               <div className='flex flex-col'>
                 <label htmlFor=""  className="text-sm font-semibold">Password:</label>
                 <input type="password" 
                 className='border rounded py-2 text-xs px-2' 
                 name="password" 
                 value={formdata.password} 
                 onChange={handleOnchange}/>
               </div> 
               {errors.map((error, index) => {
                    return (
                        <div 
                            key={`error_${index}`}
                            className="p-5 bg-red-500 text-white rounded-xl opacity-80"
                        >
                            {error}
                        </div>
                    )
                })}         
               <div className="w-full">
                 <button type="submit" className="flex items-center justify-center space-x-2 bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded w-full">
                    <span>Sign-In</span>
                    <span className="text-2xl">
                    <FaSignInAlt/>
                    </span>
                </button>
                 
               </div>
            </form>         
            </div>
        </div>
    </section>
  )
}

export default page