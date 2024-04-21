

import {despesas} from "@/data/despesas"
import React, { useState } from 'react'

const Created
 = ({isVisible, onClose, children}) => {

    if (!isVisible) return null
  
    const handlerClose = (e) =>{
  
      if(e.target.id === "wrapper") onClose();
      
    }
  
    const [formData, setFormData] = useState({
      id:"",
      status: "",
      categoria: "",
      descricao: "",
      total: "",
    });
  
    const handleChange = (e) => {
      const { name, value } = e.target;
      setFormData({
        ...formData,
        [name]: value,
      });
    };
  
    const handleSubmit = async (e) => {
      e.preventDefault();
      console.log(formData);
      onClose(true);
    };
  
    return (
      
      <div id='wrapper' className='fixed inset-0 bg-black bg-opacity-25 backdrop-blur-sm flex justify-center items-center' onClick={(handlerClose)}>
        <div className='w-[600px]'>
          <div className='bg-white py-4 px-2 rounded'>
            <header className='flex items-center justify-between px-4'> 
              <p className="mb-3 text-xl font-semibold leading-5 text-slate-900">
                Nova Movimentação.
              </p>        
              <button className='text-lg' onClick={ () => onClose()}>X</button>
            </header>
            <p className="mt-7 flex items-center text-sm leading-4 bg-red-600 text-white rounded py-4 px-2 space-x-1">
            <span className="text-lg ">Nota. </span>
            <span>Você precisa digitar os dados da receita ou despesa....</span>
            </p>
          <div>      
            <form action=""   className='px-5 ' onSubmit={handleSubmit} >
              <div className='flex  space-x-2 py-7'>
                  <div className="flex flex-col w-full">
                    <label className="text-sm font-semibold" htmlFor="">TIpo</label>
                    <select name="status" id="id_status" className='border p-2 text-sm'
                    value={formData.status} onChange={handleChange}>
                    <option value="receitas" selected="">Selecione</option>
                      <option value="receitas" >Receitas</option>
                      <option value="despesas">Despesas</option>
                    </select>            
                  </div>
                  <div className="flex flex-col w-full">
                    <label className="text-sm font-semibold" htmlFor="">Despesas</label>
                    <select name="categoria" required="" id="id_categoria" className='border p-2 text-sm'
                    value={formData.categoria} onChange={handleChange}>
                      <option value="" selected="">Selecione</option>
                      {despesas.map((item, i)=>{
                        
                        return(<option key={i} value={item.id}>{item.nome}</option>)
                        
                        })}
                     
                    </select>
                  </div>
                  <div className="flex flex-col w-full">
                    <label className="text-sm font-semibold" htmlFor="">Valor</label>
                    <input type="text" name="total" className='border p-2 text-sm' placeholder='R$ 0,00'
                    value={formData.total} onChange={handleChange}v/>
                  </div>             
              </div>
              <div className="flex flex-col w-full">
                <label className="text-sm font-semibold" htmlFor="">Descrição</label>
                <textarea name="descricao" id="" className='border rounded h-20 p-2' value={formData.descricao} onChange={handleChange}></textarea>
              </div>
              <div className="mt-7 flex items-center justify-end">
                <button className="py-2 px-14 text-sm rounded bg-blue-700 hover:bg-blue-950 text-white" type="submit">Adicionar</button>
              </div>
            </form>           
            {children}
          </div>
          </div>
        </div>
      </div>
    )
  }
  

export default Created

