"use client"

import AxiosInstance from '@/services/AxiosInstance';
import { despesas } from "@/data/despesas";
import React, { useState, useContext, useEffect } from 'react';
import { UserContext } from "@/contexts/UserContext";
import { toast } from 'react-toastify';

const Created = ({ isVisible, onClose, children }) => {
  const user = useContext(UserContext);
  const user_id = user?.username?.id;

  if (!isVisible) return null;

  const [data, setData] = useState([]);
  const [formData, setFormData] = useState({
    user_id: user_id || "",
    status: "",
    categoria_id: "",
    descricao: "",
    total: ""
  });

  useEffect(() => {
    const getUserData = async () => {
      try {
        if (user_id === undefined) return;
        
        const res = await AxiosInstance.get(`/api/v1/personal/list/periodos/${user_id}`);
        setData(res.data);
      } catch (error) {
        console.error('Erro ao obter dados do usuário:', error);
      }
    };

    getUserData();
  }, [user_id]);

  const handlerClose = (e) => {
    if (e.target.id === "wrapper") onClose();
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevState => ({
      ...prevState,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!formData.status || !formData.categoria_id || !formData.total || !formData.descricao) {
      toast.error('Por favor, preencha todos os campos!');
      return;
    }

    if(parseFloat(data[0].revenues) === 0 && formData.status === "Despesas"){

      toast.error('Saldo insuficiente para a despesa');
      onClose(true);
        
    }else{
      await AxiosInstance.post(`api/v1/personal/created/despesas/`, formData);

      const newData = { ...data[0] };
      if (formData.status === "Despesas") {
        newData.expenses = (parseFloat(newData.expenses) + parseFloat(formData.total)).toFixed(2);
      } else {
        newData.revenues = (parseFloat(newData.revenues) + parseFloat(formData.total)).toFixed(2);
      }
  
      await AxiosInstance.put(`/api/v1/personal/periodos/${user_id}/`, newData);
  
      toast.success('Despesa Adicionada no Sistema!');
      onClose(true);
    }
      

   
  };

  return (
    <div id='wrapper' className='fixed inset-0 bg-black bg-opacity-25 backdrop-blur-sm flex justify-center items-center' onClick={handlerClose}>
      <div className='w-[670px]'>
        <div className='bg-white py-4 px-2 rounded'>
          <header className='flex items-center justify-between px-4'>
            <p className="mb-3 text-xl font-semibold leading-5 text-slate-900">
              Nova Movimentação.
            </p>
            <button className='text-lg' onClick={() => onClose()}>X</button>
          </header>
          <p className="mt-7 flex items-center text-sm leading-4 bg-red-600 text-white rounded py-4 px-2 space-x-1">
            <span className="text-lg">Nota. </span>
            <span>Você precisa digitar os dados da receita ou despesa....</span>
          </p>
          <div>
            <form action="" className='px-5' onSubmit={handleSubmit}>
              <div className='flex  space-x-2 py-7'>
                <div className="flex flex-col w-full">
                  <label className="text-sm font-semibold" htmlFor="">Tipo</label>
                  <select name="status" id="id_status" className='border p-2 text-sm' value={formData.status} onChange={handleChange}>
                    <option value="">Selecione</option>
                    <option value="Receitas">Receitas</option>
                    <option value="Despesas">Despesas</option>
                  </select>
                </div>
                <div className="flex flex-col w-full">
                  <label className="text-sm font-semibold" htmlFor="">Despesas</label>
                  <select name="categoria_id" required="" id="id_categoria" className='border p-2 text-sm' value={formData.categoria_id} onChange={handleChange}>
                    <option value="">Selecione</option>
                    {despesas.map((item, i) => (
                      <option key={i} value={item.id}>{item.nome}</option>
                    ))}
                  </select>
                </div>
                <div className="flex flex-col w-full">
                  <label className="text-sm font-semibold" htmlFor="">Valor</label>
                  <input type="text"
                    name="total"
                    className='border p-2 text-sm' placeholder='R$ 0,00' value={formData.total} onChange={handleChange} />
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
  );
};

export default Created;
