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
    <div className='flex flex-col items-center px-4'>
        <button
        onClick={onClick}
        type='button'
        className={cn(
            'text-sm hover:text-orange-500',
            isActive && "text-orange-500 font-semibold")}>
            <div className='py-8 '>
            {label}
            </div>               
        </button>
        <div
            className={cn('ml-auto opacity-0 border-2 border-orange-500 w-full',
            isActive  && "opacity-100")}/>
    </div>
  )
}

export default NavbarItem