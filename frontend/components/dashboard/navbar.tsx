
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"

import { FaSignInAlt, FaRegUserCircle } from "react-icons/fa";
import Logout from "../../app/auth/Logout/page";
import NavbarRoutes from './navbar-routes'
import Image from 'next/image'


import React from 'react'
const user = JSON.parse(localStorage.getItem('user'))

const Navbar = () => {

  return (
  <section className="bg-[url('/images/banner.png')] h-[400px] flex flex-col w-full text-gray-400 cursor-pointer relative z-0 rounded-b-xl">
      <header className='w-full flex items-center justify-between px-20 h-[90px] '>
     <div className="flex items-center w-full">
          <a href="/" className="top-[-10px] relative">
            <Image
          src={"/images/favicon.png"}
          width={20}
          height={20}
          alt='logo'/>
          </a>
          <NavbarRoutes/>
     </div>
     <div className="flex items-center space-x-4 text-2xl ">      
      <a href="/settings/overview" className="text-green-500">
        <Avatar>
          <AvatarImage src="https://github.com/shadcn.png" />
          <AvatarFallback>CN</AvatarFallback>
        </Avatar>
      </a>
     <Logout/>
     
     </div>
    </header>

  </section>
  )
}

export default Navbar
