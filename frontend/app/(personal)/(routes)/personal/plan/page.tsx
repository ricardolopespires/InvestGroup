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

    </div>
  )
}

export default page