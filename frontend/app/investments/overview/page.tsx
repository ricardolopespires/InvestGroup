import ChartBaseline from "@/components/ChartBaseline"
import { ChartPie } from "@/components/ChartPie"
import TotalPortfolio from "@/components/TotalPortfolio"
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { ScrollArea, ScrollBar } from "@/components/ui/scroll-area"
import { data } from "@/utils/summary"

import React from 'react'

const page = () => {
  return (
    <div className="max-w-screen-4xl mx-auto w-full pb-10 mt-24 text-white">
      <div className="flex gap-4 h-[600px]">        
        <div className="w-4/5 ">
          <Card className="w-full h-full">
            <CardHeader>
              <div className="flex items-center justify-between">
                <div className="mb-4 flex flex-col  items-start justify-start gap-6 w-full">
                  <TotalPortfolio/>
                  <ChartBaseline
                  data={data}
                  inicial={10000} // Set baseline value
                  valueKey="close" // Use 'close' price for the chart
                  />
                </div>
              </div>
            </CardHeader>
            <CardContent>
            </CardContent>
          </Card>
        </div>
        <div className="w-1/5 h-full">
          <ChartPie />
        </div>
      </div>
    </div>
  )
}

export default page
