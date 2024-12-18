import { FiCheckCircle } from "react-icons/fi";
import Image from "next/image";
import React from 'react'
import PropTypes from 'prop-types'; // Importando PropTypes
import Footer from "@/components/home/Footer";

const Page = ({ children }) => { // Alterei o nome de 'page' para 'Page'
  return (
    <div className='main-page'>
      <section className="home">
        <div className="home-content">
          <header className="home-header">
            <div className='mt-[170px]'>
              <h1 className='text-2xl text-gray-900 uppercase relative after:content-[""] after:block after:w-[400px] after:h-[2px] after:bg-blue-700'>
                Tendências macroeconômicas
              </h1>
              <p className='mt-4 font-light text-gray-600 text-sm text-justify leading-[1.6rem]  italic'>
                A economia global e os mercados financeiros estão em constante evolução, 
                impulsionados por uma série de fatores que afetam diretamente o crescimento econômico, 
                a inflação, o emprego, a renda e o ambiente externo. Para os investidores,
                entender essas variáveis e como elas interagem é crucial para tomar decisões 
                informadas sobre onde alocar seus recursos. A análise macroeconômica é uma ferramenta 
                fundamental para entender o comportamento da economia como um todo. Ela envolve o monitoramento 
                de indicadores-chave que refletem a saúde e a direção da atividade econômica de um país. 
                Entre os principais indicadores estão.Para os investidores, rentabilidade e lucratividade são dois conceitos-chave a serem monitorados. 
                Rentabilidade se refere ao retorno que um investimento proporciona, enquanto lucratividade está diretamente ligada à capacidade das empresas de gerar lucros em relação aos custos. 
                Empresas com alta rentabilidade e lucratividade tendem a atrair mais investimentos, já que demonstram capacidade de gerar resultados consistentes, mesmo em cenários econômicos desafiadores.
              </p>
              <p className='mt-4 font-light text-gray-600 text-sm text-justify leading-[1.6rem]  italic'>
                O nível de endividamento das empresas e governos também é um indicador crucial para a análise de risco no mercado financeiro. 
                Empresas altamente endividadas podem enfrentar dificuldades em tempos de desaceleração econômica, o que pode afetar sua capacidade de gerar lucros e, consequentemente, o valor de suas ações.
                Além disso, um elevado endividamento público pode resultar em inflação elevada e na necessidade de aumentos nas taxas de juros, o que influencia negativamente os mercados financeiros.
                Compreender a economia e o mercado financeiro é essencial para qualquer investidor. A análise das previsões macroeconômicas, como as tendências do PIB, a evolução da inflação, 
                o nível de endividamento e os indicadores de crédito e emprego, ajuda a traçar uma visão mais clara do cenário futuro. Isso permite tomar decisões mais acertadas em relação aos investimentos, visando maximizar a rentabilidade e minimizar os riscos.




              </p>              
            </div>
            <div className='pt-14 pb-16 '>
                {/* Define grid*/}
                <div className='w-full  mx-auto items-center grid grid-cols-1 lg:grid-cols-2 gap-10'>
                    {/* Image Content */}
                    <div>
                              <Image src={"/images/feature-3.png"} width={700} height={700} alt="Features" className="object-contain"/>
                    </div>
                    {/* Text Content */}
                    <div className="p-6">
                          <span className="text-base font-semibold text-blue-900 relative after:content-[''] after:block after:w-[270px] after:h-[2px] after:bg-gray-200 after:rounded-full">A Análise Macroeconômica e Suas Implicações</span>
                
                            <h1 className="mt-4 text-xl sm:text-3xl font-bold text-gray-900">
                                Principais Indicadores Econômicos
                            </h1>
                            <p className="mt-4 font-light text-gray-600 text-sm text-justify leading-[1.6rem]  italic">                            
                            <strong className="text-gray-900 font-semibold">Produto Interno Bruto (PIB):</strong> O PIB é um dos principais indicadores de desempenho econômico. 
                            Ele reflete o valor total de todos os bens e serviços produzidos em um país. 
                            Crescimentos ou quedas no PIB indicam, respectivamente, expansões ou recessões na economia, influenciando diretamente as expectativas dos investidores.
                            </p>
                            <p className="mt-4 font-light text-gray-600 text-sm text-justify leading-[1.6rem]  italic">                            
                            <strong className="text-gray-900 font-semibold">Inflação:</strong>  A inflação é um fator crítico para o mercado financeiro, pois afeta o poder de compra das pessoas e as decisões de investimento.
                            Uma inflação elevada pode levar ao aumento das taxas de juros, o que impacta o custo do crédito e os lucros das empresas.
                            </p>
                            <p className="mt-4 font-light text-gray-600 text-sm text-justify leading-[1.6rem]  italic">                            
                            <strong className="text-gray-900 font-semibold">Crédito e Endividamento:</strong>  O nível de endividamento de empresas e consumidores também é monitorado de perto. 
                            O endividamento elevado pode sinalizar riscos de insolvência ou dificuldades de liquidez, afetando a confiança dos investidores e a rentabilidade das empresas. Ao mesmo tempo, um mercado de crédito acessível é crucial para impulsionar o consumo e os investimentos.
                            Uma inflação elevada pode levar ao aumento das taxas de juros, o que impacta o custo do crédito e os lucros das empresas.
                            </p>
                            <p className="mt-4 font-light text-gray-600 text-sm text-justify leading-[1.6rem]  italic">                            
                            <strong className="text-gray-900 font-semibold"> Emprego e Renda:</strong> O emprego é um reflexo importante da saúde econômica. 
                            Altos índices de emprego são indicativos de uma economia em crescimento, o que pode estimular o consumo e impulsionar o desempenho das empresas. A evolução da renda também é importante, já que influencia o poder de compra das famílias.
                            </p>
                            <p className="mt-4 font-light text-gray-600 text-sm text-justify leading-[1.6rem]  italic">                            
                            <strong className="text-gray-900 font-semibold">Setor Externo e Economia Internacional: </strong>A economia global tem grande impacto nos mercados financeiros locais. 
                            As trocas comerciais, políticas externas, acordos internacionais e crises globais podem afetar as previsões macroeconômicas. O câmbio e as taxas de juros internacionais também influenciam diretamente os fluxos de capitais.
                            </p>
                    </div>
                </div>                       
            </div>
            <div className='pt-14 pb-16 '>
                {/* Define grid*/}
                <div className='w-full  mx-auto items-center grid grid-cols-1 lg:grid-cols-2 gap-10'>                 
                    {/* Text Content */}
                    <div className="p-6">
                         <span className="text-base font-semibold text-blue-900 relative after:content-[''] after:block after:w-[270px] after:h-[2px] after:bg-gray-200 after:rounded-full">Previsões Macroeconômica e Suas Implicações</span>                
                            <h1 className="mt-4 text-xl sm:text-3xl font-bold text-gray-900">
                                Previsões e Tendências para o Futuro
                            </h1>
                        <p className="mt-4 font-light text-gray-600 text-sm text-justify leading-[1.6rem]  italic">                            
                            <strong className="text-gray-900 font-semibold">Crescimento Sustentável:</strong>  Há uma crescente ênfase no crescimento sustentável, 
                            onde os países buscam expandir suas economias sem prejudicar o meio ambiente. Esse movimento tem levado a um aumento nos investimentos em energias renováveis e tecnologias verdes, o que pode gerar novas oportunidades de lucro no longo prazo.
                        </p>
                        <p className="mt-4 font-light text-gray-600 text-sm text-justify leading-[1.6rem]  italic">                            
                            <strong className="text-gray-900 font-semibold">Digitalização e Inovação:</strong>
                            A transformação digital tem impactado diversos setores, desde os serviços financeiros até a indústria e o comércio. A inovação tecnológica pode reduzir custos operacionais e criar novos produtos e serviços, 
                            melhorando a rentabilidade das empresas e oferecendo novas possibilidades para os investidores. 
                        </p>
                        <p className="mt-4 font-light text-gray-600 text-sm text-justify leading-[1.6rem]  italic">                            
                            <strong className="text-gray-900 font-semibold">Taxas de Juros e Inflação:</strong>
                            Com a instabilidade econômica global, muitos países enfrentam o desafio de controlar a inflação enquanto mantêm as taxas de juros em níveis sustentáveis. 
                            A dinâmica entre essas variáveis influenciará diretamente as decisões de investimento, particularmente em mercados de renda fixa 
                        </p>
                        
                    </div>
                    {/* Image Content */}
                    <div>
                        <Image src={"/images/feature-4.png"} width={700} height={700} alt="Features" className="object-contain"/>
                    </div>
                </div>                       
            </div>
            {children}
            
          </header>
        </div>
      </section>
    </div>
    
  )
}

// Definindo os tipos das props para garantir que 'children' seja passado
Page.propTypes = {
  children: PropTypes.node, // 'children' pode ser qualquer tipo de nó React
};

export default Page;
