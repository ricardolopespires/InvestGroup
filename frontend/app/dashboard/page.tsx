import { ImEnter } from "react-icons/im";


import React from 'react'

const Page = ({children}) => {
  return (
    <div className='absolute inset-x-0 top-[140px] h-16 px-40'>
      <div className='flex flex-col '>
      <div className="flex items-center space-x-4">
      <div className="text-2xl text-yellow-500"><ImEnter /></div>
      <h1 className='text-2xl text-white'>Bem-vindo de volta, Ricardo!</h1>
      </div>
      <p className='text-gray-500'>Estamos aqui para ajudar a administrar seu dinheiro!</p>
      </div>
      {children}
    </div>
  )
}

export default Page