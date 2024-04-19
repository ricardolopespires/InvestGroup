
import { GoCheck } from "react-icons/go";


import React from 'react'

const Rewards = () => {
  return (
    <div className='flex flex-col w-full'>
        <div className='text-2xl font-semibold'>Recompensas</div>
        <div className='text-sm'>Tarefas completas recebem presentes</div>
        <div className="relative top-10  space-y-6">
            <div className='flex flex-col'>            
                <div className="flex space-x-2">
                    <div className="bg-primary text-white rounded-full p-1 absolute"><GoCheck /></div>
                    <div className="font-semibold relative left-5">Convide um amigo usando seu código</div>                
                </div>
                <div className="text-xs ml-7">+10.00 USDT</div>
            </div>
            <div className='flex flex-col '>            
                <div className="flex space-x-2">
                    <div className="bg-gray-400 text-white rounded-full py-1 px-2 text-xs absolute">7</div>
                    <div className="font-semibold relative left-5">Obtenha sua primeira crypto</div>                
                </div>
                <div className="text-xs ml-7">Bônus de 50% no seu próximo depósito</div>
            </div>
        </div>
      
      
    </div>
  )
}

export default Rewards
