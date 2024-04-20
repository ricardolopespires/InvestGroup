"use client"



import React from 'react'

import {data} from '@/data/portifoliodata'
import { useState } from 'react'
import {Pie} from "./Pie"

const Portifolio = () => {

    const [selected, setSelected] = useState('Portifolio')
  return (
    <div className='w-full h-[650px] bg-white rounded-xl shadow-xl'>
        <div className="flex flex-col w-full space-y-2 p-4">
            <span className="text-md text-gray-500 ">Total Investido</span>            
            <div className="flex space-x-1 ">
                <span className="text-4xl font-semibold">R$ 24,975.00</span>
                <div className="text-sm relative top-[19px] font-semibold text-green-500">
                    <span>+415,670</span>               
                </div>
            </div>
        <hr className="relative top-2"/>
        <main className='flex flex-col justify-center w-full items-center'>
        <select className='flex items-end'
          onChange={(e) => {
            setSelected(e.target.value)
          }}
        >
          <option value='Portifolio'>Total do Portifólio</option>
          <option value='Semanal'>
         Rentáveis desta semana
          </option>
        </select>
        <Pie data={data[selected]} />
      </main>
        </div>
    </div>
  )
}

export default Portifolio
