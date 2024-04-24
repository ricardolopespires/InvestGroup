
import Menu from "@/app/_components/menu";
import { FaWallet, FaPlaystation    } from "react-icons/fa";

import React from 'react'

const page = () => {
  return (
    <div className='absolute inset-x-0 top-[140px] h-full px-20'>
        <div className='flex flex-col '>
        <div className="flex items-center space-x-1">
        <div className="text-3xl text-yellow-500 mr-2"><FaWallet /></div>
        <h1 className='text-2xl text-white'>Planos pessoais</h1>
        </div>
        <p className='text-gray-500 '>Tomar decisões financeiras começa com  a administração do seu próprio dinheiro.</p>
        </div>
        <Menu/>
        <div className="relative flex items-center justify-between top-[50px] space-x-4">
        <div className="flex flex-col cursor-pointer bg-white space-y-5 border rounded-xl w-[50%] h-full p-6 shadow-sm hover:shadow-lg">             
            <div className="flex items-center space-x-1 ">
                <span className="bg-gray-200 p-3 rounded text-blue-900 shadow-lg">
                    <FaPlaystation />                
                </span>
                <span className="">
                    <div className="text-xl font-semibold">Monitor</div>
                    <div className="text-xs">Economia mensal: R$0.00</div>
                </span>
            </div>
            <div>
            <div className="flex items-center justify-between">
                <span className="font-semibold">R$ 0,00</span>
                <span className="text-xs">Meta: R$ 0,00</span> 
            </div>
            <span className="flex w-full h-[6px] bg-gray-200 rounded-full">
            <span className="w-[50%] h-[6px] bg-primary rounded-full"></span>
            </span>
            </div>
        </div> 
        <div className="flex flex-col cursor-pointer bg-white space-y-5 border rounded-xl w-[50%] h-full p-6 shadow-sm hover:shadow-lg">
        
        </div>
        </div>
    </div>
  )
}

export default page
