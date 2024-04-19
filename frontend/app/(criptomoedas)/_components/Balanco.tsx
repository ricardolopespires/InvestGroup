



import React from 'react'

const Balanco = () => {
  return (
    <div className="flex flex-col w-full space-y-2 ">
        <span className="text-md text-gray-500 ">Balanço total</span>            
        <div className="flex space-x-1 ">
            <span className="text-4xl font-semibold">R$ 24,975.00</span>
            <div className="text-sm relative top-[19px] font-semibold text-green-500">
                <span>+415,670</span>               
            </div>
        </div>
        <hr className="relative top-2"/>
    </div>  
  )
}

export default Balanco
