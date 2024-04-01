'use client'


import React from 'react'
import { LucideIcon } from 'lucide-react'
import { cn } from '@/lib/utils'
import { usePathname, useRouter } from 'next/navigation'


interface MenuItemPros{
    
    icons: LucideIcon;
    label: string;
    href: string;

}

const MenuItem = ({
    icons:Icon,
    label,
    href,

}: MenuItemPros) => {

    const pathname = usePathname();
    const router = useRouter();

    const isActive = (pathname === "/" &&  href === "/") ||
    pathname?.startsWith(`${href}`)

    const onClick = () =>{

        router.push(href)
    }


  return (
   <div className='flex flex-col items-center'>    
    <button
        onClick={onClick}
        type='button'
        className={cn(
            'text-sm text-gray-500 px-1 mr-4',
            isActive && " font-semibold rounded-full text-white space-x-2 py-1 ")}>  
            {label}                    
        </button> 
        <div className={cn('', isActive && "border w-[90%] top-5 relative")}/> 
   </div>     
   
  )
}

export default MenuItem