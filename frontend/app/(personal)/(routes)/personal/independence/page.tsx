import { FaWallet,  FaChild,FaCreditCard, FaDollarSign, FaBarcode, FaUsers , FaHandHoldingUsd,FaRegCreditCard, FaCashRegister, FaCar, FaPlaystation     } from "react-icons/fa";
import { AiFillAlert } from "react-icons/ai";
import { GoArrowUp } from "react-icons/go";
import Menu from "@/app/_components/menu";


import React from 'react'

const page = () => {
  return (
    <div className='absolute inset-x-0 top-[140px] h-full px-20'>
    <div className='flex flex-col '>
    <div className="flex items-center space-x-1">
    <div className="text-3xl text-yellow-500 mr-2"><FaWallet /></div>
    <h1 className='text-2xl text-white'>Finanças pessoais</h1>
    </div>
    <p className='text-gray-500 '>Tomar decisões financeiras começa com  a administração do seu próprio dinheiro.</p>
    </div>
    <Menu/>
      <div className="relative top-10">
        <div className="grid grid-cols-4 gap-4 ">      
          <div className="bg-white rounded-2xl shadow-xl">
            <div className="card-statistic-3 p-4">
            <div className=" text-[110px] opacity-[0.1] w-full z-40 ml-[280px] absolute top-1 text-red-500"><AiFillAlert /></div>
              <div className="mb-4">
                        <h5 className="card-title mb-0">Valor de Emergência</h5>
              </div>
              <div className="row align-items-center mb-2 d-flex">
                        <div className="col-8">
                            <h2 className="d-flex align-items-center mb-0">
                                3,243
                            </h2>
                        </div>
                        <div className="flex items-center justify-end">
                            <span>12.5%</span>
                            <GoArrowUp  className="font-semibold text-green-500"/>
                        </div>
              </div>
              <div className="progress mt-1 h-[8px]" data-height="8" >
                  <div className="progress-bar l-bg-cyan" role="progressbar" data-width="25%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
              </div>
            </div>
          </div>
          <div className="bg-white rounded-2xl shadow-xl">
                <div className="card-statistic-3 p-4">
                <div className=" text-[110px] opacity-[0.1] w-full z-40 ml-[280px] absolute top-1"><FaUsers className="" /></div>
                    <div className="mb-4">
                        <h5 className="card-title mb-0">Customers</h5>
                    </div>
                    <div className="row align-items-center mb-2 d-flex">
                        <div className="col-8">
                            <h2 className="d-flex align-items-center mb-0">
                                15.07k
                            </h2>
                        </div>
                        <div className="flex items-center justify-end">
                            <span>9.23% </span>
                            <GoArrowUp  className="font-semibold text-green-500"/>
                        </div>
                    </div>
                    <div className="progress mt-1 h-[8px] " data-height="8" >
                        <div className="progress-bar l-bg-green" role="progressbar" data-width="25%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100" s></div>
                    </div>
                </div>
          </div>
          <div className="bg-white rounded-2xl shadow-xl w-full ">
                <div className="card-statistic-3 p-4 w-full relative z-0">                   
                    <div className="mb-4">
                        <h5 className="card-title mb-0">Ticket Resolved</h5>
                    </div>
                    <div className="row align-items-center mb-2 d-flex">
                        <div className="col-8">
                            <h2 className="d-flex align-items-center mb-0">
                                578
                            </h2>
                        </div>
                        <div className="flex items-center justify-end">
                            <span>10% </span>
                            <GoArrowUp  className="font-semibold text-green-500"/>
                        </div>
                    </div>
                    <div className="progress mt-1 h-[8px]" data-height="8">
                        <div className="progress-bar l-bg-orange" role="progressbar" data-width="25%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100" ></div>
                    </div>
                </div>
                <div className=" text-[110px] opacity-[0.1] w-full z-40 ml-[280px] absolute top-1"><FaUsers className="" /></div>
          </div>
          <div className="bg-white rounded-2xl shadow-xl">
                <div className="card-statistic-3 p-4">
                    <div className="absolute text-[110px] opacity-[0.1] z-40 ml-[280px] absolute top-1 text-green-500"><i><FaDollarSign /></i></div>
                    <div className="mb-4">
                        <h5 className="card-title mb-0">Revenue Today</h5>
                    </div>
                    <div className="row align-items-center mb-2 d-flex">
                        <div className="col-8">
                            <h2 className="d-flex align-items-center mb-0">
                                $11.61k
                            </h2>
                        </div>
                        <div className="flex items-center justify-end">
                            <span>2.5% </span>
                            <GoArrowUp  className="font-semibold text-green-500"/>
                        </div>
                    </div>
                    <div className="progress mt-1 h-[8px] z-1" data-height="8" >
                        <div className="progress-bar l-bg-cyan " role="progressbar" data-width="25%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
                    </div>
                </div>
            </div>
        </div>
      </div>
    </div>
  )
}

export default page
