
import React, { useEffect, useState, useCallback } from "react";
import { Slider } from "@/components/ui/slider";
import { cn } from "@/lib/utils";
import { patchRiskAdvisors } from "@/lib/actions/actions.advisors";
import debounce from "debounce";



const StockBalance = ({AdvisorId, data }) => {
  const [stock, setStock] = useState(0);

  useEffect(() => {
    setStock(data);
  }, [data]);

  const debouncedPatch = useCallback(
    debounce(async (val) => {
      try {
        await patchRiskAdvisors({
          AdvisorId,
          data: { stock: val },
        });
      } catch (err) {
        console.error("Erro ao atualizar quantidade de operações:", err);
      }
    }, 500), // Aguarda 500ms após a última alteração
    [AdvisorId]
  );

  const handleChange = useCallback(
    ([val]) => {
      setStock(val);
      debouncedPatch(val);
    },
    [debouncedPatch]
  );

  return (
    <div className="w-full text-sm text-gray-400">
      <div className="flex items-center mb-2 justify-between w-full">
        <div>Ações</div>
        <div>{stock} %</div>
      </div>
      <Slider
        value={[stock]}
        onValueChange={handleChange}
        max={100}
        step={1}
        className={cn("w-full")}
        aria-label="Quantidade de operações slider"
      />
    </div>
  );
};

export default StockBalance