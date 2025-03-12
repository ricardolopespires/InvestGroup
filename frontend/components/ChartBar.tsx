
"use client"

import { TrendingUp } from "lucide-react"
import { Bar, BarChart, CartesianGrid, XAxis } from "recharts"

import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import {
  type ChartConfig,
  ChartContainer,
  ChartLegend,
  ChartLegendContent,
  ChartTooltip,
  ChartTooltipContent,
} from "@/components/ui/chart"

const chartData = [
    { "month": "Janeiro", "Receitas": 186, "Despesas": 80 },
    { "month": "Fevereiro", "Receitas": 305, "Despesas": 200 },
    { "month": "Março", "Receitas": 237, "Despesas": 120 },
    { "month": "Abril", "Receitas": 73, "Despesas": 190 },
    { "month": "Maio", "Receitas": 209, "Despesas": 130 },
    { "month": "Junho", "Receitas": 214, "Despesas": 140 },
    { "month": "Julho", "Receitas": 180, "Despesas": 150 },
    { "month": "Agosto", "Receitas": 220, "Despesas": 110 },
    { "month": "Setembro", "Receitas": 250, "Despesas": 170 },
    { "month": "Outubro", "Receitas": 300, "Despesas": 190 },
    { "month": "Novembro", "Receitas": 275, "Despesas": 160 },
    { "month": "Dezembro", "Receitas": 350, "Despesas": 210 }
]

const chartConfig = {
  Receitas: {
    label: "Receitas",
    color: "hsl(var(--chart-1))",
  },
  Despesas: {
    label: "Despesas",
    color: "hsl(var(--chart-2))",
  },
} satisfies ChartConfig

export function ChartBar() {
  return (
    <Card className="w-full">
      <CardHeader>
        <CardTitle>Bar Chart - Stacked + Legend</CardTitle>
        <CardDescription>January - June 2024</CardDescription>
      </CardHeader>
      <CardContent>
        <ChartContainer config={chartConfig}>
          <BarChart accessibilityLayer data={chartData}>
            <CartesianGrid vertical={false} />
            <XAxis
              dataKey="month"
              tickLine={false}
              tickMargin={10}
              axisLine={false}
              tickFormatter={(value) => value.slice(0, 3)}
            />
            <ChartTooltip content={<ChartTooltipContent hideLabel />} />
            <ChartLegend content={<ChartLegendContent />} />
            <Bar dataKey="Receitas" stackId="a" fill="var(--color-Receitas)" radius={[0, 0, 4, 4]} />
            <Bar dataKey="Despesas" stackId="a" fill="var(--color-Despesas)" radius={[4, 4, 0, 0]} />
          </BarChart>
        </ChartContainer>
      </CardContent>
      <CardFooter className="flex-col items-start gap-2 text-sm">
        <div className="flex gap-2 font-medium leading-none">
          Trending up by 5.2% this month <TrendingUp className="h-4 w-4" />
        </div>
        <div className="leading-none text-muted-foreground">Showing total visitors for the last 6 months</div>
      </CardFooter>
    </Card>
  )
}

