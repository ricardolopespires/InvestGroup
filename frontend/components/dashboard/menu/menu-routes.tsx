"use client";

import React from "react";
import { 
  Compass, 
  FileText, 
  Car, 
  PawPrint, 
  BarChart, 
  DollarSign, 
  TrendingDown, 
  TrendingUp, 
  Clock, 
  Users 
} from "lucide-react";
import { usePathname } from "next/navigation";
import MenuItem from "./menu-items";
import { FaDesktop, FaUserTie, FaChartPie, FaBuromobelexperte  } from "react-icons/fa";
import { IoWalletOutline } from "react-icons/io5";
import { SiMarketo } from "react-icons/si";
import { CiCalculator2 } from "react-icons/ci";
import { LuBellRing } from "react-icons/lu";
import { MdOutlineAdminPanelSettings } from "react-icons/md";
import { LuChartPie } from "react-icons/lu";
import { MdDisplaySettings } from "react-icons/md";
import { GiSettingsKnobs } from "react-icons/gi";
import { FaSitemap } from "react-icons/fa";
import { RiRobot3Fill } from "react-icons/ri";
import { BsRobot } from "react-icons/bs";

// Definição das rotas
const guestRoutes = [
  {
    icon: <FaDesktop />,
    label: "Overview",
    href: "/dashboard/overview",
    title: "Visão Geral",
    subtitle: "Resumo principal do dashboard",
  },
];

const personalRoutes = [
  {
    icon: <CiCalculator2 />,
    label: "Overview",
    href: "/unidades/overview",
    title: "Visão Geral das Unidades",
    subtitle: "Resumo das informações das unidades",
  },
  {
    icon: FileText,
    label: "Boletos",
    href: "/unidades/boletos",
    title: "Gestão de Boletos",
    subtitle: "Controle de pagamentos e vencimentos",
  },
  {
    icon: Car,
    label: "Garagem",
    href: "/unidades/veiculos",
    title: "Controle de Garagem",
    subtitle: "Gestão de veículos e vagas",
  },
  {
    icon: PawPrint,
    label: "Animais",
    href: "/unidades/animais",
    title: "Registro de Animais",
    subtitle: "Controle de pets nas unidades",
  },
  {
    icon: BarChart,
    label: "Analytics",
    href: "/unidades/analytics",
    title: "Análises das Unidades",
    subtitle: "Estatísticas e métricas detalhadas",
  },
];

const cryptosRoutes = [
  {
    icon: <FaUserTie />,
    label: "Overview",
    href: "/consultants/overview",
    title: "Consultores Financeiro",
    subtitle: "Escolha seu profissional que ajuda a gerir as finanças",
  },
];

const stockRoutes = [
    {
      icon: <FaChartPie />,
      label: "Overview",
      href: "/stock/overview",
      title: "Overview",
      subtitle: "Resumo e Tendências do Mercado",
    },
    {
      icon: <SiMarketo />,
      label: "Mercado",
      href: "/stock/market",
      title: "Mercado de Ações",
      subtitle: "Acompanhe as cotações e desempenho das ações em tempo real",
    },
    {
      icon: <IoWalletOutline />,
      label: "Portfólio",
      href: "/stock/portfolio",
      title: "Portfólio",
      subtitle: "Acompanhamento do seu Portfólio",
    },   
  
];

const economicRoutes = [
  {
    icon: Compass,
    label: "Overview",
    href: "/administracao/overview",
    title: "Visão Geral da Administração",
    subtitle: "Resumo administrativo",
  },
  {
    icon: DollarSign,
    label: "Taxa Ordinária",
    href: "/administracao/ordinaria",
    title: "Taxas Ordinárias",
    subtitle: "Gestão de taxas regulares",
  },
  {
    icon: FileText,
    label: "Taxa Extra",
    href: "/administracao/extra",
    title: "Taxas Extras",
    subtitle: "Controle de cobranças adicionais",
  },
];

