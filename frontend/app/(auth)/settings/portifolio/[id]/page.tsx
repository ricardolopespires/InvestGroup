"use client"



import { ExchangeByBalance } from '@/lib/actions/actions.exchange'
import { useParams } from 'next/navigation'
import React, { useEffect, useState } from 'react'
import { FaReplyAll } from 'react-icons/fa'
import { LuCodesandbox } from 'react-icons/lu'


const Page = () => {

    const id = useParams().id
    const [portifolio, setPortifolio] = useState([])
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState(null)


    
    useEffect(() => {
      const getUserData = async () => {
          setLoading(true)
          try {
              const res = await ExchangeByBalance({AccountId: id })              
              setPortifolio(res)
          } catch (error) {
              setError('Erro ao obter dados do usuário')
              console.error('Erro ao obter dados do usuário:', error)
          } finally {
              setLoading(false)
          }
      }

      if (id) {
          getUserData()
      }
  }, [id])



  return (
        <div className='absolute inset-x-0 top-[140px]  px-20  h-screen'>
            <div className='flex flex-col '>
            <div className="flex items-center space-x-1">
            <div className="text-3xl text-amber-500 mr-2"><LuCodesandbox/></div>
            <h1 className='text-2xl text-white'>{portifolio?.name}</h1>
            </div>
            <p className='text-gray-500 mt-2'>O gerenciamento de portfólio inclui a avaliação de risco e a alocação de ativos com o <span className='text-amber-400'>objetivo de atingir metas</span> financeiras específicas.</p>
            </div>
            <a href="/settings" className="mt-10 flex items-center text-white mr-5 hover:text-amber-400 text-4xl font-semibold ">     
            <FaReplyAll />     
            </a>
        <div className='w-full h-[79%] bg-white mt-9 shadow rounded-lg p-6'>

        </div>
      
    </div>
  )
}

export default Page
