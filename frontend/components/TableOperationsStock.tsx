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

const TableOperationsStock = ({ asset }: { asset: string }) => {
const [selectedTab, setSelectedTab] = React.useState("tabelas");

return (
  <Card className="w-full">
    <div className="grid grid-cols-2 items-center justify-between p-4 border-b">
      <CardHeader>
        <CardTitle>Operações - {asset}</CardTitle>
        <CardDescription>Visualize os dados de suas operações.</CardDescription>
      </CardHeader>
      <div className="flex items-center justify-end mr-10 text-xs">
        <button
          className={cn(
            "px-4 py-2 rounded", 
            selectedTab === "tabelas" ? "bg-blue-900 text-white rounded-l-lg" : ""
          )}
          onClick={() => setSelectedTab("tabelas")}
        >
          Tabelas
        </button>
        <button
          className={cn(
            "px-4 py-2 rounded", 
            selectedTab === "performance" ? "bg-blue-900 text-white rounded-r-lg" : ""
          )}
          onClick={() => setSelectedTab("performance")}
        >
          Performance
        </button>
      </div>
    </div>
    <CardContent className="flex flex-col items-center justify-center h-[500px]">
      {/* Aqui você pode adicionar o conteúdo da tabela ou gráfico com base na aba selecionada */}
      {selectedTab === "tabelas" ?  <ItemsOperationsStock/>: ""}
      {selectedTab === "performace" ?  <PerformaceOperationsStock/>: ""}
    </CardContent>
  </Card>
);
};

export default TableOperationsStock;

