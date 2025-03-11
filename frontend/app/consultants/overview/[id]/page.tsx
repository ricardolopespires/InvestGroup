"use client"


import { useParams  } from 'next/navigation'
import Image from 'next/image';
import { CircularProgress } from '@/components/circular-progress';
import { SkillBar } from '@/components/skill-bar';
import { Check } from 'lucide-react';
import { ServiceCard } from '@/components/service-card';
import { FaReplyAll } from "react-icons/fa";
const page = () => {


  const { id } = useParams();

 
  return (
    <main className="flex flex-col min-h-screen mx-16 ">      {/* Sidebar */}
    <a href="/consultants/overview/">
        <div className='w-full h-9 items-center text-4xl -mt-16 absolute text-white'>
            <FaReplyAll/>
        </div>
    </a>

  

      {/* Main Content */}
    
    </main>
  )
}

export default page