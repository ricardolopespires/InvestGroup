import { BiBitcoin } from "react-icons/bi";
import Menu from "./components/menu";

import React from 'react'

const Page = ({children}) => {
  return (
    <div className='absolute inset-x-0 top-[140px] h-16 px-40'>
      <div className='flex flex-col '>
      <div className="flex items-center space-x-1">
      <div className="text-3xl text-yellow-500"><BiBitcoin /></div>
      <h1 className='text-2xl text-white'>Criptomoedas</h1>
      </div>
      <p className='text-gray-500 '>Dados do Mercado de Criptomoedas.</p>
      </div>
      <Menu/>
      {children}
    </div>
  )
}

export default Page