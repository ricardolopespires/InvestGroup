

import { linksHome } from '@/constant/Constant'
import React from 'react'
import { CgClose } from 'react-icons/cg'

type Props ={
  showNav: boolean,
  closeNav: () => void,
}


const Mobile = ({closeNav, showNav}:Props) => {

  const navOpen = showNav?'translate-x-0':'translate-x-[-100%]';
  const navClosed = showNav? '-translate-x-full' : 'translate-x-0';

  return (
    <div>
      {/* overlay */}
      <div className={`fixed inset-0 transform transition-all duration-500 z-[10000] bg-black  opacity-70 w-full h-screen
        ${navOpen}`}>
      
      </div>
      {/* NavLinks */}
      <div className={`text-white fixed justify-center flex flex-col h-full transform transition-all duration-200
      w-[80%] sm:w-[60%] bg-indigo-900 space-y-6 z-[10006] ${navOpen}`}>
         {/* Links */}        
            {linksHome.map((link) => (
              <a href={link.url} key={link.id} className="link text-white text-[20px] ml-12 border-b-[1.5]
              pb-1 border-white sm:text-[30px]">{link.label}</a>
            ))}
               {/* Close icon*/}
      <CgClose onClick={closeNav} className="absolute top-[0.7rem] right-[1.4rem] sm:w-8 w-6 h-6 cursor-pointer"/>       
      </div>
   
    </div>
  )
}

export default Mobile
