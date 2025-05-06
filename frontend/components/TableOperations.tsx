import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { cn } from "@/lib/utils";
import React from "react";
import ItemsOperations from "./ItemsOperations";
import PerformaceOperations from "./PerformaceOperations";
import OperationsHistory from "./OperationsHistory";


const TableOperations = ({ symbol, Assest, UserId }: { symbol: string, Assest:string, UserId:string } ) => {
const [selectedTab, setSelectedTab] = React.useState("tabelas");
const user = JSON.parse(localStorage.getItem('user'))

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
    <CardContent className="flex flex-col  h-[550px]">
      {/* Aqui você pode adicionar o conteúdo da tabela ou gráfico com base na aba selecionada */}
      {selectedTab === "tabelas" ?  <ItemsOperations symbol={symbol} UserId={UserId} Assest={Assest}/>: ""}
      {selectedTab === "history" ?  <OperationsHistory symbol={symbol} UserId={UserId} Asset={Assest}/>: ""}
      {selectedTab === "performance" ?  <PerformaceOperations userId={user.email} symbol={symbol}/>: ""}
    </CardContent>
  </Card>
);
};

export default TableOperations;

