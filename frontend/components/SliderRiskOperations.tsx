import React, { useEffect, useState, useCallback } from "react";
import { Slider } from "@/components/ui/slider";
import { cn } from "@/lib/utils";
import { patchRiskAdvisors } from "@/lib/actions/actions.advisors";
import debounce from "debounce";

const SliderRiskOperations = ({ AdvisorId, data }) => {
  const [risk, setRisk] = useState(0);

  useEffect(() => {
    setRisk(data);
  }, [data]);

  const debouncedPatch = useCallback(
    debounce(async (val) => {
      try {
        await patchRiskAdvisors({
          AdvisorId,
          data: { level: val },
        });
      } catch (err) {
        console.error("Erro ao atualizar risco por operação:", err);
      }
    }, 500), // Aguarda 500ms após a última alteração
    [AdvisorId]
  );

  const handleChange = useCallback(
    ([val]) => {
      setRisk(val);
      debouncedPatch(val);
    },
    [debouncedPatch]
  );

  return (
    <div className="w-full">
      <div className="flex items-center mb-2 justify-between w-full">
        <div>Risco por Operação</div>
        <div>{risk}%</div>
      </div>
      <Slider
        value={[risk]}
        onValueChange={handleChange}
        max={100}
        step={0.01}
        className={cn("w-full")}
        aria-label="Risco por operação slider"
      />
    </div>
  );
};

export default SliderRiskOperations;