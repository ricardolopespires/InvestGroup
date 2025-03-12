


import { ChartArea } from '@/components/ChartArea'
import { ChartBar } from '@/components/ChartBar'
import { ChartPie } from '@/components/ChartPie'
import React from 'react'

const page = ({children}) => {
  return (    
    <div className="flex min-h-svh items-center justify-center p-6">
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4 w-full ">      
      <ChartBar />  
      <ChartPie />
    </div>
  </div>
  )
}

export default page