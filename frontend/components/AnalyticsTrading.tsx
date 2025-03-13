import React, { useEffect, useRef } from 'react';
import { createChart, CandlestickSeries } from 'lightweight-charts';



const AnalyticsTrading = ({data}) => {

  console.log(data)
  const chartContainerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (chartContainerRef.current) {
      const chart = createChart(chartContainerRef.current, {
        layout: {
          textColor: '#ddd',
          background: {         
            color: 'black',
          },
        },
        grid: {
            horzLines: { visible: false }, // Remove as linhas horizontais
            vertLines: { visible: false }, // Remove as linhas verticais
        },
        width: 1300,
        height: 723,
      });

      // Adicionando a série de candlestick corretamente
      const candlestickSeries = chart.addSeries(CandlestickSeries, {
        upColor: '#26a69a', 
        downColor: '#ef5350', 
        borderVisible: false,
        wickUpColor: '#26a69a', 
        wickDownColor: '#ef5350',
      });

      candlestickSeries.setData(data);

      return () => chart.remove(); // Cleanup chart on unmount
    }
  }, [data]);

  return (
    <div className='p-4'>
      <div ref={chartContainerRef} style={{ position: 'relative' }} />
    </div>
  );
};

export default AnalyticsTrading;
