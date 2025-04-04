"use client"

import Widgets from "@/components/Widgets";
import { FaPlus } from "react-icons/fa";
import React from "react";
import IndexWidgets from "@/components/IndexWidgets";
import AnalysisWidget from "@/components/AnalysisWidget";
import AddStock from "@/components/AddStock";

const Page = () => {

  const [showModal, setShowModal] = React.useState(false);

  return (
    <div className="z-40 ml-14 mr-10 -mt-16 flex flex-col gap-4 p-4 text-center text-white">
      {/* Cabeçalho com Botão */}
      <div className="w-full  flex items-center justify-between -mt-10">
        <div></div>
        <button className="flex items-center gap-2 bg-blue-900 text-xs py-2 px-7 rounded-sm text-white"
        onClick={() => setShowModal(true)}>
          <FaPlus />
          <span>Nova Ação</span>
        </button>
      </div>

      {/* Seção de Widgets Principais */}
      <div className="w-full flex  items-center justify-between gap-4 mt-4">
        <div className="w-[75%]">
          <IndexWidgets asset="SP500" />
        </div>
        <div className="w-[25%]">
          <AnalysisWidget asset="SPX" />
        </div>
      </div>

      {/* Grid de Widgets */}
      <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4 p-4">
        <Widgets asset="AMZN" />
        <Widgets asset="AAPL" />
        <Widgets asset="MSFT" />
        <Widgets asset="MSTR" />
        <Widgets asset="NVDA" />
        <Widgets asset="TSLA" />
      </div>
      <AddStock isVisible={showModal} onClose={()=>setShowModal(false)}/>
    </div>
  );
};

export default Page;
