import { FaWallet, FaBarcode,FaHandHoldingUsd,FaRegCreditCard, FaCar, FaPlaystation } from "react-icons/fa";
import Image from "next/image";

import React, { useState, useEffect, useContext } from "react";
import AxiosInstance from '@/services/AxiosInstance'
import { UserContext } from "@/contexts/UserContext";


const Balanco = () => {


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
        console.log(res.data)
         setData(res.data);
       
      } catch (error) {
        console.error('Erro ao obter dados do usuário:', error);
      }
    };

    getUserData();
  }, [user]);

  return (
    <div className="flex flex-col justify-between bg-white rounded-xl px-4 py-4 shadow-2xl space-y-4  mb-4">
      <div className="flex items-center justify-between">          
        <h1 className='text-md text-gray-500 '>Balanço total</h1> 
        <div className="flex space-x-1">
          <Image src={"/images/mastercard.png"} width={40} height={90} alt="card"/>
        <span>***4444</span>
        </div>    
      </div>                  
        {data.map((item, i)=>{
          return(
            <h1 className='text-3xl font-bold text-gray-800 '>R$ {item.total}</h1>
          )
        }) }   
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
  )
}

export default Balanco
