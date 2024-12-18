"use client";
import { HiBars3BottomRight, HiMiniArrowLeftOnRectangle } from "react-icons/hi2";
import { linksHome } from "@/constant/Constant";
import Image from "next/image";
import React, { useEffect, useState, useCallback } from "react";


type Props={
    openNav:()=> void;
}


const NavBar = ({openNav}:Props) => {
  const [navBg, setNavBg] = useState(false);

  // Função para alterar o background do navbar ao rolar a página
  const handleScroll = useCallback(() => {
    if (window.scrollY >= 60) setNavBg(true);
    else setNavBg(false);
  }, []);

  useEffect(() => {
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, [handleScroll]);

  return (
    <div className={`fixed w-full transition-all duration-200 h-[12vh] z-[1000] ${navBg ? 'bg-white shadow-md' : ''}`}>
      <div className="flex items-center h-full justify-between w-[90%] xl:w-[80%] mx-auto">
        {/* Logo */}
        <Image src={'/images/logo.png'} width={140} height={140} alt="logo" />
        {/* Links */}
        <div className="hidden lg:flex items-center space-x-10">
          {linksHome.map((link) => (
            <a href={link.url} key={link.id} className="link">{link.label}</a>
          ))}
        </div>
        {/* Buttons */}
        <div className="flex items-center space-x-4">
          <a href="/Sign-In">
            <HiMiniArrowLeftOnRectangle className="mr-20 text-[200%]" />
          </a>
          {/* Burger menu */}
          <HiBars3BottomRight onClick={openNav} className="w-8 h-8 cursor-pointer text-black lg:hidden" />
        </div>
      </div>
    </div>
  );
};

export default NavBar;
