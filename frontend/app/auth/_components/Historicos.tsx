import { FaHistory } from "react-icons/fa";
import { GrHistory } from "react-icons/gr";

import React from 'react'

const Historicos = () => {
  return (
    <div className='flex flex-col px-10 relative top-[-74px]'>
    <div className="flex items-center space-x-1">
      <div className="text-2xl text-primary"><GrHistory/></div>
      <h1 className='text-2xl '>Histórico</h1>

      </div>
    </div>
  )
}

export default Historicos
