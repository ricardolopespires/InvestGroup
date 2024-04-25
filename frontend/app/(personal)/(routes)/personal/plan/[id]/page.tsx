"use client"


import Menu from "@/components/dashboard/Menu/menu";
import { FaWallet, FaPlaystation    } from "react-icons/fa";
import React, { useState, useEffect } from "react";
import AxiosInstance from '@/services/AxiosInstance'
import List from "../_components/Quantias/List";
import Created from "../_components/Quantias/Created";

import { usePathname, useSearchParams, useRouter, useParams } from 'next/navigation'


const page = ({}) => {


    const[data, setData] = useState([]); 

    const router = useRouter();
    const pathname = usePathname()   
    const params = useParams();

    const id =  params.id    
    
    useEffect(() => {
        const getUserData = async () => {
          try {
            if(id === undefined){
  
            }else{
              const res = await AxiosInstance.get(`api/v1/personal/plan/${id}/`);              
              setData(res.data);
            }
          } catch (error) {
            console.error('Erro ao obter dados do usuário:', error);
          }
        };
    
        getUserData();
      }, [id]);
  return (
    <div className='absolute inset-x-0 top-[140px] h-full px-20'>
        <div className='flex flex-col '>
        <div className="flex items-center space-x-1">
        <div className="text-3xl text-yellow-500 mr-2"><FaWallet /></div>
        <h1 className='text-2xl text-white'>Planos pessoais</h1>
        </div>
        <p className='text-gray-500 '>Tomar decisões financeiras começa com  a administração do seu próprio dinheiro.</p>
        </div>
        <Menu/>
        <div className="relative flex flex-col top-[50px] justify-between ">
            <div className="flex  items-center justify-between space-x-4">
                <div className="flex flex-col cursor-pointer bg-white space-y-5 border rounded-xl w-[79%] h-full p-6 shadow-sm hover:shadow-lg">             
                    <div className="flex items-center space-x-1 ">
                        <span className="bg-gray-200 p-3 rounded text-blue-900 shadow-lg">
                            <FaPlaystation />                
                        </span>
                        <span className="">
                            <div className="text-xl font-semibold">{ data.nome }</div>
                            <div className="text-xs">Economia mensal: R$ {data.economia}</div>
                        </span>
                    </div>
                    <div>
                    <div className="flex items-center justify-between">
                        <span className="font-semibold">R$ {data.quantia}</span>
                        <span className="text-xs">Meta: R$ {data.meta}</span> 
                    </div>
                    <span className="flex w-full h-[6px] bg-gray-200 rounded-full">
                    <span className="h-[6px] bg-primary rounded-full" style={{ width: `${data.percent}%` }}></span>
                    </span>
                    </div>
                </div> 
                <Created data={data}/>
            </div>        
            <List id={data.id} plano={data}/>     
        </div>
       
    </div>
  )
}

export default page
