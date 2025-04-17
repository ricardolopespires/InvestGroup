import {
    Card,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle,
  } from "@/components/ui/card"
  
  import React, { useEffect, useState } from 'react'
  
  const ITEMS_PER_PAGE = 10;
  
  const TableStock = ({ stock = [] }) => {
    const [filteredStock, setFilteredStock] = useState([]);
    const [performance, setPerformance] = useState(1);
    const [currentPage, setCurrentPage] = useState(1);
    const [totalPages, setTotalPages] = useState(1);
    const [loading, setLoading] = useState(true); // novo estado
  
    useEffect(() => {
      setLoading(true); // começa carregando
      if (stock.length > 0) {
        const sortedStock = [...stock].sort((a, b) => {
          return performance === 1
            ? b.price_change_percentage_24h - a.price_change_percentage_24h
            : a.price_change_percentage_24h - b.price_change_percentage_24h;
        });
  
        const total = Math.ceil(sortedStock.length / ITEMS_PER_PAGE);
        setTotalPages(total);
        setFilteredStock(sortedStock);
        setCurrentPage(1);
      }
      setTimeout(() => setLoading(false), 500); // simula um carregamento suave
    }, [stock, performance]);
  
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
      <Card>
        <CardHeader>
          <div className="flex items-center justify-between w-full">
            <div className="w-[50%]">
              <CardTitle>Ações</CardTitle>
              <CardDescription>Lista de ações</CardDescription>
            </div>
            <div className="w-full flex items-center justify-end text-black text-xs">
              <button
                className={`py-2 px-4 shadow-md rounded-l-lg ${performance === 1 ? "bg-green-500 text-white" : ""}`}
                onClick={() => setPerformance(1)}
              >
                Maiores Altas
              </button>
              <button
                className={`py-2 px-4 shadow-md rounded-r-lg ${performance === 0 ? "bg-red-500 text-white" : ""}`}
                onClick={() => setPerformance(0)}
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
  
          {/* Loading Spinner ou Dados */}
          {loading ? (
            <div className="flex justify-center items-center h-40">
              <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-gray-900" />
            </div>
          ) : (
            paginatedStock.map((item, i) => (
              <a href={`/investments/stock/${item.symbol}`}>
              <div key={i} className="grid grid-cols-10 gap-4 text-xs p-4 border-b items-center cursor-pointer hover:bg-gray-100">
                <span className="flex items-center gap-2">
                    <span className="h-11 w-16 rounded ">
                    <img src={item.image} alt="" className="w-full h-full object-cover" />
                    </span>
                    <span>{item.name}</span>

                </span>
                <span>R$ {item.current_price?.toFixed(2)}</span>
                <span className={`${item.price_change_percentage_24h >= 0 ? 'text-green-600' : 'text-red-600'}`}>
                  {item.price_change_percentage_24h?.toFixed(2)}%
                </span>
                
                <span>R$ {item.close_24h?.toFixed(2)}</span>
                <span>R$ {item.high_24h?.toFixed(2)}</span>
                <span>R$ {item.low_24h?.toFixed(2)}</span>
                <span>R$ {item.open_24h?.toFixed(2)}</span>
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
                  currentPage === i + 1 ? 'bg-blue-500 text-white' : 'bg-gray-200'
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
  
  export default TableStock;
  