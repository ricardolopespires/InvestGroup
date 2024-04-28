import { FaDoorOpen, FaUserTie } from "react-icons/fa";
import React, { useState, useEffect } from 'react';
import AxiosInstance from '@/services/AxiosInstance'


const Perfil = () => {
  const [perfil, setPerfil] = useState(null);
  const [username, setUsername] = useState([]);

  const user = JSON.parse(localStorage.getItem('user'));

  useEffect(() => {
    const getUserData = async () => {
      try {
        const res = await AxiosInstance.get(`/api/v1/auth/user/${user.email}`);        
        setUsername(res.data);
      } catch (error) {
        console.error('Erro ao obter dados do usuário:', error);
      }
    };

    getUserData();
  }, [user.email]);

  useEffect(() => {
    if (username && username.id) {
      const getUserProfile = async () => {
        try {
          const res = await AxiosInstance.get(`/api/v1/management/perfil/${username.id}`);        
          setPerfil(res.data);
        } catch (error) {
          console.error('Erro ao obter perfil:', error);
        }
      };

      getUserProfile();
    }
  }, [username]);

  return (
    <div className="flex space-x-2 items-center h-10">
      <FaUserTie className="text-2xl" />
      {perfil ? (<span className={`${perfil.color}`}>{perfil.investor}</span>) : (<span className="">Não tem perfil</span>)}
    </div>
  );
};

export default Perfil;
