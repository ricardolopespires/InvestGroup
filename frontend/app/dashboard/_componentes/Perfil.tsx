import { FaDoorOpen, FaUserTie } from "react-icons/fa";



import React from 'react'

const Perfil = () => {
  return (
    <div className="flex space-x-2 items-center h-10">
        <FaUserTie className="text-2xl"/>
        <span className="text-orange-500">Moderado</span>
    </div>
  )
}

export default Perfil
