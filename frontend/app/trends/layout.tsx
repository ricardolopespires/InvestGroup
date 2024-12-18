
import Responsive from '@/components/home/Responsive'
import React from 'react'

const layout = ( {children}) => {
  return (
    <section 
    className="bg-cover bg-center h-[400px] flex flex-col w-full text-gray-400 cursor-pointer relative z-0 rounded-b-xl"
    style={{ backgroundImage: `url(/images/trends-maps.png)` }}>
      <Responsive/>
       {children}    
    </section>
  )
}

export default layout
