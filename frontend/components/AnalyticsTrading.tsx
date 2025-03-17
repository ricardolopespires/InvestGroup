import React, { useEffect, useRef } from 'react';
import { createChart, CandlestickSeries, createSeriesMarkers } from 'lightweight-charts';

const AnalyticsTrading = ({ data, signals, selected }) => {
  const chartContainerRef = useRef<HTMLDivElement>(null);
  

  useEffect(() => {
    // Initialize markers array
    const markers = [];

    // Loop through signals to process each one
    signals.forEach((signal) => {
      if (signal.type === 'sell') {
        markers.push({
          time: signal.time,
          position: 'aboveBar',
          color: '#ff0000',
          shape: 'arrowDown',
          text: `Sell @ ${signal.text.split(' @ ')[1]}`,  // Display the sell price
          size: 2,
        });
      } else if (signal.type === 'buy') {
        markers.push({
          time: signal.time,
          position: 'belowBar',
          color: '#00e600',
          shape: 'arrowUp',
          text: `Buy @ ${signal.text.split(' @ ')[1]}`,  // Display the buy price
          size: 2,
        });
      }
    });

    if (chartContainerRef.current) {
      const chart = createChart(chartContainerRef.current, {
        layout: {
          textColor: '#ddd',
          background: {
            color: 'black',
          },
        },
        grid: {
          horzLines: { visible: false },
          vertLines: { visible: false },
        },
        width: 1300,
        height: 680,
      });

      // Add the candlestick series
      const candlestickSeries = chart.addSeries(CandlestickSeries, {
        upColor: '#26a69a',
        downColor: '#ef5350',
        borderVisible: false,
        wickUpColor: '#26a69a',
        wickDownColor: '#ef5350',
      });

      candlestickSeries.setData(data);

      // Set markers for the candlestick series
      createSeriesMarkers(candlestickSeries, markers);;

      // Handle resizing of the chart
      const handleResize = () => {
        chart.applyOptions({
          width: chartContainerRef.current.clientWidth,
        });
      };

      window.addEventListener('resize', handleResize);

      // Cleanup on component unmount
      return () => chart.remove();
    }
  }, [data, signals]);

  return (
    <div className="p-2">
      <div ref={chartContainerRef} style={{ position: 'relative' }}>
        <div className="text-white flex items-center gap-2">
          <img src={selected.image} alt={selected.symbol} className="w-9 h-9" />
          <div className="flex flex-col">
            <span>{selected.symbol.toUpperCase()}</span>
            <span className="text-sm text-gray-500">{selected.name}</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AnalyticsTrading;
