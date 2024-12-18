"use client"




import Perfil from "@/components/settings/Perfil";
import Settings from "@/components/settings/Settings";
import Situacao from "@/components/settings/Situacao";
import Notificacoes from "@/components/settings/Notifications";
import {  FaAddressCard, FaCamera, FaKey  } from "react-icons/fa";
import { MdOutlineAdminPanelSettings } from "react-icons/md";
import { useRouter } from 'next/navigation'
import { useEffect, useState } from 'react'
import Birthday from "@/components/settings/Birthday";
import ResetPassword from "@/components/settings/modals/ResetPassword";
import UploadImage from "@/components/settings/modals/UploadImage";
import Username from "@/components/settings/Username";


import React from 'react'
import Portifolios from "@/components/settings/Portifolios";
import Exchange from "@/components/settings/Exchange";
import MetaTrader from "@/components/settings/MetaTrader";
import Management from "@/components/settings/ManagementWallet";

const Page = ({children}) => {

  const [toggle, setToggle] = useState("perfil")
  const [showModal, setShowModal] = useState(false);
  const [showImage, setShowImage] = useState(false);

    const handlerToggle = (event) => {

    setToggle(event.target.value) 
    
  }

  const jwt=localStorage.getItem('token')
  const user = JSON.parse(localStorage.getItem('user'))
  const router = useRouter();
   useEffect(() => {
     if (jwt === null && !user) {
         router.push('/auth/Sign-In')
     }
     
   }, [jwt, user])
   

  return (
    <div className='absolute inset-x-0 top-[140px]  px-20  h-screen'>
      <div className='flex flex-col '>
        <div className="flex items-center space-x-1">
        <div className="text-3xl text-amber-500 mr-2"><MdOutlineAdminPanelSettings /></div>
        <h1 className='text-2xl text-white'>Informações geral do usuário!</h1>
        </div>
        <p className='text-gray-500 '>Tomar decisões financeiras começa com  a administração do seu próprio dinheiro.</p>
      </div>
      <div className="flex items-center justify-between space-x-4 absolute  top-[199px] inset-0 h-screen px-20">

      <div className="flex items-center justify-between space-x-4 w-full mx-auto h-screen mt-5">
        <div className="flex flex-col w-full  shadow-2xl bg-white rounded-2xl">
        <div className="relative h-[1700] flex flex-col w-full min-w-0 mb-6 break-words bg-clip-border rounded-2xl border-stone-200 bg-light/30 draggable">
         
          <div className="px-9 pt-9 flex-auto min-h-[70px] pb-0 bg-transparent">
            <div className="flex flex-wrap mb-6 xl:flex-nowrap">
              <div className="mb-5 mr-5">
                <div className="relative inline-block shrink-0 rounded-2xl">
                  <div onClick={() => setShowImage(true)}   className="absolute bg-gray-100 p-4 rounded-full  cursor-pointer">
                  <FaCamera />
                  </div>
                  <img className="inline-block shrink-0 rounded-2xl w-[80px] h-[80px] lg:w-[160px] lg:h-[160px]" src="https://static-00.iconduck.com/assets.00/avatar-default-symbolic-icon-2048x1949-pq9uiebg.png" alt="image" />
                  <div className="group/tooltip relative">
                    <span className="w-[15px] h-[15px] absolute bg-success rounded-full bottom-0 end-0 -mb-1 -mr-2  border border-white"></span>
                    <span className="text-xs absolute z-10 transition-opacity duration-300 ease-in-out px-3 py-2 whitespace-nowrap text-center transform bg-white rounded-2xl shadow-sm bottom-0 -mb-2 start-full ml-4 font-medium text-secondary-inverse group-hover/tooltip:opacity-100 opacity-0 block"> Status: Ativo </span>
                  </div>
                </div>
              </div>
              <div className="grow">
                <div className="flex flex-wrap items-start justify-between mb-2">
                <Username/>
                  <div onClick={() => setShowModal(true)}  className="flex items-center gap-2 inline-block px-6 py-3 text-base font-medium leading-normal text-center text-white align-middle transition-colors duration-150 ease-in-out border-0 shadow-none cursor-pointer rounded-md bg-gray-400 hover:bg-primary active:bg-page-primary focus:bg-gray-200 ">
                  <FaKey className="text-lg"/>
                    <a href="javascript:void(0)"  className="">Alterar Senha</a>
                  </div>
                </div>
                <Birthday/>
              </div>
            </div>
            <hr className="w-full h-px border-neutral-200"/>
            <ul nav-tabs className={`z-10 group flex absolute flex-wrap items-stretch text-[1.15rem] font-semibold list-none border-b-2 border-transparent border-solid active-${toggle}`}>          
              <li className="flex mt-2 -mb-[2px]" >
                <button aria-controls="perfil" className="py-5 mr-1 sm:mr-3 lg:mr-10 transition-colors duration-200 ease-in-out border-b-2 border-transparent group-[.active-perfil]:border-primary group-[.active-perfil]:text-primary text-gray-300 hover:border-primary hover:border-primary" href="javascript:void(0)" onClick={handlerToggle} value="perfil"  >Perfil do Investidor</button>
              </li>
              <li className="flex mt-2 -mb-[2px]" >
                <button aria-controls="situation" className="py-5 mr-1 sm:mr-3 lg:mr-10 transition-colors duration-200 ease-in-out border-b-2 border-transparent group-[.active-situation]:border-primary group-[.active-situation]:text-primary text-gray-300 hover:border-primary" href="javascript:void(0)" onClick={handlerToggle} value="situation">Situação financeira </button>
              </li>
              <li className="flex mt-2 -mb-[2px]">
                <button aria-controls="settings" className="py-5 mr-1 sm:mr-3 lg:mr-10 transition-colors duration-200 ease-in-out border-b-2 border-transparent group-[.active-settings]:border-primary group-[.active-settings]:text-primary text-gray-300 hover:border-primary" href="javascript:void(0)" onClick={handlerToggle} value="settings">Settings</button>
              </li>
              <li className="flex mt-2 -mb-[2px] group" >
                <button aria-controls="notifications" className="py-5 mr-1 sm:mr-3 lg:mr-10 transition-colors duration-200 ease-in-out border-b-2 border-transparent group-[.active-notifications]:border-primary group-[.active-notifications]:text-primary text-gray-300 hover:border-primary " href="javascript:void(0)" onClick={handlerToggle} value="notifications"> Notificações</button>
              </li>
              <li className="flex mt-2 -mb-[2px] group" >
                <button aria-controls="portifolios" className="py-5 mr-1 sm:mr-3 lg:mr-10 transition-colors duration-200 ease-in-out border-b-2 border-transparent group-[.active-portifolios]:border-primary group-[.active-portifolios]:text-primary text-gray-300 hover:border-primary " href="javascript:void(0)" onClick={handlerToggle} value="portifolios"> Portifólios</button>
              </li>
              <li className="flex mt-2 -mb-[2px] group" >
                <button aria-controls="exchange" className="py-5 mr-1 sm:mr-3 lg:mr-10 transition-colors duration-200 ease-in-out border-b-2 border-transparent group-[.active-exchange]:border-primary group-[.active-exchange]:text-primary text-gray-300 hover:border-primary " href="javascript:void(0)" onClick={handlerToggle} value="exchange">Exchange/API</button>
              </li>
              <li className="flex mt-2 -mb-[2px] group" >
                <button aria-controls="metatrader" className="py-5 mr-1 sm:mr-3 lg:mr-10 transition-colors duration-200 ease-in-out border-b-2 border-transparent group-[.active-metatrader]:border-primary group-[.active-metatrader]:text-primary text-gray-300 hover:border-primary " href="javascript:void(0)" onClick={handlerToggle} value="metatrader">MetaTrader</button>
              </li>
              <li className="flex mt-2 -mb-[2px] group" >
                <button aria-controls="management" className="py-5 mr-1 sm:mr-3 lg:mr-10 transition-colors duration-200 ease-in-out border-b-2 border-transparent group-[.active-management]:border-primary group-[.active-management]:text-primary text-gray-300 hover:border-primary " href="javascript:void(0)" onClick={handlerToggle} value="management">Gerenciamentos</button>
              </li>

            </ul>
          </div> 
            <div className="h-screen w-full">              
              <div className={ toggle === "perfil" ? "visible h-screen":'invisible'} >
                <Perfil/>
              </div>
              <div className={ toggle === "situation" ? "visible h-screen  ":'invisible'} >
                <Situacao  />
              </div>
              <div className={ toggle === "settings" ? "visible h-screen":'invisible'}> 
                <Settings />
              </div>
              <div className={ toggle === "notifications" ? "visible h-screen":'invisible'}  >
              <Notificacoes/>
              </div>
              <div className={ toggle === "portifolios" ? "visible h-screen":'invisible'}  >
                <Portifolios/>
              </div> 
              <div className={ toggle === "exchange" ? "visible h-screen":'invisible'}  >
                <Exchange/>
              </div> 
              <div className={ toggle === "metatrader" ? "visible h-screen":'invisible'}  >
                <MetaTrader/>
              </div> 
              <div className={ toggle === "management" ? "visible h-screen":'invisible'}  >
                <Management/>
              </div>  
            </div>        
        </div>
        </div>       
      </div>
      <div>   
      </div>
      
      </div>


      {children}
      <ResetPassword isVisible={showModal}  onClose={() => setShowModal(false)}/>
      <UploadImage isVisible={showImage}  onClose={() => setShowImage(false)}/>
     
    </div>
  )
}

export default Page