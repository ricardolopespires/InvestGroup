
import {
    Card,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle,
  } from "@/components/ui/card"
  

  import { AiFillDashboard } from "react-icons/ai";

import React, { useEffect } from 'react'
import { cn } from "@/lib/utils";
import SliderQtOperations from "./SliderQtOperations";
import SliderRiskOperations from "./SliderRiskOperations";
import Breakeven from "./breakeven";
import { getRiskAdvisors } from "@/lib/actions/actions.advisors";


const RiskAdvisor = ({AdvisorId}) => {

  const [risk, setRisk] = React.useState({})
  const [loading, setLoading] = React.useState(true)
  const [error, setError] = React.useState(null)
  

  useEffect(() => {
    const fecthRisk = async () => {
      const res = await getRiskAdvisors({AdvisorId:AdvisorId});
      setRisk(res)
      setLoading(false)
    };
    fecthRisk();
  }, [AdvisorId]);
  
  return (
    <Card className="w-[45%]">
        <CardHeader>
            <CardTitle className="flex items-center gap-2">
                <AiFillDashboard className="text-xl text-blue-900"/>
                <span>Gereciamento de Risco</span>
            </CardTitle>
            <CardDescription>Gerenciamento de risco visa proteger o capital e evitar perdas significativas</CardDescription>
        </CardHeader>
        <CardContent>
            <div className="text-sm text-gray-500 flex flex-col gap-5">
            <SliderRiskOperations AdvisorId={AdvisorId} data={risk?.level}/>            
            <SliderQtOperations AdvisorId={AdvisorId} data={risk?.amount}/>
            <Breakeven AdvisorId={AdvisorId} data={risk?.breakeven}/>
            </div>
        </CardContent>
        <CardFooter>
            <p>Card Footer</p>
        </CardFooter>
        </Card>

  )
}

export default RiskAdvisor