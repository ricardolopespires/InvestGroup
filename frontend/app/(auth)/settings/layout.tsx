"use client"

import { useEffect } from 'react'
import { useRouter } from 'next/navigation'
import Navbar from '@/components/dashboard/navbar'


const Layout = ({children}) => {


    const jwt=localStorage.getItem('token')
    const user = JSON.parse(localStorage.getItem('user'))
    const router = useRouter();

   

   useEffect(() => {

     if (jwt === null && !user) {
         router.push('/Sign-In')

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

export default Layout
