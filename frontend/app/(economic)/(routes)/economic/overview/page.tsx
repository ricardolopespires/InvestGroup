import Menu from '@/components/dashboard/Menu/menu'
import { FaGlobeAmericas } from "react-icons/fa";
import List from '../_components/List';

import React from 'react'

const page = ({children}) => {
  return (
    <div className='absolute inset-x-0 top-[140px] h-screen px-20 w-full'>
    <div className='flex flex-col '>
    <div className="flex items-center space-x-1">
    <div className="text-3xl text-yellow-500 mr-2"><FaGlobeAmericas /></div>
    <h1 className='text-2xl text-white'>Economia</h1>
    </div>
    <p className='text-gray-500 mt-2'>Economia é o conjunto de atividades de produção, distribuição e o consumo de bens e serviços necessários à sobrevivência.</p>
    </div>
    <Menu/>
    <List/>
    {children}
    
    </div>
  )
}

export default page
