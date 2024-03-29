'use client'


import React from 'react'
import { LucideIcon } from 'lucide-react'
import { cn } from '@/lib/utils'
import { usePathname, useRouter } from 'next/navigation'


interface NavbarItemPros{
    
    icons: LucideIcon;
    label: string;
    href: string;

}

const NavbarItem = ({
    icons:Icon,
    label,
    href,

}: NavbarItemPros) => {

    const pathname = usePathname();
    const router = useRouter();

    const isActive = (pathname === "/" &&  href === "/") ||
    pathname?.startsWith(`${href}`)

    const onClick = () =>{

        router.push(href)
    }


  return (
   
        <button
        onClick={onClick}
        type='button'
        className={cn(
            'text-sm ',
            isActive && " font-semibold  rounded-full text-white px-6 py-1  bg-gradient-to-r from-[#0B2353] to-[#0B4278]")}>  
            {label}                    
        </button>       
   
  )
}

export default NavbarItem