






import { Separator } from '@radix-ui/react-separator'
import React from 'react'
import { Button } from './ui/button'
import { ChevronDown } from 'lucide-react'

const AboutInvest = () => {
  return (
    <div className="flex-1 p-6">
    {/* About Section */}
    <section className="mb-10">
    <h1 className="text-3xl font-semibold mb-2">Sobre</h1>
    <p className="text-gray-700 mb-4">
      Microsoft is a global technology company dedicated to empowering every person and every organization on the
      planet to achieve more. Founded in 1975, we have pioneered software, cloud computing, and AI innovations
      that drive the digital transformation of businesses and individuals worldwide. From Windows and Azure to
      Office 365 and AI-driven solutions, Microsoft continues to shape the future of work, security, and
      innovation.
    </p>
    <p className="text-gray-700 mb-6">
      With a commitment to sustainability, accessibility, and ethical AI, we strive to create technology that
      enhances productivity, fuels creativity, and connects the world. Our diverse ecosystem of products,
      services, and partners ensures that businesses of all sizes can thrive in an increasingly digital world.
    </p>

    <h2 className="text-xl font-medium mb-4">CEO Quote</h2>
    <blockquote className="bg-green-50 border-l-4 border-green-500 p-4 mb-6">
      <p className="italic text-gray-700">
        "Our industry does not respect tradition—it only respects innovation. At Microsoft, we are constantly
        pushing the boundaries of technology to build a future that is inclusive, intelligent, and empowering for
        all."
      </p>
    </blockquote>

    <Button variant="ghost" className="text-green-600 flex items-center">
      Show more <ChevronDown size={16} className="ml-1" />
    </Button>
  </section>

  <Separator className="my-6" />

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

export default AboutInvest




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
  