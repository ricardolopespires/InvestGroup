"use client";
import { BsSliders2 } from "react-icons/bs";
import React, { useEffect, useState } from "react";
import { Separator } from "@/components/ui/separator";
import { ScrollArea } from "@/components/ui/scroll-area"
import { GoTriangleDown, GoTriangleUp } from "react-icons/go";
import { cn } from "@/lib/utils";

// Tipando a propriedade CodeAsset
interface AtivoListProps {
  CodeAsset: string; // Exemplo de tipo para o CodeAsset, ajustado conforme seu caso
}

const AtivoList = ({ ListAsset, setSelected, selected }: AtivoListProps) => {
 
  const [filter, setFilter] = useState<string>(""); // Estado para o filtro de pesquisas
  const [search, setSearch] = useState<string>({}); // Estado para o]

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setFilter(event.target.value.toLowerCase()); // Atualiza o filtro com o valor do input
  };

  // Filtrando os ativos com base no nome (ou qualquer outra propriedade)
  const filterAssets = ListAsset.filter((asset) =>
    asset.name.toLowerCase().includes(filter)
  );

  return (
    <div className="bg-[#151928] h-[784px]">
      <div className="flex items-center w-full border p-2 rounded-md gap-2  ">
        <BsSliders2 className="text-white text-lg" />
        <Separator orientation="vertical" />
        <input
          type="text"
          placeholder="Search ativos"
          onChange={handleChange}
          className="text-sm bg-transparent text-white w-full outline-none"
        />
      </div>
      <ScrollArea className="h-[94%] w-full">
      {filterAssets.map((item, i) =>{
        return(
          <div key={i} className={cn(
              "h-full w-full p-4 flex items-center border-b border-gray-600 cursor-pointer hover:bg-gray-700 hover:text-white",
              { "bg-gray-700 text-white": selected?.name === item.name }
            )}
            onClick={() => setSelected(item)}
          >

              <div className="flex flex-col w-full">
                <div className="flex  items-center gap-2 w-full">
                  <img src={item?.image} alt={item?.name} className="w-7 h-7 rounded-sm"/>
                    <div className="flex flex-col">
                      <span className="text-sm text-white">{item?.symbol?.toUpperCase()}</span>
                      <span className="text-xs text-gray-400">{item?.name}</span>
                    </div>
                </div>              
              </div>
              <div className="text-xs">
                {item?.price_change_percentage_24h > 0 ?(
                  <div className="text-green-500 flex flex-col items-center">
                      <p className="text-md">{item?.current_price}</p>
                      <div className="flex items-center gap-1">
                      <GoTriangleUp />
                      <span>{item?.price_change_percentage_24h?.toFixed(2)}%</span>
                     </div>
                  </div>
                  ):(
                  <div className="text-red-500 flex flex-col items-center">
                    <p className="text-md">{item?.current_price}</p>
                    <div className="flex items-center gap-1">
                      <GoTriangleDown/>
                      <span>{item?.price_change_percentage_24h?.toFixed(2)}%</span>
                    </div>
                  </div>
                )}
              </div>  
          </div>
        )
      })}
      </ScrollArea>
    </div>
  );
};

export default AtivoList;
