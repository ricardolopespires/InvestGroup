


import React, { useEffect, useState, useCallback } from "react";
import { Slider } from "@/components/ui/slider";
import { cn } from "@/lib/utils";
import { patchRiskAdvisors } from "@/lib/actions/actions.advisors";
import debounce from "debounce";



const CryptoBalance = ({AdvisorId, data}) => {
      const [crypto, setCrypto] = useState(0);
    
      useEffect(() => {
        setCrypto(data);
      }, [data]);
    
      const debouncedPatch = useCallback(
        debounce(async (val) => {
          try {
            await patchRiskAdvisors({
              AdvisorId,
              data: { crypto: val },
            });
          } catch (err) {
            console.error("Erro ao atualizar quantidade de operações:", err);
          }
        }, 500), // Aguarda 500ms após a última alteração
        [AdvisorId]
      );
    
      const handleChange = useCallback(
        ([val]) => {
          setCrypto(val);
          debouncedPatch(val);
        },
        [debouncedPatch]
      );
    
  return (
     <div className="w-full text-sm text-gray-400">
          <div className="flex items-center mb-2 justify-between w-full">
            <div>Crypto</div>
            <div>{crypto} %</div>
          </div>
          <Slider
            value={[crypto]}
            onValueChange={handleChange}
            max={100}
            step={1}
            className={cn("w-full")}
            aria-label="Quantidade de operações slider"
          />
        </div>
  )
}

export default CryptoBalance