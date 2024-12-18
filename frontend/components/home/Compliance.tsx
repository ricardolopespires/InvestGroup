import { FaDesktop, FaLaptop, FaLayerGroup, FaMobileAlt } from "react-icons/fa";

import Image from "next/image";
import React from 'react'






const Compliance = () => {

       const features = [
          { 
            icon: <FaLayerGroup/>,
            name: '100% Online',
            description: "Acesso ilimitado para todos os clientes"
            
          },
          { 
            icon: <FaLaptop/>,    
            name: '600M+ Usuários',
            description: "Até 600 milhões de clientes com um único dispositivo móvel"      
          },
          { 
            icon: <FaMobileAlt/>,
            name: '10+ Países',
            description: "Até 10 países com um único dispositivo móvel"      
          },
          { 
            icon: <FaDesktop/>,
            name: '5+ Milhões',            
            description: "Até 1 milhões de clientes com um único desktop"       
          },
        ]
    
  return (
    <div className='pt-14 pb-16 bg-[#F7F6FB]'>
            {/* Define grid*/}
            <div className='w-[95%]  sm:w-[80%] mx-auto items-center grid grid-cols-1 lg:grid-cols-2 gap-10'>         
              {/* Text Content */}
              <div className="p-6">
                <span className="text-base font-semibold text-blue-900 relative after:content-[''] after:block after:w-[270px] after:h-[2px] after:bg-gray-200 after:rounded-full">Segurança & Conformidade</span>
                <h1 className="mt-4 text-xl sm:text-3xl font-bold text-gray-900">
                    Os Dados Transformando Negócios
                </h1>
                <p className="mt-4 font-light text-gray-600 text-sm text-justify leading-[1.6rem]  italic">
                    Entender o potencial estratégico da análise das informações para obter insights e descobrir
                    tendências com os rigorosos padrões de segurança e conformidade estão no centro de tudo o que fazemos.
                    Trabalhamos incansavelmente para analisar os dados e entender como esse ecossistema pode melhorar positivamente
                    o futuro dos mais diversos tipos de negócios e levando a movimentos de negócios mais inteligentes, operações mais eficientes....
                </p>               
                <div className="flex flex-col items-start mt-11">
                    <button className="px-8 py-3 text-sm bg-gray-100 text-gray-800 font-semibold rounded-full hover:bg-blue-900
                    hover:text-white transition-all duration-200">
                    Explorar o Guia de Legalidade &rarr;
                    </button>
                    <button className=" px-8 py-3 text-sm bg-gray-100 text-gray-800 font-semibold rounded-full hover:bg-blue-900
                    hover:text-white transition-all duration-200">
                   Visite a Central de Confiabilidade &rarr;
                    </button>
                </div>
              </div>
               {/* Image Content */}
               <div className="mt-16">
                    <div className="grid gap-8 grid-cols-1 lg:grid-cols-2">
                    {features.map((feature, index) => (
                        <div key={index} className="flex flex-col justify-center p-8 rounded-md">
                        <div className="flex items-center justify-center w-16 h-16 text-4xl text-green-500">
                            {feature.icon}
                        </div>
                        <div className="ml-4">
                            <h2 className="text-xl font-bold">{feature.name}</h2>
                            <p className="w-full">{feature.description}</p>
                        </div>
                        </div>
                    ))}
                    </div>
                </div>
            </div>
            
    </div>
  )
}

export default Compliance
