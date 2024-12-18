import { HiDevicePhoneMobile, HiChevronRight } from "react-icons/hi2";
import AxiosInstance from "@/services/AxiosInstance";
import { toast } from "react-toastify";

import React from 'react'

const Message = () => {


    const handleSubmit = async (e) => {
        e.preventDefault();
        toast.success("O novo foi enviado para seu email")
     
    }

  return (
    <div className=" w-full px-7" onClick={handleSubmit}>
        <div className='border rounded-lg flex flex-col p-4 gap-4 hover:border-gray-400 cursor-pointer'>
            <div className="flex items-center space-x-1 justify-between">
               <div className="flex items-center space-x-1">
                    <div className="text-2xl text-primary"><HiDevicePhoneMobile /></div>
                    <h1 className='text-sm font-semibold'>Tente por mensagem de texto</h1>
               </div>
                <HiChevronRight />
            </div>
            <p className="text-xs font-semibold text-gray-400">Enviaremos uma mensagem de texto com um código de verificação.</p>    
        </div>
    </div>
  )
}

export default Message
