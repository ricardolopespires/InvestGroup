
"use client"


import OverviewWidget from '@/components/OverviewWidget';
import AnalysisWidget from '@/components/AnalysisWidget';
import { useParams  } from 'next/navigation'
import { FaReplyAll } from "react-icons/fa";
import FundamentalDataWidget from '@/components/FundamentalDataWidget';
import CompanyProfileWidget from '@/components/CompanyProfileWidget';
import TableOperations from '@/components/TableOperations';
import { MdCurrencyExchange } from "react-icons/md";
import TrendFollowing from '@/components/TrendFollowing';
import CreatedOperations from '@/components/CreatedOperations';
import React, {useState } from 'react';



const page = () => {

  const [showModal, setShowModal] = useState(false);


  const { id } = useParams();
  const user = JSON.parse(localStorage.getItem('user'))

 
  return (
    <main className="flex flex-col max-w-screen-4xl mx-auto w-full pb-10 mt-24 text-white gap-4">      {/* Sidebar */}   
    <div className='flex items-center justify-between gap-4 mb-4'>
      <div></div>
      <button className='flex items-center gap-2 text-xs mb-2 bg-blue-950 text-white px-6 py-2 rounded hover:bg-blue-7 00'
      onClick={() => setShowModal(true)}>
        <MdCurrencyExchange className='text-lg'/>
        <span>Operações	</span>
      </button>
    </div>
      <div className="flex gap-4 w-full z-40">
        <div className="w-3/4 ">
          <OverviewWidget asset={id}/>
        </div>
        <div className="w-1/4">
          {/* Main Content */}
          <AnalysisWidget asset={id}/>
        </div>
      </div>
      <div className="w-full flex items-center justify-between gap-4">       
        <div className='w-[50%]'>
          <CompanyProfileWidget asset={id}/>
        </div>
        <div className='w-[50%]'>
          <FundamentalDataWidget asset={id}/>
        </div>
      </div>
      <div >
        <TableOperations symbol={id} Assest={"currencies"} UserId={user.email}/>
      </div>
      <div className='mb-16'>
        <TrendFollowing symbol={id} Assest={"currencies"} UserId={user.email}/>
      </div>
      

  

      {/* Main Content */}
      <CreatedOperations isVisible={showModal} onClose={()=>setShowModal(false)}/>
    </main>
  )
}

export default page