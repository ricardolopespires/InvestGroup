
import { FaSignInAlt, FaRegUserCircle } from "react-icons/fa";
import NavbarRoutes from './navbar-routes'
import Image from 'next/image'


import React from 'react'

const Navbar = () => {
  return (
  <section className="bg-[url('/images/banner.png')] h-[400px] flex flex-col w-full text-gray-400 cursor-pointer relative z-0 rounded-b-xl">
      <header className='w-full flex fixed items-center justify-between px-20 h-[90px] '>
     <div className="flex items-center w-full">
          <a href="/" className="mt-[-15px]">
            <Image
          src={"/images/favicon.png"}
          width={15}
          height={20}
          alt='logo'/>
          </a>
          <NavbarRoutes/>
     </div>
     <div className="flex items-center space-x-4 text-2xl ">      
     <span className="text-green-500"><FaRegUserCircle /></span>
     <span className="hover:text-white"><FaSignInAlt/></span>
     </div>
    </header>

  </section>
  )
}

export default Navbar