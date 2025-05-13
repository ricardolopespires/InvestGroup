"use client"





import AnalysisWidget from '@/components/AnalysisWidget'
import Commodities from '@/components/Commodities'
import IndexWidgets from '@/components/IndexWidgets'
import TableCommodities from '@/components/TableCommodities'
import { getAssetsCommodities } from '@/lib/actions/actions.commodities'
import React, { useEffect } from 'react'

const page = () => {

    const [asset, setAsset] = React.useState([]);
    const [error, setError] = React.useState(false)
    const user = JSON.parse(localStorage.getItem('user'))

    useEffect(() => {
        const fetchCryptos = async () => {
        try {
            const res = await getAssetsCommodities({UserId: user.email });
            setAsset(res);
        } catch (err) {
            setError(true);
            console.error(err);
        }
        };
        
        fetchCryptos();
    }, [user]);
   
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
        <TableCommodities commodities={asset} />
    </div>


  )
}

export default page