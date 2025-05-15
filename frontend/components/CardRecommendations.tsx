import { FaCaretUp, FaCaretDown } from "react-icons/fa";
import React, { Fragment, useState } from 'react';
import { BsClockHistory } from "react-icons/bs";
import { calculate24HourProgress, countdown24Hours } from "@/lib/utils";
import { MdOutlineTimer } from "react-icons/md";
import OpenOperations from "./OpenOprations";
// Define the interface with proper TypeScript types
interface CardRecommendationsProps {
  asset: string;
  symbol: string;
  logo: string;
  timeToBuy: string;
  price: string;
  timeframe: string;
  signal_time: string;
  signal?: string; // Optional property
}

// Use defaultProps for default values
const defaultProps: CardRecommendationsProps = {
  asset: "AMAZON",
  symbol: "AMZN",
  logo: "https://logospng.org/download/amazon/logo-amazon-4096.png",
  timeToBuy: "24:00:00",
  price: "R$ 4.500,00",
  signal_time: "00",
  signal: "buy",
};

const CardRecommendations: React.FC<CardRecommendationsProps> = ({
  asset = defaultProps.asset,
  symbol = defaultProps.symbol,
  logo = defaultProps.logo,
  price = defaultProps.price,
  timeframe = defaultProps.timeframe,
  signal_time = defaultProps.signal_time,
  signal = defaultProps.signal,
}) => {
  
  const[showModal, setShowModal] = useState(false);
  
  // Determine if percentage is positive or negative
  const percentage = calculate24HourProgress(signal_time);
  const countdown = countdown24Hours(signal_time);
  
  return (
    <Fragment>
    <div className="w-full  rounded-xl p-5 border shadow-md bg-gray-200">
      <div className="grid grid-cols-1 lg:grid-cols-12 items-center gap-6">
        <div className="lg:col-span-3">
          <div className="mx-auto flex h-[99px] w-[99px] items-center justify-center rounded-full border shadow p-4 bg-white">
            <img src={`http://localhost:8000${logo}`} alt={`${asset} logo`} className="max-w-full max-h-full object-contain" />
          </div>
        </div>

        <div className="lg:col-span-9">
          <div className="flex items-center justify-between">
            <div className="text-center lg:text-left">
              <h2 className="text-2xl font-bold flex items-center gap-2">
                <span>{asset}</span>
                <div className={`flex items-center gap-1 bg-blue-950 text-white rounded-sm px-2 py-1 text-sm`}>
                    <span className="font-light">{timeframe}</span>
                    <BsClockHistory className="text-md"/>                  
                </div>
              </h2>
              <p className="mt-0 font-light text-sm">({symbol})</p>
            </div>
            <div>
              <span className="text-md">${price}</span>
            </div>
          </div>
          <div className="mt-9 flex justify-center items-center"
          onClick={() => setShowModal(true)}>
            <button className={`w-[90%] rounded-sm border bg-slate-100  px-3 py-2 hover:bg-gray-50 transition-colors`}>
               {signal === 'buy' ? 'Compra' : 'Venda'}
            </button>
          </div>
        </div>

        <div className="lg:col-span-12 flex flex-col gap-2">
          <div className="flex items-center justify-between text-xs">
            <span>Tempo para comprar</span>
            <div className="flex items-center gap-1 text-sm">
              <span>{countdown.hours}:{countdown.minutes}:{countdown.seconds}</span>
              <MdOutlineTimer className="text-lg" />
            </div>
            
          </div>
          <div className="w-full h-2 rounded-full bg-gray-200">
            <div
              className="h-2 rounded-full bg-amber-400"
              style={{ width: percentage }}
            />
          </div>
        </div>
      </div>
    </div>
    <OpenOperations Symbol={symbol} isVisible={showModal} onClose={() => {setShowModal(false)}} />
    </Fragment>
  );
};

CardRecommendations.defaultProps = defaultProps;

export default CardRecommendations;