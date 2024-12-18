"use client"

import { TbMapPinDollar } from "react-icons/tb";
import { MdHistory } from "react-icons/md";
import { FaMoneyBillTransfer } from "react-icons/fa6";
import { SiSoundcharts } from "react-icons/si";
import { FaReplyAll, FaThermometerThreeQuarters  } from "react-icons/fa";
import { PiShieldWarningBold } from "react-icons/pi";
import { FiActivity } from "react-icons/fi";
import React, { useState, useEffect } from 'react';
import { useParams } from "next/navigation";
import AxiosInstance from '@/services/AxiosInstance'


const Page = () => {


  const [data, setData] = useState([])
  const investimento_id = useParams().id

  
  useEffect(() => {

      const getUserProfile = async () => {
        try {
          const res = await AxiosInstance.get(`api/v1/management/investimentos/${investimento_id}/list/`);
          console.log(res.data);             
          setData(res.data);
        } catch (error) {
          console.error('Erro ao obter perfil:', error);
        }
      };

      getUserProfile();
   
  }, [investimento_id]);

  return (
    <div className='absolute inset-x-0 top-[140px]  px-20  h-screen'>
    <div className='flex flex-col '>
      <div className="flex items-center space-x-1">
      <div className="text-3xl text-amber-500 mr-2"><SiSoundcharts/></div>
      <h1 className='text-2xl text-white'>{ data.name}</h1>
      </div>
      <p className='text-gray-500 mt-2'>O tipo de investimento é de renda <strong className="text-white">{data.type}</strong>  é preciso saber quais são as vantagem e se adequam ao que você está buscando.</p>
    </div>
    <a href="/settings" className="mt-10 flex items-center text-white mr-5 hover:text-yellow-500 text-4xl font-semibold ">     
      <FaReplyAll />     
    </a>
    <div className="flex items-center justify-between space-x-4 absolute  top-[119px] inset-0 h-screen px-20">
      <div className="flex flex-col space-y-[70px] w-full  shadow-2xl bg-white rounded-2xl h-[90%] relative inset-0 p-9">
        <div className="flex flex-col space-x-1 w-full ">
          <div className="text-2xl flex space-x-2">
            <TbMapPinDollar className="text-primary"/>
            <h1 className='text-2xl w-full font-semibold'>Descrição</h1>    
          </div>   
          <div className="relative top-[9px]">
            {data?(<p>{data.description}</p> ):("")}
          </div>  
        </div>        
        <div className="grid grid-cols-4 items-center gap-4">
          <div className="flex flex-col space-x-1 w-full items-center">
            <div className="text-2xl flex items-center space-x-2">
              <MdHistory  className=" text-primary text-4xl"/>
              <h1 className='w-full font-semibold'>Periodo</h1>   
            </div>
            <div className="relative top-[9px] flex items-center gap-2">
              {data?(data.time?.map((item, i)=>{return(<div className="bg-primary py-1 px-4 rounded-full text-xs text-white">{item.title}</div>)}) ):("")}
            </div>             
          </div>
          <div className="flex flex-col space-x-1 w-full items-center">
            <div className="text-2xl flex items-center space-x-2">
              <PiShieldWarningBold className=" text-primary text-4xl"/>
              <h1 className='w-full font-semibold'>Risco</h1>   
              </div>
              <div className="relative top-[9px] flex items-center gap-2">
              {data?(data.risco?.map((item, i)=>{return(<div key={i} className={`${item.color} py-1 px-4 rounded-full text-xs text-white`}>{item.nivel}</div>)}) ):("")}
            </div>             
          </div>
          <div className="flex flex-col space-x-1 w-full items-center">
            <div className="text-2xl flex items-center space-x-2">
              <FiActivity   className=" text-primary text-4xl"/>
              <h1 className='w-full font-semibold'>Volatilidade</h1>   
              </div>
              <div className="relative top-[9px] flex items-center gap-2">
              {data?(data.volatilidade?.map((item, i)=>{return(<div key={i} className={`${item.color} py-1 px-4 rounded-full text-xs text-white`}>{item.nivel}</div>)}) ):("")}
            </div>             
          </div>
          <div className="flex flex-col space-x-1 w-full items-center">
            <div className="text-2xl flex items-center space-x-2">
              <FaThermometerThreeQuarters   className=" text-primary "/>
              <h1 className='w-full font-semibold'>Nivel</h1>   
              </div>
              <div className="relative top-[9px] flex items-center gap-2">
              {data?(<div className="bg-primary py-1 px-4 rounded-full text-xs text-white">{data.nivel}</div>):("")}
            </div>             
          </div>
        </div>
        <div className="flex flex-col space-x-1 w-full ">
          <div className="text-2xl flex space-x-2 items-center">
            <FaMoneyBillTransfer  className="text-primary"/>
            <h1 className='text-2xl w-full font-semibold'>Locação do capital</h1>    
          </div>   
          <div className="relative top-[9px] bg-gray-200 w-full h-4 rounded-full">
            <div className="absolute flex w-full text-xs font-semibold items-center justify-center">50%</div>
            <div className="flex w-[45%] bg-primary h-4 rounded-full"></div>
            
          </div>  
        </div>  
      </div>
    </div>
    </div>

  )
}

export default Page
