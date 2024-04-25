"use client"

import { FaWallet, FaBarcode,FaHandHoldingUsd,FaRegCreditCard, FaCar, FaPlaystation } from "react-icons/fa";
import Transactions from "../transactions/_components/tables/Transactions";
import Movimentacao from "./_components/Movimentacao";
import Balanco from "./_components/Balanco";
import Menu from "@/components/dashboard/Menu/menu";
import Lista from "../plan/_components/planos/List";
import React from 'react'

const Page = ({children}) => {
  return (
    <div className='absolute inset-x-0 top-[140px] h-screen px-20 w-full'>
      <div className='flex flex-col '>
      <div className="flex items-center space-x-1">
      <div className="text-3xl text-yellow-500 mr-2"><FaWallet /></div>
      <h1 className='text-2xl text-white'>Finanças pessoais</h1>
      </div>
      <p className='text-gray-500 '>Tomar decisões financeiras começa com  a administração do seu próprio dinheiro.</p>
      </div>
      <Menu/>
      <div className="flex items-center justify-between space-x-4 absolute  top-[199px] inset-0 h-screen px-20">
        <div className="w-[25%] flex-col relative h-full">
          <Balanco/>
          <div className="flex flex-col bg-white rounded-xl px-4 py-4 shadow-2xl ">
            <h1 className="font-semibold py-6 px-2">Salvando planos</h1>
            <div className="flex flex-col space-y-6">
              <div className="flex flex-col justify-between border rounded-xl w-full h-40 p-6 shadow-sm hover:shadow-lg">             
              <div className="flex items-center space-x-2 ">
                  <span className="bg-gray-200 p-3 rounded text-blue-900 shadow-lg">
                    <FaCar />                
                  </span>
                  <span className="">
                    <div className="text-xl font-semibold">Obter carro novo</div>
                    <div className="text-xs">Economia mensal: R$0.00</div>
                  </span>
              </div>
              <div className="flex items-center justify-between">
                <span className="font-semibold">R$ 0.00</span>
                <span className="text-xs">Meta: R$ 0.00</span> 
              </div>
              <span className="flex w-full h-[6px] bg-gray-200 rounded-full ">
                <span className="w-[20%] h-[6px] bg-lime-600 rounded-full"></span>
              </span>
              </div>
              
            </div>
          </div>
        </div>
        <div className="w-[75%] flex-col flex-col relative  h-full ">
        <Movimentacao/>
         <Transactions/>
        </div>   
     

      </div>
      {children}
    </div>
  )
}

export default Page