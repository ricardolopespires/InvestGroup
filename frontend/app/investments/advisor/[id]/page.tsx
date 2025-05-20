"use client"


import { useParams  } from 'next/navigation'

import Image from "next/image"
import { Heart, MapPin, Clock, Users, ChevronDown } from "lucide-react"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import { Separator } from "@/components/ui/separator"

import React, { useEffect } from 'react'
import { FaReplyAll } from 'react-icons/fa';
import { cn } from '@/lib/utils'
import CategoriesAssets from '@/components/CategoriesAssets'
import AboutInvest from '@/components/AboutInvest'
import PortifolioInvest from '@/components/PortifolioInvest'
import SettingsInvest from '@/components/SettingsInvest'
import NotificationsInvest from '@/components/NotificationsInvest'
import ReviewInvest from '@/components/ReviewInvest'
import { RiRobot2Line } from 'react-icons/ri'
import IsActiveRobo from '@/components/IsActiveRobo'
import OperationsAdvisor from '@/components/OperationsAdvisor'
import PerformaceAdvisor from '@/components/PerformaceAdvisor'
import { getDetailAdvisors } from '@/lib/actions/actions.advisors'

const page = () => {


  const { id } = useParams();

  const [tableData, setTableData] = React.useState("about");
  const [advisor, setAdvisor] = React.useState({})
  const [loading, setLoading] = React.useState(true);
  const [error, setError] = React.useState(null);

  useEffect(() => {
    setLoading(true);
    const fetchAdvisor = async () => {
      try {
        const res = await getDetailAdvisors({AdvisorId:id});
        setAdvisor(res);
      } catch (error) {
        setError(error);
      } finally {
        setLoading(false);
      }
    };
    fetchAdvisor();
    setLoading(false);
  },[id]);
  
 
  return (
    <main className="flex flex-col min-h-screen  ">      {/* Sidebar */}
      <div className='flex items-center justify-between mt-28'>
        <a href="/investments/advisor">
            <div className='w-full h-9 items-center text-4xl   text-white'>
                <FaReplyAll/>
            </div>
        </a>
        <IsActiveRobo roboId={id}/>
      </div>
   
        <div className="flex flex-col md:flex-row min-h-screen bg-white mt-10 z-50">
      {/* Sidebar */}
      <div className="w-full md:w-64 border-r  flex flex-col mb-[400px] bg-white">
        <div className="mb-6">
          <div className='flex items-center gap-4'>
            <div className="w-14 h-14 bg-blue-950 rounded-2xl flex items-center justify-center text-2xl">
              <RiRobot2Line className="text-white w-9 h-9"/>
            </div>
            <div className='flex flex-col  mt-4'>
                <div className="flex items-center gap-2 mb-1">
                  <h2 className="text-xl font-semibold">Specter</h2>
                  <Badge className="bg-amber-100 text-amber-800 hover:bg-amber-100 px-2 text-xs font-medium">Iniciantes</Badge>
                </div>
                <div className="flex items-center gap-1 mb-4">
                  <div className="flex text-amber-400">
                    {"★".repeat(4)}
                    <span className="text-gray-300">{"★".repeat(1)}</span>
                  </div>
                  <span className="text-sm text-gray-600">4.6 (5 reviews)</span>
            </div>
          </div>
          </div>
          <div className="space-y-4 mb-6 mt-4">
            <div className="flex items-center gap-2">
              <Users size={18} className="text-gray-500" />
              <div>
                <div className="font-medium">220,000 Employees</div>
                <div className="text-xs text-gray-500">Headcount</div>
              </div>
            </div>

            <div className="flex items-center gap-2">
              <MapPin size={18} className="text-gray-500" />
              <div>
                <div className="font-medium">Redmond, WA, GMT-08:00</div>
                <div className="text-xs text-gray-500">Location & Timezone</div>
              </div>
            </div>

            <div className="flex items-center gap-2">
              <Clock size={18} className="text-gray-500" />
              <div>
                <div className="font-medium">€50-70/hour</div>
                <div className="text-xs text-gray-500">Average Hourly Rate</div>
              </div>
            </div>
          </div>
          <Button variant="outline" className="w-[90%] flex items-center justify-center gap-2 ">
            <Heart size={16} />
            <span>Favoritos</span>
          </Button>
           <CategoriesAssets items={advisor}/>
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
                "pb-2", tableData=== "Operations" ? "border-b-2 border-green-600 font-medium":"text-gray-600")}
                onClick={() => setTableData("Operations")}>Operações
            </li>
            <li className={cn(
                "pb-2", tableData=== "settings" ? "border-b-2 border-green-600 font-medium":"text-gray-600")}
                onClick={() => setTableData("settings")}>Settings
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

        { tableData === "about" ? <AboutInvest description={advisor.description}/>:""}
        { tableData === "Operations" ? <OperationsAdvisor/>:""}
        { tableData === "settings" ? <SettingsInvest AdvisorId={id}/>:""}
        { tableData === "notifications" ? <NotificationsInvest/>:""}
        { tableData === "Review" ? <ReviewInvest/>:""}
        { tableData === "Performace" ? <PerformaceAdvisor AdvisorId={undefined}/>:""}
      </div>
    </div>
        
      
                                            
  

  

      {/* Main Content */}
    
    </main>
  )
}

export default page

