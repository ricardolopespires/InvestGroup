"use client";

import {
  Pagination,
  PaginationContent,
  PaginationEllipsis,
  PaginationItem,
  PaginationLink,
  PaginationNext,
  PaginationPrevious,
} from "@/components/ui/pagination";

import { AiOutlineSearch } from "react-icons/ai";
import React, { useEffect, useState } from "react";
import axios from "axios";

const Page = ({ children }) => {
  const [query, setQuery] = useState("");
  const [countries, setCountries] = useState([]);
  const [searchResults, setSearchResults] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [itemsPerPage] = useState(20);

  useEffect(() => {
    const fetchCountries = async () => {
      try {
        const res = await axios.get("https://restcountries.com/v3.1/all");
        const countriesData = res.data.map((country) => ({
          name: country.name.common,
          flags: country.flags,
          codigo: country.cca2,
          region: country.region,
          subregion: country.subregion,
          capital: country.capital,
          population: country.population,
        }));
        setCountries(countriesData);
      } catch (error) {
        console.error("Error fetching countries:", error);
      }
    };
    fetchCountries();
  }, []);

  const handleSearch = (e) => {
    const searchValue = e.target.value;
    setQuery(searchValue);
    setCurrentPage(1);

    if (!searchValue) {
      setSearchResults([]);
      return;
    }

    const filteredCountries = countries.filter((country) =>
      country.name.toLowerCase().includes(searchValue.toLowerCase())
    );
    setSearchResults(filteredCountries);
  };

  // Pagination calculations
  const dataToDisplay = query ? searchResults : countries;
  const totalItems = dataToDisplay.length;
  const totalPages = Math.ceil(totalItems / itemsPerPage);
  const indexOfLastItem = currentPage * itemsPerPage;
  const indexOfFirstItem = indexOfLastItem - itemsPerPage;
  const currentItems = dataToDisplay.slice(indexOfFirstItem, indexOfLastItem);


  const handlePageChange = (pageNumber) => {
    if (pageNumber >= 1 && pageNumber <= totalPages) {
      setCurrentPage(pageNumber);
    }
  };

  return (
    <div className="z-40 ml-14 mr-10 -mt-[110px] flex flex-col gap-4 p-4 text-center text-white">
      <div className="flex items-center justify-between mb-4">
        <div className="z-40 flex items-center text-xs py-2 px-7 rounded-sm text-white w-full justify-end">
          <form className="w-[500px] relative" onSubmit={(e) => e.preventDefault()}>
            <div className="relative">
              <input
                type="search"
                placeholder="Pesquisar por nome do país ou nome da região"
                className="w-full p-4 rounded-full border bg-transparent text-white placeholder:text-white/70 focus:outline-none focus:ring-2 focus:ring-white/50"
                value={query}
                onChange={handleSearch}
              />
              <button
                type="submit"
                className="absolute right-1 top-1/2 -translate-y-1/2 p-4 bg-white text-slate-600 rounded-full"
              >
                <AiOutlineSearch />
              </button>
            </div>

            {searchResults.length > 0 && (
              <div className="absolute top-full left-0 right-0 mt-2 bg-white rounded-md shadow-lg max-h-60 overflow-y-auto">
                {searchResults.slice(0, 8).map((country) => (
                  <div
                    key={country.name}
                    className="p-2 text-black hover:bg-gray-100 cursor-pointer"
                  >
                    {country.name}
                  </div>
                ))}
              </div>
            )}
          </form>
        </div>
      </div>

      <div className="grid grid-cols-6 mt-4 gap-4">
        {currentItems.map((item, index) => (
         <a
         href={`/economic/overview/${item.codigo}`} // Adjust the href as needed
         key={index}
         className="gtid grid-cols-6"
       >
         <img
           src={item.flags?.png}
           alt={`Flag of ${item.name}`}
           className="w-full h-40 object-cover rounded-lg"
         />
         <span className="text-black">{item.cca2}</span>
       </a>
        ))}
      </div>

        <div className="flex items-center justify-center w-full' mt-4">
          <div className="flex items-center xmt-4 w-full">
              {totalPages > 1 && (
                <Pagination>
                  <PaginationContent>
                    <PaginationItem>
                      <PaginationPrevious
                        onClick={() => handlePageChange(currentPage - 1)}
                        className={currentPage === 1 ?  "pointer-events-none opacity-50 " : "bg-slate-200 text-black"}
                      />
                    </PaginationItem>

                    {Array.from({ length: totalPages }, (_, i) => i + 1).map((page) => (
                      <PaginationItem key={page}>
                        <PaginationLink
                          onClick={() => handlePageChange(page)}
                          isActive={currentPage === page}
                          className={currentPage === page ? "pointer-events-none opacity-50 text-black" : "bg-slate-200 text-black"}
                        >
                          {page}
                        </PaginationLink>
                      </PaginationItem>
                    ))}

                    <PaginationItem>
                      <PaginationNext
                        onClick={() => handlePageChange(currentPage + 1)}
                        className={currentPage === totalPages ? "pointer-events-none opacity-50 " : "bg-slate-200 text-black"}
                      />
                    </PaginationItem>
                  </PaginationContent>
                </Pagination>
              )}
          </div>
        </div>

      {children}
    </div>
  );
};

export default Page;