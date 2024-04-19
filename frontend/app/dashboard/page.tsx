"use client"

import { AiOutlineRise } from "react-icons/ai";
import { FaDoorOpen } from "react-icons/fa";
import AxiosInstance from '@/services/AxiosInstance'
import { useEffect, useState } from 'react'
import { useRouter } from 'next/navigation'
import Balance from "./_componentes/Balance"
import Perfil from "./_componentes/perfil";
import React from 'react'

const Page = ({children}) => {

  const [quiz, setQuiz] = useState([]);

  const jwt=localStorage.getItem('token')
  const user = JSON.parse(localStorage.getItem('user'))
  const router = useRouter();

  useEffect(() => {
    const getUserData = async () => {
      try {
        const res = await AxiosInstance.get(`http://localhost:8000/api/v1/auth/user/${user.email}`);
                 
        return res.data;
      } catch (error) {
        console.error('Erro ao obter dados:', error);
        return [];
      }
    };

    getUserData()
      .then(Data => {
        setQuiz(Data);
      })
      .catch(error => {
        console.error('Erro ao obter condomínios:', error);
      });
  }, []);


  useEffect(() => {
     if (jwt === null && !user) {

         router.push('/auth/Sign-In')

     }else{
      if (quiz.perfil === false){

        router.push('/quiz/perfil')

      }else if (quiz.situation === false){

        router.push('/quiz/situation')
      }
     }
     
   }, [jwt, user])


  
  

  return (
    <div className='absolute inset-x-0 top-[140px] h-16 px-20'>
      <div className='flex flex-col '>
      <div className="flex items-center space-x-4">
      <div className="text-2xl text-yellow-500"><FaDoorOpen/></div>
      <h1 className='text-2xl text-white'>Bem-vindo de volta, {user && user.full_name}!</h1>
      </div>
      <p className='text-gray-500'>Estamos aqui para ajudar a administrar seu dinheiro!</p>
      </div>
      <div className='absolute inset-x-0 top-[90px] h-full px-20'>
        <div className='flex flex-col '>
          <div className="flex items-center justify-between w-full h-10 text-white">
            <div className="flex flex-col ">
              <Balance/>
              <div className="flex items-center space-x-10 top-5">
                <span>11 April 2022</span>
                <div className="flex items-center space-x-2">
                <AiOutlineRise className="text-2xl text-green-500"/>
                <span>2,05%</span>
                </div>
                </div>
            </div>
            <Perfil/>
          </div>
            <div className="flex space-x-4 relative top-[60px]" >
              <div className="w-[70%] h-[400px] bg-white rounded-xl shadow-xl">

              </div>
              <div className="w-[30%] h-[400px] bg-white rounded-xl shadow-xl">

              </div>
            </div>
          

          </div>
        </div>
      {children}
    </div>
  )
}

export default Page