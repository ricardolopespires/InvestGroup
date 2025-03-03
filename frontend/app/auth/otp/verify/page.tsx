"use client"


import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import axios from 'axios'
import React, {useState} from 'react'
import { useRouter } from 'next/navigation';
import { GoShieldLock } from "react-icons/go";
import { toast } from "react-toastify";
import Image from 'next/image';
import AxiosInstance from "@/services/AxiosInstance";

const Page = () => {
    const [otp, setOtp]=React.useState(new Array(4).fill(""))
    const router = useRouter();

    const handleOtpSubmit = async(e)=>{
            e.preventDefault()
          
            const numeros = otp.join("")    

            if (otp) {
                const res = await AxiosInstance.post('/api/v1/auth/verify-email/', {'otp':numeros})
                const resp = res.data
                if (res.status === 200) {
                    router.push('/auth/Sign-In')
                    toast.success(resp.message)
                }
                
            }
         
    }

    const handleChange = async (el, index) =>{

        if(isNaN(el.value)) return false

        setOtp([...otp.map((data,i) =>(i===index?el.value:data))])

        if(el.nextSibling){

            el.nextSibling.focus()
        }

    }

 
  return (
    <div className='h-screen flex items-center'>     
      <Card className=" max-w-md mx-auto text-center bg-white px-4 sm:px-8 py-10 rounded-xl border shadow">      
        <CardHeader className="mb-8 flex flex-col items-center space-y-9">
              <a href="/">
                <Image src={"/images/logo.png"} width={160} height={160} alt='logotipo'/>
              </a>
            <div className='text-primary text-[70px]'>
            <GoShieldLock />
            </div>
            <h1 className="text-2xl font-bold mb-1">Verificação de Email</h1>
            <div className="text-[15px] text-slate-500">
              <p >Digite o código de verificação de 4 dígitos </p>
              <p>que foi enviado para o seu email.</p>
            </div>          
        </CardHeader> 
        <CardContent>   
          <form className='space-y-4 w-full' action=""  onSubmit={handleOtpSubmit}>
                    <div className='flex flex-col space-y-2 '>
                      <label htmlFor="otp" className='text-xs font-semibold'>Digite seu código OTP:</label>
                        <div className='flex items-center py-4'>
                        {otp.map((data, i)=>{

                                return(
                                    <input type="text"
                                    className='border-b border-gray-400 focus:outline-none w-12 h-12 text-2xl  m-auto text-center' 
                                    name="otp"                             
                                    maxLength={1}
                                    key={i}
                                    value={data}
                                    onChange={e => handleChange(e.target, i)}
                                    onFocus={e => e.target.select}/>
                                )
                                })}
                        </div>
                    </div>
                    <button type='submit' className={`px-9 py-2 rounded font-semibold ${otp[otp.length -1]  ? 'bg-primary text-white' : 'bg-gray-200 text-gray-400'}`}>Verificar conta</button>
          </form>  
          <div className="text-xs text-slate-500 mt-4">Não recebeu o código?
            <a className="font-medium text-indigo-500 hover:text-indigo-600" href="#0"> Reenviar</a>
          </div>
        </CardContent>   
      </Card>
    </div>
    
  )
}

export default Page