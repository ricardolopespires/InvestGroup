import Image from "next/image";


import React from 'react'

const Noticias = () => {
  return (
    <div className="bg-white rounded-xl px-4 py-4 shadow-2xl h-[490px] w-[60%]">
    <div>
      <h1 className="font-semibold py-6 px-2">Notícias</h1>
      <div className="flex flex-col space-y-6">
        <div className="flex items-center space-x-4 text-sm border-b py-4">
          <Image src={"/images/noticias-1.png"} width={90} height={90} alt="noticias" />
          <div className="text-[16px] font-semibold">Por que stableecoins não podem substituir a moeda fiduciária, como diz Pe Bis Chief</div>           
        </div>
        <div className="flex items-center space-x-4 text-sm border-b py-4">
          <Image src={"/images/noticias-2.png"} width={90} height={90} alt="noticias" />
          <div className="text-[16px] font-semibold">Análise de preço do Bitcoin: nível 23836 testado - 23 de fevereiro de 2023</div>           
        </div>
      </div>
    </div>
  </div>
  )
}

export default Noticias
