


import React from 'react'
import WhyChooseCard from './WhyChooseCard'

const WhyChoose = () => {
  return (
    <div className='pt-16 pb-16'>
        <h1 className='mt-6 text-2xl md:tex-3xl capitaliza font-bold text-center'>
            Soluções para seus investimentos
        </h1>
        <div className="mt-20 w-[90%] grid mx-auto grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-12">
            <div>
                {/* Cards */}
                < WhyChooseCard
                image="/images/i1.png"
                title="Inteligência artificial"
                />
            </div>
            <div>         
                < WhyChooseCard
                image="/images/i2.png"
                title="Finanças Pessoais"
                />
            </div>
            <div>         
                < WhyChooseCard
                image="/images/i3.png"
                title="Gestão de Carteiras"
                />
            </div>
            <div>         
                < WhyChooseCard
                image="/images/i4.png"
                title="Estratégias  Financeiras"
                />
            </div>
        </div>
    </div>
  )
}

export default WhyChoose
