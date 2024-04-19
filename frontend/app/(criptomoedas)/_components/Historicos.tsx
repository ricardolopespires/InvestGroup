
import Image from 'next/image'
import React from 'react'

const Historicos = () => {
  return (
    <div className="bg-white rounded-xl px-4 py-4 shadow-2xl h-[490px] w-[40%]">
    <div>
      <h1 className="font-semibold py-6 px-2">Histórico de transações</h1>
      <div className="flex flex-col space-y-4">
        <div className="flex items-center justify-between text-sm py-4 border-b">
            <div className="flex items-center space-x-4 ">
              <Image src={"/images/Bitcoin.png"} width={60} height={60} alt="bitcoin" />
              <div className="flex flex-col">
                  <div className="font-semibold">Bitcoin</div>
                  <div className="text-xs text-gray-400 font-semibold">Buy</div>
              </div> 
            </div>               
            <div className="flex flex-col items-center justify-end">
                <div className="font-semibold text-green-500"> +0,004 BTC</div>
                <div className="text-xs">09:22 PM</div> 
            </div>
        </div>
        <div className="flex items-center justify-between text-sm py-4 border-b">
            <div className="flex items-center space-x-4 ">
              <Image src={"/images/Ethereum.png"} width={50} height={50} alt="bitcoin" />
              <div className="flex flex-col">
                  <div className="font-semibold">Ethereum</div>
                  <div className="text-xs text-gray-400 font-semibold">Buy</div>
              </div> 
            </div>               
            <div className="flex flex-col items-center justify-end">
                <div className="font-semibold text-green-500"> +0,004 BTC</div>
                <div className="text-xs">09:22 PM</div> 
            </div>
        </div>
      </div>
    </div>
  </div>
  )
}

export default Historicos
