"use client"

import React, { createContext, useState, useEffect } from 'react';
import AxiosInstance from '@/services/AxiosInstance';

const user = JSON.parse(localStorage.getItem('user'))

export const UserContext = createContext();

const UserProvider = ({ children }) => {

  const [username, setUsername] = useState([]);
  
  useEffect(() => {
    const getUserData = async () => {
      try {
        const res = await AxiosInstance.get(`http://localhost:8000/api/v1/auth/list/${user.email}/`);       
        return res.data[0];
      } catch (error) {
        console.error('Erro ao obter dados:', error);
        return [];
      }
    };

    getUserData()
      .then(Data => {
        setUsername(Data);
      })
      .catch(error => {
        console.error('Erro ao obter condomínios:', error);
      });
  }, []);
  



  return (
    <UserContext.Provider value={{ username}}>
      {children}
    </UserContext.Provider>
  );
};

export default UserProvider;