"use client"


import { useState } from 'react'
import React from 'react'
import AxiosInstance from '@/services/AxiosInstance'
import { toast } from 'react-toastify';


const Created = ({data}) => {
      
  
    const[formData, setFormData] = useState(
      {
    
        "plano_id":"",      
        "quantia": "",        
        "meta":"",
    } )

    const handleChange = (e) => {
      const { name, value } = e.target;
      setFormData(prevState => ({
        ...prevState,
        [name]: value
      }));
    };
  
    const handleSubmit = async (e) => {
      e.preventDefault();
      formData["plano_id"] = data["id"]
      formData["meta"] = data["meta"]    

          
      await AxiosInstance.post(`/api/v1/personal/quantias/created/${data["id"]}/`, formData);

      data["quantia"] = parseFloat(data["quantia"]) + parseFloat(formData["quantia"]);

      await AxiosInstance.put(`/api/v1/personal/plan/${data["id"]}/`, data); 
      
      toast.success('Parabéns mais quantia....');
      window.location.reload();  
    };
    
  return (
    <div className='w-[21%] h-full  flex flex-col cursor-pointer bg-white space-y-2 border rounded-xl px-6 py-3 shadow-sm hover:shadow-lg'>
        <div className="font-semibold">Adicinar Quantia</div>
        <form className="flex flex-col rounded space-y-3" onSubmit={handleSubmit}>
            <div className="flex flex-col">
                <label htmlFor="" className="text-xs font-semibold">Quantia</label>
                <input type="number" name="quantia"  className="border px-2 rounded text-sm py-1" step="0.01" placeholder="0,00"
                value={formData.quantia}  
                onChange={handleChange}/>
            </div>
            <button className="bg-primary text-white rounded">adicionar</button>
        </form>      
    </div>
  )
}

export default Created
