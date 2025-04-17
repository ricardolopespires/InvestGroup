import React, { useEffect, useState, useCallback } from "react";
import { Slider } from "@/components/ui/slider";
import { cn } from "@/lib/utils";
import { patchRiskAdvisors } from "@/lib/actions/actions.advisors";
import debounce from "debounce";

const SliderQtOperations = ({ AdvisorId, data }) => {
  const [amount, setAmount] = useState(0);

  useEffect(() => {
    setAmount(data);
  }, [data]);

  const debouncedPatch = useCallback(
    debounce(async (val) => {
      try {
        await patchRiskAdvisors({
          AdvisorId,
          data: { amount: val },
        });
      } catch (err) {
        console.error("Erro ao atualizar quantidade de operações:", err);
      }
    }, 500), // Aguarda 500ms após a última alteração
    [AdvisorId]
  );

  const handleChange = useCallback(
    ([val]) => {
      setAmount(val);
      debouncedPatch(val);
    },
    [debouncedPatch]
  );

  return (
    <div className="w-full">
      <div className="flex items-center mb-2 justify-between w-full">
        <div>Operações</div>
        <div>{amount} Qts</div>
      </div>
      <Slider
        value={[amount]}
        onValueChange={handleChange}
        max={100}
        step={1}
        className={cn("w-full")}
        aria-label="Quantidade de operações slider"
      />
    </div>
  );
};

export default SliderQtOperations;