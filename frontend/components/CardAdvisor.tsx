
import { RiRobot2Line } from "react-icons/ri";













import React, { useEffect, useState } from 'react'
import { formatDayAndMonth } from "@/lib/utils";
import { getLevelAdvisors } from "@/lib/actions/actions.advisors";

const CardAdvisor = ({item}) => {

    const[level, setLevel] =  useState({})

        useEffect(() => {
            const feachtData = async () => {
                const res = await getLevelAdvisors({AdvisorId:item.id})
                setLevel(res[0])  
    
    
            }
            feachtData()
        }, [item])
     
    
  return (
    <a href={`/investments/advisor/${item.id}`}>
        <div className="bg-white rounded-xl border p-4 mb-2 shadow-lg hover:shadow-xl transition-shadow duration-300">
        <div className="flex justify-between items-center">
                <div className="flex items-center space-x-2">
                    <div className="w-12 h-12 bg-blue-950 rounded-2xl flex items-center justify-center text-2xl">
                    <RiRobot2Line className="text-white"/>
                    </div>
                    <div className="c-details">
                    <h6 className="text-base font-semibold mb-0">{item.name}</h6>
                    <span className="text-xs font-light">{formatDayAndMonth(item.created_at)}</span>
                    </div>
                </div>
                <div className="badge">
                    {item.asset == 1 ? <span className="bg-green-50 text-green-700 px-3 py-1 rounded-md text-sm">Ações</span>:""}
                    {item.asset == 2 ? <span className="bg-amber-50 text-amber-700 px-3 py-1 rounded-md text-sm">Commodities</span>:""}
                    {item.asset == 3 ? <span className="bg-blue-50 text-blue-700 px-3 py-1 rounded-md text-sm">Moedas</span>:""}
                    {item.asset == 4 ? <span className="bg-gray-50 text-gray-700 px-3 py-1 rounded-md text-sm">Índices</span>:""}
                    {item.asset == 5 ? <span className="bg-yellow-50 text-yellow-600 px-3 py-1 rounded-md text-sm">CriptoMeodas</span>:""}
                </div>
        </div>
        <div className="mt-6">
            <h3 className="flex flex-col font-ligth leading-tight">
                    <span className="text-gray-400">Investidor</span>
                    <span className="text-xl ">
                        {level.risk_level === 1 ? "Conservador":""}
                        {level.risk_level === 2 ? "Moderado":""}
                        {level.risk_level === 3 ? "Agressivo":""}
                        {level.risk_level === 4 ? "Ulta - Agressivo":""}
                    </span>
            </h3>
            <div className="mt-6">
                    <div className="w-full bg-gray-200 rounded-full h-2.5">
                    <div className="bg-red-500 h-2.5 rounded-full w-1/2"></div>
                    </div>
                    <div className="mt-3">
                    <span className="text-sm font-semibold">
                        32 Profit <span className="text-gray-500 font-normal">de 40 Operação</span>
                    </span>
                    </div>
            </div>
        </div>
        </div>
    </a>
  )
}

export default CardAdvisor