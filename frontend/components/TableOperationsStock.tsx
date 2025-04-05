import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { cn } from "@/lib/utils";
import React from "react";
import ItemsOperationsStock from "./ItemsOperationsStock";
import PerformaceOperationsStock from "./PerformaceOperationsStock";

const TableOperationsStock = ({ symbol, UserId }: { symbol: string, UserId:string } ) => {
const [selectedTab, setSelectedTab] = React.useState("tabelas");

return (
  <Card className="w-full">
    <div className="grid grid-cols-2 items-center justify-between p-4 border-b">
      { selectedTab == "tabelas" ? <CardHeader>
        <CardTitle>Operações - {symbol}</CardTitle>
        <CardDescription>Visualize os dados de suas operações.</CardDescription>
      </CardHeader>
      :
      <CardHeader>
        <CardTitle>Performance - {symbol}</CardTitle>
        <CardDescription>Visualize a performance de suas operações.</CardDescription>
      </CardHeader>
      }
      <div className="flex items-center justify-end mr-10 text-xs">
        <button
          className={cn(
            "px-4 py-2", 
            selectedTab === "tabelas" ? "bg-blue-900 text-white rounded-l-lg" : "rounded-l-lg border"
          )}
          onClick={() => setSelectedTab("tabelas")}
        >
          Abertas
        </button>
        <button
          className={cn(
            "px-4 py-2", 
            selectedTab === "history" ? "bg-blue-900 text-white " : " border"
          )}
          onClick={() => setSelectedTab("history")}
        >
          Histórico
        </button>
        <button
          className={cn(
            "px-4 py-2", 
            selectedTab === "performance" ? "bg-blue-900 text-white rounded-r-lg" : " border rounded-r-lg"
          )}
          onClick={() => setSelectedTab("performance")}
        >
          Performance
        </button>
      </div>
    </div>
    <CardContent className="flex flex-col  h-[500px]">
      {/* Aqui você pode adicionar o conteúdo da tabela ou gráfico com base na aba selecionada */}
      {selectedTab === "tabelas" ?  <ItemsOperationsStock symbol={symbol} UserId={UserId}/>: ""}
      {selectedTab === "performance" ?  <PerformaceOperationsStock/>: ""}
    </CardContent>
  </Card>
);
};

export default TableOperationsStock;

