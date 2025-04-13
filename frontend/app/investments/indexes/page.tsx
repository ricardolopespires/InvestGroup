"use client"


import React, { useEffect, useState } from "react";
import IndexWidgets from "@/components/IndexWidgets";
import { getAssetsStocks } from "@/lib/actions/actions.stock";
import Stock from "@/components/Stock";
import AnalysisWidget from "@/components/AnalysisWidget";

const ITEMS_PER_PAGE = 10; // Número de itens por página

const Page = () => {
  const [stock, setStock] = useState([]);
  const [filteredStock, setFilteredStock] = useState([]);
  const [performance, setPerformance] = useState(1); // 1 para altas, 0 para baixas
  const [error, setError] = useState(false);
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);

  useEffect(() => {
    const fetchCryptos = async () => {
      try {
        const res = await getAssetsStocks();
        setStock(res);
      } catch (err) {
        setError(true);
        console.error(err);
      }
    };
    
    fetchCryptos();
  }, []);

  // Filtra e ordena os dados quando stock ou performance mudam
  useEffect(() => {
    if (stock.length > 0) {
      const sortedStock = [...stock].sort((a, b) => {
        if (performance === 1) {
          // Maiores altas primeiro
          return b.price_change_percentage_24h - a.price_change_percentage_24h;
        } else {
          // Maiores baixas primeiro
          return a.price_change_percentage_24h - b.price_change_percentage_24h;
        }
      });
      
      const total = Math.ceil(sortedStock.length / ITEMS_PER_PAGE);
      setTotalPages(total);
      setFilteredStock(sortedStock);
      setCurrentPage(1); // Reset para primeira página ao mudar filtro
    }
  }, [stock, performance]);

  // Calcula os itens da página atual
  const paginatedStock = filteredStock.slice(
    (currentPage - 1) * ITEMS_PER_PAGE,
    currentPage * ITEMS_PER_PAGE
  );

  const handlePageChange = (page) => {
    if (page >= 1 && page <= totalPages) {
      setCurrentPage(page);
    }
  };

  return (
    <div className="max-w-screen-4xl mx-auto w-full pb-10 mt-24 text-white">
      {/* Cabeçalho com Botão */}
      <div className="w-full flex items-center justify-between gap-4 mt-4">
        <div className="w-[75%]">
          <IndexWidgets asset="SP500" />
        </div>
        <div className="w-[25%]">
          <AnalysisWidget asset="SPX" />
        </div>
      </div>

      {/* Controles de filtro */}
      <div className="w-full flex items-center justify-end gap-1 mt-4 text-black text-xs">
        <button 
          className={`py-2 px-4  shadow-md rounded-l-lg  ${performance === 1 ? "bg-green-500 text-white rounded-l-lg" : "rounded-l-lg "}`}
          onClick={() => setPerformance(1)}
        >
          Maiores Altas
        </button>
        <button 
          className={`py-2 px-4 shadow-md rounded-r-lg  ${performance === 0 ? "bg-red-500 text-white rounded-r-lg" : "rounded-r-lg "}`}
          onClick={() => setPerformance(0)}
        >
          Maiores Baixas
        </button>
      </div>

      {/* Grid de Widgets */}
      <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4">
        {paginatedStock.map((item) => (
          <div key={item.id} className="w-full h-full">
            <Stock asset={item.symbol} />
          </div>
        ))}
      </div>

      {/* Controles de Paginação */}
     <div className="flex items-center justify-end  mt-4 mb-9">
      <div>
        {totalPages > 1 && (
            <div className="flex justify-center items-center gap-4 mt-4">
              <button
                onClick={() => handlePageChange(currentPage - 1)}
                disabled={currentPage === 1}
                className="px-4 py-2 bg-gray-700 rounded disabled:opacity-50"
              >
                Anterior
              </button>
              <span className="text-black">
                Página {currentPage} de {totalPages}
              </span>
              <button
                onClick={() => handlePageChange(currentPage + 1)}
                disabled={currentPage === totalPages}
                className="px-4 py-2 bg-gray-700 rounded disabled:opacity-50"
              >
                Próxima
              </button>
            </div>
          )}
      </div>
     </div>

      {error && (
        <div className="text-red-500 text-center">
          Erro ao carregar os dados
        </div>
      )}
    </div>
  );
};

export default Page;