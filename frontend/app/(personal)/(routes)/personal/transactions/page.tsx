"use client"

import { FaWallet, FaSync, FaChild,FaCreditCard, FaDollarSign, FaBarcode, FaHandHoldingUsd,FaRegCreditCard, FaCashRegister, FaCar, FaPlaystation     } from "react-icons/fa";

import Menu from "@/components/dashboard/Menu/menu";
import Created from "./_components/modals/Created";
import Transactions from "./_components/tables/Transactions";
import React, { useState } from 'react'

const page = () => {


  const [showModal, setShowModal] = useState(false);


  return (
    <div className='absolute inset-x-0 top-[140px] h-full px-20'>
    <div className='flex flex-col '>
    <div className="flex items-center space-x-1">
    <div className="text-3xl text-yellow-500 mr-2"><FaWallet /></div>
    <h1 className='text-2xl text-white'>Finanças pessoais</h1>
    </div>
    <p className='text-gray-500 '>Tomar decisões financeiras começa com  a administração do seu próprio dinheiro.</p>
    </div>   
      <div className=" flex items-center justify-between">
      <Menu/>
      <button onClick={() => setShowModal(true)} className="flex items-center space-x-2 border hover:border-yellow-500 text-white mr-5 hover:bg-yellow-500 text-sm font-semibold rounded-xl px-6 py-2">
          <FaSync />
          <span>Nova transação</span>
        </button>
      </div>
    <Transactions/>  
    <Created isVisible={showModal}  onClose={() => setShowModal(false)}/>
    </div>
  )
}

export default page