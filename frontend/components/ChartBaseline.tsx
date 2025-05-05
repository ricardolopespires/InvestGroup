'use client';

import { createChart, ColorType, Time, BaselineSeries} from 'lightweight-charts';
import React, { useEffect, useRef } from 'react';

const ChartBaseline = ({
  data,
  inicial = 25,
}) => {
  const chartContainerRef = useRef(null);
  const chartRef = useRef(null);
  const baselineSeriesRef = useRef(null);

  useEffect(() => {
    if (!chartContainerRef.current) return;

    // Initialize chart
    const chartOptions = {
      layout: {
        textColor: 'black',
        background: { type: ColorType.Solid, color: 'white' },
      },
    };
    const chart = createChart(chartContainerRef.current, chartOptions);
    chartRef.current = chart;

    // Add baseline series
    const baselineSeries = chart.addSeries(BaselineSeries,{
      baseValue: { type: 'price', price: inicial },
      topLineColor: 'rgba(38, 166, 154, 1)',
      topFillColor1: 'rgba(38, 166, 154, 0.28)',
      topFillColor2: 'rgba(38, 166, 154, 0.05)',
      bottomLineColor: 'rgba(239, 83, 80, 1)',
      bottomFillColor1: 'rgba(239, 83, 80, 0.05)',
      bottomFillColor2: 'rgba(239, 83, 80, 0.28)',
    });
    baselineSeriesRef.current = baselineSeries;

    // Set data
    baselineSeries.setData(data);

    // Handle resize
    const handleResize = () => {
      chart.applyOptions({
        width: chartContainerRef.current.clientWidth,
        height: chartContainerRef.current.clientHeight,
      });
    };

    window.addEventListener('resize', handleResize);

    // Cleanup
    return () => {
      window.removeEventListener('resize', handleResize);
      chart.remove();
    };
  }, [data, inicial]);

  return (
    <div
      ref={chartContainerRef}
      className="w-full h-[470px] rounded-lg overflow-hidden shadow-sm"
    />
  );
};

export default ChartBaseline;