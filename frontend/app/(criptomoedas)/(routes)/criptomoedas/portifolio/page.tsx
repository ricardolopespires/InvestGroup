"use client"

import AxiosInstance from '@/services/AxiosInstance'
import { BiBitcoin } from "react-icons/bi";
import { useRouter } from 'next/navigation';
import { useEffect } from 'react';
import Menu from "@/components/dashboard/Menu/menu";

import React from 'react'

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
      {children}
    </div>
  )
}

export default Page