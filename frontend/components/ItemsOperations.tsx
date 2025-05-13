import { ScrollArea } from "@/components/ui/scroll-area"
import { getPositions } from "@/lib/actions/actions.positions"
import  InverterOperations from "@/components/InverterOperations"
import { cn } from "@/lib/utils"
import React, { use, useEffect } from 'react'
import CloseOperation from "./CloseOperation"

const ItemsOperations = ({symbol,Assest, UserId}) => {

  const [operations, setOperations] = React.useState([])
  const [loading, setLoading] = React.useState(true)


   useEffect(() => {
    const fetchData = async () => {
      const res = await getPositions({symbol:symbol, Assest:Assest, UserId:UserId})     
        setOperations(res)        
        setLoading(false)
      }
    fetchData()
  }, [symbol, Assest, UserId])

  
  
  
  return (
    <div className='w-full h-full flex flex-col items-center '>
        <div className="w-full grid grid-cols-11 items-center justify-center h-9 text-xs bg-gray-100">       
            <div className='flex items-center justify-center'>Ativo</div>
            <div className='flex items-center justify-center'>Nº</div>
            <div className='flex items-center justify-center'>data</div>
            <div className='flex items-center justify-center'>Tipo</div>
            <div className='flex items-center justify-center'>Volume</div>
            <div className='flex items-center justify-center'>Entrada</div>
            <div className='flex items-center justify-center'>S/L</div>
            <div className='flex items-center justify-center'>T/P</div> 
            <div className='flex items-center justify-center'>Saida</div>
            <div className='flex items-center justify-center'>Lucro</div>
            <div className='flex items-center justify-center'></div>

        </div>
        <ScrollArea className="h-[95%] w-full ">
        {operations.length > 0 ? (
                operations.map((item, i) => (                
                  <div key={i} className="w-full grid grid-cols-11 items-center justify-center border-b h-9 border-gray-300 text-xs">
                  <div className='flex items-center justify-center'>{item.symbol}</div> {/* Supondo que a chave seja 'symbol' */}
                  <div className='flex items-center justify-center'>{item.ticket}</div>   {/* Substitua pelo valor correto */}
                  <div className='flex items-center justify-center'>{item.time}</div> {/* Substitua pelo valor correto */}
                  <div className={cn("flex items-center justify-center",
                    item.type === "buy" ? "text-green-500":"text-red-500")}>{item.type}</div> {/* Substitua pelo valor correto */}
                  <div className='flex items-center justify-center'>{item.volume}</div> {/* Substitua pelo valor correto */}
                  <div className='flex items-center justify-center'>{item.price_open}</div> {/* Substitua pelo valor correto */}
                  <div className='flex items-center justify-center'>{item.sl}</div> {/* Substitua pelo valor correto */}
                  <div className='flex items-center justify-center'>{item.tp}</div> {/* Substitua pelo valor correto */}
                  <div className='flex items-center justify-center'>{item.exit}</div> {/* Substitua pelo valor correto */}
                  <div className={cn("flex items-center justify-center",
                    item.profit > 0 ? "text-green-500":"text-red-500"
                  )}>{item.profit}</div> {/* Substitua pelo valor correto */}
                   <div className='flex items-center justify-center gap-2'>
                    <CloseOperation ticket={item.ticket} />
                    <InverterOperations operation = {item}/>
                    </div> 
              </div>
              )
                )
            ) : (
                <div className="w-full h-[200px] flex items-center justify-center text-gray-500">
                    {loading ? "Carregando..." : "Nenhum dado encontrado"}
                </div>
            )}

        </ScrollArea>

    </div>
  )
}

export default ItemsOperations