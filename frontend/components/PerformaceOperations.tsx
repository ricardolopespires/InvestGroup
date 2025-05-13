import React, { useEffect, useState } from 'react';
import { getPerformanceAsset } from '@/lib/actions/actions.analytics';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import { subDays, format } from 'date-fns';
import { formatBRL, formatMinutes, formatNumber, formatPercentage } from '@/lib/utils';





const PerformanceOperations: React.FC<PerformanceOperationsProps> = ({ userId, symbol }) => {
  const [data, setData] = useState<PerformanceMetrics | null>(null);
  const [message, setMessage] = useState<string | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const [startDate, setStartDate] = useState<Date>(subDays(new Date(), 30)); // Default: last 30 days
  const [endDate, setEndDate] = useState<Date>(new Date());

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      setError(null);
      setMessage(null);

      try {
        const response: ApiResponse = await getPerformanceAsset({
          userId,
          symbol,
          startDate: format(startDate, 'yyyy-MM-dd'),
          endDate: format(endDate, 'yyyy-MM-dd'),
          initialCapital: 10000, // Default value, can be made configurable
        });

        if ('data' in response && response.data) {
          setData(response.data[0]);
          setMessage(null);
        } else if ('message' in response) {
          setData(null);
          setMessage(response.message);
        } else {
          setError(response.message || 'Erro ao buscar métricas de desempenho');
        }
      } catch (err: any) {
        setError(err.message || 'Erro na requisição de métricas');
      } finally {
        setLoading(false);
      }
    };

    if (userId && symbol && startDate && endDate) {
      fetchData();
    } else {
      setError('Parâmetros userId, symbol ou datas inválidos');
      setLoading(false);
    }
  }, [userId, symbol, startDate, endDate]);

  // Handle date range changes
  const handleDateChange = (dates: [Date | null, Date | null]) => {
    const [start, end] = dates;
    if (start) setStartDate(start);
    if (end) setEndDate(end);
  };


  return (
    <div className="mt-4 flex flex-col h-full w-full">
      {/* Date Range Picker */}
      <div className="mb-4 flex gap-4 w-full items-center justify-end">
        <div className="flex flex-col">
          <label className="text-sm text-gray-400 mb-1">Período</label>
          <DatePicker
            selected={startDate}
            onChange={handleDateChange}
            startDate={startDate}
            endDate={endDate}
            selectsRange
            dateFormat="dd/MM/yyyy"
            className="bg-gray-800 text-white rounded p-2 text-sm w-[200px]"
            placeholderText="Selecione o período"
          />
        </div>
      </div>

      {/* Loading State */}
      {loading && (
        <div className="flex justify-center items-center h-40">
          <div className="animate-spin rounded-full h-8 w-8 border-t-2 border-b-2 border-blue-500"></div>
        </div>
      )}

      {/* Error State */}
      {error && (
        <div className="text-red-400 text-sm p-4 bg-gray-800 rounded">{error}</div>
      )}

      {/* Message for Empty Results */}
      {message && !loading && !error && (
        <div className="text-gray-400 text-sm p-4 bg-gray-800 rounded">{message}</div>
      )}

      {/* Data Display */}
      {data && !loading && !error && !message && (
        <>
          {/* Header Summary */}
          <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-6 gap-2 text-sm mb-4 pb-2 w-full">
            <div className="flex items-center gap-2">
              <span className="text-gray-400">Resultado Liq Tot:</span>
              <span className={data.Resultado_Liq_Tot >= 0 ? 'text-green-400' : 'text-red-400'}>
                {formatBRL(data.Resultado_Liq_Tot)}
              </span>
            </div>
            <div className="flex items-center gap-2">
              <span className="text-gray-400">Resultado Total:</span>
              <span className={data.Resultado_Total >= 0 ? 'text-green-400' : 'text-red-400'}>
                {formatBRL(data.Resultado_Total)}
              </span>
            </div>
            <div className="flex items-center gap-2">
              <span className="text-gray-400">Lucro Bruto:</span>
              <span className="text-green-400">{formatBRL(data.Lucro_Bruto)}</span>
            </div>
            <div className="flex items-center gap-2">
              <span className="text-gray-400">Prejuízo Bruto:</span>
              <span className="text-red-400">{formatBRL(-data.Prejuizo_Bruto)}</span>
            </div>
            <div className="flex items-center gap-2">
              <span className="text-gray-400">Operações:</span>
              <span className="text-white">{formatNumber(data.Operacoes)}</span>
            </div>
            <div className="flex items-center gap-2">
              <span className="text-gray-400">Vencedoras:</span>
              <span className="text-white">{formatNumber(data.Vencedoras)}</span>
            </div>
          </div>

          {/* Detailed Metrics */}
          <div className="flex flex-col md:flex-row items-center gap-6 w-full mt-6 text-xs">
            <div className="w-full md:w-[50%]">
              <div className="grid grid-cols-2 gap-y-3">
                <div className="text-gray-400">Saldo Líquido Total</div>
                <div className={`text-right ${data.Saldo_Liquido_Total >= 0 ? 'text-green-400' : 'text-red-400'}`}>
                  {formatBRL(data.Saldo_Liquido_Total)}
                </div>
                <div className="text-gray-400">Lucro Bruto</div>
                <div className="text-right text-green-400">{formatBRL(data.Lucro_Bruto)}</div>
                <div className="text-gray-400">Fator de Lucro</div>
                <div className="text-right">{data.Fator_de_Lucro === Infinity ? '∞' : formatNumber(data.Fator_de_Lucro)}</div>
                <div className="text-gray-400">Número Total de Operações</div>
                <div className="text-right">{formatNumber(data.Numero_Total_de_Operacoes)}</div>
                <div className="text-gray-400">Operações Vencedoras</div>
                <div className="text-right">{formatNumber(data.Vencedoras)}</div>
                <div className="text-gray-400">Operações Zeradas</div>
                <div className="text-right">{formatNumber(data.Operacoes_Zeradas)}</div>
                <div className="text-gray-400">Média de Lucro/Prejuízo</div>
                <div className={`text-right ${data.Media_de_Lucro_Prejuizo >= 0 ? 'text-green-400' : 'text-red-400'}`}>
                  {formatBRL(data.Media_de_Lucro_Prejuizo)}
                </div>
                <div className="text-gray-400">Média de Operações Vencedoras</div>
                <div className="text-right text-green-400">{formatBRL(data.Media_de_Operacoes_Vencedoras)}</div>
                <div className="text-gray-400">Maior Operação Vencedora</div>
                <div className="text-right text-green-400">{formatBRL(data.Maior_Operacao_Vencedora)}</div>
                <div className="text-gray-400">Maior Sequência Vencedora</div>
                <div className="text-right">{formatNumber(data.Maior_Sequencia_Vencedora)}</div>
                <div className="text-gray-400">Média de Tempo em Op. Vencedoras</div>
                <div className="text-right">{formatMinutes(data.Media_de_Tempo_em_Op_Vencedoras_mins)}</div>
                <div className="text-gray-400">Média de Tempo em Operações</div>
                <div className="text-right">{formatMinutes(data.Media_de_Tempo_em_Operacoes_mins)}</div>
              </div>
            </div>
            <div className="w-full md:w-[50%]">
              <div className="grid grid-cols-2 gap-y-3">
                <div className="text-gray-400">Saldo Total</div>
                <div className={`text-right ${data.Saldo_Total >= 0 ? 'text-green-400' : 'text-red-400'}`}>
                  {formatBRL(data.Saldo_Total)}
                </div>
                <div className="text-gray-400">Prejuízo Bruto</div>
                <div className="text-right text-red-400">{formatBRL(-data.Prejuizo_Bruto)}</div>
                <div className="text-gray-400">Custos</div>
                <div className="text-right text-red-400">{formatBRL(-data.Custos)}</div>
                <div className="text-gray-400">Percentual de Operações Vencedoras</div>
                <div className="text-right">{formatPercentage(data.Percentual_de_Operacoes_Vencedoras)}</div>
                <div className="text-gray-400">Operações Perdedoras</div>
                <div className="text-right">{formatNumber(data.Operacoes_Perdedoras)}</div>
                <div className="text-gray-400">Razão Média Lucro:Média Prejuízo</div>
                <div className="text-right">{data.Razao_Media_Lucro_Media_Prejuizo === Infinity ? '∞' : formatNumber(data.Razao_Media_Lucro_Media_Prejuizo)}</div>
                <div className="text-gray-400">Média de Operações Perdedoras</div>
                <div className="text-right text-red-400">{formatBRL(-data.Media_de_Operacoes_Perdedoras)}</div>
                <div className="text-gray-400">Maior Operação Perdedora</div>
                <div className="text-right text-red-400">{formatBRL(-data.Maior_Operacao_Perdedora)}</div>
                <div className="text-gray-400">Maior Sequência Perdedora</div>
                <div className="text-right">{formatNumber(data.Maior_Sequencia_Perdedora)}</div>
                <div className="text-gray-400">Média de Tempo em Op. Perdedoras</div>
                <div className="text-right">{formatMinutes(data.Media_de_Tempo_em_Op_Perdedoras)}</div>
                <div className="text-gray-400">Patrimônio Necessário (Maior Operação)</div>
                <div className="text-right">{formatBRL(data.Patrimonio_Necessario_Maior_Operacao)}</div>
                <div className="text-gray-400">Retorno no Capital Inicial</div>
                <div className={`text-right ${data.Retorno_no_Capital_Inicial >= 0 ? 'text-green-400' : 'text-red-400'}`}>
                  {formatPercentage(data.Retorno_no_Capital_Inicial)}
                </div>
                <div className="text-gray-400">Patrimônio Máximo</div>
                <div className="text-right">{formatBRL(data.Patrimonio_Maximo)}</div>
              </div>
            </div>
          </div>
        </>
      )}
    </div>
  );
};

export default PerformanceOperations;