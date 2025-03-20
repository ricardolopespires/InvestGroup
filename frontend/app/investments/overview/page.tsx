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

import React from 'react'

const page = () => {
  return (
    <div className="max-w-screen-4xl mx-auto w-full pb-10 mt-24 text-white">
      <div className="flex gap-4 h-[600px]">        
        <div className="w-4/5 ">
          <Card className="w-full h-full">
            <CardHeader>
              <div className="flex items-center justify-between">
                <div className="mb-4 flex  items-start justify-start gap-6 w-full">
                  <div>
                    <div className="mb-1 text-sm text-gray-500">Total Portfolio</div>
                    <div className="flex items-center gap-2">
                      <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-teal-100">
                        <svg viewBox="0 0 24 24" className="h-5 w-5 text-teal-600" fill="none" stroke="currentColor">
                          <path
                            d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                            strokeWidth="2"
                            strokeLinecap="round"
                            strokeLinejoin="round"
                          />
                        </svg>
                      </div>
                      <span className="text-3xl font-semibold">$145,628.01</span>
                    </div>
                  </div>
             

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
