"use client";

import React from 'react'; // Importação correta do React
import { useParams, usePathname } from "next/navigation";
import PlataformsMetaTrader from "@/components/PlataformsMetaTrader";
import ApiCrypto from '@/components/ApiCrypto';

const Page = () => { // Usar PascalCase para nome de componentes

  const params = useParams(); // Correção na definição do tipo

  console.log(params); // Lembre-se de remover ou ajustar isso em produção

  return (
    <div className="z-40">
      {params.id === "metaTrader" ? <PlataformsMetaTrader /> : ""}
      {params.id === "crypto" ? <ApiCrypto/> : ""}
      
    </div>
  );
};

export default Page; // Garantir que o nome da exportação corresponda ao nome do componente
