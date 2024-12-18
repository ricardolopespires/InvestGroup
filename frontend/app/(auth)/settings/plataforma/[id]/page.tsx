'use client'


import {
    Card,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle,
  } from "@/components/ui/card"
  

import { getAccessPlataform, getPlatformDetails } from '@/lib/actions/actions.platraforms'
import { cn, truncateText } from '@/lib/utils'
import { useParams } from 'next/navigation'
import React, { useEffect, useState } from 'react'
import { FaReplyAll } from 'react-icons/fa'
import BalancePlatform from "@/components/BalancePlatform";
import { ScrollArea } from "@radix-ui/react-scroll-area";
import { AiOutlineAppstoreAdd } from "react-icons/ai";
import BalanceAreaVariant from "@/components/BalanceAreaVariant ";
import AcessPlatForm from "@/components/AcessPlatForm";
import CurrencyConverter from "@/components/CurrencyConverter";
import SwitchActive from "@/components/SwitchActive";
import CardOpenOrder from "@/components/CardOpenOrder";


const Page = () => {
    const { id } = useParams()
    const [platform, setPlatform] = useState({});
    const [balance, setBalance] = useState({});
    const [time, setTime] = useState(1);
    const [selected, setSelected] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [visible, setVisible] = useState(true);
    const [showModal, setShowModal] = useState(false);

    useEffect(() => {
        const getUserData = async () => {
            setLoading(true)
            try {
                const res = await getPlatformDetails({ PlatformId: id })               
                setPlatform(res)
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




    useEffect(() => {
      const getUserData = async () => {
          setLoading(true)
          try {
              const res = await getAccessPlataform({ PlatFormId: id })                       
              setBalance(res)
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



  useEffect(() => {    
    setSelected(balance[0])   
  },[balance])

    if (loading) {
        return <div className="text-white">Carregando...</div>
    }

    if (error) {
        return <div className="text-red-500">{error}</div>
    }

    const handleVisible = () => {
        setVisible(!visible)
        }


        

    return (
        <div className='absolute inset-x-0 top-[140px] px-20 h-screen '>
            <div className='flex flex-col'>
                <div className="flex items-center space-x-4 mb-4">
                    <div className="text-3xl text-amber-500">
                    <img src={`http://localhost:8000/media/${platform?.broker?.img}`} alt={platform?.broker?.name || 'Imagem do platform'} className="w-12 h-12 object-cover rounded-full" />
                    </div>
                    <h1 className='text-3xl text-white'>{platform?.broker?.name}</h1>
                </div>
                <p className='text-gray-300 mt-2'>
                    {platform?.broker?.description ? truncateText(platform?.broker?.description, 140) : "Descrição não disponível"}
                </p>
            </div>
            <div className='flex items-center justify-between w-full mt-10'>
            <a href="/settings" className=" flex items-center text-white text-4xl font-semibold hover:text-amber-400">
                <FaReplyAll />
            </a>
            <SwitchActive AccountId={selected}/>
            </div>
            <div className='flex flex-col items-center w-full  mt-0 gap-2'>
                <div className="w-full flex gap-2">
                    <div className="w-4/5 h-[600px] flex flex-col bg-white shadow-lg rounded-lg p-6">
                        <div className="grid grid-cols-4 h-28">
                            <BalancePlatform PlatFormId={balance} setVisible={setVisible}/>
                             <div></div>
                             <div></div>
                            <div className="flex flex-col items-center gap-6">
                                <div className="flex items-center w-full mt-4">
                                    <ul className="flex items-center gap-4 text-sm text-gray-400">
                                        <li className="flex flex-col gap-0" onClick={()=> setTime(1)}>
                                            <span className={`cursor-pointer ${time == 1 ? "text-[#000] font-semibold":""}`}>24h</span>
                                            <span className={`${time == 1 ? "bg-[#000] w-full h-0.5":""}`}/>
                                        </li>
                                        <li className="flex flex-col gap-0" onClick={()=> setTime(7)}>
                                            <span className={`cursor-pointer ${time == 7 ? "text-[#000] font-semibold":""}`}>7d</span>
                                            <span className={`${time == 7 ? "bg-[#000] w-full h-0.5":""}`}/>
                                        </li>
                                        <li className="flex flex-col gap-0" onClick={()=> setTime(30)}>
                                            <span className={`cursor-pointer ${time == 30 ? "text-[#000] font-semibold":""}`}>30d</span>
                                            <span className={`${time == 30 ? "bg-[#000] w-full h-0.5":""}`}/>
                                        </li>
                                        <li className="flex flex-col gap-0" onClick={()=> setTime(90)}>
                                            <span className={`cursor-pointer ${time == 90 ? "text-[#000] font-semibold":""}`}>90d</span>
                                            <span className={`${time == 90 ? "bg-[#000] w-full h-0.5":""}`}/>
                                        </li>
                                        <li className="flex flex-col gap-0" onClick={()=> setTime(365)}>
                                            <span className={`cursor-pointer ${time == 365 ? "text-[#000] font-semibold":""}`}>All</span>
                                            <span className={`${time == 365 ? "bg-[#000] w-full h-0.5":""}`}/>
                                        </li>
                                    </ul>
                                </div>
                               <CurrencyConverter balance={324662.16} currencyFrom={"USD"} currencyTo={"BRL"} visibility={visible}/>
                            
                            </div> 
                        </div>
                        <BalanceAreaVariant PlatformId={selected?.id}  />
                    </div>
                    <div className='w-1/5 flex flex-col items-center h-full'>
                  <Card className='w-full h-[600px] bg-white'>
                    <CardHeader>
                      <CardTitle>Contas de Negociação</CardTitle>
                      <CardDescription>
                        Lista de contas na corretora {platform?.broker?.name}
                      </CardDescription>
                    </CardHeader>
                    <CardContent className='flex flex-col justify-between w-full h-[85%]'>
                      <div className='h-[100%] w-full flex items-center justify-between '>
                        {balance?.length > 0 ? (
                          <ScrollArea className='h-full w-full'>
                            <div className='space-y-2'>
                              {balance.map((item) => (
                                <div
                                  key={item.id}
                                  onClick={() => setSelected(item)}
                                  className={cn(
                                    'border bg-white font-semibold flex items-center justify-between p-4 cursor-pointer rounded-md',
                                    {
                                      'border-2 border-blue-700 text-blue-700 shadow-sm':
                                        item.id === selected?.id,
                                    }
                                  )}>
                                  <div className='flex items-center justify-between w-full h-full'>
                                    <div className="flex flex-col gap-0">
                                      <span className='text-sm'>
                                        <span>Nº: </span>
                                        <span >{item.platform_id}</span>
                                      </span>
                                      <span className='text-xs flex gap-1'>
                                        <span>Server:</span> 
                                          <span className='text-xs'>{item.server }</span>
                                        </span>
                                    </div>                                 
                                  </div>
                                </div>
                              ))}
                            </div>
                          </ScrollArea>
                        ) : (
                          <div className='flex w-full items-center justify-center h-[100%]'>
                            <h1>Você ainda não tem Conta</h1>
                          </div>
                        )}
                      </div>
                      <div className='w-full flex justify-center items-center gap-4 mt-9'>
                        <button
                          onClick={() => setShowModal(true)}
                          className='w-full flex items-center justify-center gap-2 px-9 py-2 app-bg-gradient-blue font-semibold rounded-md'>
                          <AiOutlineAppstoreAdd />
                          <span>Nova Conta</span>
                        </button>
                      </div>
                    </CardContent>
                  </Card>
                </div>
                </div>
               <CardOpenOrder AccessId={undefined}/>
                <Card className='w-full h-[400px] bg-white'>
                    <CardHeader>
                      <CardTitle>Performace das Negociações</CardTitle>
                      <CardDescription>
                      A performance de negociações é a avaliação do desempenho de um trader nas suas negociações
                      </CardDescription>
                    </CardHeader>
                    <CardContent className='flex flex-col justify-between w-full h-[85%]'>
                      <div className='h-[100%] w-full flex items-center justify-between '>
                     
                      </div>                  
                    </CardContent>
                </Card>                
                <AcessPlatForm isVisible={showModal} onClose={() => setShowModal(false)} PlatFormId={id}/>   
            </div>
        </div>
    )
}

export default Page
