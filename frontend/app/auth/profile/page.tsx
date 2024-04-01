"use client"

import {  FaAddressCard } from "react-icons/fa";
import AxiosInstance from '@/services/AxiosInstance'
import { useEffect } from 'react'
import { useRouter } from 'next/navigation'


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
      <div className="flex items-center space-x-4">
      <div className="text-2xl text-yellow-500">< FaAddressCard/></div>
      <h1 className='text-2xl text-white'>Profile!</h1>
      </div>
      <p className='text-gray-500'>Informações geral do usuário!</p>
      </div>
      <div className="flex items-center justify-between space-x-4 w-full mx-auto h-screen mt-5">
        <div className="flex flex-col w-[20%] h-[90%] shadow-2xl bg-white rounded-2xl">

        </div>
        <div className="flex flex-col w-[80%] h-[90%] shadow-2xl bg-white rounded-2xl">

        </div>
      </div>
      {children}
    </div>
  )
}

export default page