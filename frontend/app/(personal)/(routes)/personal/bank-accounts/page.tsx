"use client"
import { FaWallet, FaChild,FaCreditCard, FaDollarSign, FaBarcode, FaHandHoldingUsd,FaRegCreditCard, FaCashRegister, FaCar, FaPlaystation     } from "react-icons/fa";


import AxiosInstance from '@/services/AxiosInstance'
import { useEffect } from 'react'
import { useRouter } from 'next/navigation'
import Menu from "@/app/_components/menu";

import React from 'react'

const page = ({children}) => {



  const jwt=localStorage.getItem('token')
  const user = JSON.parse(localStorage.getItem('user'))
  const router = useRouter();


   useEffect(() => {
     if (jwt === null && !user) {
         router.push('/auth/Sign-In')
     }
     
   }, [jwt, user])


  return (
    <div className='absolute inset-x-0 top-[140px] h-16 px-20'>
      <div className='flex flex-col '>
        <div className="flex items-center space-x-1">
        <div className="text-3xl text-yellow-500 mr-2"><FaWallet /></div>
        <h1 className='text-2xl text-white'>Finanças pessoais</h1>
        </div>
        <p className='text-gray-500 '>Tomar decisões financeiras começa com  a administração do seu próprio dinheiro.</p>
      </div>
      <Menu/>
      <div className="flex items-center justify-between space-x-4 w-full mx-auto h-screen mt-5">
        <div className="flex flex-col w-[94%] mt-[190px] absolute inset-y-0 ">
          <div className="flex items-center space-x-2">
            <div className="bg-white w-[75%] h-[490px] rounded shadow-xl p-6 ">
            <div className="flex items-center justify-between">
              <div className="text-2xl font-semibold">Visão geral do pagamento</div>              
              <div className="space-x-2">
                <span>Ordenar por</span>
                <select name="" id="" className="border p-1 rounded text-sm">
                  <option value="">Semana passada</option>
                  <option value="">Mês passado</option>
                  <option value="">Ano passado</option>
                </select>
              </div>
            </div>
            <div className="border-b border-dashed border-indigo-200 mt-6"></div>
            </div>
            <div className="bg-white w-[25%] h-[490px] rounded shadow-xl p-6 ">
            <div className="text-2xl font-semibold  ">Saldo da conta</div>
            <div className="border-b border-dashed border-indigo-200 mt-6"></div>
             
            </div>           
          </div>
        </div>
     
      </div>
      {children}
    </div>
  )
}

export default page