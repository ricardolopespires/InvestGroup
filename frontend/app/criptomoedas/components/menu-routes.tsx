"use client"


import React from 'react'
import { BarChart, Compass, Layout, List } from "lucide-react";
import { usePathname } from "next/navigation";
import MenuItem from './menu-items';


const guestRoutes = [

    {
        icons: Compass,
        label:"Overview",
        href: "/criptomoedas"
    },
    {
        icons: Compass,
        label:"Lista de interesse",
        href: "/criptomoedas/interesse"
    },    
    {
        icons: Compass,
        label:"Portifolio",
        href: "/criptomoedas/portifolio"
    },       
    {
        icons: Compass,
        label:"Analytics",
        href: "/criptomoedas/analytics"
    },
]


  
const MenuRoutes = () => {

    const pathname = usePathname();  
    const routes = guestRoutes;  
     
  return (
    <div>
        <div className='mt-10 flex'>
        {routes.map((route) => (
            <MenuItem
            key={route.href}
            icons={route.icons}
            label={route.label}
            href={route.href}/>

        ))}        
    </div>
    </div>
  )
}

export default MenuRoutes
