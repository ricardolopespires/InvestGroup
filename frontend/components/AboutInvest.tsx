import { Separator } from '@radix-ui/react-separator'
import React from 'react'
import { Button } from './ui/button'
import { ChevronDown } from 'lucide-react'
import PortifolioInvest from './PortifolioInvest'

const AboutInvest = ({ description }) => {
  return (
    <div className="flex-1 p-6">
      {/* About Section */}
      <section className="mb-10">
        <h1 className="text-3xl font-semibold mb-2">Sobre</h1>
        {/* Verificação se a descrição existe */}
        {description ? (
          <p className="text-gray-700 mb-4 text-justify">{description}</p>
        ) : (
          <p className="text-gray-700 mb-4">
            Robo-advisors ou robo-advisors são consultores financeiros que fornecem aconselhamento financeiro personalizado
            e gestão de investimentos online com intervenção humana moderada a mínima. Um robo-advisor fornece aconselhamento
            financeiro digital com base em regras matemáticas ou algoritmos. Esses algoritmos são projetados por consultores
            financeiros humanos, gestores de investimentos e cientistas de dados, e codificados em software por programadores.
          </p>
        )}
        <p className="text-gray-700 mb-6">
          Esses algoritmos são executados por software e não requerem um consultor humano para fornecer aconselhamento financeiro
          a um cliente. O software utiliza seus algoritmos para alocar, gerenciar e otimizar automaticamente os ativos dos clientes
          para investimentos de curto ou longo prazo.
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
      <PortifolioInvest />
    </div>
  )
}

export default AboutInvest
