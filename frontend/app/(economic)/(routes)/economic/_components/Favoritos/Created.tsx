"use client"

import { FaGlobeAmericas, FaReplyAll, FaRegStar, FaStar  } from "react-icons/fa";
import AxiosInstance from '@/services/AxiosInstance'
import React, { useState, useContext } from "react";
import { toast } from "react-toastify";
import { UserContext } from "@/contexts/UserContext";

const Created = ({id}) => {

  const [star, setStar] = useState(false);
  const user =  useContext(UserContext);
  const user_id = user.username.id  


  const handlerStar = async () =>{
    setStar(!star);
    
    if(star == true){
      toast.error("Voce tirou do pais da lista de favorito")
    } else{      
      toast.success("Parabens você adicionou o pais da lista de favorito")
      await AxiosInstance.post(`/api/v1/economia/list/countries/`, {"countries":id,"user_id":user_id,});
  
  }
}

  

  return (
    <div className="text-white top-10 relative text-[40px] cursor-pointer ">   
    {star ? (
      <FaStar className="text-yellow-500" onClick={handlerStar}/>
    ):(
      <FaRegStar onClick={handlerStar} className="hover:text-yellow-500 " />
    )}
</div>
  )
}

export default Created
