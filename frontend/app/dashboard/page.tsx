"use client"

import { AiOutlineRise, AiOutlineFall } from "react-icons/ai";
import { FaDoorOpen, FaUserTie } from "react-icons/fa";
import AxiosInstance from '@/services/AxiosInstance'
import { useEffect } from 'react'
import { useRouter } from 'next/navigation'
import Balance from "./_componentes/Balance"

import React from 'react'

const Page = ({children}) => {



  const jwt=localStorage.getItem('token')
  const user = JSON.parse(localStorage.getItem('user'))
  const router = useRouter();

 


   useEffect(() => {
     if (jwt === null && !user) {
         router.push('/auth/Sign-In')
     }else{
      if (user.perfil === false){
        router.push('/quiz/perfil')
      }
     }
     
   }, [jwt, user])


  return (
    <div className='absolute inset-x-0 top-[140px] h-16 px-20'>
      <div className='flex flex-col '>
      <div className="flex items-center space-x-4">
      <div className="text-2xl text-yellow-500"><FaDoorOpen/></div>
      <h1 className='text-2xl text-white'>Bem-vindo de volta, {user && user.full_name}!</h1>
      </div>
      <p className='text-gray-500'>Estamos aqui para ajudar a administrar seu dinheiro!</p>
      </div>
      <div className='absolute inset-x-0 top-[90px] h-full px-20'>
        <div className='flex flex-col '>
          <div className="flex items-center justify-between w-full h-10 text-white">
            <div className="flex flex-col ">
              <Balance/>
              <div className="flex items-center space-x-10 top-5">
                <span>11 April 2022</span>
                <div className="flex items-center space-x-2">
                <AiOutlineRise className="text-2xl text-green-500"/>
                <span>2,05%</span>
                </div>
                </div>
            </div>
            <div className="flex space-x-2 items-center h-10">
              <FaUserTie className="text-2xl"/>
              <span className="text-orange-500">Moderado</span>
            </div>
          </div>
            <div className="flex space-x-4 relative top-[60px]" >
              <div className="w-[70%] h-[400px] bg-white rounded-xl shadow-xl">

              </div>
              <div className="w-[30%] h-[400px] bg-white rounded-xl shadow-xl">

              </div>
            </div>
          

          </div>
        </div>
      {children}
    </div>
  )
}

export default Page