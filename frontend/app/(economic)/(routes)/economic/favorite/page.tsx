import Menu from '@/components/dashboard/Menu/menu'
import { FaStar } from "react-icons/fa";
import List from '../_components/List';

import React from 'react'

const page = ({children}) => {
  return (
    <div className='absolute inset-x-0 top-[140px] h-screen px-20 w-full'>
    <div className='flex flex-col '>
    <div className="flex items-center space-x-1">
    <div className="text-3xl text-yellow-500 mr-2"><FaStar /></div>
    <h1 className='text-2xl text-white'>Favoritos</h1>
    </div>
    <p className='text-gray-500 mt-2'>Acompanhe o desempenho da sua lista de interesses para analise de dados em tempo real, notícias recentes do mercado financeiro e estatísticas.</p>
    </div>
    <Menu/>
    <List/>
    {children}
    
    </div>
  )
}

export default page
