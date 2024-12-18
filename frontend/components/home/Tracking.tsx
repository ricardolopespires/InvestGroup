import { FiCheckCircle } from "react-icons/fi";
import Image from "next/image";






import React from 'react'

const Tracking = () => {
  return (
      <div className='pt-14 pb-16 bg-[#F7F6FB]'>
        {/* Define grid*/}
        <div className='w-[95%]  sm:w-[80%] mx-auto items-center grid grid-cols-1 lg:grid-cols-2 gap-10'>         
          {/* Text Content */}
          <div className="p-6">
            <span className="text-base font-semibold text-blue-900 relative after:content-[''] after:block after:w-[270px] after:h-[2px] after:bg-gray-200 after:rounded-full">Economia e Mercado Financeiro </span>
            <h1 className="mt-4 text-xl sm:text-3xl font-bold text-gray-900">
              Previsões e tendências macroeconômicas
            </h1>
            <p className="mt-4 font-light text-gray-600 text-sm text-justify leading-[1.6rem]  italic">
            A análise e as projeções macroeconômicas como os resultado decorre do dinamismo econômico, monitorados a evolução e a tendências dos indicadores relativos à atividade econômica, inflação, 
            crédito, emprego e renda, setor externo e economia internacional. E seus das principais indicadores.           
            Entender sobre economia e mercado financeiro é fundamental para todos os investidores.
            </p>
            <ul className="mt-7 space-y-4 text-gray-800">
              <li className="flex items-center font-semibold">
                <FiCheckCircle className="text-2xl text-green-500 mr-2"/>
                <span>PIB</span>
              </li>
              <li className="flex items-center font-semibold">
                <FiCheckCircle className="text-2xl text-green-500 mr-2"/>
                <span>Rentabilidade</span>
              </li>
              <li className="flex items-center font-semibold">
                <FiCheckCircle className="text-2xl text-green-500 mr-2"/>
                <span>Lucratividade</span>
              </li>
              <li className="flex items-center font-semibold">
                <FiCheckCircle className="text-2xl text-green-500 mr-2"/>
                <span>Endividamento.</span>
              </li>
            </ul>
            <a href={"/trends"}>
              <button className="mt-9 px-8 py-3 text-sm border border-blue-800 font-semibold rounded-full 
              text-blue-800 transition-all duration-200 hover:bg-gradient-to-r from-[#0B2353] to-[#364FCE] hover:text-white">
                Mais informações &rarr;
              </button>
            </a>
          </div>
           {/* Image Content */}
           <div>
              <Image src={"/images/feature-1.png"} width={900} height={900} alt="Features" className="object-contain"/>
          </div>
        </div>
        
      </div>
  )
}

export default Tracking
