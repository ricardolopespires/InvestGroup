






import React from 'react'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './ui/card'
import { Progress } from './ui/progress'
import { Separator } from './ui/separator'
import { BarChart4, DollarSign, LineChart, TrendingDown } from 'lucide-react'

const PerformaceAdvisor = ({AdvisorId}) => {
  return (
    <section>
        <h2 className="text-3xl font-semibold mb-4">Performace Advisor</h2>
        <p className="text-gray-700 mb-8">
            Essa seção fornece informações sobre o desempenho do agente, incluindo lucros, perdas e métricas de desempenho. Isso ajuda a entender como o agente está se saindo em suas operações e se ele está atingindo seus objetivos financeiros.
        </p>
        <div className="mt-4 flex flex-col h-full w-full gap-2">  
            {/* Header Summary */}
            <div className="w-full grid grid-cols-6 items-center justify-center h-9 text-xs bg-gray-100 px-4">
                <div className="flex items-center gap-2">
                <span className="text-gray-400">Resultado Liq Tot:</span>
                <span className="text-red-400">R$ -1.396,50</span>
                </div>
                <div className="flex items-center gap-2">
                <span className="text-gray-400">Resultado Total:</span>
                <span className="text-red-400">R$ -1.367,00</span>
                </div>
                <div className="flex items-center gap-2">
                <span className="text-gray-400">Lucro Bruto:</span>
                <span className="text-green-400">R$ 6.808,00</span>
                </div>
                <div className="flex items-center gap-2">
                <span className="text-gray-400">Prejuízo Bruto:</span>
                <span className="text-red-400">R$ -8.175,00</span>
                </div>
                <div className="flex items-center gap-2">
                <span className="text-gray-400">Operações:</span>
                <span className="text-white">27</span>
                </div>
                <div className="flex items-center gap-2">
                <span className="text-gray-400">Vencedoras:</span>
                <span className="text-white">13</span>
                </div>       
            </div>
            <div className="flex items-center gap-6 w-full mt-6 text-xs mb-6">
                <div className="w-[50%]">
                    <div className="grid grid-cols-2 gap-y-3">
                    <div className="text-gray-400">Saldo Líquido Total</div>
                    <div className="text-right text-red-400">R$ -1.396,50</div>

                    <div className="text-gray-400">Lucro Bruto</div>
                    <div className="text-right text-green-400">R$ 6.808,00</div>

                    <div className="text-gray-400">Fator de Lucro</div>
                    <div className="text-right">0,83</div>

                    <div className="text-gray-400">Número Total de Operações</div>
                    <div className="text-right">27</div>

                    <div className="text-gray-400">Operações Vencedoras</div>
                    <div className="text-right">13</div>

                    <div className="text-gray-400">Operações Zeradas</div>
                    <div className="text-right">1</div>

                    <div className="text-gray-400">Média de Lucro/Prejuízo</div>
                    <div className="text-right text-red-400">R$ -51,72</div>

                    <div className="text-gray-400">Média de Operações Vencedoras</div>
                    <div className="text-right text-green-400">R$ 523,69</div>

                    <div className="text-gray-400">Maior Operação Vencedora</div>
                    <div className="text-right text-green-400">R$ 3.181,00</div>

                    <div className="text-gray-400">Maior Sequência Vencedora</div>
                    <div className="text-right">2</div>

                    <div className="text-gray-400">Média de Tempo em Op. Vencedoras</div>
                    <div className="text-right">6min22s</div>

                    <div className="text-gray-400">Média de Tempo em Operações</div>
                    <div className="text-right">3min54s</div>
                    </div>
                </div>
                <div className="w-[50%]">
                    <div className="grid grid-cols-2 gap-y-3">
                    <div className="text-gray-400">Saldo Total</div>
                    <div className="text-right text-red-400">R$ -1.367,00</div>

                    <div className="text-gray-400">Prejuízo Bruto</div>
                    <div className="text-right text-red-400">R$ -8.175,00</div>

                    <div className="text-gray-400">Custos</div>
                    <div className="text-right text-red-400">R$ -29,50</div>

                    <div className="text-gray-400">Percentual de Operações Vencedoras</div>
                    <div className="text-right">48,15%</div>

                    <div className="text-gray-400">Operações Perdedoras</div>
                    <div className="text-right">13</div>

                    <div className="text-gray-400">Razão Média Lucro:Média Prejuízo</div>
                    <div className="text-right">0,83</div>

                    <div className="text-gray-400">Média de Operações Perdedoras</div>
                    <div className="text-right text-red-400">R$ -628,85</div>

                    <div className="text-gray-400">Maior Operação Perdedora</div>
                    <div className="text-right text-red-400">R$ -4.000,00</div>

                    <div className="text-gray-400">Maior Sequência Perdedora</div>
                    <div className="text-right">4</div>

                    <div className="text-gray-400">Média de Tempo em Op. Perdedoras</div>
                    <div className="text-right">1min40s</div>

                    <div className="text-gray-400">Património Necessário(Maior Operação)</div>
                    <div className="text-right">R$ 4.019.505,00</div>

                    <div className="text-gray-400">Retorno no Capital Inicial</div>
                    <div className="text-right text-red-400">-0,03%</div>

                    <div className="text-gray-400">Património Máximo</div>
                    <div className="text-right">R$ 3.157,00</div>
                    </div>
                </div>
                
            </div>
            <Card >
                <CardHeader>
                    <CardTitle>Métricas de Desempenho</CardTitle>
                    <CardDescription>Análise detalhada do desempenho deste agente de IA</CardDescription>
                </CardHeader>
                <CardContent>
                            <div className="h-[300px] w-full bg-muted/20 rounded-md flex items-center justify-center mb-6">
                            <div className="text-center text-muted-foreground">
                                <LineChart className="mx-auto h-8 w-8 mb-2" />
                                <p>O gráfico de desempenho seria renderizado aqui</p>
                            </div>
                            </div>

                            <div className="grid gap-4 md:grid-cols-3">
                            <div className="space-y-2">
                                <div className="flex items-center">
                                <DollarSign className="mr-2 h-4 w-4 text-muted-foreground" />
                                <h4 className="text-sm font-medium">Retorno Total</h4>
                                </div>
                                <div className="text-2xl font-bold text-green-500">
                                +0%
                                </div>
                                <p className="text-xs text-muted-foreground">vs. S&P 500: +10.2%</p>
                            </div>
                            <div className="space-y-2">
                                <div className="flex items-center">
                                <TrendingDown className="mr-2 h-4 w-4 text-muted-foreground" />
                                <h4 className="text-sm font-medium">Drawdown Máximo</h4>
                                </div>
                                <div className="text-2xl font-bold text-red-500">-8.4%</div>
                                <p className="text-xs text-muted-foreground">vs. S&P 500: -12.5%</p>
                            </div>
                            <div className="space-y-2">
                                <div className="flex items-center">
                                <BarChart4 className="mr-2 h-4 w-4 text-muted-foreground" />
                                <h4 className="text-sm font-medium">Máximo de average run-up</h4>
                               </div>
                                <div className="text-2xl font-bold">68%</div>
                                <p className="text-xs text-muted-foreground">17 de 25 negociações lucrativas</p>
                            </div>
                            </div>

                            <Separator className="my-6" />

                            <div className="space-y-4">
                            <h4 className="text-md font-medium">Desempenho da classe de ativos</h4>
                            <div className="space-y-4 text-xs text-gray-400">
                                <div className="space-y-2">
                                <div className="flex items-center justify-between">
                                    <span>Stocks</span>
                                    <span className="font-medium text-green-500">+14.2%</span>
                                </div>
                                <Progress value={14.2} max={20} className="h-2" />
                                </div>
                                <div className="space-y-2">
                                <div className="flex items-center justify-between">
                                    <span>ETFs</span>
                                    <span className="font-medium text-green-500">+9.8%</span>
                                </div>
                                <Progress value={9.8} max={20} className="h-2" />
                                </div>
                                <div className="space-y-2">
                                <div className="flex items-center justify-between">
                                    <span>Bonds</span>
                                    <span className="font-medium text-green-500">+4.5%</span>
                                </div>
                                <Progress value={4.5} max={20} className="h-2" />
                                </div>
                                <div className="space-y-2">
                                <div className="flex items-center justify-between">
                                    <span>Crypto</span>
                                    <span className="font-medium text-red-500">-2.3%</span>
                                </div>
                                <Progress value={0} max={20} className="h-2 bg-red-200" />
                                </div>
                            </div>
                            </div>
                </CardContent>
            </Card>
        </div>
    </section>
  )
}

export default PerformaceAdvisor