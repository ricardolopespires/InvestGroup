'use client'

import React, { useState } from 'react'
import NavBar from './NavBar'
import Mobile from './Mobile'

const Responsive = () => {


    const [showNav, setShowNav] = useState(false);
    const handlerNavShow = () =>{
        setShowNav(true);
    };
    const handlerNavHide = () =>{
        setShowNav(false);
    }

  return (
    <div className=''>
        <NavBar openNav={handlerNavShow}/>
        <Mobile showNav={showNav} closeNav={handlerNavHide}/>
      
    </div>
  )
}

export default Responsive
