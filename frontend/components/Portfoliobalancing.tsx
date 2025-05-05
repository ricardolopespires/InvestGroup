
import { HiOutlineAdjustmentsHorizontal } from "react-icons/hi2";

import {
    Card,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle,
  } from "@/components/ui/card"


import React from 'react'
import StockBalance from "./StockBalance"
import CryptoBalance from "./CryptoBalance";
import CurrenciesBalance from "./CurrenciesBalance";
import CommoditiesBalance from "./CommoditiesBalance";
import IsActiveBalancing from "./IsActiveBalancing";

const Portfoliobalancing = ({AdvisorId}) => {
  return (
    <Card className="w-full h-full">
        <CardHeader>
            <CardTitle >
              <div className="flex items-center justify-between gap-2">
                <div className="flex items-center gap-2">
                <HiOutlineAdjustmentsHorizontal className="text-xl text-blue-900"/>
                <span>Balaceamento de Portfólio</span>
                </div>
                <IsActiveBalancing AdvisorId={AdvisorId}/>
              </div>
             
            </CardTitle>
            <CardDescription>O balanceamento de portfólio é um processo de ajustar a alocação de ativos ou projetos.. </CardDescription>
        </CardHeader>
        <CardContent className="flex flex-col items-center gap-4">
            <StockBalance AdvisorId={AdvisorId} data={0}/>
            <CryptoBalance AdvisorId={AdvisorId} data={0}/>
            <CurrenciesBalance AdvisorId={AdvisorId} data={0}/>
            <CommoditiesBalance AdvisorId={AdvisorId} data={0}/>
        </CardContent>
      
        </Card>

  )
}

export default Portfoliobalancing