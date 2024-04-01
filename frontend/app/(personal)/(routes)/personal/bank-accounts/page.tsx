import { FaWallet, FaChild,FaCreditCard, FaDollarSign, FaBarcode, FaHandHoldingUsd,FaRegCreditCard, FaCashRegister, FaCar, FaPlaystation     } from "react-icons/fa";

import Menu from "@/app/_components/menu";

import React from 'react'

const page = () => {
  return (
    <div className='absolute inset-x-0 top-[140px] h-full px-20'>
    <div className='flex flex-col '>
    <div className="flex items-center space-x-1">
    <div className="text-3xl text-yellow-500 mr-2"><FaWallet /></div>
    <h1 className='text-2xl text-white'>Finanças pessoais</h1>
    </div>
    <p className='text-gray-500 '>Tomar decisões financeiras começa com  a administração do seu próprio dinheiro.</p>
    </div>
      <Menu/>
      <div className="flex items-center justify-between space-x-4 w-full mx-auto h-screen mt-5  inset-x-0 ">  
        <div className="bg-wgite w-full h-40 shadow-xl rounded">4</div>
        <div className="bg-wgite w-full h-40 shadow-xl rounded">4</div>
        <div className="bg-wgite w-full h-40 shadow-xl rounded">4</div>
        <div className="bg-wgite w-full h-40 shadow-xl rounded">4</div>
      </div>
    </div>
  )
}

export default page