import { FiCheckCircle } from "react-icons/fi";
import Image from "next/image";
import React from 'react'

const Indicators = () => {

  return (
    <div className='pt-14 pb-16 '>
            {/* Define grid*/}
            <div className='w-[95%]  sm:w-[80%] mx-auto items-center grid grid-cols-1 lg:grid-cols-2 gap-10'>
              {/* Image Content */}
              <div>
                  <Image src={"/images/feature-2.png"} width={900} height={900} alt="Features" className="object-contain"/>
              </div>
              {/* Text Content */}
              <div className="p-6">
              <span className="text-base font-semibold text-blue-900 relative after:content-[''] after:block after:w-[270px] after:h-[2px] after:bg-gray-200 after:rounded-full">Indicadores Econômicos</span>
    
                <h1 className="mt-4 text-xl sm:text-3xl font-bold text-gray-900">
                    Principais Indicadores Econômicos
                </h1>
                <p className="mt-4 font-light text-gray-600 text-sm text-justify leading-[1.6rem]  italic">
                Os indicadores econômicos ajudam a entender em números os resultados das decisões coletivas.
                Sendo assim, eles ajudam a entender o cenário macroeconômico.
                Os indicadores servem para que seja possível visualizar a realidade econômica de forma direta e quantitativa.
                </p>
                <ul className="mt-7 space-y-4 text-gray-800">
                  <li className="flex items-center font-semibold">
                    <FiCheckCircle className="text-2xl text-green-500 mr-2"/>
                    <span>Taxa de Crescimento do PIB</span>
                  </li>
                  <li className="flex items-center font-semibold">
                    <FiCheckCircle className="text-2xl text-green-500 mr-2"/>
                    <span>Taxa De Juros.</span>
                  </li>
                  <li className="flex items-center font-semibold">
                    <FiCheckCircle className="text-2xl text-green-500 mr-2"/>
                    <span>Taxa De Inflação.</span>
                  </li>
                  <li className="flex items-center font-semibold">
                    <FiCheckCircle className="text-2xl text-green-500 mr-2"/>
                    <span>Taxa de Desemprego.</span>
                  </li>
                  <li className="flex items-center font-semibold">
                    <FiCheckCircle className="text-2xl text-green-500 mr-2"/>
                    <span>Classificação de Risco de Crédito.</span>
                  </li>
                </ul>
                <a href={"/trends"}>
                    <button className="mt-9 px-8 py-3 text-sm bg-gray-100 text-gray-800 font-semibold rounded-full hover:bg-gradient-to-r from-[#0B2353] to-[#364FCE]
                    hover:text-white transition-all duration-200">
                      Mais informações &rarr;
                    </button>
                </a>                
              </div>
            </div>
            
    </div>
  )
}

export default Indicators
