import {
    Card,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle,
} from "@/components/ui/card";
import { ScrollArea } from "@/components/ui/scroll-area";
import React, { useState, useMemo } from "react";

const TableCurrencies = ({ currencies = [] }) => {
    const [performance, setPerformance] = useState(1); // 1 for top gainers, 0 for top losers

    // Memoize sorted currencies
    const sortedCurrencies = useMemo(() => {
        return [...currencies].sort((a, b) =>
            performance === 1
                ? b.price_change_percentage_24h - a.price_change_percentage_24h
                : a.price_change_percentage_24h - b.price_change_percentage_24h
        );
    }, [currencies, performance]);

    return (
        <Card>
            <CardHeader>
                <div className="flex items-center justify-between w-full">
                    <div className="w-[50%]">
                        <CardTitle className="flex items-center gap-2 text-lg font-semibold text-gray-900">
                            <img
                                src="/currency.png"
                                alt="currencies"
                                className="h-9 w-9"
                            />
                            <span>Currencies</span>
                        </CardTitle>
                        <CardDescription>Lista de Currencies</CardDescription>
                    </div>
                    <div className="w-full flex items-center justify-end text-black text-xs">
                        <button
                            className={`py-2 px-4 shadow-md rounded-l-lg ${
                                performance === 1 ? "bg-green-500 text-white" : ""
                            }`}
                            onClick={() => setPerformance(1)}
                        >
                            Maiores Altas
                        </button>
                        <button
                            className={`py-2 px-4 shadow-md rounded-r-lg ${
                                performance === 0 ? "bg-red-500 text-white" : ""
                            }`}
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

                <ScrollArea className="h-[400px]">
                    {currencies?.length === 0 ? (
                        <div className="flex justify-center items-center h-40">
                            <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-gray-900" />
                        </div>
                    ) : (
                        sortedCurrencies.map((item, i) => (
                            <a
                                href={`/investments/currencies/${item.symbol}`}
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
                </ScrollArea>
            </CardContent>
        </Card>
    );
};

export default TableCurrencies;