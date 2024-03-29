import { BiBitcoin } from "react-icons/bi";
import { FaWallet } from "react-icons/fa";
import Menu from "./components/menu";

import React from 'react'

const Page = ({children}) => {
  return (
    <div className='absolute inset-x-0 top-[140px] h-16 px-20'>
      <div className='flex flex-col '>
      <div className="flex items-center space-x-1">
      <div className="text-3xl text-yellow-500 mr-2"><FaWallet /></div>
      <h1 className='text-2xl text-white'>Finanças pessoais</h1>
      </div>
      <p className='text-gray-500 '>Tomar decisões financeiras começa com  a administração do seu próprio dinheiro.</p>
      </div>
      <Menu/>
      <div className="flex items-center justify-between mt-14 space-x-4">
        <div className="w-full h-[190px] bg-white rounded-lg px-4 py-6 shadow-2xl">Total Balance</div>
        <div className="w-full h-[190px] bg-white rounded-lg px-4 py-6 shadow-2xl">Total Income</div>
        <div className="w-full h-[190px] bg-white rounded-lg px-4 py-6 shadow-2xl">Total Expends</div>

      </div>
      {children}
    </div>
  )
}

export default Page