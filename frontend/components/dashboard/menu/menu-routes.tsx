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
import { FaDesktop, FaUserTie, FaChartPie, FaBuromobelexperte, FaGlobeAmericas  } from "react-icons/fa";
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

const economicRoutes = [
  {
    icon: <FaGlobeAmericas />,
    label: "Overview",
    href: "/economic/overview",
    title: "Visão Geral da Economia",	
    subtitle: "A visão geral da economia analisa a produção, distribuição e consumo de bens e serviços.",
  },
  {
    icon: DollarSign,
    label: "Indices",
    href: "/economic/ordinaria",
    title: "Indeces",
    subtitle: "Gestão de taxas regulares",
  },
  {
    icon: FileText,
    label: "Analytics",
    href: "/economic/extra",
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
    subtitle: "Consultores de investimentos especializados para ajudar em suas decisões financeiras",
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
  {
    icon: <LuChartPie />,
    label: "Criptomoedas",
    href: "/investments/cryptos",
    title: "Criptomoedas",
    subtitle: "Descubra onde investir o seu dinheiro, com boa rentabilidade e muita segurança.",
  },
  {
    icon: <LuChartPie />,
    label: "Ações",
    href: "/investments/stock",
    title: "Ações",
    subtitle: "Descubra onde investir o seu dinheiro, com boa rentabilidade e muita segurança.",
  },
  {
    icon: <LuChartPie />,
    label: "Commodities",
    href: "/investments/commodities",
    title: "Commodities",
    subtitle: "Descubra onde investir o seu dinheiro, com boa rentabilidade e muita segurança.",
  },
  {
    icon: <LuChartPie />,
    label: "Moedas",
    href: "/investments/currencies",
    title: "Moedas",
    subtitle: "Descubra onde investir o seu dinheiro, com boa rentabilidade e muita segurança.",
  },
  {
    icon: <LuChartPie />,
    label: "Índices",
    href: "/investments/indexes",
    title: "índeces",
    subtitle: "Descubra onde investir o seu dinheiro, com boa rentabilidade e muita segurança.",
  },
  {
    icon: <LuChartPie />,
    label: "Advisor",
    href: "/investments/advisor",
    title: "Agentes de Investimento com IA",
    subtitle: "Assistentes inteligentes que ajudam a gerenciar e investir o seu dinheiro, com boa rentabilidade e muita segurança.",
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
  const isEconomicPage = pathname?.includes("/economic");
  const isConsultantPage = pathname?.includes("/consultants");
  const isInvestmentsPage = pathname?.includes("/investments");
  const isSettingsPage = pathname?.includes("/settings");


  // Seleciona as rotas com base na página atual
  const routes = isPersonalPage
    ? personalRoutes
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
