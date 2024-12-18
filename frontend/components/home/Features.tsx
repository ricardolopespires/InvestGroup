import { FaBook, FaCog, FaDesktop, FaHeadset, FaInfinity, FaLaptop, FaLayerGroup, FaMobileAlt, FaShieldAlt } from "react-icons/fa";
import { MdOutlineSecurity } from "react-icons/md";
import React from 'react'




const Features = () => {

  const features = [
    { 
      icon: <FaLayerGroup className="text-red-500"/>,
      name: '50+ Design Exclusivo', 
    },
    { 
      icon: <FaLaptop className="text-green-500"/>,    
      name: 'Multiplos Layouts',      
    },
    { 
      icon: <FaMobileAlt className="text-green-500"/>,
      name: 'Dispositivo Móvel',      
    },
    { 
      icon: <FaDesktop className="text-red-500"/>,
      name: 'Totalmente Responsivo',       
    },
    { 
      icon: <FaCog className="text-red-500"/>,
      name: 'Recursos Personalizáveis',       
    },
    { 
      icon: <FaHeadset className="text-red-500"/>,
      name: 'Suporte 12H',       
    },
    { 
      icon: <FaInfinity className="text-red-500"/>,
      name: 'Atualizações Vitalícias',       
    },
    { 
      icon: <FaBook className="text-red-500"/>,
      name: 'Documentações',       
    },
    { 
      icon: <FaShieldAlt className="text-red-500"/>,
      name: 'Segurança Aprimorada',       
    },
  ]
  


  return (
   <div className=" pb-20 pt-20">
      <div className="w-[80%] mx-auto text-center">
          <h1 className="mt-6 text-2xl md:text-3xl capitalize font-bold">
            É tudo o que você sempre precisará
          </h1>
          <div className="mt-16">
            <div className="grid gap-8 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3">
              {features.map((feature, index) => (
                <div key={index} className="flex items-center justify-center p-8 rounded-md shadow-md bg-white gap-6">
                  <div className="flex items-center justify-center w-16 h-16 text-3xl bg-gradient-to-r from-[#0B2353] to-[#364FCE] bg-opacity-10 rounded-full">
                    {feature.icon}
                  </div>
                  <div className="ml-4">
                    <h2 className="text-xl font-bold">{feature.name}</h2>
                    <p>{feature.description}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
      </div>
   </div>
  )
}

export default Features
