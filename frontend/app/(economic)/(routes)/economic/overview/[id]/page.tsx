"use client"

import { FaGlobeAmericas, FaReplyAll,FaMapMarkerAlt, FaLanguage, FaMapSigns, FaMapMarkedAlt, FaRestroom, FaRegEnvelope, FaFontAwesomeFlag    } from "react-icons/fa";
import { BsCurrencyExchange } from "react-icons/bs";
import { IoMdGlobe } from "react-icons/io";
import { useRouter, useParams } from "next/navigation";
import React, { useState, useEffect } from "react";
import Created from "../../_components/Favoritos/Created";
import Populacao from "../../_components/Populacao";

const page = ({children}) => {

    const params = useParams();
    const [country, setCountry] = useState(null);


    useEffect(() => {
        const getCountries = async () => {
        try {
            const res = await fetch(`https://restcountries.com/v3.1/alpha/${params.id}`);          
            const data = await res.json();         
            setCountry(data[0]);
        } catch (error) {
            console.error(error);
        }
        };

        getCountries();
    }, [params.id]);




  return (
    <div className='absolute inset-x-0 top-[140px] h-screen px-20 w-full'>
    <div className='flex flex-col '>
    <div className="flex items-center space-x-1">
    <div className="text-3xl text-yellow-500 mr-2"> {country ? (<img src={country.flags.png} className="h-6 w-12 bg-white rounded " alt="..."/>) : (
    <FaGlobeAmericas />
    )}
    </div>
    {country ? (<h1 className='text-2xl text-white'>{ country.translations.por.official}</h1>) : (
    <h1 className='text-2xl text-white'></h1>
    )}
    </div>
    <p className='text-gray-500 mt-2'>
         {country ? (<p>{ country.translations.por.official} tem o total <Populacao id={params.id}/> da população mundial</p>) : (
    <p className='text-2xl text-white'></p>    )}
       
        
        </p>
    </div> 
    <div className="flex items-center justify-between"> 
        <a href="/economic/overview/" className="text-white top-10 relative text-[40px]">        
            <FaReplyAll className="hover:text-yellow-500"/>
        </a>
        <Created id={params.id}/>   
        
    </div>
    <div className="w-full flex flex-col h-screen absolute inset-0 top-[190px] px-20 mx-auto space-y-7"> 
        {country ? (
            <div className="w-full h-[29%] flex flex-col bg-white rounded-2xl shadow-xl px-4">
                <div className="flex items-center justify-between space-x-2 p-4 border-b border-dashed">
                    <div className="text-2xl font-semibold">Informações Gerais</div> 
                    <img src={country.coatOfArms.png} className="h-16 w-28 bg-white rounded border" alt="..."/>                     
                </div>
                <div className="grid grid-cols-3 gap-4 mt-5">
                    <div className="flex flex-col space-y-4">
                        <div className="flex items-center space-x-2 "><FaMapMarkerAlt className="text-red-600 text-xl"/> <span className="font-semibold">Capital: </span><span>{country.capital}</span></div>
                        <div className="flex items-center space-x-2 "><FaLanguage className="text-blue-700 text-2xl"/> <span className="font-semibold">Idiomas: </span>
                        <ul className="flex items-center space-x-2">
                            {Object.entries(country.languages).map(([langId, langName]) => (
                                <li key={langId} className="bg-primary text-sm rounded-full px-6 py-0 text-white ">{langName}</li>
                            ))}
                            </ul>
                        </div>
                        <div className="flex items-center space-x-2 "><FaMapMarkedAlt className="text-blue-950 text-xl"/> <span className="font-semibold">Território: </span><span>{country.area}KM²</span></div>
                    </div>
                    <div className="flex flex-col space-y-4">
                    <div className="flex items-center space-x-2 "><IoMdGlobe className=" text-xl text-orange-700"/> <span className="font-semibold">Continente: </span><span>{country.continents}</span></div>
                    <div className="flex items-center space-x-2 "><FaMapSigns className=" text-xl"/> <span className="font-semibold">Fronteias: </span>
                    <ul className="flex items-center space-x-2">
                        {Object.entries(country.borders).map(([langId, langName]) => (
                            <li key={langId} className="text-sm">{langName},</li>
                        ))}
                    </ul>
                    </div>
                    <div className="flex items-center space-x-2 "><BsCurrencyExchange className=" text-xl text-green-600"/>
                    <ul>
                            {Object.entries(country.currencies).map(([currencyCode, currencyInfo]) => (
                                <li key={currencyCode} className="flex space-x-2">
                                    <p><span className="font-semibold">Moedas</span>: {currencyInfo.name}</p>
                                    <p><span className="font-semibold">Símbolo</span>: {currencyInfo.symbol}</p>
                                </li>
                            ))}
                        </ul>
                    </div>
                    </div>
                    <div className="flex flex-col space-y-4 relative left-[190px]">
                    <div className="flex items-center space-x-2 "><FaRestroom  className=" text-xl text-orange-700"/> <span className="font-semibold">População: </span><span>{country.population}</span></div>
                    <div className="flex items-center space-x-2 "><FaRegEnvelope  className=" text-xl"/> <span className="font-semibold">Sigla :</span> <span>{country.cca2 }</span></div>
                    <div className="flex items-center space-x-2 "><FaFontAwesomeFlag  className=" text-xl"/> <span className="font-semibold">Independente:</span> <span>{country.independent == true ?(<span className="text-sm bg-green-700 px-6 py-0 text-white rounded-full">Sim</span>):(<span>Não</span>    ) }</span></div>
                    </div>

                </div>
            </div>     
         ) : (
            <div className="text-2xl flex items-center justify-center h-screen">
            Carregando informações do país....
            </div>
        )}
        <div className="w-full h-[29%] flex flex-col bg-white rounded-2xl shadow-xl px-4 border border-gray-200">
            <div className="flex items-center justify-between space-x-2 p-4 border-b border-dashed">
                <div className="text-2xl font-semibold">Informações Economicas</div> 
                                        
            </div>
            <div className="grid grid-cols-3 gap-4 mt-5">

            </div>
        </div>
        <div className="w-full h-[29%] flex flex-col bg-white rounded-2xl shadow-xl px-4 border border-gray-200">
            <div className="flex items-center justify-between space-x-2 p-4 border-b border-dashed">
                <div className="text-2xl font-semibold">Principais Setores Econômicos</div> 
                                        
            </div>
            <div className="grid grid-cols-3 gap-4 mt-5">

            </div>
        </div>

    </div>
    {children}    
    </div>
  )
}

export default page
