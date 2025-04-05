



import React from 'react'
import { FaPlus } from 'react-icons/fa'

const page = () => {
  return (
    <div className="z-40 ml-14 mr-10 -mt-16 flex flex-col gap-4 p-4 text-center text-white">
      <div className="w-full  flex items-center justify-between -mt-10">
        <div></div>
        <button className="flex items-center gap-2 bg-blue-900 text-xs py-2 px-7 rounded-sm text-white">
          <FaPlus />
          <span>Adicionar</span>
          </button>
      </div>
   

    </div>
  )
}

export default page