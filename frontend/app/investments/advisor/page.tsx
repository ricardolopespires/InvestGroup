
"use client"

import React, { useEffect, useState } from "react"
import { useTheme } from "next-themes"
import {
  Plus,
  Bot,
  Zap,
  LineChart,
  AlertTriangle,
  Shield,
  Trash2,
  TrendingUp,
  TrendingDown,
  DollarSign,
  BarChart4,
} from "lucide-react"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Badge } from "@/components/ui/badge"
import { Input } from "@/components/ui/input"
import { Separator } from "@/components/ui/separator"
import { Switch } from "@/components/ui/switch"
import { Slider } from "@/components/ui/slider"
import { Label } from "@/components/ui/label"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from "@/components/ui/alert-dialog"
import { Progress } from "@/components/ui/progress"

import { getListAdvisors } from "@/lib/actions/actions.advisors"
import { cn } from "@/lib/utils"
import CardAdvisor from "@/components/CardAdvisor"


const page = () => {
    const [seleted, setSelected] = React.useState("lucro")
    const [advisors, setAdvisors] = React.useState([])   


    useEffect(() => {
        const feachtData = async () => {
            const res = await getListAdvisors()
            setAdvisors(res)  


        }
        feachtData()
    }, [])
    const { theme, setTheme } = useTheme()
    const [activeAgent, setActiveAgent] = useState("agent_1")
    const [riskTolerance, setRiskTolerance] = useState(30)
  
    const agents = [
      {
        id: "agent_1",
        name: "Conservative Investor",
        description: "Focuses on stable, low-risk investments with consistent returns",
        active: true,
        riskTolerance: 30,
        investmentHorizon: "long",
        preferredAssets: ["bonds", "bluechip", "dividend"],
        performance: {
          monthly: 2.1,
          yearly: 8.4,
          allTime: 12.6,
        },
        trades: [
          { asset: "AAPL", action: "buy", quantity: 10, price: 182.63, date: "2023-05-02" },
          { asset: "TSLA", action: "sell", quantity: 5, price: 241.05, date: "2023-04-25" },
          { asset: "VTI", action: "buy", quantity: 15, price: 235.17, date: "2023-04-18" },
        ],
        insights: [
          {
            title: "Increased Bond Allocation",
            description: "Increased bond allocation by 5% to reduce portfolio volatility",
            date: "2023-05-01",
            type: "action",
          },
          {
            title: "Market Volatility Alert",
            description: "Detected increased market volatility, reducing exposure to high-beta stocks",
            date: "2023-04-28",
            type: "alert",
          },
          {
            title: "Dividend Opportunity",
            description: "Identified 3 undervalued dividend stocks with strong fundamentals",
            date: "2023-04-20",
            type: "opportunity",
          },
        ],
      },
      {
        id: "agent_2",
        name: "Growth Seeker",
        description: "Targets high-growth opportunities with higher risk tolerance",
        active: false,
        riskTolerance: 70,
        investmentHorizon: "medium",
        preferredAssets: ["tech", "emerging", "crypto"],
        performance: {
          monthly: 4.8,
          yearly: -3.2,
          allTime: 22.5,
        },
        trades: [
          { asset: "NVDA", action: "buy", quantity: 5, price: 881.86, date: "2023-04-15" },
          { asset: "COIN", action: "buy", quantity: 8, price: 245.32, date: "2023-04-10" },
          { asset: "SHOP", action: "sell", quantity: 12, price: 72.45, date: "2023-04-05" },
        ],
        insights: [
          {
            title: "AI Sector Momentum",
            description: "AI sector showing strong momentum, increased allocation to NVDA and AMD",
            date: "2023-04-15",
            type: "action",
          },
          {
            title: "Crypto Recovery",
            description: "Crypto market showing signs of recovery, monitoring for entry points",
            date: "2023-04-12",
            type: "opportunity",
          },
          {
            title: "Tech Sector Rotation",
            description: "Detected rotation from software to semiconductor stocks",
            date: "2023-04-08",
            type: "alert",
          },
        ],
      },
      {
        id: "agent_3",
        name: "Income Generator",
        description: "Focuses on dividend income and stable cash flow",
        active: true,
        riskTolerance: 40,
        investmentHorizon: "long",
        preferredAssets: ["dividend", "reit", "bonds"],
        performance: {
          monthly: 1.8,
          yearly: 6.5,
          allTime: 9.8,
        },
        trades: [
          { asset: "SCHD", action: "buy", quantity: 20, price: 78.42, date: "2023-04-28" },
          { asset: "O", action: "buy", quantity: 15, price: 62.18, date: "2023-04-22" },
          { asset: "JNJ", action: "buy", quantity: 5, price: 152.78, date: "2023-04-15" },
        ],
        insights: [
          {
            title: "Dividend Increase",
            description: "3 holdings announced dividend increases averaging 7%",
            date: "2023-04-30",
            type: "opportunity",
          },
          {
            title: "REIT Sector Analysis",
            description: "Completed analysis of REIT sector, identified 2 undervalued opportunities",
            date: "2023-04-25",
            type: "action",
          },
          {
            title: "Interest Rate Impact",
            description: "Monitoring impact of interest rate changes on dividend stocks",
            date: "2023-04-20",
            type: "alert",
          },
        ],
      },
    ]
  
  

  return (
    <div className="max-w-screen-4xl mx-auto w-full pb-10 mt-24 ">
        <div className="flex items-center justify-end gap-2 mb-10 text-xs">            
            <button className={cn("",
                seleted==="lucro" ? "bg-gray-100 py-2.5 px-6 rounded-l-sm":"border text-white rounded-l-sm py-2 px-6")}
                onClick={() => setSelected("lucro")}>Lucro</button>
            <button className={cn(
                seleted==="performace" ? "bg-gray-100 py-2.5 px-6 rounded-r-sm":"text-white border rounded-r-sm py-2 px-6")} onClick={() => setSelected("performace")}>Performace</button>
        </div>
              
                {/* AI Agents Overview */}
            <div className="grid gap-4 md:grid-cols-4">
              {advisors.map((agent) => (
                <CardAdvisor agent={agent} key={agent.id}/>
              ))}
            </div>
        
    </div>
  )
}

export default page
