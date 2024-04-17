import { HiMiniArrowLeftOnRectangle } from "react-icons/hi2";
import { FaSignInAlt } from "react-icons/fa";
import NavbarRoutes from './navbar-routes'
import Image from 'next/image'


import React from 'react'

const Navbar = () => {
  return (
    <section className='w-full flex  bg-white shadow-2xl fixed items-center justify-between px-40'>
    <div className="p-6 ">
        <div className='w-full h-full'>
            <a href="/"><Image
            src={"/images/logo.png"}
            width={140}
            height={140}
            alt='logo'/></a>
        </div>        
    </div>
    <div className=" flex items-center space-x-4">
        <NavbarRoutes/>
        <a href="/auth/Sign-In"><HiMiniArrowLeftOnRectangle className="mr-20 text-2xl hover:text-4xl"/></a>
    </div>     
    </section>
  )
}

export default Navbar