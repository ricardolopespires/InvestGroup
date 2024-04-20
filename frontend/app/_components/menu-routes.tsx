"use client"


import React from 'react'
import { BarChart, Compass, Layout, List } from "lucide-react";
import { usePathname } from "next/navigation";
import MenuItem from './menu-items';


const guestRoutes = [

    {
      
        label:"Overview",
        href: "/dashboard/overview"
    }
]


const personalRoutes = [
    
    {
        icons:"",
        label:"Overview",
        href: "/personal/overview"
    },
    {
        icons:"",
        label:"Transações",
        href: "/personal/transactions"
    },    
    {
        icons:"",
        label:"Contas bancárias",
        href: "/personal/bank-accounts"
    }, 
      {
        icons:"",
        label:"Planos",
        href: "/personal/plan"
    },      
    {
        icons:"",
        label:"Analytics",
        href: "/personal/analytics"
    },
    {
        icons:"",
        label:"Independência",
        href: "/personal/independence"
    },
  ]

  
const criptosRoutes = [
    
    {
        icons: Compass,
        label:"Overview",
        href: "/criptomoedas/overview"
    },
    {
        icons: Compass,
        label:"Mercado",
        href: "/criptomoedas/marketplace"
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

    const isPersonalPage = pathname?.includes("/personal");
    const isCriptosPage = pathname?.includes("/criptomoedas");

    const routes = isPersonalPage ? personalRoutes : isCriptosPage ? criptosRoutes : guestRoutes;

    
     
  return (
    <div>
        <div className='mt-10 flex items-center'>
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
