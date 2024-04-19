import { GiSettingsKnobs } from "react-icons/gi";


import React from 'react'

const Settings = () => {
  return (
    <div className='flex flex-col px-10 relative top-[-40px]'>
    <div className="flex items-center space-x-1">
      <div className="text-2xl text-primary"><GiSettingsKnobs /></div>
      <h1 className='text-2xl '>Settings</h1>

      </div>
    </div>
  )
}

export default Settings
