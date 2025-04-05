

import { Card } from "@/components/ui/card"
import { InfoIcon as InfoCircle, TrendingDown } from "lucide-react"
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from "@/components/ui/tooltip"




import React from 'react'

const PerformaceOperationsStock = () => {
  return (
    <div className="mt-4 flex flex-col h-full w-full">
      {/* Header Summary */}
      <div className="grid grid-cols-6 gap-2 text-sm mb-4  pb-2 w-full">
        <div className="flex items-center gap-2">
          <span className="text-gray-400">Resultado Liq Tot:</span>
          <span className="text-red-400">R$ -1.396,50</span>
        </div>
        <div className="flex items-center gap-2">
          <span className="text-gray-400">Resultado Total:</span>
          <span className="text-red-400">R$ -1.367,00</span>
        </div>
        <div className="flex items-center gap-2">
          <span className="text-gray-400">Lucro Bruto:</span>
          <span className="text-green-400">R$ 6.808,00</span>
        </div>
        <div className="flex items-center gap-2">
          <span className="text-gray-400">Prejuízo Bruto:</span>
          <span className="text-red-400">R$ -8.175,00</span>
        </div>
        <div className="flex items-center gap-2">
          <span className="text-gray-400">Operações:</span>
          <span className="text-white">27</span>
        </div>
        <div className="flex items-center gap-2">
          <span className="text-gray-400">Vencedoras:</span>
          <span className="text-white">13</span>
        </div>       
      </div>
      <div className="flex items-center gap-6 w-full mt-6 text-xs">
          <div className="w-[50%]">
            <div className="grid grid-cols-2 gap-y-3">
              <div className="text-gray-400">Saldo Líquido Total</div>
              <div className="text-right text-red-400">R$ -1.396,50</div>

              <div className="text-gray-400">Lucro Bruto</div>
              <div className="text-right text-green-400">R$ 6.808,00</div>

              <div className="text-gray-400">Fator de Lucro</div>
              <div className="text-right">0,83</div>

              <div className="text-gray-400">Número Total de Operações</div>
              <div className="text-right">27</div>

              <div className="text-gray-400">Operações Vencedoras</div>
              <div className="text-right">13</div>

              <div className="text-gray-400">Operações Zeradas</div>
              <div className="text-right">1</div>

              <div className="text-gray-400">Média de Lucro/Prejuízo</div>
              <div className="text-right text-red-400">R$ -51,72</div>

              <div className="text-gray-400">Média de Operações Vencedoras</div>
              <div className="text-right text-green-400">R$ 523,69</div>

              <div className="text-gray-400">Maior Operação Vencedora</div>
              <div className="text-right text-green-400">R$ 3.181,00</div>

              <div className="text-gray-400">Maior Sequência Vencedora</div>
              <div className="text-right">2</div>

              <div className="text-gray-400">Média de Tempo em Op. Vencedoras</div>
              <div className="text-right">6min22s</div>

              <div className="text-gray-400">Média de Tempo em Operações</div>
              <div className="text-right">3min54s</div>
            </div>
          </div>
          <div className="w-[50%]">
            <div className="grid grid-cols-2 gap-y-3">
              <div className="text-gray-400">Saldo Total</div>
              <div className="text-right text-red-400">R$ -1.367,00</div>

              <div className="text-gray-400">Prejuízo Bruto</div>
              <div className="text-right text-red-400">R$ -8.175,00</div>

              <div className="text-gray-400">Custos</div>
              <div className="text-right text-red-400">R$ -29,50</div>

              <div className="text-gray-400">Percentual de Operações Vencedoras</div>
              <div className="text-right">48,15%</div>

              <div className="text-gray-400">Operações Perdedoras</div>
              <div className="text-right">13</div>

              <div className="text-gray-400">Razão Média Lucro:Média Prejuízo</div>
              <div className="text-right">0,83</div>

              <div className="text-gray-400">Média de Operações Perdedoras</div>
              <div className="text-right text-red-400">R$ -628,85</div>

              <div className="text-gray-400">Maior Operação Perdedora</div>
              <div className="text-right text-red-400">R$ -4.000,00</div>

              <div className="text-gray-400">Maior Sequência Perdedora</div>
              <div className="text-right">4</div>

              <div className="text-gray-400">Média de Tempo em Op. Perdedoras</div>
              <div className="text-right">1min40s</div>

              <div className="text-gray-400">Património Necessário(Maior Operação)</div>
              <div className="text-right">R$ 4.019.505,00</div>

              <div className="text-gray-400">Retorno no Capital Inicial</div>
              <div className="text-right text-red-400">-0,03%</div>

              <div className="text-gray-400">Património Máximo</div>
              <div className="text-right">R$ 3.157,00</div>
            </div>
          </div>
          
      </div>

    </div>
  )
}

export default PerformaceOperationsStock