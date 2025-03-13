import { cn } from "@/lib/utils"
import { ArrowDownIcon, ArrowUpIcon, CircleIcon } from "lucide-react"

export default function TradingHeader({ item, typeSelected, setTypeSelected }: TradingHeaderProps) {

  return (
    <div className="w-full text-white p-4 flex flex-col md:flex-row justify-between items-start md:items-center text-sm">
      <div className="flex gap-9 items-center">
        <div className="flex flex-col md:flex-row md:items-center gap-2 md:gap-4">
          <div className="flex flex-col items-center gap-2">
            <span className="text-gray-400 text-xs">Último preço negociado</span>
            <div className="flex items-center">
              <span className="text-white font-bold text-lg">{item?.current_price?.toLocaleString()} USD</span>
            </div>
          </div>
        </div>
        <div className="flex flex-wrap gap-4 mt-2 md:mt-0">
          <div className="flex flex-col">
            <span className="text-gray-400 text-xs">24h Change</span>
            <span className={cn("font-medium flex items-center", {
              "text-green-500": item?.price_change_percentage_24h > 0,
              "text-red-500": item?.price_change_percentage_24h < 0,
            })}>
              {item?.price_change_percentage_24h > 0 ?
              <ArrowUpIcon className="h-3 w-3 mr-1" />:
              <ArrowDownIcon className="h-3 w-3 mr-1" />}
              {item?.price_change_percentage_24h?.toFixed(2)}%
            </span>
          </div>
          <div className="flex flex-col">
            <span className="text-gray-400 text-xs">24h High</span>
            <span className="text-white">{item?.high_24h ? item.high_24h?.toLocaleString() : "N/A"}</span>
          </div>

          <div className="flex flex-col">
            <span className="text-gray-400 text-xs">24h Low</span>
            <span className="text-white">{item?.low_24h ? item.low_24h?.toLocaleString() : "N/A"}</span>
          </div>

          <div className="flex flex-col">
            <span className="text-gray-400 text-xs">24h Volume (USDT)</span>
            <div className="flex items-center">
              <span className="text-white">{item?.total_volume ? item?.total_volume?.toLocaleString() : "N/A"}</span>
              <CircleIcon className="h-3 w-3 ml-2 text-green-500 fill-green-500" />
            </div>
          </div>
        </div>
      </div>
      <div className="flex items-center gap-4 mr-16">
        <button className={cn({
          "bg-white text-black py-2 rounded-sm text-xs px-6": typeSelected === "tradingview", 
          "bg-black text-white py-2 rounded-sm text-xs px-6": typeSelected === ""
            })} onClick={() => setTypeSelected("tradingview")}>
              TradingView
        </button>
        <button className={cn({
          "bg-white text-black py-2 rounded-sm text-xs px-6": typeSelected === "strategic", 
          "bg-black text-white py-2 rounded-sm text-xs px-6": typeSelected === ""
            })} onClick={() => setTypeSelected("strategic")}>
              Strategic
        </button>
      </div>
    </div>
  )
}
