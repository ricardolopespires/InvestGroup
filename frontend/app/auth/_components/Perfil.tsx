import { FaMoneyCheckDollar } from "react-icons/fa6";
import { TbMapPinDollar } from "react-icons/tb";


import React from 'react'

const Perfil = () => {
  return (
    <div className='flex flex-col px-10 relative top-[20px]'>
    <div className="flex items-center space-x-1">
      <div className="text-2xl text-primary"><TbMapPinDollar /></div>
      <h1 className='text-2xl '>Perfil do Investidor</h1>

      </div>
    </div>
  )
}

export default Perfil
