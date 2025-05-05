
import { FaStreetView } from "react-icons/fa";




import React, { useEffect } from 'react'
import axios from "axios";

const CountPopulation = ({population}) => {

    const [countries, setCountries] = React.useState([])

      useEffect(() => {
        const fetchCountries = async () => {
          try {
            const res = await axios.get("https://restcountries.com/v3.1/all");
            const countriesData = res.data.map((country) => ({              
              population: country.population,
            }));
            setCountries(countriesData);
          } catch (error) {
            console.error("Error fetching countries:", error);
          }
        };
        fetchCountries();
      }, []);

      const totalPopulation = countries.reduce((acc, country) => acc + country.population, 0);
      const populationPercentage = ((population / totalPopulation) * 100).toFixed(2); // Calculate the percentage of the population


    // const population = 1000000; // Example population value
  return (
    <section className='flex items-center justify-between gap-2 has-tooltip'>
        <div className='tooltip rounded shadow-lg p-2 bg-blue-700 text-xs text-white  -mt-[80px]  right-80 w-60 '>
          <span className="flex items-center justify-center gap-2 w-full h-full ">  Porcentagem em relação da população mundial</span>
        </div>
        <FaStreetView className="text-2xl text-gray-500"/>
        <span className='text-sm'>{populationPercentage } %</span>
    </section>
  )
}

export default CountPopulation