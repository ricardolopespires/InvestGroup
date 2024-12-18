'use client';

import { AiOutlineMinus, AiOutlinePlus } from "react-icons/ai";
import React from 'react';

interface AccordionItemProps {
  open: boolean;
  toggle: () => void;
  title: string;
  desc?: string;
}

const AccordionItem: React.FC<AccordionItemProps> = ({ open, toggle, title, desc }) => {
  return (
    <div className="pt-[5px] w-full border-b border-gray-200 pb-6 cursor-pointer">
      <div className='py-[14px] px-[50px] flex justify-between items-center w-full' onClick={toggle}>
        <p className='text-lg font-light text-left'>{title}</p>  {/* Adicionado text-left */}
        <span className="text-2xl">{open ? <AiOutlineMinus /> : < AiOutlinePlus />}</span>
      </div>   
      {open && (
        <div className="text-gray-400 font-light text-left">  {/* Adicionado text-left */}
          <p>{desc || 'Este é o conteúdo do accordion. Pode ser qualquer coisa aqui!'}</p>
        </div>
      )}
    </div>
  );
};

export default AccordionItem;
