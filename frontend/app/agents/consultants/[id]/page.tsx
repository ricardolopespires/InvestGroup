"use client"


import { useParams  } from 'next/navigation'
import Image from 'next/image';
import { CircularProgress } from '@/components/circular-progress';
import { SkillBar } from '@/components/skill-bar';
import { ChartPie, Percent, MapPin, Users, Table } from 'lucide-react';
import { ServiceCard } from '@/components/service-card';
import { FaReplyAll } from "react-icons/fa";
import { RiRobot2Line } from 'react-icons/ri';
import { Badge } from '@/components/ui/badge';
import { cn } from '@/lib/utils';
import React, { use, useEffect } from 'react';
import { getManagerId } from '@/lib/actions/actions.agents';
import AboutAgents from '@/components/AboutAgents';
import ChartsConsultants from '@/components/ChartsConsultants';
import Recommendations from '@/components/Recommendations';
import AgentReviews from '@/components/AgentReviews';

const page = () => {


  const { id } = useParams();
    
  const [tableData, setTableData] = React.useState("about");
  const [loading, setLoading] = React.useState(true);
  const [error, setError] = React.useState(null);
  const [agent, setAgent] = React.useState([]);



  useEffect(() => {
    const fetchData = async () => {     
        const response = await getManagerId({agentId:id});    
        setAgent(response);     
    };
    fetchData();
  }, [id]);



  return (
    <main className="flex flex-col min-h-screen  ">      {/* Sidebar */}
      <div className='flex items-center justify-between mt-28'>
        <a href="/agents/consultants">
            <div className='w-full h-9 items-center text-4xl   text-white'>
                <FaReplyAll/>
            </div>
        </a>        
      </div>   
        <div className="flex flex-col md:flex-row min-h-screen bg-white mt-10 z-50">
      {/* Sidebar */}
      <div className="w-full md:w-64 border-r  flex flex-col mb-[400px] bg-white">
        <div className="mb-6">
          <div className='flex items-center gap-4'>
            <div className="w-14 h-14  flex items-center justify-center text-2xl">
              <img src={`http://localhost:8000${agent.avatar}`} alt={agent.name} className="w-full h-full rounded-2xl object-cover" />
            </div>
            <div className='flex flex-col  mt-4'>
                <div className="flex flex-col items-start  mb-1">
                  <h2 className="text-xl font-semibold">{agent.name}</h2>
                  <Badge className="bg-amber-100 text-amber-800 hover:bg-amber-100 px-2 text-xs font-medium">{agent.asset}</Badge>
                </div>
                <div className="flex items-center gap-1 mb-4">
                  <div className="flex text-amber-400">
                    {"★".repeat(4)}
                    <span className="text-gray-300">{"★".repeat(0)}</span>
                  </div>
                  <span className="text-sm text-gray-600">{agent.rating} ({agent.reviews} reviews)</span>
            </div>
          </div>
          </div>
          <div className="space-y-4 mb-6 mt-4">
            <div className="flex items-center gap-2">
              <Users size={18} className="text-gray-500" />
              <div>
                <div className="font-medium">0</div>
                <div className="text-xs text-gray-500">Total Investidores</div>                
              </div>
            </div>

            <div className="flex items-center gap-2">
              <ChartPie size={18} className="text-gray-500" />
              <div>
                <div className="font-medium">R$ 0,00</div>
                <div className="text-xs text-gray-500">Valor de Alocações</div>
              </div>
            </div>

            <div className="flex items-center gap-2">
              <Percent size={18} className="text-gray-500" />
              <div>
                <div className="font-medium">0%</div>
                <div className="text-xs text-gray-500">Taxa média de retorno</div>
              </div>
            </div>
          </div>
       
        </div>
  
      </div>

      {/* Main Content */}
      <div className="flex-1 p-6">
        {/* Navigation */}
        <nav className="mb-8 border-b">
          <ul className="flex flex-wrap gap-6 text-sm cursor-pointer">
            <li className={cn(
                "pb-2", tableData=== "about" ? "border-b-2 border-green-600 font-medium":"text-gray-600")}
                onClick={() => setTableData("about")}>Sobre
            </li>
            <li className={cn(
                "pb-2", tableData=== "chats" ? "border-b-2 border-green-600 font-medium":"text-gray-600")}
                onClick={() => setTableData("chats")}>Chats
            </li>
            <li className={cn(
                "pb-2", tableData=== "recommendations" ? "border-b-2 border-green-600 font-medium":"text-gray-600")}
                onClick={() => setTableData("recommendations")}>Recomendações
            </li>          
            <li className={cn(
                "pb-2", tableData=== "notifications" ? "border-b-2 border-green-600 font-medium":"text-gray-600")}
                onClick={() => setTableData("notifications")}>Notificações
            </li>
            <li className={cn(
                "pb-2", tableData=== "Review" ? "border-b-2 border-green-600 font-medium":"text-gray-600")}
                onClick={() => setTableData("Review")}>Reviews
            </li>
            <li className={cn(
                "pb-2", tableData=== "Performace" ? "border-b-2 border-green-600 font-medium":"text-gray-600")}
                onClick={() => setTableData("Performace")}>Performace
            </li>
          </ul>
        </nav>
        {tableData === "about" ? <AboutAgents description={agent.description}/>:""}
        {tableData === "chats" ? <ChartsConsultants agent={agent}/>:""}
        {tableData === "recommendations" ? <Recommendations asset={agent.asset}/>:""}
        {tableData === "notifications" ? <div className="flex-1 p-6">Notificações</div>:""}
        {tableData === "Review" ? <AgentReviews Asset={agent.asset}/>:""}
        {tableData === "Performace" ? <div className="flex-1 p-6">Performace</div>:""}

       
      </div>
    </div>
        
      
                                            
  

  

      {/* Main Content */}
    
    </main>
  )
}

export default page


