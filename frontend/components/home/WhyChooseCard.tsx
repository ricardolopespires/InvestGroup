

import Image from "next/image";
import React from 'react'

type Props ={
    title: string;
    linkText: string;
    image: string;
}


const WhyChooseCard = ({image, title}:Props) => {
  return (
    <div className="">
      <Image 
      src={image}
      width={90}
      height={90}
      alt={title}
      className="object-contain mx-auto"/>
      <h1 className="text-center text-lg mt-5 mb-5 font-semibold text-gray-700">{title}</h1>
      <p className="text-gray-600 text-center font-light text-sm mb-7">
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Omnis pariatur cum dicta aliquid fugit perspiciatis sint unde similique, aut doloremque.
      </p>     
    </div>
  )
}

export default WhyChooseCard
