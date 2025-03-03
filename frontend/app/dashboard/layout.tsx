"use client"

import Navbar from '@/components/dashboard/navbar'
import AxiosInstance from '@/services/AxiosInstance'
import { useEffect } from 'react'
import { useRouter } from 'next/navigation'
import Menu from "@/components/dashboard/menu/menu";
import { FaDoorOpen } from "react-icons/fa";

import React from 'react'

const layout = ({children}) => {

  const jwt=localStorage.getItem('token')
  const user = JSON.parse(localStorage.getItem('user'))
  const perfil = JSON.parse(localStorage.getItem('perfil'))
  const situation = JSON.parse(localStorage.getItem('situation'))
  const router = useRouter();


   useEffect(() => {
     if (jwt === null && !user) {
         router.push('/auth/Sign-In')
     }
      if (perfil === false) {
          router.push('/quiz/perfil')
      }
      if (situation === false) {
        router.push('/quiz/situation')
    }
     
   }, [jwt, user, perfil])


  return (
    <main className="flex min-h-screen flex-col z-10 ">
      <Navbar/>   
      <section className='absolute inset-x-0 top-[70px] h-screen px-20'>
      
      </section> 
      </main>
    )
};


export default  layout