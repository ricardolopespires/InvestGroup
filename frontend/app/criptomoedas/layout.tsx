import Navbar from '@/components/dashboard/navbar'

import React from 'react'

const layout = ({children}) => {
  return (
    <main className="flex min-h-screen flex-col z-10 ">
      <Navbar/> 
      <section>
      {children}
 
      </section> 
    </main>
  )
}

export default layout