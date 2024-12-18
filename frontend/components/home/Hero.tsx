"use client"



import Image from "next/image";
import React from 'react'
import Tilt from 'react-parallax-tilt'

const Hero = () => {
  return (
    <main className="w-full pt-[4vh] md:pt[12vh] h-screen bg-[#F7F6FB]">
        <div className="flex justify-center flex-col w-[90%] sm:w-[80%] h-full  mx-auto">
            <div className="grid grid-cols-1 lg:grid-cols-2 items-center gap-12">
                {/*Text Content*/}
                <div>
                    {/* Top box*/}
                    <div className="w-fit py-1.5 px-2 md:px-5 rounded-full shadow-md flex items-center space-x-3 bg-white">
                        <div className="px-3 py-1 md:px-5 md:py-1 rounded-full bg-blue-900 md:text-base sm:text-sm text-xs text-white">
                        Investgroup
                        </div>
                        <p className="text-xs sm:text-sm">Investimentos e finanças feito de maneira mais inteligente</p>
                    </div>
                    {/* Heading */}
                    <h1 className="text-2xl sm:text-4xl md:text-5xl mt-6 mb-6 font-bold md:leading-[3rem] lg:leading-[3.5rem]">Estratégias com Inteligência Artificial para Investimentos Inteligentes. </h1>
                    {/* Description */}
                    <p className="justify font-light">
                    <strong className="text-blue-600">Invesgroup</strong> é a solução definitiva para quem busca uma gestão financeira inteligente e eficiente. Integrando IA e técnicas avançadas de análise de dados,
                    a <strong className="text-blue-600">Invesgroup</strong> proporciona uma experiência de investimento personalizada, permitindo que os usuários aproveitem ao máximo suas carteiras de ativos.
                    </p>
                    <div className="flex items-center flex-wrap space-x-16 mt-8">
                        <div className="text-center">
                            <p className="md:text-xl lg:text-2xl text-base font-bold">2680+</p>
                            <p className="w-[100px] h-[4px] bg-[#00e600] mt-2 mb-2 rounded-lg"></p>
                            <p className="md:text:lg text-sm text-opacity-70" >Investidores</p>
                        </div>
                        <div className="text-center">
                            <p className="md:text-xl lg:text-2xl text-base font-bold">55%</p>
                            <p className="w-[100px] h-[4px] bg-[#ffff1a] mt-2 mb-2 rounded-lg"></p>
                            <p className="md:text:lg text-sm text-opacity-70" >Retono médio</p>
                        </div>
                        <div className="text-center">
                            <p className="md:text-xl lg:text-2xl text-base font-bold">$260+</p>
                            <p className="w-[100px] h-[4px] bg-indigo-600 mt-2 mb-2 rounded-lg"></p>
                            <p className="md:text:lg text-sm text-opacity-70" >Rendimentos</p>                           
                        </div>
                    </div>
                </div>
                {/* Image Content*/}
                <div className="hidden lg:block">
                    <Tilt>
                    <Image src={"/images/estatistica.png"} width={700} height={700} alt="hero"/>
                    </Tilt>
                </div>
            </div>
        </div>
    </main>
  )
}

export default Hero
