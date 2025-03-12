
import { data } from "@/constant/Constant"





import React from 'react'
import AnalyticsTrading from './AnalyticsTrading'

const CardAnalytics = ({selected}) => {
  return (
    <section className='flex flex-col ml-1 mr-1'>
        <header className='w-full h-11 flex items-center  bg-[#151928]'>

        </header>
        <AnalyticsTrading data={data}/> 
    </section>
  )
}

export default CardAnalytics