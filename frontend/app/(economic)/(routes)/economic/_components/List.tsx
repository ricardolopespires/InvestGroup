"use client"

import { useState, useEffect } from "react";
import { useRouter, useParams } from "next/navigation";
import { FaAngleLeft,  FaAngleRight } from "react-icons/fa";
import Head from "next/head";
import Layout from "./layout";
import Neighbors from "./Neighbors";
import Search from "./Search";


import React from 'react'

const getCountry = async () => {
    // const data = await fetch(`https://restcountries.eu/rest/v2/alpha/${id}`);
    const data = await fetch(`https://restcountries.com/v3.1/all`);  
    const country = await data.json();
    return country;
  };

 

const List = () => {
 
    const router = useRouter();
    const params = useParams();
    const query = params.query;
  
    const [countries, setCountries] = useState([]);
    const [currentPage, setCurrentPage] = useState(1);
    const [countriesPerPage] = useState(10); // Defina o número de países por página
  
    const [searchText, setSearchText] = useState("");
    const regions = [
        {
        name: "Europe",
        },
        {
        name: "Asia",
        },
        {
        name: "Africa",
        },
        {
        name: "Oceania",
        },
        {
        name: "Americas",
        },
        {
        name: "Antarctic",
        },
    ];

    useEffect(() => {
        document.title = `Showing All Countries`;
    }, []);

    useEffect(() => {
        const getCountries = async () => {
        try {
            const res = await fetch("https://restcountries.com/v3.1/all");          
            const data = await res.json();      
            setCountries(data);
        } catch (error) {
            console.error(error);
        }
        };

        getCountries();
    }, []);

    async function searchCountry() {
        try {
        const res = await fetch(
            `https://restcountries.com/v3.1/name/${searchText}`
        );
        const data = await res.json();
        setCountries(data);
        } catch (error) {
        console.error(error);
        }
    }

    async function filterByRegion(region) {
        try {
        const res = await fetch(
            `https://restcountries.com/v3.1/region/${region}`
        );
        const data = await res.json();
        setCountries(data);
        } catch (error) {
        console.error(error);
        }
    }

    function handleSearchCountry(e) {
        e.preventDefault();
        searchCountry();
    }

    function handleFilterByRegion(e) {
        e.preventDefault();
        filterByRegion();
    }


     // Calcular os índices do primeiro e último país na página atual
    const indexOfLastCountry = currentPage * countriesPerPage;
    const indexOfFirstCountry = indexOfLastCountry - countriesPerPage;
    const currentCountries = countries.slice(indexOfFirstCountry, indexOfLastCountry);

    // Mudar para a próxima página
    const nextPage = () => {
        setCurrentPage(currentPage + 1);
    };

    // Mudar para a página anterior
    const prevPage = () => {
        setCurrentPage(currentPage - 1);
    };

    
  return (
    <div className="bg-white rounded-xl px-4 py-4 shadow-2xl  mt-10">
    <div>
      <div className="flex items-center justify-between">
        <h1 className="font-semibold py-6 px-2">Lista dos paises</h1>
        <form
              onSubmit={handleSearchCountry}
              autoComplete="off"
              className="max-w-4xl md:flex-1"
            >
              <input
                type="text"
                name="search"
                id="search"
                placeholder="Procure um país pelo nome"
                required
                value={searchText}
                onChange={(e) => setSearchText(e.target.value)}
                className="py-3 px-4 text-gray-600 placeholder-gray-600 w-full shadow rounded-full border outline-none dark:text-gray-400 dark:placeholder-gray-400 dark:bg-gray-800 dark:focus:bg-gray-700 transition-all duration-200"
              />
            </form>

            <form onSubmit={handleFilterByRegion}>
              <select
                name="filter-by-region"
                id="filter-by-region"
                className="w-52 py-3 px-4 outline-none shadow rounded border text-gray-600 dark:text-gray-400 dark:bg-gray-800 dark:focus:bg-gray-700"
                value={regions.name}
                onChange={(e) => filterByRegion(e.target.value)}
              >
                {regions.map((region, index) => (
                  <option key={index} value={region.name}>
                    {region.name}
                  </option>
                ))}
              </select>
            </form>      
      </div>
      <div className="block w-full overflow-x-auto ">
        <table className="items-center w-full bg-transparent border-collapse">
          <thead>
            <tr>
            <th className="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left  border-gary-700">Bandeira</th>
                <th className="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left  border-gary-700">País</th>
                <th className="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left  border-gary-700">Capital</th>
                <th className="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left  border-gary-700">População</th>
                <th className="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left  border-gary-700">Região</th>
                <th className="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left  border-gary-700">Area Km²</th>              
              </tr>
          </thead>
          {!countries ? (
        <h1 className="text-gray-900 font-bold uppercase tracking-wide flex items-center justify-center text-center h-screen text-4xl dark:text-white">
          Loading...
        </h1>
      ) : (
          <tbody> 
                
           {currentCountries.map((item, i)=>{
            return(
                <tr key={i}>
              <td className="border-t-0 px-4 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4 text-left flex items-center">
                <a href={`/economic/overview/${item.cca2}`}><img src={item.flags.png} className="h-12 w-28 bg-white rounded border" alt="..."/> </a>              
            </td>
            <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-sm font-semibold whitespace-nowrap p-4">{item.translations.por.official}</td>
            <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-sm font-semibold whitespace-nowrap p-4">{item.capital}</td>
              <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-sm font-semibold whitespace-nowrap p-4">{item.population}</td>
              <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">
                <div className="flex flex-col">
                    <span className="text-md font-semibold">{item.region }</span>                                     
                </div>
              </td>
              <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">{item.area}KM²</td>
              <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">
                <div className="flex items-center">
                      
                 </div>
              </td>                          
            </tr>
            )
           })}     
          </tbody>)}    
        </table>
        
        <div className="flex py-6 border-t space-x-2 items-center justify-end">
       {currentPage === 1 ?(""):(<button onClick={prevPage} disabled={currentPage === 1} 
       className="bg-primary px-4 rounded-l-lg text-white flex items-center space-x-1 px-4 py-1">
          <FaAngleLeft />
          <span>Anterior</span>
        </button>)}
        <p className="text-primary border border-primary px-3 p-1 rounded-full font-semibold">{currentPage}</p>        
        {indexOfLastCountry >= countries.length ?(""):(<button onClick={nextPage} disabled={indexOfLastCountry >= countries.length}
        className="bg-primary px-4 py-1 rounded-r-lg text-white flex items-center space-x-1">
          <span>Próximo</span>
          <FaAngleRight />
        </button>)}
      </div>
      </div>
    </div>
  </div>
  )
}

export default List
