


import { ChartArea } from '@/components/ChartArea'
import { ChartBar } from '@/components/ChartBar'
import { ChartPie } from '@/components/ChartPie'
import React from 'react'

const page = ({children}) => {
  return (    
    <div className="max-w-screen-2xl mx-auto w-full pb-10 mt-24">
    <div className="grid grid-cols-1 lg:grid-cols-3 gap-4 w-full ">      
      <ChartBar />  
      <ChartPie />
    </div>
  </div>
  )
}

export default page