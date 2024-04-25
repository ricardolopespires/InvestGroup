


import React, { useState, useEffect, useContext } from "react";
import AxiosInstance from '@/services/AxiosInstance'
import { UserContext } from "@/contexts/UserContext";
import {planos }from "@/data/planos"
import Image from "next/image";
import Item from "./item";






const Lista = () => {
  
  const[data, setData] = useState([]);  
  const user =  useContext(UserContext);
  const user_id = user.username.id  


  useEffect(() => {
      const getUserData = async () => {
        try {
          if(user_id === undefined){

          }else{
            const res = await AxiosInstance.get(`/api/v1/personal/list/plan/${user_id}`);
            console.log(res.data)
            setData(res.data);
          }
        } catch (error) {
          console.error('Erro ao obter dados do usuário:', error);
        }
      };
  
      getUserData();
    }, [user]);

  return (
    <div className='absolute inset-0 px-20 top-[210px]' >
      <div className='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4'>  
      {data.map((item, i)=>{
        return(
          <Item item={item} key={i}/>        )
      })}
      </div>
    </div>
  )
}

export default Lista
