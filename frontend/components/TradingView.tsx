'use client'

import {AdvancedRealTimeChart } from "react-ts-tradingview-widgets"
import React from 'react'




const TradingView = ({symbol, CodeAsset}:TradingViewProps) => {


  return (
    
    <div className="h-[98%] w-full">
        { CodeAsset === "crypto" ? <AdvancedRealTimeChart 
        theme="dark"
        interval="D"
        symbol={`${symbol}USD`}
        allow_symbol_change={false}
        withdateranges={true}
        timezone={true}
        autosize={true}
        show_popup_button={true}
        >

    </AdvancedRealTimeChart>:
    <AdvancedRealTimeChart 
    theme="dark"
    interval="D"
    symbol={symbol}
    allow_symbol_change={false}
    withdateranges={true}
    timezone={true}
    autosize={true}
    show_popup_button={true}
    >

</AdvancedRealTimeChart>}
    </div>
  )
}

export default TradingView