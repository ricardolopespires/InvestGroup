'use client'

import { exchangeAPId } from '@/lib/actions/actions.exchange'
import { truncateText } from '@/lib/utils'
import { useParams } from 'next/navigation'
import React, { useEffect, useState } from 'react'
import { FaReplyAll } from 'react-icons/fa'

const Page = () => {
    const { id } = useParams()
    const [exchange, setExchange] = useState(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState(null)

    useEffect(() => {
        const getUserData = async () => {
            setLoading(true)
            try {
                const res = await exchangeAPId({ ExchangeId: id })
                setExchange(res)
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

    if (loading) {
        return <div className="text-white">Carregando...</div>
    }

    if (error) {
        return <div className="text-red-500">{error}</div>
    }

    return (
        <div className='absolute inset-x-0 top-[140px] px-20 h-screen '>
            <div className='flex flex-col'>
                <div className="flex items-center space-x-4 mb-4">
                    <div className="text-3xl text-amber-500">
                        <img src={exchange?.image} alt={exchange?.name || 'Imagem do Exchange'} className="w-12 h-12 object-cover rounded-full" />
                    </div>
                    <h1 className='text-3xl text-white'>{exchange?.name}</h1>
                </div>
                <p className='text-gray-300 mt-2'>
                    {exchange?.description ? truncateText(exchange.description, 140) : "Descrição não disponível"}
                </p>
            </div>
            <a href="/settings" className="mt-10 flex items-center text-white text-4xl font-semibold hover:text-amber-400">
                <FaReplyAll />
            </a>
            <div className='w-full h-[79%] bg-white mt-9 shadow-lg rounded-lg p-6'>
                {/* Adicione conteúdo adicional aqui, se necessário */}
            </div>
        </div>
    )
}

export default Page
