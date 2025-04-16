"use client"

import CardAdvisor from "@/components/CardAdvisor"
import { ChartPie } from "@/components/ChartPie"
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { ScrollArea, ScrollBar } from "@/components/ui/scroll-area"
import { getListAdvisors } from "@/lib/actions/actions.advisors"
import { cn } from "@/lib/utils"

import React, { useEffect } from 'react'

const page = () => {
    const [seleted, setSelected] = React.useState("lucro")
    const [advisors, setAdvisors] = React.useState([])   


    useEffect(() => {
        const feachtData = async () => {
            const res = await getListAdvisors()
            setAdvisors(res)  


        }
        feachtData()
    }, [])


  return (
    <div className="max-w-screen-4xl mx-auto w-full pb-10 mt-24 ">
        <div className="flex items-center justify-end gap-2 mb-10 text-xs">            
            <button className={cn("",
                seleted==="lucro" ? "bg-gray-100 py-2.5 px-6 rounded-l-sm":"border text-white rounded-l-sm py-2 px-6")}
                onClick={() => setSelected("lucro")}>Lucro</button>
            <button className={cn(
                seleted==="performace" ? "bg-gray-100 py-2.5 px-6 rounded-r-sm":"text-white border rounded-r-sm py-2 px-6")} onClick={() => setSelected("performace")}>Performace</button>
        </div>
        {advisors.map((item, i )=>{

          return(
            <div className="grid grid-cols-1 md:grid-cols-4 gap-4" key={i}>
              <CardAdvisor item={item}/>    
            </div>
          )
        })} 
        
    </div>
  )
}

export default page
