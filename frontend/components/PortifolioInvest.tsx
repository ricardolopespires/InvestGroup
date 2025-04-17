













import React from 'react'

const PortifolioInvest = () => {
  return (
    <div className="flex-1 ">
      {/* What We Build Section */}
      <section>
        <h2 className="text-3xl font-semibold mb-4">Portifólio</h2>
        <p className="text-gray-700 mb-8">
        É fundamental que o Advisor possua habilidades técnicas que ajudem a oferecer uma orientação financeira mais eficiente para os seus clientes.
        </p>

        <div className="flex flex-col md:flex-row items-center gap-8">
          <div className="relative w-64 h-64">
            <div className="absolute inset-0 flex items-center justify-center">
              <div className="text-center">
                <div className="text-5xl font-bold">5</div>
                <div className="text-sm uppercase text-gray-500">ATIVOS</div>
              </div>
            </div>
            <SkillsChart />
          </div>

          <div className="space-y-4">
            <div className="flex items-center gap-2">
              <div className="w-3 h-3 rounded-full bg-blue-500"></div>
              <div>Figma — 5 years</div>
              <div className="ml-auto">30%</div>
            </div>
            <div className="flex items-center gap-2">
              <div className="w-3 h-3 rounded-full bg-purple-500"></div>
              <div>User Testing — 5 years</div>
              <div className="ml-auto">20%</div>
            </div>
            <div className="flex items-center gap-2">
              <div className="w-3 h-3 rounded-full bg-green-500"></div>
              <div>Web Design — 3 years</div>
              <div className="ml-auto">20%</div>
            </div>
            <div className="flex items-center gap-2">
              <div className="w-3 h-3 rounded-full bg-amber-400"></div>
              <div>Miro — 5 years</div>
              <div className="ml-auto">10%</div>
            </div>
            <div className="flex items-center gap-2">
              <div className="w-3 h-3 rounded-full bg-gray-300"></div>
              <div>SaaS — 4 years</div>
              <div className="ml-auto">20%</div>
            </div>
          </div>
        </div>
      </section>
    </div>
  )
}

export default PortifolioInvest




function SkillsChart() {
  return (
    <svg viewBox="0 0 100 100" className="w-full h-full">
      {/* Blue segment (30%) */}
      <circle
        cx="50"
        cy="50"
        r="40"
        fill="transparent"
        stroke="#3B82F6"
        strokeWidth="12"
        strokeDasharray="75.4 251.2"
        strokeDashoffset="0"
      />

      {/* Purple segment (20%) */}
      <circle
        cx="50"
        cy="50"
        r="40"
        fill="transparent"
        stroke="#8B5CF6"
        strokeWidth="12"
        strokeDasharray="50.3 251.2"
        strokeDashoffset="-75.4"
      />

      {/* Green segment (20%) */}
      <circle
        cx="50"
        cy="50"
        r="40"
        fill="transparent"
        stroke="#22C55E"
        strokeWidth="12"
        strokeDasharray="50.3 251.2"
        strokeDashoffset="-125.7"
      />

      {/* Amber segment (10%) */}
      <circle
        cx="50"
        cy="50"
        r="40"
        fill="transparent"
        stroke="#F59E0B"
        strokeWidth="12"
        strokeDasharray="25.1 251.2"
        strokeDashoffset="-176"
      />

      {/* Gray segment (20%) */}
      <circle
        cx="50"
        cy="50"
        r="40"
        fill="transparent"
        stroke="#D1D5DB"
        strokeWidth="12"
        strokeDasharray="50.3 251.2"
        strokeDashoffset="-201.1"
      />
    </svg>
  )
}
