

import React, { useEffect, useState, useCallback } from "react";
import { Slider } from "@/components/ui/slider";
import { cn } from "@/lib/utils";
import { patchRiskAdvisors } from "@/lib/actions/actions.advisors";
import debounce from "debounce";



const CommoditiesBalance = ({AdvisorId, data}) => {
      const [commodity, setCommodity] = useState(0);
    
      useEffect(() => {
        setCommodity(data);
      }, [data]);
    
      const debouncedPatch = useCallback(
        debounce(async (val) => {
          try {
            await patchRiskAdvisors({
              AdvisorId,
              data: { commodity: val },
            });
          } catch (err) {
            console.error("Erro ao atualizar quantidade de operações:", err);
          }
        }, 500), // Aguarda 500ms após a última alteração
        [AdvisorId]
      );
    
      const handleChange = useCallback(
        ([val]) => {
          setCommodity(val);
          debouncedPatch(val);
        },
        [debouncedPatch]
      );

  return (
    <div className="w-full text-sm text-gray-500">
        <div className="flex items-center mb-2 justify-between w-full">
            <div>Commodities</div>
            <div>{commodity} %</div>
        </div>
        <Slider
            value={[commodity]}
            onValueChange={handleChange}
            max={100}
            step={1}
            className={cn("w-full")}
            aria-label="Quantidade de operações slider"
        />
    </div>
  )
}

export default CommoditiesBalance