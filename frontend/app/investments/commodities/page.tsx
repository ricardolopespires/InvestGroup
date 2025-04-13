"use client"





import AnalysisWidget from '@/components/AnalysisWidget'
import Commodities from '@/components/Commodities'
import IndexWidgets from '@/components/IndexWidgets'
import { getAssetsCommodities } from '@/lib/actions/actions.commodities'
import React, { useEffect } from 'react'

const page = () => {

    const [asset, setAsset] = React.useState([]);
    const [error, setError] = React.useState(false)

    useEffect(() => {
        const fetchCryptos = async () => {
        try {
            const res = await getAssetsCommodities();
            setAsset(res);
        } catch (err) {
            setError(true);
            console.error(err);
        }
        };
        
        fetchCryptos();
    }, []);
   
  return (
    <div className="flex flex-col max-w-screen-4xl mx-auto w-full pb-10 mt-24 text-white gap-4">
         {/* Cabeçalho com Botão */}
        <div className="w-full flex items-center justify-between gap-4 mt-4">
            <div className="w-[75%]">
            <IndexWidgets asset={asset[0]?.symbol} />
            </div>
            <div className="w-[25%]">
            <AnalysisWidget asset={asset[0]?.symbol} />
            </div>
        </div>  
        {/* Grid de Widgets */}
        <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4">
                {asset.map((item) => (
                  <div key={item.id} className="w-full h-full">
                    <Commodities asset={item.symbol} />
                  </div>
                ))}
        </div>        
        {error && (
            <div className="text-red-500 text-center">
                Erro ao carregar os dados
            </div>
         )}
    </div>


  )
}

export default page