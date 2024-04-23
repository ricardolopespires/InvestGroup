
import { format } from 'date-fns';
import React, { useState, useEffect, useContext } from "react";
import AxiosInstance from '@/services/AxiosInstance'
import { UserContext } from "@/contexts/UserContext";



const Transactions = () => {



    const[data, setData] = useState([]);  
    const user =  useContext(UserContext);
    const user_id = user.username.id  


    useEffect(() => {
        const getUserData = async () => {
          try {
            if(user_id === undefined){

            }else{
              const res = await AxiosInstance.get(`http://localhost:8000/api/v1/personal/list/despesas/${user_id}`);
              setData(res.data);
            }
          } catch (error) {
            console.error('Erro ao obter dados do usuário:', error);
          }
        };
    
        getUserData();
      }, [user]);

  
  return (
    <div className="bg-white rounded-xl px-4 py-4 shadow-2xl  mt-10">
    <div>
      <div className="flex items-center justify-between">
        <h1 className="font-semibold py-6 px-2">Histórico de transações</h1>      
      </div>
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
            { data.map((item, i) =>{

            const formattedDate = format(new Date(item.created), "MMM dd',' yyyy ");
            const formattedHoras = format(new Date(item.created), "hh:mm:ss a");           

            return(
            <tr key={i}>
              <th className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4 text-left flex items-center">
                        <img src="https://demos.creative-tim.com/notus-js/assets/img/bootstrap.jpg" className="h-12 w-12 bg-white rounded-full border" alt="..."/>
                <span className="ml-3 font-bold "> {item.categoria} </span></th>
              <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-sm font-semibold whitespace-nowrap p-4">Inscrição</td>
              <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">
                <div className="flex flex-col">
                  <span className="text-md font-semibold">{formattedDate}</span>
                  <span className="text-xs font-light">{formattedHoras}</span>                      
                </div>
              </td>
              <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">R$ {item.total}</td>
              <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">
                <div className="flex items-center">
                {item.status === "Despesas" ?
                (<span className="bg-red-500 py-1 px-6 rounded-full text-white">{item.status}</span>):
                (<span className="bg-green-500 py-1 px-6 rounded-full text-white">{item.status}</span>)
                }
                 </div>
              </td>                          
            </tr>  )})} 
          </tbody>    
        </table>
      </div>
    </div>
  </div>
  )
}

export default Transactions
