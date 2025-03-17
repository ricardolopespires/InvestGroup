import React, { useEffect, useState } from 'react'
import AnalyticsTrading from './AnalyticsTrading'
import { getHistoryAssets } from "@/lib/actions/actions.trading"
import { cn } from '@/lib/utils'


const CardAnalytics = ({ selected , CodeAsset}) => {
    const [time, setTime] = useState("1d")
    const [data, setData] = useState({
        prices: [],
        signals: []
    })

    useEffect(() => {
        const fetchData = async () => {
            if(CodeAsset === "crypto"){
                const res = await getHistoryAssets({ symbol: selected.symbol, period:time, CodeAsset:CodeAsset })
            setData(res)
            }else{
                const res = await getHistoryAssets({ symbol: selected.yahoo, period:time, CodeAsset:CodeAsset })
                setData(res)
            }
            }
        fetchData();
    }, [selected, time, CodeAsset])

    return (
        <section className='flex flex-col ml-1 mr-1'>
            <header className='w-full h-11 bg-[#151928] text-gray-500 gap-2 text-xs'>
                <div className='flex w-full h-full items-center gap-2 ml-9'>
                    <button
                        className={cn({ "text-white": time === "1m", "text-gray-500": time !== "1m" })}
                        onClick={() => setTime("1m")}
                    >
                        1m
                    </button>
                    <button
                        className={cn({ "text-white": time === "5m", "text-gray-500": time !== "5m" })}
                        onClick={() => setTime("5m")}
                    >
                        5m
                    </button>
                    <button
                        className={cn({ "text-white": time === "15m", "text-gray-500": time !== "15m" })}
                        onClick={() => setTime("15m")}
                    >
                        15m
                    </button>
                    <button
                        className={cn({ "text-white": time === "30m", "text-gray-500": time !== "30m" })}
                        onClick={() => setTime("30m")}
                    >
                        30m
                    </button>
                    <button
                        className={cn({ "text-white": time === "1h", "text-gray-500": time !== "1h" })}
                        onClick={() => setTime("1h")}
                    >
                        1h
                    </button>
                    <button
                        className={cn({ "text-white": time === "1d", "text-gray-500": time !== "1d" })}
                        onClick={() => setTime("1d")}
                    >
                        1d
                    </button>
                    <button
                        className={cn({ "text-white": time === "5d", "text-gray-500": time !== "5d" })}
                        onClick={() => setTime("5d")}
                    >
                        5d
                    </button>
                    <button
                        className={cn({ "text-white": time === "1wk", "text-gray-500": time !== "1wk" })}
                        onClick={() => setTime("1wk")}
                    >
                        1wk
                    </button>                   
                </div>
            </header>
            <AnalyticsTrading data={data.prices} signals={data.signals} selected={selected} />
        </section>
    )
}

export default CardAnalytics
