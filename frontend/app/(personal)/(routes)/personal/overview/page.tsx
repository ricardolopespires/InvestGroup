import { BiBitcoin } from "react-icons/bi";
import { FaWallet, FaChild,FaCreditCard, FaDollarSign, FaBarcode, FaHandHoldingUsd,FaRegCreditCard, FaCashRegister, FaCar, FaPlaystation     } from "react-icons/fa";
import { GoArrowUp } from "react-icons/go";
import { GrCreditCard } from "react-icons/gr";
import Image from "next/image";
import Menu from "@/app/_components/menu";
import React from 'react'

const Page = ({children}) => {
  return (
    <div className='absolute inset-x-0 top-[140px] h-full px-20'>
      <div className='flex flex-col '>
      <div className="flex items-center space-x-1">
      <div className="text-3xl text-yellow-500 mr-2"><FaWallet /></div>
      <h1 className='text-2xl text-white'>Finanças pessoais</h1>
      </div>
      <p className='text-gray-500 '>Tomar decisões financeiras começa com  a administração do seu próprio dinheiro.</p>
      </div>
      <Menu/>
      <div className="flex items-center justify-between space-x-4 relative top-9">
        <div className="w-[25%] flex-col">
          <div className="flex flex-col justify-between bg-white rounded-xl px-4 py-4 shadow-2xl h-[190px]  mb-4">
            <div className="flex items-center justify-between">          
                <h1 className='text-md text-gray-500 '>Balanço total</h1> 
                <div className="flex space-x-1">
                  <Image src={"/images/mastercard.png"} width={40} height={90} alt="card"/>
                <span>***4444</span>
                </div>    
            </div>                  
                <h1 className='text-3xl font-bold text-gray-800 '>R$ 0,00</h1>     
              <div className="flex space-x-2 items-center justify-between px-10">
                <button className="flex items-center space-x-2 text-sm py-2 px-9 rounded  bg-gradient-to-r from-[#0B2353] to-[#364FCE] text-white">
                <FaBarcode />
                  <span>Transfer</span>
                  </button>
                <button className="flex items-center space-x-2 text-sm py-2 px-9 rounded  bg-gradient-to-r from-[#0B2353] to-[#364FCE] text-white">
                <FaHandHoldingUsd />
                  <span>Receive</span>
                  </button>
              </div>
            
          </div>
          <div className="flex flex-col bg-white rounded-xl px-4 py-4 shadow-2xl h-[600px]">
            <h1 className="font-semibold py-6 px-2">Salvando planos</h1>
            <div className="flex flex-col space-y-6">
              <div className="flex flex-col justify-between border rounded-xl w-full h-40 p-6 shadow-sm hover:shadow-lg">             
              <div className="flex items-center space-x-2 ">
                  <span className="bg-gray-200 p-3 rounded text-blue-900 shadow-lg">
                    <FaCar />                
                  </span>
                  <span className="">
                    <div className="text-xl font-semibold">Obter carro novo</div>
                    <div className="text-xs">Economia mensal: R$0.00</div>
                  </span>
              </div>
              <div className="flex items-center justify-between">
                <span className="font-semibold">R$ 0.00</span>
                <span className="text-xs">Meta: R$ 0.00</span> 
              </div>
              <span className="flex w-full h-[6px] bg-gray-200 rounded-full ">
                <span className="w-[20%] h-[6px] bg-lime-600 rounded-full"></span>
              </span>
              </div>
              <div className="flex flex-col justify-between border rounded-xl w-full h-40 p-6 shadow-sm hover:shadow-lg">             
                <div className="flex items-center space-x-2 ">
                    <span className="bg-gray-200 p-3 rounded text-blue-900 shadow-lg">
                      <FaPlaystation />                
                    </span>
                    <span className="">
                      <div className="text-xl font-semibold">Comprar PS5</div>
                      <div className="text-xs">Economia mensal: R$0.00</div>
                    </span>
                </div>
                <div className="flex items-center justify-between">
                  <span className="font-semibold">R$ 0.00</span>
                  <span className="text-xs">Meta: R$ 0.00</span> 
                </div>
                <span className="flex w-full h-[6px] bg-gray-200 rounded-full">
                  <span className="w-[50%] h-[6px] bg-lime-600 rounded-full"></span>
                </span>
                </div>
            </div>
          </div>
        </div>
        <div className="w-[75%] flex-col relative ">
          <div className="h-[290px] flex bg-white rounded-xl px-4  shadow-2xl mb-6">
          <div className="flex flex-col w-[29%]">
            <div className="w-full h-[50%] flex py-4 border-r  border-b">
                <div className="flex flex-col w-full ">
                  <span className="text-md text-gray-500 ">Renda total</span>
                  <span className="text-3xl font-semibold">R$ 0,00</span>
                  <div className="flex items-center space-x-1 text-xs">
                    <span className="text-green"><GoArrowUp /></span>
                    <span>0%</span>
                    <span>Das últimas semanas</span>
                  </div>

                </div>
                <div className="mr-10 bg-blue-100 p-4 h-[50px] rounded-lg text-lg text-blue-700 flex"> 
                  <FaWallet/>
                </div>
            </div>
            <div className="w-full h-[50%] flex py-4 border-r  ">
                <div className="flex flex-col w-full justify-between">
                  <span className="text-md text-gray-500 ">Custo total</span>
                  <span className="text-3xl font-semibold">R$ 0,00</span>
                  <div className="flex items-center space-x-1 text-xs">
                    <span className="text-green"><GoArrowUp /></span>
                    <span>0%</span>
                    <span>Das últimas semanas</span>
                  </div>

                </div>
                <div className="mr-10 bg-red-100 p-4 h-[50px] rounded-lg text-lg text-red-700 flex"> 
                <FaRegCreditCard/>
                </div>
            </div>
          </div>
          <div className="flex flex-col w-[71%]">
          <div className="w-full h-[50%] flex py-4 border-b px-4 ">
                <div className="flex flex-col w-full justify-between">
                  <div className="flex items-center justify-between">
                    <span className="text-md text-gray-500 ">Limite de gastos</span>
                    <div className="mr-10 bg-blue-100 p-4 h-[50px] rounded-lg text-lg text-blue-700 flex"> 
                    <FaWallet/>
                    </div>
                  </div>                  
                  <span className="text-3xl font-semibold">R$ 0,00</span>
                  <div className="flex items-center space-x-1 text-xs w-full">
                    <span className=" flex bg-gray-200 w-[70%] h-[10px] rounded-full ">
                      <span className="w-[70%] bg-blue-900  h-[10px] rounded-full "></span>
                    </span>                
                    <span className="flex w-[30%] bg-gray-200 h-[10px] rounded-full">
                    <span className="w-[90%] bg-red-400  h-[10px] rounded-full"></span>
                    </span> 
                  </div>
                </div>                
            </div>
            <div className="w-full h-[50%] flex py-4 px-4 ">
              <div className="flex flex-col w-full justify-between h-full">                  
                <div className="flex items-center justify-between">
                    <span className="text-md text-gray-500 ">Análise de despesas</span>
                    <div className="mr-10 bg-blue-100 p-4 h-[50px] rounded-lg text-lg text-blue-700 flex"> 
                    <FaWallet/>
                    </div>
                </div>                
              </div>                
            </div>
          </div>
          </div>
          <div className="bg-white rounded-xl px-4 py-4 shadow-2xl h-[490px]">
            <div>
              <h1 className="font-semibold py-6 px-2">Histórico de transações</h1>
              <div className="block w-full overflow-x-auto ">
                    <table className="items-center w-full bg-transparent border-collapse">
                      <thead>
                        <tr>
                          <th className="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left  border-gary-700">Nome</th>
                          <th className="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left  border-gary-700">Tipo</th>
                          <th className="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left  border-gary-700">Data</th>
                          <th className="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left  border-gary-700">Valor</th>
                          <th className="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left  border-gary-700">Status</th>                         
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                        <th className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4 text-left flex items-center">
                          <img src="https://demos.creative-tim.com/notus-js/assets/img/bootstrap.jpg" className="h-12 w-12 bg-white rounded-full border" alt="..."/>
                          <span className="ml-3 font-bold "> Argon Design System </span></th>
                        <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-sm font-semibold whitespace-nowrap p-4">Inscrição</td>
                        <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">
                          <div className="flex flex-col">
                            <span className="text-md font-semibold">Oct 20,2022</span>
                            <span className="ml-2">10:40 PM</span>
                          </div>
                        </td>
                          <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">$2,500 USD</td>
                            <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"><div className="flex items-center">
                            <span className="bg-orange-500 py-1 px-6 rounded-full text-white">pendente</span>
                              </div>
                            </td>                          
                          </tr>   
                      </tbody>    
                    </table>
                  </div>
            </div>
          </div>
        </div>   
     

      </div>
      {children}
    </div>
  )
}

export default Page