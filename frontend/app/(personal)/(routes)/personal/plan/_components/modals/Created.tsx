"use client"

import AxiosInstance from '@/services/AxiosInstance';
import { despesas } from "@/data/despesas";
import React, { useState, useContext, useEffect } from 'react';
import { UserContext } from "@/contexts/UserContext";
import { toast } from 'react-toastify';
import EmojiPicker from 'emoji-picker-react';
const Created = ({ isVisible, onClose, children }) => {
  const user = useContext(UserContext);
  const user_id = user?.username?.id;

  if (!isVisible) return null;

  const [data, setData] = useState([]);
  const[emojiIcon, setEmojiIcon] = useState('😀');
  const [emoji, setEmoji] = useState(false);
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
   
  };

  return (
    <div id='wrapper' className='fixed inset-0 bg-black bg-opacity-25 backdrop-blur-sm flex justify-center items-center' onClick={handlerClose}>
      <div className='w-[470px]'>
        <div className='bg-white py-4 px-2 rounded'>
          <header className='flex items-center justify-between px-4'>
            <p className="mb-3 text-xl font-semibold leading-5 text-slate-900">
              Novo Plano.
            </p>
            <button className='text-lg' onClick={() => onClose()}>X</button>
          </header>
          <p className="mt-7 flex items-center text-sm leading-4 bg-red-600 text-white rounded py-4 px-2 space-x-1">
            <span className="text-lg">Nota. </span>
            <span>Você precisa digitar os dados do novo plano....</span>
          </p>
          <div>
            <form action="" className='px-5  flex flex-col full space-y-10' onSubmit={handleSubmit}>
              <div className='absolute py-5'>
                <button className='border p-2 rounded' onClick={()=> setEmoji(!emoji)}>{emojiIcon}</button>
                <div>
                 <EmojiPicker open={emoji}
                 onEmojiClick={(e) =>{
                  setEmojiIcon(e.emoji)
                  setEmoji(false)
                  }}/>
                </div>
              </div>
              <div className='flex  top-[28px] relative items-center justify-between text-sm w-full space-x-2'>
                  <div className='flex flex-col w-full'>
                  <label htmlFor="">Nome</label>
                  <input type="text" name='name' className='border p-2 w-full' />
                  </div>
                  <div className='flex flex-col w-full'>
                  <label htmlFor="">Valor</label>
                  <input type="text" name='valor' className='border p-2 w-full' />
                  </div>
              </div>
              <div className="mt-7 flex items-center">
                <button  className="py-2 px-14 text-sm rounded bg-blue-700 hover:bg-blue-950 text-white" type="submit">Adicionar</button>
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
