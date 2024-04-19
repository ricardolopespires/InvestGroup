import { LiaExchangeAltSolid } from "react-icons/lia";

import {useEffect} from "react";
import {useState} from "react";
import CurrencyDropdown from "./dropdown";
import {HiArrowsRightLeft} from "react-icons/hi2";


import React from 'react'

const Exchange = () => {
    const [currencies, setCurrencies] = useState([]);
    const [amount, setAmount] = useState(1);
    const [fromCurrency, setFromCurrency] = useState("USD");
    const [toCurrency, setToCurrency] = useState("BRL");
    const [convertedAmount, setConvertedAmount] = useState(null);
    const [converting, setConverting] = useState(false);
    const [favorites, setFavorites] = useState(
      JSON.parse(localStorage.getItem("favorites")) || ["BRL", "EUR"]
    );
  
    // Currencies -> https://api.frankfurter.app/currencies
    const fetchCurrencies = async () => {
      try {
        const res = await fetch("https://api.frankfurter.app/currencies");
        const data = await res.json();
  
        setCurrencies(Object.keys(data));
      } catch (error) {
        console.error("Error Fetching", error);
      }
    };
  
    useEffect(() => {
      fetchCurrencies();
    }, []);
  
    console.log(currencies);
  
    // Conversion -> https://api.frankfurter.app/latest?amount=1&from=USD&to=INR
    const convertCurrency = async () => {
      if (!amount) return;
      setConverting(true);
      try {
        const res = await fetch(
          `https://api.frankfurter.app/latest?amount=${amount}&from=${fromCurrency}&to=${toCurrency}`
        );
        const data = await res.json();
  
        setConvertedAmount(data.rates[toCurrency] + " " + toCurrency);
      } catch (error) {
        console.error("Error Fetching", error);
      } finally {
        setConverting(false);
      }
    };
  
    const handleFavorite = (currency) => {
      let updatedFavorites = [...favorites];
  
      if (favorites.includes(currency)) {
        updatedFavorites = updatedFavorites.filter((fav) => fav !== currency);
      } else {
        updatedFavorites.push(currency);
      }
  
      setFavorites(updatedFavorites);
      localStorage.setItem("favorites", JSON.stringify(updatedFavorites));
    };
  
    const swapCurrencies = () => {
      setFromCurrency(toCurrency);
      setToCurrency(fromCurrency);
    };
  
  return (
    <div className='flex flex-col  w-full'>
        <div className="flex items-center justify-between ">
        <div className=" font-semibold">Exchange</div>        
        </div>
             <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 items-end">
        <CurrencyDropdown
          favorites={favorites}
          currencies={currencies}
          title="From:"
          currency={fromCurrency}
          setCurrency={setFromCurrency}
          handleFavorite={handleFavorite}
        />
        {/* swap currency button */}
        <div className="flex justify-center -mb-5 sm:mb-0">
          <button
            onClick={swapCurrencies}
            className="p-2 bg-gray-200 rounded-full cursor-pointer hover:bg-gray-300"
          >
            <HiArrowsRightLeft className="text-xl text-gray-700" />
          </button>
        </div>
        <CurrencyDropdown
          favorites={favorites}
          currencies={currencies}
          currency={toCurrency}
          setCurrency={setToCurrency}
          title="To:"
          handleFavorite={handleFavorite}
        />
      </div>

      <div className="mt-4">
        <label
          htmlFor="amount"
          className="block text-sm font-medium text-gray-700"
        >
          Amount:
        </label>
        <input
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
          type="number"
          className="w-full p-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 mt-1"
        />
      </div>

      <div className="flex  mt-6">
        <button
          onClick={convertCurrency}
          className={`px-5 py-2 bg-indigo-600 text-white rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2
          ${converting ? "animate-pulse" : ""}`}
        >
          Exchange
        </button>
      </div>

      {convertedAmount && (
          <div className="flex justify-end text-sm font-semibold text-gray-400 relative top-[-40px]">{amount} {fromCurrency} = {convertedAmount}</div>        
      )}
    </div>
  )
}

export default Exchange
