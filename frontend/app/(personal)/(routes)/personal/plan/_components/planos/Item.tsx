import Image from 'next/image'
import { FaPlaystation } from "react-icons/fa";



import React from 'react'

const Item = ({item}) => {
  return (
    <a href={`plan/${item.id}/`}>
        <div className="flex flex-col cursor-pointer bg-white space-y-5 border rounded-xl w-full h-full p-6 shadow-sm hover:shadow-lg">             
            <div className="flex items-center space-x-1 ">
                <span className="bg-gray-200 p-3 rounded text-blue-900 shadow-lg">
                    <FaPlaystation />                
                </span>
                <span className="">
                    <div className="text-xl font-semibold">{ item.nome }</div>
                    <div className="text-xs">Economia mensal: R$ {item.economia}</div>
                </span>
            </div>
            <div>
            <div className="flex items-center justify-between">
                <span className="font-semibold">R$ {item.quantia}</span>
                <span className="text-xs">Meta: R$ { item.meta }</span> 
            </div>
            <span className="flex w-full h-[6px] bg-gray-200 rounded-full">
            <span className="h-[6px] bg-primary rounded-full"  style={{ width: `${item.percent}%` }}></span>
            </span>
            </div>
        </div>    
    </a>
  )
}

export default Item
