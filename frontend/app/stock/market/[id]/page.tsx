"use client"


import OverviewWidget from '@/components/OverviewWidget';
import AnalysisWidget from '@/components/AnalysisWidget';
import { useParams  } from 'next/navigation'
import { FaReplyAll } from "react-icons/fa";
import FundamentalDataWidget from '@/components/FundamentalDataWidget';
import CompanyProfileWidget from '@/components/CompanyProfileWidget';
import TableOperationsStock from '@/components/TableOperationsStock';
const page = () => {


  const { id } = useParams();

 
  return (
    <main className="flex flex-col min-h-screen mx-16 gap-4">      {/* Sidebar */}   
      <div className="flex gap-4 -mt-[80px]  w-full z-40">
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
      <div className='mb-16'>
        <TableOperationsStock asset={id}/>
      </div>
      

  

      {/* Main Content */}
    
    </main>
  )
}

export default page