import React, { useState, useEffect } from 'react';

const Populacao = ({ id }) => {
    const [country, setCountry] = useState(null);
    const [countries, setCountries] = useState([]);
    const [totalPopulationPercentage, setTotalPopulationPercentage] = useState(0);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const res = await fetch(`https://restcountries.com/v3.1/alpha/${id}`);
                const data = await res.json();
                setCountry(data[0]);
            } catch (error) {
                console.error(error);
            }
        };

        fetchData();
    }, [id]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const res = await fetch("https://restcountries.com/v3.1/all");
                const data = await res.json();
                setCountries(data);
            } catch (error) {
                console.error(error);
            }
        };

        fetchData();
    }, []);

    useEffect(() => {
        if (country && countries.length > 0) {
            const totalPopulation = countries.reduce((total, c) => total + c.population, 0);
            const countryPopulation = country.population;
            const percentage = (countryPopulation / totalPopulation) * 100;
            setTotalPopulationPercentage(percentage.toFixed(2));
        }
    }, [country, countries]);

    return (
        <span className="text-white relative mr-1">{totalPopulationPercentage}%</span>
    );
};

export default Populacao;
