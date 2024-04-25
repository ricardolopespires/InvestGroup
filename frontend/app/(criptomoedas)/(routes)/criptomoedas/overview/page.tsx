"use client"

import Exchange from "@/app/(criptomoedas)/_components/exchange";
import Balanco from "@/app/(criptomoedas)/_components/Balanco";
import Rewards from "@/app/(criptomoedas)/_components/Rewards";
import Noticias from "@/app/(criptomoedas)/_components/Noticias";
import Historicos from "@/app/(criptomoedas)/_components/Historicos";
import Charts from "@/app/(criptomoedas)/_components/Charts";
import { BiBitcoin } from "react-icons/bi";
import { useRouter } from 'next/navigation';
import { useEffect } from 'react';
import Menu from "@/components/dashboard/Menu/menu";
import React from 'react'
import Image from "next/image";
const Page = ({children}) => {

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
      <div className="text-3xl text-yellow-500"><BiBitcoin /></div>
      <h1 className='text-2xl text-white'>Criptomoedas</h1>
      </div>
      <p className='text-gray-500 '>Dados do Mercado de Criptomoedas.</p>
      </div>
      <Menu/>
      <div className="flex items-center justify-between space-x-4 relative top-9">       
        <div className="w-[75%] flex-col  ">
          <Charts/>
          <div className="flex items-center justify-between space-x-4">
          <Historicos/>
           <Noticias/>
          </div>
          
        </div>
        <div className="w-[25%] flex-col">
          <div className="flex flex-col justify-between bg-white rounded-xl px-4 py-4 shadow-2xl h-[790px]  mb-4">
            <Balanco/>
           <div className="absolute top-[140px] w-[400px]">
           <Exchange/>  
           </div>
            <div className="absolute top-[400px] w-[400px] border-t py-4 ">
              <Rewards/>
            </div>
          </div>         
        </div>  
     

      </div>
      {children}
    </div>
  )
}

export default Page