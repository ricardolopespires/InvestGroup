"use client"


import React from 'react'
import { BarChart, Compass, Layout, List } from "lucide-react";
import { usePathname } from "next/navigation";
import MenuItem from './menu-items';


const guestRoutes = [

    {
        icons: Compass,
        label:"Overview",
        href: "/personal"
    },
    {
        icons: Compass,
        label:"Transactions",
        href: "/personal/transactions"
    },    
    {
        icons: Compass,
        label:"Bank Accounts",
        href: "/personal/bank-accounts"
    },       
    {
        icons: Compass,
        label:"Analytics",
        href: "/personal/analytics"
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
