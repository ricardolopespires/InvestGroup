import Image from "next/image";

import Item from "./item";
import {planos }from "@/data/planos"
import React from 'react'

const[data, setData] = ([""])



const Lista = () => {
  return (
    <div className='absolute inset-0 px-20 top-[210px]' >
      <div className='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4'>  
      {planos.map((item, i)=>{
        return(
          <Item data={item} key={i}/>        )
      })}
      </div>
    </div>
  )
}

export default Lista
