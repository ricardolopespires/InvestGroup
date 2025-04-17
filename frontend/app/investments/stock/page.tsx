"use client"


import React, { useEffect, useState } from "react";
import IndexWidgets from "@/components/IndexWidgets";
import { getAssetsStocks } from "@/lib/actions/actions.stock";
import Stock from "@/components/Stock";
import AnalysisWidget from "@/components/AnalysisWidget";
import TableStock from "@/components/TableStock";

const ITEMS_PER_PAGE = 10; // Número de itens por página

const Page = () => {
  const [stock, setStock] = useState([]);
  const [error, setError] = useState(false);
  

  useEffect(() => {
    const fetchCryptos = async () => {
      try {
        const res = await getAssetsStocks();
        console.log(res)
        setStock(res);
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
          <IndexWidgets asset="SP500" />
        </div>
        <div className="w-[25%]">
          <AnalysisWidget asset="SPX" />
        </div>
      </div>
      <TableStock stock={stock}/>

     
    </div>
  );
};

export default Page;