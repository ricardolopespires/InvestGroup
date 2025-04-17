import React, { useEffect, useState, useCallback } from "react";
import { Slider } from "@/components/ui/slider";
import { patchRiskAdvisors } from "@/lib/actions/actions.advisors";
import debounce from "debounce";

const Breakeven = ({ AdvisorId, data }) => {
  const [breakeven, setBreakeven] = useState(0);

  useEffect(() => {
    setBreakeven(data);
  }, [data]);

  const debouncedPatch = useCallback(
    debounce(async (val) => {
      try {
        await patchRiskAdvisors({
          AdvisorId,
          data: { breakeven: val },
        });
      } catch (err) {
        console.error("Erro ao atualizar breakeven:", err);
      }
    }, 500), // Aguarda 500ms após a última alteração
    [AdvisorId]
  );

  const handleChange = useCallback(
    ([val]) => {
      setBreakeven(val);
      debouncedPatch(val);
    },
    [debouncedPatch]
  );

  return (
    <div className="w-full">
      <div className="flex items-center justify-between mb-2">
        <span className="text-sm font-medium">Breakeven</span>
        <span className="text-sm text-muted-foreground">{breakeven} Pontos</span>
      </div>
      <Slider
        value={[breakeven]}
        onValueChange={handleChange}
        max={1000}
        step={1}
        className="w-full"
        aria-label="Breakeven slider"
      />
    </div>
  );
};

export default Breakeven;