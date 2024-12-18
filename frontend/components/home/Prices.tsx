import { IoCheckmarkDoneOutline } from "react-icons/io5";
import { LuBadgeCheck } from "react-icons/lu";
import React from 'react'

const prices = [
    {
        name: 'Iniciante',
        price: 29,
        description: 'Melhor opção para uso pessoal e para o seu próximo projeto.',
        items:[
            {info: 'Configuração individual'},
            {info: 'Sem configuração ou taxas ocultas'},
            {info: 'Tamanho da equipe: 1 desenvolvedor'},
            {info: 'Suporte premium: 6 meses'},
            {info: 'Atualizações gratuitas: 6 meses'},
        ]
    },
    {
        name: 'Avançado',
        price: 499,
        description: 'Melhor para usos em grande escala e direitos de redistribuição estendidos.',
        items:[
            {info: 'Configuração individual'},
            {info: 'Sem configuração ou taxas ocultas'},
            {info: 'Equipe: mais de 100 desenvolvedores'},
            {info: 'Suporte premium: 36 meses'},
            {info: 'Atualizações gratuitas: 36 meses'},
        ]
    },
    {
        name: 'Premium',
        price: 99,
        description: 'Relevante para vários usuários, suporte estendido e premium.',
        items:[
            {info: 'Configuração individual'},
            {info: 'Sem configuração ou taxas ocultas'},
            {info: 'Equipe: 10 desenvolvedores'},
            {info: 'Suporte premium: 24 meses'},
            {info: 'Atualizações gratuitas: 24 meses'},
        ]
    }
 
]

const Prices = () => {
  return (
    <div className=" pb-20 pt-20">
        <div className="flex flex-col w-[80%] mx-auto text-center gap-6">
            <h1 className="mt-6 text-2xl md:text-3xl capitalize font-bold">
                Projetado o futuro das operações de Longo prazo
            </h1>
            <div>
                <p >
                    A Investgroup está concentrada nos mercados onde tecnologia, inovação e capital                 
                </p>
                <p>
                    podem liberar valor a longo prazo e impulsionar o crescimento econômico.
                </p>
            </div>
            <div className="mt-16">
                <div className="grid gap-8 grid-cols-1 lg:grid-cols-3">
                {prices.map((prices)=>(
                    <div key={prices.name} className="flex flex-col items-center bg-white shadow-md border rounded-lg p-9 gap-2">
                        <h2 className="text-3xl ">{prices.name}</h2>
                        <p className="text-gray-600 text-md font-light">{prices.description}</p>
                        <div className="flex justify-center gap-2 items-center mt-4">
                            <span className="text-4xl font-normal">R${prices.price}</span>
                            <span className="text-gray-600">/Mês</span>
                        </div>
                        <div className='flex flex-col mt-6 mb-6 w-full gap-4'>
                            {prices.items.map((item)=>(
                                <div key={item.info} className="flex gap-2 text-md items-center">
                                    <span className="text-xl text-green-500">
                                    <LuBadgeCheck />
                                    </span>
                                    <span className="text-gray-600">{item.info}</span>                                    
                                </div>
                            ))}
                        </div>
                        <div className="flex w-full">
                            <button className="w-full text-sm px-2 py-2 text-white bg-gradient-to-r from-[#0B2353] to-[#364FCE] rounded-md hover:bg-green-600">Vamos Começar</button>
                        </div>
                    </div>
                ))}
                </div>
            </div>
        </div>
    </div>
  )
}

export default Prices
