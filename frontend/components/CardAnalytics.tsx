






import React, { useEffect, useState } from 'react'
import AnalyticsTrading from './AnalyticsTrading'
import { getHistoryAssets } from "@/lib/actions/actions.trading"

const CardAnalytics = ({selected}) => {
    const [time,setTime] = useState("1")
    const [data, setData] = useState({
        prices: [],
        signals: []
    })

    useEffect(() => {
      const fetchData = async () => {
        
        const res = await getHistoryAssets({symbol:selected.symbol, period:time})
        setData(res)
      }
      fetchData();
    } ,[selected,time])
    

  return (
    <section className='flex flex-col ml-1 mr-1'>
        <header className='w-full h-11 flex items-center  bg-[#151928]'>

        </header>
        <AnalyticsTrading data={data.prices} signals={data.signals} selected={selected}/> 
    </section>
  )
}

export default CardAnalytics