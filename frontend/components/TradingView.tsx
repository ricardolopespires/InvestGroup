'use client'

import {AdvancedRealTimeChart } from "react-ts-tradingview-widgets"
import React from 'react'




const TradingView = ({symbol}:TradingViewProps) => {
  return (
    
    <div className="h-[98%] w-full">
        <AdvancedRealTimeChart 
        theme="dark"
        interval="D"
        symbol={`binance:${symbol}USD`}
        allow_symbol_change={false}
        withdateranges={true}
        timezone={true}
        autosize={true}
        show_popup_button={true}
        >

    </AdvancedRealTimeChart>
    </div>
  )
}

export default TradingView