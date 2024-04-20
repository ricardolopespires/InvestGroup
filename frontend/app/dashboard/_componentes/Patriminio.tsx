"use client"
import React from 'react'
import {data} from "@/data/data"
import {Line} from "./line"
import { ResponsivePie } from '@nivo/pie'

const Patriminio = () => {

    
  return (
    <div className='w-full h-[650px] bg-white rounded-xl shadow-xl'>
        <div className="flex flex-col w-full space-y-2 px-9 py-4">
            <span className="text-md text-gray-500 ">Total do Patrimonio</span>            
            <div className="flex space-x-1 ">
                <span className="text-4xl font-semibold">R$ 24,975.00</span>
                <div className="text-sm relative top-[19px] font-semibold text-green-500">
                    <span>+415,670</span>
                    <span>(4.57%)</span>
                </div>
             </div>
             <div>
                <Line data={data}/>
             </div>
        </div>
    </div>
  )
}

export default Patriminio
