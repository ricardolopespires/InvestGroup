"use client"


import { FaRegBell,  } from "react-icons/fa";
import { GoTriangleDown, GoTriangleUp } from "react-icons/go";

import React, { useEffect, useState } from 'react'
import AtivoList from "@/components/AtivoList";
import Boleta from "@/components/Boleta";
import { getAssetList } from "@/lib/actions/actions.trading";
import TradingHeader from "@/components/TradingHeader";

const page = ({childrens}) => {
    
    const [typeAsset, setTypeAsset] = useState("crypto")
    const [listAsset, setListAsset] = useState<any[]>([]);     
    const [filter, setFilter] = useState<string>(""); // Estado para o filtro de pesquisa
    const [error, setError] = useState<string | null>(null);
    const [selected, setSelected] = useState([])
    const [typeSelected, setTypeSelected] = useState("tradingview")
    
      useEffect(() => {
        const fetchCryptos = async () => {
          const data = await getAssetList({ CodeAsset: typeAsset });
          if (typeof data === "string") {
            setError(data); // Se for uma string, é erro
          } else {
            setListAsset(data); // Caso contrário, é a lista de ativos
          }
        };
    
        fetchCryptos();
      }, [typeAsset]); // Adiciona CodeAsset como dependência para refazer a requisição quando mudar
    
      useEffect(() => {
        setSelected(listAsset[0])

      },[listAsset])
    
  return (
    
    <div className="flex flex-col gap-1" >
        <header className='bg-[#151928] w-full h-16'>
            <div className='ml-20 mr-20 flex h-full items-center justify-between'>
                
                <div className="flex items-center gap-4 text-white">
                <img src={"/images/favicon.png"} alt="logotipo" className='w-[20px]' />
                        <div className="flex items-center gap-4 text-sm">
                            <button onClick={()=>setTypeAsset("crypto")}>Crypto</button>
                            <button onClick={()=>setTypeAsset("currency")}>Currency</button>
                            <button onClick={()=>setTypeAsset("index")}>Indexs</button>
                            <button onClick={()=>setTypeAsset("commodities")}>Commodities</button>
                        </div>
                    </div>
                <div className='flex items-center gap-4'>                    
                    <FaRegBell className="text-2xl text-white"/>
                    <a href="dashboard/overview">
                        <button className='bg-white text-sm py-1 px-7 rounded-sm hover:bg-gray-200'>
                            Voltar
                        </button>
                    </a>                    
                </div>
            </div>
        </header>
        <div className="flex items-center w-full h-16 bg-[#151928]">
            <div className="w-[15%] bg-[#2a2a3c] h-full">
            <div  className="flex items-center justify-between p-4 text-white h-full">
                <div className="flex flex-col">
                  <div className="flex  items-center gap-2">
                    <img src={selected?.image} alt={selected?.name} className="w-7 h-7 rounded-full"/>
                    <div className="flex flex-col">
                      <span className="text-sm">{selected?.symbol?.toUpperCase()}</span>
                      <span className="text-xs text-gray-400">{selected?.name}</span>
                    </div>
                  </div>              
                </div>
                <div className="text-xs">
                {selected?.price_change_percentage_24h > 0 ?(
                  <div className="text-green-500 flex flex-col items-center">
                    <p className="text-md">{selected?.current_price}</p>
                    <div className="flex items-center gap-1">
                      <GoTriangleUp />
                      <span>{selected?.price_change_percentage_24h?.toFixed(2)}%</span>
                    </div>
                    </div>
                ):(
                  <div className="text-red-500 flex flex-col items-center">
                    <p className="text-md">{selected?.current_price}</p>
                      <div className="flex items-center gap-1">
                      <GoTriangleDown/>
                      <span>{selected?.price_change_percentage_24h?.toFixed(2)}%</span>
                    </div>
                    </div>
                )}
                </div>         
            </div>
            </div>
            <div className="w-[85%]">
            <TradingHeader item={selected} typeSelected={typeSelected} setTypeSelected={setTypeSelected}/>
            </div>
        </div>
        <div className="flex w-full h-[800px]">
            <div className="w-[15%] h-full ">
                <AtivoList ListAsset={listAsset} setSelected={setSelected} selected={selected}/>
            </div>
            <div className="w-[70%]">

            </div>
            <div className="w-[15%]">
            <Boleta/>
            </div>
        </div>

    </div>
  )
}

export default page