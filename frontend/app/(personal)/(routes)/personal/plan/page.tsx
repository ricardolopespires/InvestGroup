"use client"

import { FaWallet, FaChild,FaCreditCard, FaDollarSign, FaBarcode, FaHandHoldingUsd,FaRegCreditCard, FaCashRegister, FaCar, FaPlaystation     } from "react-icons/fa";
import Menu from "@/app/_components/menu";
import React, { useState } from 'react'
import Created from "./_components/modals/Created";
import Lista from "./_components/List";


const page = () => {

  const [showModal, setShowModal] = useState(false);
  return (
    <div className='absolute inset-x-0 top-[140px] h-full px-20'>
    <div className='flex flex-col '>
    <div className="flex items-center space-x-1">
    <div className="text-3xl text-yellow-500 mr-2"><FaWallet /></div>
    <h1 className='text-2xl text-white'>Planos pessoais</h1>
    </div>
    <p className='text-gray-500 '>Tomar decisões financeiras começa com  a administração do seu próprio dinheiro.</p>
    </div>
    <Menu/>
    <div className="relative flex items-center justify-end top-[-20px]">
      <button onClick={() => setShowModal(true)} className="flex items-center space-x-2 border hover:border-yellow-500 text-white mr-5 hover:bg-yellow-500 text-sm font-semibold rounded-xl px-6 py-2">       
      <span>Novo Plano</span>
      </button>
    </div>
    <Lista/>

    <Created isVisible={showModal}  onClose={() => setShowModal(false)}/>
    </div>
  )
}

export default page