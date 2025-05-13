





import React from 'react'
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from './ui/card'
import { Separator } from '@radix-ui/react-select'
import { Badge } from './ui/badge'
import { Button } from './ui/button'
import { DollarSign, Shield, TrendingDown, TrendingUp } from 'lucide-react'

const TradeAnalysis = () => {


  return (
    <div  className="space-y-4 mt-6">   

    <Card>
      <CardHeader>
        <CardTitle>Análise do Trade</CardTitle>
        <CardDescription>Métricas de desempenho para negociações</CardDescription>
      </CardHeader>
      <CardContent>
        <div className="grid gap-4 md:grid-cols-2">
          <div className="space-y-4">
            <div className="flex items-center justify-between">
              <div className="flex items-center">
                <Shield className="mr-2 h-4 w-4 text-primary" />
                <span className="font-medium">Gestão de Riscos</span>
              </div>
              <Badge>Good</Badge>
            </div>
            <p className="text-sm text-muted-foreground">
            Este agente mantém o dimensionamento adequado da posição e implementa stop losses em 92% das negociações.
            </p>
          </div>
          <div className="space-y-4">
            <div className="flex items-center justify-between">
              <div className="flex items-center">
                <TrendingUp className="mr-2 h-4 w-4 text-primary" />
                <span className="font-medium">Tempo de entrada</span>
              </div>
              <Badge>Excellent</Badge>
            </div>
            <p className="text-sm text-muted-foreground">
            Os pontos de entrada são oportunos, com 78% das entradas ocorrendo perto dos níveis de suporte local.
            </p>
          </div>
          <div className="space-y-4">
            <div className="flex items-center justify-between">
              <div className="flex items-center">
                <TrendingDown className="mr-2 h-4 w-4 text-primary" />
                <span className="font-medium">Estratégia de Saída</span>
              </div>
              <Badge>Fair</Badge>
            </div>
            <p className="text-sm text-muted-foreground">
            As saídas tendem a ser prematuras, deixando uma média de 12% de lucro potencial sobre a mesa.
            </p>
          </div>
          <div className="space-y-4">
            <div className="flex items-center justify-between">
              <div className="flex items-center">
                <DollarSign className="mr-2 h-4 w-4 text-primary" />
                <span className="font-medium">Fator de Lucro</span>
              </div>
              <Badge>Good</Badge>
            </div>
            <p className="text-sm text-muted-foreground">
            Fator de lucro de 2,3 (lucros totais divididos pelas perdas totais)..
            </p>
          </div>
        </div>
      </CardContent>
    </Card>
  </div>
  )
}

export default TradeAnalysis