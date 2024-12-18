"use client"


import AxiosInstance from '@/services/AxiosInstance';
import React, {useState} from 'react'
import { useRouter } from 'next/navigation';
import { GoShieldLock } from "react-icons/go";
import { toast } from "react-toastify";
import Timer from './_components/Timer';
import Message from './_components/Message';

function startTimer() {
  this.counter = { min: 30, sec: 0 } // choose whatever you want
  let intervalId = setInterval(() => {
    if (this.counter.sec - 1 == -1) {
      this.counter.min -= 1;
      this.counter.sec = 59
    } 
    else this.counter.sec -= 1
    if (this.counter.min === 0 && this.counter.sec == 0) clearInterval(intervalId)
  }, 1000)
}


const page = () => {
  
const [otp, setOtp]=React.useState(new Array(6).fill(""))

const router = useRouter();

const handleOtpSubmit = async(e)=>{
        e.preventDefault()          
        const towfactor = otp.join("")   

        console.log({'otp':towfactor})

        if (otp) {
            const res = await AxiosInstance.post(`/api/v1/auth/verify/two-factor/2/`, {'otp':towfactor})
            const resp = res.data
            if (res.status === 200) {
                router.push('/dashboard/overview')
                localStorage.setItem('2FA', JSON.stringify({"otp":true}))
                toast.success(resp.message)
            }else{
              toast.error(resp.message)
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
    <div className='flex w-full h-screen items-center justify-center'>
      <div className='flex flex-col shadow-2xl bg-white rounded w-[600px] p-9'>
        <header className='flex flex-col gap-4 items-center justify-center p-9'>   
            <img src={"/images/twofactor.png"} alt="2FA" className='w-40 h-40' />
            <h1 className='mt-7 text-xl font-semibold'>Verificação necessária</h1>
            <p className='font-semibold text-gray-400'>
            Digite o código que foi enviado para o seu celular via
                <strong className='text-gray-900 font-bold'> Notificação.</strong>
            </p>
        </header>
          <div className='flex flex-col items-center justify-center '>
            <form action="" className='flex flex-col items-center justify-center gap-4'  onSubmit={handleOtpSubmit}>
                 <div className='space-y-4  gap-4 flex flex-col justify-center' >
                    <div className='flex justify-center space-y-2 '>             
                        <div className='flex items-center py-4 gap-4'>
                        {otp.map((data, i)=>{

                                return(
                                    <input type="text"
                                    className='border-b border-gray-400 focus:outline-none border-black w-12 h-7 text-2xl  m-auto text-center' 
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
                    <div className=' font-semibold text-gray-400'>
                      <strong className='text-gray-900'>Não consegue ver? </strong>                   
                        Deslize para baixo ou acesse as configurações do dispositivo  para garantir que as notificações push estejam ativadas.
                    </div>
                    <div className='flex items-center justify-center gap-2 font-semibold text-gray-400'>
                      <span>Reenviar código em </span>
                      <Timer />
                    </div>
                 </div>
                 <Message/>
                 <div className='font-semibold text-primary'>
                  Perdi acesso a esse número
                 </div>
                  <button type='submit' className={`px-9 py-2 rounded font-semibold ${otp[otp.length -1]  ? 'bg-primary text-white' : 'bg-gray-200 text-gray-400'}`}>Continuar</button>
            </form>  
          </div>
      </div>
    </div>
  )
}

export default page
