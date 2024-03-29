"use client"


import React from 'react'
import { BarChart, Compass, Layout, List } from "lucide-react";
import { cn } from '@/lib/utils'
import { usePathname } from "next/navigation";
import NavbarItem from './navbar-items';


const guestRoutes = [

    {
        icons: Compass,
        label:"Contato",
        href: "/contact"
    },
]


  
const NavbarRoutes = () => {

    const pathname = usePathname();  
    const routes = guestRoutes;

    
  
  return (
    <div className='flex w-full items-center'>
        {routes.map((route) => (
            <NavbarItem
            key={route.href}
            icons={route.icons}
            label={route.label}
            href={route.href}/>

        ))}        
    </div>
  )
}

export default NavbarRoutes
