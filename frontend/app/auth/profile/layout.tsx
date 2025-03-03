"use client"

import Navbar from '@/app/(dashboard)/(routes)/dashboard/_components/navbar'
import AxiosInstance from '@/services/AxiosInstance'
import { useEffect } from 'react'
import { useRouter } from 'next/navigation'

import React from 'react'

const layout = ({children}) => {

  const jwt=localStorage.getItem('token')
  const user = JSON.parse(localStorage.getItem('user'))
  const router = useRouter();


   useEffect(() => {
     if (jwt === null && !user) {
         router.push('/auth/Sign-In')
     }
     
   }, [jwt, user])


  return (
    <main className="flex min-h-screen flex-col z-10 ">
      <Navbar/> 
      <section>
      {children}
 
      </section> 
    </main>
  )
}

export default layout