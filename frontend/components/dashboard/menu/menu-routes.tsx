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


const unidadesRoutes = [
    
    {
        icons:"",
        label:"Overview",
        href: "/unidades/overview"
    },
    {
        icons:"",
        label:"Boletos",
        href: "/unidades/boletos"
    },    
    {
        icons:"",
        label:"Garagem",
        href: "/unidades/veiculos"
    }, 
      {
        icons:"",
        label:"Animais",
        href: "/unidades/animais"
    },      
    {
        icons:"",
        label:"Analytics",
        href: "/unidades/analytics"
    },
  ]


  const contabilidadesRoutes = [

    {
        icons: Compass,
        label:"Overview",
        href: "/contabilidades/overview"
    },
    {
        icons: Compass,
        label:"Receitas",
        href: "/contabilidades/receitas"
    },
    {
        icons: Compass,
        label:"Despesas",
        href: "/contabilidades/despesas"
    },
    {
        icons: Compass,
        label:"Previsão Orçamentária",
        href: "/contabilidades/previsao"
    },
    {
        icons: Compass,
        label:"Analytics",
        href: "/contabilidades/analytics"
    },
    

  ]

  const colaboradoresRoutes = [


    {
        icons: Compass,
        label:"Overview",
        href: "/colaboradores/overview"
    },
    {
        icons: Compass,
        label:"folha de ponto",
        href: "/colaboradores/receitas"
    },
    {
        icons: Compass,
        label:"Férias",
        href: "/colaboradores/despesas"
    },


  ] //

  const administracaoRoutes = [


    {
        icons: Compass,
        label:"Overview",
        href: "/administracao/overview"
    },
    {
        icons: Compass,
        label:"Taxa Ordinária",
        href: "/administracao/ordinaria"
    },
    {
        icons: Compass,
        label:"Taxa Extra",
        href: "/administracao/extra"
    },
    
    


  ] //
  
  

  
const MenuRoutes = () => {

    const pathname = usePathname();

    const isUnidadesPage = pathname?.includes("/unidades");   
    const isContabilidadesPage = pathname?.includes("/contabilidades");
    const isColaboradoresPage = pathname?.includes("/colaboradores");
    const isAdministracaoPage = pathname?.includes("/administracao");

    const routes = isUnidadesPage ? unidadesRoutes : isContabilidadesPage ? contabilidadesRoutes : isColaboradoresPage ? colaboradoresRoutes: isAdministracaoPage ? administracaoRoutes : guestRoutes ;

    
     
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
