import { FaTrashAlt    } from "react-icons/fa";
import AxiosInstance from '@/services/AxiosInstance'
import { toast } from 'react-toastify';


import React from 'react'

const Delete = () => {


    const handleDeleteClick = () => {
        // Lógica para deletar o item
        // Por enquanto, apenas definindo isDeleted como true
    
      };

      
  return (
    <button onClick={handleDeleteClick} className="flex items-center space-x-2 border text-sm py-1 text-gray-200 hover:bg-red-500 hover:text-white px-7 rounded-full ">
         <FaTrashAlt className="xcursor-pointer"/>
        <span>Delete</span>
    </button>   
  )
}

export default Delete
