"use client"


import Menu from '@/components/dashboard/menu/menu'
import Navbar from '@/components/dashboard/navbar'
import React from 'react'

const layout = ({children}) => {


   


  return (
    <main className="flex min-h-screen flex-col z-10 ">
    <Navbar/>   
    <section className='absolute inset-x-0 top-[50px] h-screen px-20'>
    <Menu/>
    </section>
    {children} 
    </main>
  )
}

export default layout