

import { FaTrashAlt    } from "react-icons/fa";
import React, { useState, useEffect } from "react";
import AxiosInstance from '@/services/AxiosInstance'
import { format } from 'date-fns';
import { toast } from 'react-toastify';



const List = ({id, plano}) => {

 
    const[data, setData] = useState([]); 

    useEffect(() => {
        const getUserData = async () => {
          try {
            if(id === undefined){
  
            }else{
              const res = await AxiosInstance.get(`/api/v1/personal/quantias/list/${id}/`); 
              console.log(res.data);                       
              setData(res.data);
            }
          } catch (error) {
            console.error('Erro ao obter dados do usuário:', error);
          }
        };
    
        getUserData();
      }, [id]);

      const handleDeleteClick = async (e) => {
        // Lógica para deletar o item
        // Por enquanto, apenas definindo isDeleted como true

        const item = data.find(item => item.id === parseInt(e));

        if (!item) {
            toast.error('A quantia não esta no banco de dados....');
            window.location.reload();  
        }else{
    
          plano["quantia"] = parseFloat(plano["quantia"]) - parseFloat(item["quantia"]);
          await AxiosInstance.put(`/api/v1/personal/plan/${plano["id"]}/`, plano); 
          await AxiosInstance.delete(`api/v1/personal/quantias/delete/${e}/`);
          toast.success('Parabéns mais quantia....');
          window.location.reload();
        
        }

       
       
 
      
      
        
      };

  return (
    <div className="bg-white rounded-xl px-4 py-4 shadow-2xl  mt-10 border border-gray-200">
    <div>
      <div className="flex items-center justify-between">
        <h1 className="font-semibold py-6 px-2">Histórico de quantias</h1>      
      </div>
      <div className="block w-full overflow-x-auto ">
        <table className="items-center w-full bg-transparent border-collapse">
          <thead>
            <tr>
                <th className="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left  border-gary-700">Plano</th>       
                <th className="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left  border-gary-700">Data</th>
                <th className="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left  border-gary-700">Valor</th>
                <th className="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left  border-gary-700">Percentual</th>
                <th className="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left  border-gary-700">Status</th>
                <th className="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left  border-gary-700"></th>                           
            </tr>
          </thead>
          <tbody>
            { data.map((item, i) =>{

            const formattedDate = format(new Date(item.created), "MMM dd',' yyyy ");
            const formattedHoras = format(new Date(item.created), "hh:mm:ss a");           

            return(
            <tr key={i}>
              <th className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4 text-left flex items-center">
                        <img src="https://demos.creative-tim.com/notus-js/assets/img/bootstrap.jpg" className="h-12 w-12 bg-white rounded-full border" alt="..."/>
                <span className="ml-3 font-bold "> {item.plano} </span></th>
              <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">
                <div className="flex flex-col">
                  <span className="text-md font-semibold">{formattedDate}</span>
                  <span className="text-xs font-light">{formattedHoras}</span>                      
                </div>
              </td>
              <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">R$ {item.quantia}</td>
              <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-sm font-semibold whitespace-nowrap p-4">{item.percent}%</td>
              <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">
                <div className="flex items-center">
                    <span className="bg-green-500 py-1 px-6 rounded-full text-white">Depósito</span>          
                 </div>
              </td> 
              <td >                  
              <button onClick={(e)=> handleDeleteClick(item.id) } className="flex items-center space-x-2 border text-sm py-1 text-gray-200 hover:bg-red-500 hover:text-white px-7 rounded-full ">
                <FaTrashAlt className="xcursor-pointer"/>
                <span>Delete</span>
              </button>      
              </td>                         
            </tr>  )})} 
          </tbody>    
        </table>
      </div>
    </div>
  </div>
  )
}

export default List
