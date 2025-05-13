"use client"

import type React from "react"

import { useState, useRef, useEffect } from "react"
import Link from "next/link"
import { useTheme } from "next-themes"
import {

  Plus,
  Briefcase,
  Building,
  BarChart4,
  Bitcoin,
  Home,
  Globe,
  PieChart,

} from "lucide-react"
import { getManagers } from "@/lib/actions/actions.agents"
import CardManager from "@/components/CardManager"


const page = ({children}) => {
  const { theme, setTheme } = useTheme()
  const [activeConsultant, setActiveConsultant] = useState<string | null>(null)
  const [messages, setMessages] = useState<{ role: string; content: string; timestamp: Date }[]>([])
  const [inputMessage, setInputMessage] = useState("")
  const messagesEndRef = useRef<HTMLDivElement>(null)
  const [consultants, setConsultants] = useState([])


  useEffect(() => {
    const fetchConsultants = async () => { 
      const res = await getManagers()
      setConsultants(res)
     }
    fetchConsultants()
    }, [])


  const selectedConsultant = consultants?.find((c) => c.id === activeConsultant)

  useEffect(() => {
    if (messagesEndRef.current) {
      messagesEndRef.current.scrollIntoView({ behavior: "smooth" })
    }
  }, [messages])

  useEffect(() => {
    if (selectedConsultant && messages.length === 0) {
      // Add greeting message when consultant is selected
      setMessages([
        {
          role: "assistant",
          content: selectedConsultant.greeting,
          timestamp: new Date(),
        },
      ])
    }
  }, [selectedConsultant])

  const handleSendMessage = () => {
    if (!inputMessage.trim() || !selectedConsultant) return

    // Add user message
    const newMessages = [...messages, { role: "user", content: inputMessage, timestamp: new Date() }]
    setMessages(newMessages)
    setInputMessage("")

    // Simulate consultant response (in a real app, this would call an AI API)
    setTimeout(() => {
      const responses = [
        `Based on your interest in ${selectedConsultant.specialty}, I'd recommend considering a diversified approach. Would you like me to elaborate on specific strategies?`,
        `That's a great question about ${selectedConsultant.specialty}. The current market conditions suggest caution, but there are still opportunities in select areas.`,
        `When investing in ${selectedConsultant.specialty}, it's important to consider your time horizon and risk tolerance. Have you defined your investment goals?`,
        `I've analyzed recent trends in ${selectedConsultant.specialty} markets, and there are several promising developments. Would you like me to share my top recommendations?`,
        `For your ${selectedConsultant.specialty} portfolio, I'd suggest allocating across different sub-sectors to minimize risk while maximizing potential returns.`,
      ]

      const randomResponse = responses[Math.floor(Math.random() * responses.length)]

      setMessages((prev) => [...prev, { role: "assistant", content: randomResponse, timestamp: new Date() }])
    }, 1000)
  }

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault()
      handleSendMessage()
    }
  }

  const getSpecialtyIcon = (specialty: string) => {
    switch (specialty) {
      case "ações":
        return <BarChart4 className="h-4 w-4" />
      case "bonds":
        return <Building className="h-4 w-4" />
      case "cripto":
        return <Bitcoin className="h-4 w-4" />
      case "fundos imobiliárioss":
        return <Home className="h-4 w-4" />
      case "commodities":
        return <Globe className="h-4 w-4" />
      case "etf":
        return <PieChart className="h-4 w-4" />
      default:
        return <Briefcase className="h-4 w-4" />
    }
  }


  return (
    <div className='z-40  mt-[90px] flex flex-col gap-4 p-4 text-center text-white'>
     <div className="flex items-center justify-end w-full mb-4">
     <button  className="flex py-2 px-6 rounded-sm items-center text-sm bg-blue-900 text-white hover:bg-blue-800 ">
        <Plus className="h-4 w-4 mr-1" />
        Novo
      </button>
     </div>
     <div className="grid grid-cols-6 gap-6 w-full mb-4 mt-9">
     {consultants.map((consultant) => (
     
      <CardManager
            key={consultant.id}
            id={consultant.id}
            name={consultant.name}
            about={consultant.specialty}
            imageUrl={`http://localhost:8000${consultant.avatar}`}   
            asset={consultant.asset}       
            likes="25.6k"
            comments="18.2k"
            shares="15.4k"
          />
     ))}
     </div>
     
   
     <div className="flex mt-6   text-black ">
   
      {/*
        <div className="w-1/5  shadow pr-4">
        <ScrollArea className="h-[calc(100vh-14rem)]">
              <div className="p-4 space-y-3">
                {consultants.map((consultant) => (
                  <Card
                    key={consultant.id}
                    className={`cursor-pointer hover:border-primary transition-colors ${
                      activeConsultant === consultant.id ? "border-primary" : ""
                    }`}
                    onClick={() => setActiveConsultant(consultant.id)}
                  >
                    <CardContent className="p-4">
                      <div className="flex items-start gap-3">
                      <Avatar className="h-12 w-12 bg-gray-200 text-sm flex items-center justify-center rounded-full">
                      {consultant.avatar ? (
                        <AvatarImage src={`http://localhost:8000${consultant.avatar}`} alt={consultant.name} className="h-12 w-12 rounded-full z-40" />
                      ) : (
                        <AvatarFallback>
                          {consultant.name
                            .split(" ")
                            .map((n) => n[0])
                            .join("")}
                        </AvatarFallback>
                      )}
                    </Avatar>
                        <div className="flex-1 min-w-0">
                          <div className="flex items-center justify-between">
                            <h3 className="font-medium truncate text-sm">{consultant.name}</h3>
                            <Badge variant="outline" className="ml-2 flex items-center gap-1">
                              {getSpecialtyIcon(consultant.specialty)}
                              <span className="capitalize">{consultant.specialty}</span>
                            </Badge>
                          </div>
                          <p className="text-sm text-muted-foreground">{consultant.title}</p>
                          <div className="flex items-center mt-1 text-sm">
                            <div className="flex items-center text-amber-500">
                              <Star className="h-3 w-3 fill-current" />
                              <span className="ml-1 text-xs">{consultant.rating}</span>
                            </div>
                            <span className="mx-1 text-muted-foreground text-xs">•</span>
                            <span className="text-xs text-muted-foreground">{consultant.experience}</span>
                          </div>
                        </div>
                      </div>
                    </CardContent>
                  </Card>
                ))}
              </div>
            </ScrollArea>  
        </div>
        
        <div className="w-4/5 shadow">
              
          {activeConsultant ? (
            <div className="flex-1 flex flex-col h-[calc(100vh-3.5rem)]">
           
              <div className="border-b p-4 flex items-center justify-between">
                <div className="flex items-center gap-3">
                  <Button variant="ghost" size="icon" className="md:hidden" onClick={() => setActiveConsultant(null)}>
                    <ChevronRight className="h-5 w-5" />
                  </Button>
                  <Avatar className="h-10 w-10 bg-gray-200 text-sm flex items-center justify-center rounded-full">
                  {selectedConsultant.avatar ? (
                        <AvatarImage src={`http://localhost:8000/${selectedConsultant.avatar}`} alt={selectedConsultant.name} className="h-full w-full rounded-full" />
                      ) : (
                        <AvatarFallback>
                          {selectedConsultant.name
                            .split(" ")
                            .map((n) => n[0])
                            .join("")}
                        </AvatarFallback>
                      )}
                  </Avatar>
                  <div>
                    <h3 className="font-medium">{selectedConsultant?.name}</h3>
                    <p className="text-xs text-muted-foreground">{selectedConsultant?.title}</p>
                  </div>
                </div>
                <div className="flex items-center gap-2">
                  <DropdownMenu>
                    <DropdownMenuTrigger asChild>
                      <Button variant="ghost" size="icon">
                        <Settings className="h-4 w-4" />
                      </Button>
                    </DropdownMenuTrigger>
                    <DropdownMenuContent align="end">
                      <DropdownMenuLabel>Consultant Options</DropdownMenuLabel>
                      <DropdownMenuSeparator />
                      <DropdownMenuItem>
                        <Users className="mr-2 h-4 w-4" />
                        View Profile
                      </DropdownMenuItem>
                      <DropdownMenuItem>
                        <Edit className="mr-2 h-4 w-4" />
                        Customize Responses
                      </DropdownMenuItem>
                      <DropdownMenuItem>
                        <Clock className="mr-2 h-4 w-4" />
                        View Chat History
                      </DropdownMenuItem>
                      <DropdownMenuSeparator />
                      <DropdownMenuItem className="text-red-500">
                        <Trash2 className="mr-2 h-4 w-4" />
                        Clear Conversation
                      </DropdownMenuItem>
                    </DropdownMenuContent>
                  </DropdownMenu>
                </div>
              </div>

        
              <ScrollArea className="flex-1 p-4">
                <div className="space-y-4">
                  {messages.map((message, index) => (
                    <div key={index} className={`flex ${message.role === "user" ? "justify-end" : "justify-start"}`}>
                      <div
                        className={`max-w-[80%] rounded-lg p-3 ${
                          message.role === "user" ? "bg-primary text-primary-foreground" : "bg-muted"
                        }`}
                      >
                        <p className="text-sm">{message.content}</p>
                        <p className="text-xs mt-1 opacity-70">
                          {message.timestamp.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" })}
                        </p>
                      </div>
                    </div>
                  ))}
                  <div ref={messagesEndRef} />
                </div>
              </ScrollArea>

       
              <div className="border-t p-4">
                <div className="flex items-center gap-2">
                  <Input
                    placeholder="Type your message..."
                    value={inputMessage}
                    onChange={(e) => setInputMessage(e.target.value)}
                    onKeyDown={handleKeyPress}
                    className="flex-1"
                  />
                  <Button size="icon" onClick={handleSendMessage} disabled={!inputMessage.trim()}>
                    <Send className="h-4 w-4" />
                  </Button>
                </div>
                <div className="mt-2 flex items-center justify-between">
                  <div className="flex items-center text-xs text-muted-foreground">
                    <Sparkles className="h-3 w-3 mr-1" />
                    <span>AI-powered investment advice</span>
                  </div>
                  <Button variant="ghost" size="sm" className="h-6 text-xs">
                    Suggested Questions
                  </Button>
                </div>
              </div>
            </div>
          ) : (
            <div className="flex-1 flex items-center justify-center p-8 h-screen">
              <div className="text-center max-w-md">
                <MessageSquare className="h-12 w-12 mx-auto mb-4 text-muted-foreground" />
                <h2 className="text-2xl font-bold mb-2">Select a Consultant</h2>
                <p className="text-muted-foreground mb-6">
                  Choose an investment consultant from the list to get personalized advice for your financial goals.
                </p>
                <div className="grid grid-cols-3 gap-4 mb-6">
                  <div className="text-center">
                    <BarChart4 className="h-8 w-8 mx-auto mb-2 text-primary" />
                    <p className="text-sm font-medium">Stocks</p>
                  </div>
                  <div className="text-center">
                    <Building className="h-8 w-8 mx-auto mb-2 text-primary" />
                    <p className="text-sm font-medium">Bonds</p>
                  </div>
                  <div className="text-center">
                    <Bitcoin className="h-8 w-8 mx-auto mb-2 text-primary" />
                    <p className="text-sm font-medium">Crypto</p>
                  </div>
                </div>
                <Button>
                  <Plus className="h-4 w-4 mr-2" />
                  Create Custom Consultant
                </Button>
              </div>
            </div>
          )}
        </div>
        */}
      </div>
      {children}
    </div>
  )
}

export default page