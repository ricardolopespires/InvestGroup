








import React, { useState } from 'react'
import ApiMetaTrader from './ApiMetaTrader'
import { FaPlus, FaReplyAll } from 'react-icons/fa'
import { Switch } from './ui/switch'


const PlataformsMetaTrader = () => {

    const [showModal, setShowModal] = useState(false)
  return (
    <div className="flex-1 space-y-4 px-20 -mt-16 z-20 text-white">
      <div className="flex flex-col items-center justify-between space-y-2 gap-4">
       <div className="w-full flex items-center justify-between">
          <a href="/settings/api" className=" text-4xl">
            <FaReplyAll />
          </a>
          <button className="flex items-center gap-2 py-2 px-6 rounded-sm bg-blue-900"
          onClick={()=> setShowModal(true)}>
            <FaPlus />
            <span className="text-sm ">Nova Api</span>
          </button>
       </div>
        <div className="grid sm:grid-cols-2 sm:gap-x-6 lg:grid-cols-3  w-full">
        <div className="mb-6 rounded-lg bg-white p-6 shadow w-full border">
              <div className="flex items-center justify-between">
                <div className="flex items-center">
                  <img className="mr-2 h-10 w-10  object-cover" src="https://s3.tradingview.com/userpics/36254724-gw8u_big.png" alt="profile" />
                  <div>
                    <h3 className="text-base font-semibold text-gray-900">Eightcap</h3>
                    <span className="block text-xs font-normal text-gray-500">Demo</span>
                  </div>
                </div>
                <p className="text-sm font-medium text-indigo-500">
                  <span className="mr-0.5">
                   <Switch/>
                  </span>
                </p>
              </div>
              <p className="my-6 text-sm font-normal text-gray-500">
                <div className="font-semibold">Login:<span></span></div>
                <div className="font-semibold">Password:<span></span></div>
                <div className="font-semibold">Server:<span></span></div>
                
              </p>
              <div className="mt-6 flex items-center justify-between text-sm font-semibold text-gray-900">
                <div className="flex">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" className="mr-2 h-5 w-5 text-base text-gray-500">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M6 6.878V6a2.25 2.25 0 012.25-2.25h7.5A2.25 2.25 0 0118 6v.878m-12 0c.235-.083.487-.128.75-.128h10.5c.263 0 .515.045.75.128m-12 0A2.25 2.25 0 004.5 9v.878m13.5-3A2.25 2.25 0 0119.5 9v.878m0 0a2.246 2.246 0 00-.75-.128H5.25c-.263 0-.515.045-.75.128m15 0A2.25 2.25 0 0121 12v6a2.25 2.25 0 01-2.25 2.25H5.25A2.25 2.25 0 013 18v-6c0-.98.626-1.813 1.5-2.122" />
                  </svg>
                  <span className="mr-1">40</span> Ativos
                </div>
                <div className="flex items-center">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" className="mr-1 h-5 w-6 text-yellow-500">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M11.48 3.499a.562.562 0 011.04 0l2.125 5.111a.563.563 0 00.475.345l5.518.442c.499.04.701.663.321.988l-4.204 3.602a.563.563 0 00-.182.557l1.285 5.385a.562.562 0 01-.84.61l-4.725-2.885a.563.563 0 00-.586 0L6.982 20.54a.562.562 0 01-.84-.61l1.285-5.386a.562.562 0 00-.182-.557l-4.204-3.602a.563.563 0 01.321-.988l5.518-.442a.563.563 0 00.475-.345L11.48 3.5z" />
                  </svg>
                  4,7 (750 Reviews)
                </div>
              </div>
        </div>
        </div>

      </div>
      < ApiMetaTrader isVisible={showModal} onClose={()=> setShowModal(false)}/>
      </div>
  )
}

export default PlataformsMetaTrader