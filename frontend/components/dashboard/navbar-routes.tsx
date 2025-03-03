"use client"


import React from 'react'
import { BarChart, Compass, Layout, List } from "lucide-react";
import { cn } from '@/lib/utils'
import { usePathname } from "next/navigation";
import NavbarItem from './navbar-items';


const guestRoutes = [

    {
        icons: Compass,
        label:"Dashboard",
        href: "/dashboard/overview"
    },   
    {
        icons: Compass,
        label:"Pessoal",
        href: "/contabilidades/overview"
    },    
    {
        icons: Compass,
        label:"Criptos",
        href: "/colaboradores/overview"
    },
    {
        icons: Compass,
        label:"Ações",
        href: "/colaboradores/overview"
    },
    {
        icons: Compass,
        label:"Economina",
        href: "/unidades/overview"
    },
]


  
const NavbarRoutes = () => {

    const pathname = usePathname();  
    const routes = guestRoutes;   
  
  return (
    <div className='flex w-full items-center space-x-4 ml-9'>
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


export default NavbarRoutes;