






import React from 'react'
import RiskAdvisor from './RiskAdvisor'

const SettingsInvest = ({AdvisorId}) => {
  return (
    <div className="flex-1 p-6 ">
        {/* Settings Section */}
        <section className="mb-10 flex flex-col">
        <h1 className="text-3xl font-semibold mb-2">Settings </h1>
        <p className="text-gray-700 mb-7">
          Interface intuitiva, é possível otimizar o desempenho do Advisor, garantindo que ele se alinhe às suas necessidades operacionais e estratégicas. Mantenha o controle total com configurações seguras e flexíveis.
        </p>
        <div className='flex items-center justify-between gap-2'>
        <RiskAdvisor AdvisorId={AdvisorId}/>
        

        </div>
        
        
        
        </section>
    </div>
    
  )
}

export default SettingsInvest