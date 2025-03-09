
import { FaRegBell,  } from "react-icons/fa";


import React from 'react'

const page = ({childrens}) => {
  return (
    
    <div className="flex flex-col gap-1" >
        <header className=' bg-[#1f1f2e] w-full h-16'>
            <div className='ml-20 mr-20 flex h-full items-center justify-between'>
                
                <div className="flex items-center gap-4 text-white">
                <img src={"/images/favicon.png"} alt="logotipo" className='w-[20px]' />
                        <ul className="flex items-center gap-4 text-sm">
                            <li>Crypto</li>
                            <li>Currency</li>
                            <li>Indexs</li>
                            <li>Commodities</li>
                        </ul>
                    </div>
                <div className='flex items-center gap-4'>                    
                    <FaRegBell className="text-2xl text-white"/>
                    <a href="dashboard/overview">
                        <button className='bg-white text-sm py-1 px-7 rounded-sm hover:bg-gray-200'>
                            Voltar
                        </button>
                    </a>                    
                </div>
            </div>
        </header>
        <div className="flex items-center w-full h-16 bg-[#1f1f2e]">
            <div className="w-1/6 bg-[#2a2a3c] h-full">

            </div>
            <div className="w-5/6">

            </div>
        </div>

    </div>
  )
}

export default page