import {
    Card,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle,
  } from "@/components/ui/card";
  import React, { useState, useMemo } from "react";
  
  const ITEMS_PER_PAGE = 10;
  
  const TableCommodities = ({ commodities = [] }) => {
    const [performance, setPerformance] = useState(1); // 1 for top gainers, 0 for top losers
    const [currentPage, setCurrentPage] = useState(1);
  
    // Memoize sorted commodities and total pages
    const { sortedCommodities, totalPages } = useMemo(() => {
      const sorted = [...commodities].sort((a, b) =>
        performance === 1
          ? b.price_change_percentage_24h - a.price_change_percentage_24h
          : a.price_change_percentage_24h - b.price_change_percentage_24h
      );
      return {
        sortedCommodities: sorted,
        totalPages: Math.ceil(sorted.length / ITEMS_PER_PAGE),
      };
    }, [commodities, performance]);
  
    // Memoize paginated commodities
    const paginatedCommodities = useMemo(
      () =>
        sortedCommodities.slice(
          (currentPage - 1) * ITEMS_PER_PAGE,
          currentPage * ITEMS_PER_PAGE
        ),
      [sortedCommodities, currentPage]
    );
  
    const handlePageChange = (page) => {
      if (page >= 1 && page <= totalPages) {
        setCurrentPage(page);
      }
    };
  
    return (
      <Card>
        <CardHeader>
          <div className="flex items-center justify-between w-full">
            <div className="w-[50%]">
              <CardTitle className="flex items-center gap-2 text-lg font-semibold text-gray-900">
                <img
                  src="/commodities/commodity.png"
                  alt="commodities"
                  className="h-7 w-7"
                />
                <span>Commodities</span>
              </CardTitle>
              <CardDescription>Lista de Commodities</CardDescription>
            </div>
            <div className="w-full flex items-center justify-end text-black text-xs">
              <button
                className={`py-2 px-4 shadow-md rounded-l-lg ${
                  performance === 1 ? "bg-green-500 text-white" : ""
                }`}
                onClick={() => {
                  setPerformance(1);
                  setCurrentPage(1); // Reset to first page on sort change
                }}
              >
                Maiores Altas
              </button>
              <button
                className={`py-2 px-4 shadow-md rounded-r-lg ${
                  performance === 0 ? "bg-red-500 text-white" : ""
                }`}
                onClick={() => {
                  setPerformance(0);
                  setCurrentPage(1); // Reset to first page on sort change
                }}
              >
                Maiores Baixas
              </button>
            </div>
          </div>
        </CardHeader>
  
        <CardContent>
          <div className="grid grid-cols-10 gap-4 text-xs font-semibold bg-gray-50 p-4 border-b">
            <span>Ativo</span>
            <span>Preço</span>
            <span>Variação</span>
            <span>Close</span>
            <span>High</span>
            <span>Low</span>
            <span>Open</span>
            <span>Signal 1W</span>
            <span>Signal 1D</span>
            <span>Signal 4H</span>
          </div>
  
          {commodities.length === 0 ? (
            <div className="flex justify-center items-center h-40">
              <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-gray-900" />
            </div>
          ) : (
            paginatedCommodities.map((item, i) => (
              <a
                href={`/investments/commodities/${item.symbol}`}
                key={item.symbol || i}
              >
                <div className="grid grid-cols-10 gap-4 text-xs p-4 border-b items-center cursor-pointer hover:bg-gray-100">
                  <span className="flex items-center gap-2">
                    <span className="h-11 w-16 rounded">
                      <img
                        src={item.image}
                        alt={item.name}
                        className="w-full h-full object-cover"
                      />
                    </span>
                    <span>{item.name}</span>
                  </span>
                  <span>R$ {item.current_price?.toFixed(2)}</span>
                  <span
                    className={`${
                      item.price_change_percentage_24h >= 0
                        ? "text-green-600"
                        : "text-red-600"
                    }`}
                  >
                    {item.price_change_percentage_24h?.toFixed(2)}%
                  </span>
                  <span>R$ {item.close_24h?.toFixed(2)}</span>
                  <span>R$ {item.high_24h?.toFixed(2)}</span>
                  <span>R$ {item.low_24h?.toFixed(2)}</span>
                  <span>R$ {item.open_24h?.toFixed(2)}</span>
                  <span>-</span>
                  <span>-</span>
                  <span>-</span>
                </div>
              </a>
            ))
          )}
        </CardContent>
  
        <CardFooter className="flex items-center justify-end w-full mt-9 h-full">
          <div className="flex items-center justify-center gap-2">
            {Array.from({ length: totalPages }, (_, i) => (
              <button
                key={i}
                onClick={() => handlePageChange(i + 1)}
                className={`px-3 py-1 rounded text-sm ${
                  currentPage === i + 1 ? "bg-blue-500 text-white" : "bg-gray-200"
                }`}
              >
                {i + 1}
              </button>
            ))}
          </div>
        </CardFooter>
      </Card>
    );
  };
  
  export default TableCommodities;