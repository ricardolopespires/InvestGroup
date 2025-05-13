import { ScrollArea } from "@/components/ui/scroll-area"
import React from 'react'
import TradeAnalysis from './TradeAnalysis'

const OperationsAdvisor = () => {
  return (
    <div className="flex-1 p-6">
        {/* Portifólio Section */}
        <section className="mb-10 ">
        <h1 className="text-3xl font-semibold mb-2">Operações</h1>
        <p className="text-gray-700 mb-4">
          Monitorar as operações do robo-advisors permitem acopanhar toda a movimentção da alocação eficiente, diversificação e ajustes contínuos. Esses recursos facilitam decisões estratégicas, reduzindo riscos e otimizando retornos.
        </p>

        <div className='flex flex-col h-[299px] '>
            <div className='grid grid-cols-10  mt-4  text-sm bg-gray-100'>
                <span className='flex items-center justify-center h-7'>Id</span>
                <span className='flex items-center justify-center h-7'>Ativo</span>
                <span className='flex items-center justify-center h-7'>Data</span>
                <span className='flex items-center justify-center h-7'>Tipo</span>
                <span className='flex items-center justify-center h-7'>Volume</span>
                <span className='flex items-center justify-center h-7'>Entrada</span>
                <span className='flex items-center justify-center h-7'>S/L</span>
                <span className='flex items-center justify-center h-7'>T/P</span>
                <span className='flex items-center justify-center h-7'>Saida</span>
                <span className='flex items-center justify-center h-7'>Lucro</span>
            </div>

            <ScrollArea className="h-72 w-full rounded-md border">
            <div className='border-b grid grid-cols-10 text-sm'>                
                <span className='flex items-center justify-center h-7'>0</span>
                <span className='flex items-center justify-center h-7'>0</span>
                <span className='flex items-center justify-center h-7'>0</span>
                <span className='flex items-center justify-center h-7'>0</span>
                <span className='flex items-center justify-center h-7'>0</span>
                <span className='flex items-center justify-center h-7'>0</span>
                <span className='flex items-center justify-center h-7'>0</span>
                <span className='flex items-center justify-center h-7'>0</span>
                <span className='flex items-center justify-center h-7'>0</span>
                <span className='flex items-center justify-center h-7'>0</span>
            </div> 
            </ScrollArea>
            

        </div>
        <TradeAnalysis/>
      

        </section>
    </div>  
  )
}

export default OperationsAdvisor