const consultantRoutes = [
  {
    icon: <FaUserTie />,
    label: "Overview",
    href: "/consultants/overview",
    title: "Consultores Financeiro",
    subtitle: "Escolha seu profissional que ajuda a gerir as finanças",
  },
];

const investmentsRoutes = [
  {
    icon: <LuChartPie />,
    label: "Overview",
    href: "/investments/overview",
    title: "Inestimentos",
    subtitle: "Descubra onde investir o seu dinheiro, com boa rentabilidade e muita segurança.",
  },
];


const settingsRoutes = [
  {
    icon: <MdDisplaySettings />,
    label: "Settings",
    href: "/settings/overview",
    title: "Configurações ",
    subtitle: "Gerencie suas configurações de privacidade e dados",
  },
  {
    icon: <MdOutlineAdminPanelSettings />,
    label: "Segurança",
    href: "/settings/security",
    title: "Segurança ",
    subtitle: "Gerencie as configurações de segurança da sua conta",
  },
  {
    icon: <GiSettingsKnobs />,
    label: "Preferências",
    href: "/settings/preferences",
    title: "Preferências",
    subtitle: "Gerencie suas configurações de privacidade e dados",
  },
  {
    icon: <LuBellRing />,
    label: "Notificações",
    href: "/settings/notifications",
    title: "Notificações",
    subtitle: "Gerencie como você recebe notificações",
  },
  
  {
    icon: <FaSitemap />,
    label: "API",
    href: "/settings/api",
    title: "APIs ",
    subtitle: "Gerencie suas configurações das suas APIs",
  },
  {
    icon: <BsRobot />,
    label: "Agentes",
    href: "/settings/agents",
    title: "Agentes",
    subtitle: "Gerencie suas configurações das suas APIs",
  },
  {
    icon: <FaBuromobelexperte />,
    label: "Gerenciamento",
    href: "/settings/management",
    title: "Gerenciamentos ",
    subtitle: "Gerencie suas configurações das suas APIs",
  },
]

const MenuRoutes = () => {
  const pathname = usePathname();

  // Determina qual grupo de rotas usar com base no pathname
  const isPersonalPage = pathname?.includes("/unidades");
  const isCryptoPage = pathname?.includes("/consultants");
  const isStockPage = pathname?.includes("/stock");
  const isEconomicPage = pathname?.includes("/administracao");
  const isConsultantPage = pathname?.includes("/consultants");
  const isInvestmentsPage = pathname?.includes("/investments");
  const isSettingsPage = pathname?.includes("/settings");


  // Seleciona as rotas com base na página atual
  const routes = isPersonalPage
    ? personalRoutes
    : isCryptoPage
    ? cryptosRoutes
    : isStockPage
    ? stockRoutes
    : isEconomicPage
    ? economicRoutes
    : isConsultantPage
    ? consultantRoutes
    : isInvestmentsPage
    ? investmentsRoutes
    : isSettingsPage
    ? settingsRoutes
    : guestRoutes;

  // Encontra a rota atual com base no pathname
  const currentRoute = routes.find((route) => pathname === route.href) || routes[0];

  return (
    <div className="z-20">
      <div className="flex flex-col gap-1 mb-6">
        <div className="flex items-center gap-2">
          <span className="text-2xl text-yellow-500">
            {currentRoute.icon}
          </span>
          <h1 className="text-2xl text-white">{currentRoute.title}</h1>
        </div>
        <p className="text-gray-500">{currentRoute.subtitle}</p>
      </div>

      <div className="flex gap-1">
        {routes.map((route) => (
          <MenuItem
            key={route.href}
            icon={route.icon}
            label={route.label}
            href={route.href}
            title={route.title}
            subtitle={route.subtitle}
            isActive={pathname === route.href} // Opcional: destacar o item ativo
          />
        ))}
      </div>
    </div>
  );
};

export default MenuRoutes;
