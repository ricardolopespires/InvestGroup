



import React from 'react'

const Charts = () => {
  return (
    <div className="h-[290px] flex flex-col bg-white rounded-xl px-9 py-4  shadow-2xl mb-6">
    <div className="flex flex-col w-full space-y-2 ">
      <span className="text-md text-gray-500 ">Bitcoin USD (BTC-USD)</span>            
        <div className="flex space-x-1 ">
        <span className="text-4xl font-semibold">R$ 24,975.00</span>
          <div className="text-sm relative top-[19px] font-semibold text-green-500">
          <span>+415,670</span>
          <span>(4.57%)</span>
          </div>
        </div>
    </div>
  </div>
  )
}

export default Charts
