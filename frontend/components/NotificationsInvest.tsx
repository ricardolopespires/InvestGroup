"use client"

import { useState } from "react"
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Switch } from "@/components/ui/switch"
import { Bell, AlertTriangle, TrendingUp, TrendingDown, DollarSign, Users } from "lucide-react"
import { Separator } from "@/components/ui/separator"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { Label } from "./ui/label"

const notificationTypes = [
  { id: "account", label: "Atividade da conta", icon: Bell },
  { id: "security", label: "Alertas de segurança", icon: AlertTriangle },
  { id: "performance", label: "Atualizações de desempenho", icon: TrendingUp },
  { id: "market", label: "Tendências de Mercado", icon: TrendingDown },
  { id: "financial", label: "Relatórios Financeiros", icon: DollarSign },
  { id: "user", label: "Comportamento do usuário", icon: Users },
]

const notificationSend = [
    { id: "Email", label: "Notificações por e-mail", icon: Bell },   
    { id: "SMS", label: "Notificações por SMS", icon: AlertTriangle },    
    { id: "market", label: "Marketing e promoções", icon: TrendingDown },   
    
  ]

const NotificationsInvest = () => {

    const [notifications, setNotifications] = useState({
        account: true,
        security: true,
        performance: false,
        market: false,
        financial: true,
        user: false,
      })
    
      const toggleNotification = (id) => {
        setNotifications((prev) => ({ ...prev, [id]: !prev[id] }))
      }

  return (
    <div className="flex-1 p-6">
        {/* Notifications Section */}
        <section className="mb-10">
            <h1 className="text-3xl font-semibold mb-6">Notificações </h1>
                <div className="space-y-4">
                    <Card>
                        <CardHeader>
                        <CardTitle className="text-xl font-semibold">Preferências de notificação</CardTitle>
                        </CardHeader>
                        <CardContent className="flex flex-col gap-6">
                        <div className="flex gap-9 items-center w-full">
                        <div className="flex flex-col  space-y-4 w-[50%]">
                            {notificationTypes.map((type) => (
                                <div key={type.id} className="flex items-center justify-between">
                                <div className="flex items-center space-x-4">
                                    <type.icon className="h-5 w-5 text-muted-foreground" />
                                    <span className="text-sm font-medium">{type.label}</span>
                                </div>
                                <Switch checked={notifications[type.id]} onCheckedChange={() => toggleNotification(type.id)} />
                                </div>
                            ))}
                        </div>
                        <Separator orientation="vertical" />
                        <div className="flex flex-col inset-0 relative top-0 space-y-4 w-[50%]">
                            {notificationSend.map((type) => (
                                <div key={type.id} className="flex items-center justify-between">
                                <div className="flex items-center space-x-4">
                                    <type.icon className="h-5 w-5 text-muted-foreground" />
                                    <span className="text-sm font-medium">{type.label}</span>
                                </div>
                                <Switch checked={notifications[type.id]} onCheckedChange={() => toggleNotification(type.id)} />
                                </div>
                            ))}
                        </div>
                        </div>                       
                     
                        </CardContent>
                        <CardFooter className="mt-11">
                            <Button  className="text-sm">Salvar configurações de notificação</Button>
                        </CardFooter>
                    </Card>
                    <Card>
                        <CardHeader>
                        <CardTitle className="text-xl font-semibold">Notificações recentes</CardTitle>
                        </CardHeader>
                        <CardContent className="space-y-4">
                        <div className="flex items-center space-x-4">
                            <AlertTriangle className="h-5 w-5 text-yellow-500" />
                            <div>
                            <p className="text-sm font-medium">Unusual account activity detected</p>
                            <p className="text-xs text-muted-foreground">2 hours ago</p>
                            </div>
                        </div>
                        <div className="flex items-center space-x-4">
                            <TrendingUp className="h-5 w-5 text-green-500" />
                            <div>
                            <p className="text-sm font-medium">Your portfolio has grown by 5% this week</p>
                            <p className="text-xs text-muted-foreground">1 day ago</p>
                            </div>
                        </div>
                        <div className="flex items-center space-x-4">
                            <Bell className="h-5 w-5 text-blue-500" />
                            <div>
                            <p className="text-sm font-medium">New feature: Advanced analytics now available</p>
                            <p className="text-xs text-muted-foreground">3 days ago</p>
                            </div>
                        </div>
                        <div className="flex items-center space-x-4">
                            <DollarSign className="h-5 w-5 text-purple-500" />
                            <div>
                            <p className="text-sm font-medium">Monthly financial report is ready for review</p>
                            <p className="text-xs text-muted-foreground">5 days ago</p>
                            </div>
                        </div>
                        </CardContent>
                    </Card>
                    <div className="flex justify-end">
                        <Button variant="outline" className="text-sm">
                        View All Notifications
                        </Button>
                    </div>
                </div>       
        </section>
    </div>
  )
}

export default NotificationsInvest