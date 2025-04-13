
import { RiRobot2Line } from "react-icons/ri";













import React from 'react'

const CardAdvisor = () => {
  return (
    <a href="/investments/advisor/4">
        <div className="bg-white rounded-xl border p-4 mb-2 shadow-lg hover:shadow-xl transition-shadow duration-300">
        <div className="flex justify-between items-center">
                <div className="flex items-center space-x-2">
                    <div className="w-12 h-12 bg-blue-950 rounded-2xl flex items-center justify-center text-2xl">
                    <RiRobot2Line className="text-white"/>
                    </div>
                    <div className="c-details">
                    <h6 className="text-base font-semibold mb-0">Mailchimp</h6>
                    <span className="text-xs font-light">1 days ago</span>
                    </div>
                </div>
                <div className="badge">
                    <span className="bg-green-50 text-green-500 px-3 py-1 rounded-md text-sm">Ações</span>
                </div>
        </div>
        <div className="mt-6">
            <h3 className="text-xl font-ligth leading-tight">
                    Senior Product<br />Designer-Singapore
            </h3>
            <div className="mt-6">
                    <div className="w-full bg-gray-200 rounded-full h-2.5">
                    <div className="bg-red-500 h-2.5 rounded-full w-1/2"></div>
                    </div>
                    <div className="mt-3">
                    <span className="text-sm font-semibold">
                        32 TrakeProfit <span className="text-gray-500 font-normal">de 40 Operação</span>
                    </span>
                    </div>
            </div>
        </div>
        </div>
    </a>
  )
}

export default CardAdvisor