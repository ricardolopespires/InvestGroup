"use client"

import { accordionData } from '@/constant/Constant'
import React, { useState } from 'react'
import AccordionItem from './AccordionItem'

const Accordion = () => {

    const[open, setOpen] = useState(false)

    const toggle = (index)=>{
        if(open === index){
            return setOpen(null)
        }
        return setOpen(index)
    }


  return (
    <div className="flex items-center justify-center py-20 ">
      <div className="flex flex-col w-full max-w-7xl text-center gap-6">
        <h1 className="text-2xl md:text-3xl font-bold capitalize text-gray-800">
          Perguntas frequentes
        </h1>
        <div className="px-6 md:px-10">
          {accordionData.map((item, i) => (
            <div key={i} className="w-full mb-4">
              <AccordionItem open={i === open } toggle={() => toggle(i)} title={item.title} desc={item.desc} />
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}

export default Accordion
