import { FaWallet, FaRegCreditCard } from "react-icons/fa";
import { GoArrowUp } from "react-icons/go";

import React, { useState, useEffect, useContext } from "react";
import AxiosInstance from '@/services/AxiosInstance'
import { UserContext } from "@/contexts/UserContext";


const Movimentacao = () => {


  const[data, setData] = useState([]);

  const user =  useContext(UserContext);
  const user_id = user.username.id  


    useEffect(() => {
        const getUserData = async () => {
          try {
            if(user_id === undefined){
              return
            }
            const res = await AxiosInstance.get(`/api/v1/personal/list/periodos/${user_id}`);     
             setData(res.data);
           
          } catch (error) {
            console.error('Erro ao obter dados do usuário:', error);
          }
        };
    
        getUserData();
      }, [user]);



  return (
    <div>
      {data.map((item, i)=>{

        return(
          <div className=" flex bg-white rounded-xl px-4  shadow-2xl mb-6 h-[280px]" key={i}>
            <div className="flex flex-col w-[29%] ">
              <div className="w-full h-[50%] flex py-4 border-r  border-b">
                  <div className="flex flex-col w-full ">
                    <span className="text-md text-gray-500 ">Renda total</span>
                    <span className="text-3xl font-semibold">R$ {item .revenues }</span>
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
                    <span className="text-3xl font-semibold">R$ {item.expenses }</span>
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
                    <span className="text-3xl font-semibold">R$ {item.spending}</span>
                    <div className="flex items-center space-x-1 text-xs w-full">
                      <span className=" flex bg-gray-200 w-[100%] h-[10px] rounded-full ">
                        <span className={`bg-blue-900  h-[10px] rounded-full `} style={{ width: `${item.limit}%` }}></span>
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
        )
      })}
    </div>
  )
}

export default Movimentacao
