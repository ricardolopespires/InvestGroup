"use client"


import axios from 'axios'
import React, {useState} from 'react'
import { useRouter } from 'next/navigation';
import { GoShieldLock } from "react-icons/go";
import { toast } from "react-toastify";
import Image from 'next/image';

const VerifyEmail = () => {
    const [otp, setOtp]=React.useState(new Array(4).fill(""))
    const router = useRouter();

    const handleOtpSubmit = async(e)=>{
            e.preventDefault()
            const codigo = otp         
          
            if (otp) {
                const res = await axios.post('http://localhost:8000/api/v1/auth/verify-email/', {'otp':otp})
                const resp = res.data
                if (res.status === 200) {
                    router.push('/Sign-in')
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
      <div className=" max-w-md mx-auto text-center bg-white px-4 sm:px-8 py-10 rounded-xl border shadow">      
      <header className="mb-8 flex flex-col items-center space-y-9">
            <a href="/">
              <Image src={"/images/logo.png"} width={160} height={160} alt='logotipo'/>
            </a>
          <div className='text-green-600 text-[70px]'>
          <GoShieldLock />
          </div>
          <h1 className="text-2xl font-bold mb-1">Verificação de Email</h1>
          <div className="text-[15px] text-slate-500">
            <p >Digite o código de verificação de 4 dígitos </p>
            <p>que foi enviado para o seu email.</p>
          </div>          
      </header>       
      <form className='space-y-4 w-full' action=""  onSubmit={handleOtpSubmit}>
                <div className='flex flex-col space-y-2 '>
                  <label htmlFor="otp" className='text-xs font-semibold'>Digite seu código OTP:</label>
                    <div className='flex items-center py-4'>
                    {otp.map((data, i)=>{

                            return(
                                <input type="text"
                                className='border-2 border-black w-12 h-12 text-2xl rounded-xl m-auto text-center' 
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
                <button type='submit' className='bg-blue-400 px-9 py-2 rounded text-white hover:bg-green-600'>Verificar conta</button>
      </form>  
      <div className="text-xs text-slate-500 mt-4">Não recebeu o código?
        <a className="font-medium text-indigo-500 hover:text-indigo-600" href="#0"> Reenviar</a>
      </div>
      </div>
    </div>
    
  )
}

export default VerifyEmail