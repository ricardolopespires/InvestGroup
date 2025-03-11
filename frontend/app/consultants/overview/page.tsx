


import CardConsultant from '@/components/CardConsultant'
import React from 'react'

const page = ({children}) => {
  return (
    <div className='grid grid-cols-5 items-center mx-16 -mt-5'>
      <CardConsultant/>
     
      {children}
    </div>
  )
}

export default page