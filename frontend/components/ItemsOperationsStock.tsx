import { ScrollArea } from "@/components/ui/scroll-area"
import React from 'react'

const ItemsOperationsStock = () => {
  return (
    <div className='w-full h-full flex flex-col items-center '>
        <div className="w-full grid grid-cols-10 items-center justify-center h-9 text-xs bg-gray-100">       
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
        </div>
        <ScrollArea className="h-[95%] w-full ">
            <div className="w-full grid grid-cols-10 items-center justify-center border-b h-9 border-gray-300 text-xs">
                <div className='flex items-center justify-center'>PETR3</div>
                <div className='flex items-center justify-center'>1</div>   
                <div className='flex items-center justify-center'>01/01/2023</div>
                <div className='flex items-center justify-center'>Compra</div>
                <div className='flex items-center justify-center'>100</div>
                <div className='flex items-center justify-center'>10</div>
                <div className='flex items-center justify-center'>5</div>
                <div className='flex items-center justify-center'>15</div>
                <div className='flex items-center justify-center'>20</div>
                <div className='flex items-center justify-center'>100</div>


            </div>

        </ScrollArea>

    </div>
  )
}

export default ItemsOperationsStock