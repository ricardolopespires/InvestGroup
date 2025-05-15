"use client";

import React, { useState, useRef, useEffect } from "react";
import { Button } from "@/components/ui/button";
import { ScrollArea,  } from "@radix-ui/react-scroll-area"; // Corrected import
import { Input } from "@/components/ui/input";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Settings, Send, Trash2, Users, Edit, Clock, Sparkles } from "lucide-react"; // Only import used icons
import { getConsultants } from "@/lib/actions/actions.agents";

// Define the Agent type for the prop
interface Agent {
  id: string;
  specialty: string;
  name: string;
  // Add other relevant fields as needed
}

interface ChartsConsultantsProps {
  agent: Agent;
}

const ChartsConsultants = ({ agent }: ChartsConsultantsProps) => {
  const [messages, setMessages] = useState<
    { role: string; content: string; timestamp: Date }[]
  >([]);
  const [inputMessage, setInputMessage] = useState("");
  const messagesEndRef = useRef<HTMLDivElement>(null);

  // Auto-scroll to the bottom when new messages are added
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  // Fetch consultants (example usage, adjust based on your needs)
  useEffect(() => {
    const fetchConsultants = async () => {
      try {
        const consultants = await getConsultants();
        // Optionally set consultants state if needed
        // setConsultants(consultants);
      } catch (error) {
        console.error("Failed to fetch consultants:", error);
      }
    };
    fetchConsultants();
  }, []);

  const handleSendMessage = () => {
    if (!inputMessage.trim()) return;

    // Add user message
    const newMessages = [
      ...messages,
      { role: "user", content: inputMessage, timestamp: new Date() },
    ];
    setMessages(newMessages);
    setInputMessage("");

    // Simulate consultant response
    setTimeout(() => {
      const responses = [
        `Based on your interest in ${agent.specialty}, I'd recommend considering a diversified approach. Would you like me to elaborate on specific strategies?`,
        `That's a great question about ${agent.specialty}. The current market conditions suggest caution, but there are still opportunities in select areas.`,
        `When investing in ${agent.specialty}, it's important to consider your time horizon and risk tolerance. Have you defined your investment goals?`,
        `I've analyzed recent trends in ${agent.specialty} markets, and there are several promising developments. Would you like me to share my top recommendations?`,
        `For your ${agent.specialty} portfolio, I'd suggest allocating across different sub-sectors to minimize risk while maximizing potential returns.`,
      ];

      const randomResponse =
        responses[Math.floor(Math.random() * responses.length)];

      setMessages((prev) => [
        ...prev,
        { role: "assistant", content: randomResponse, timestamp: new Date() },
      ]);
    }, 1000);
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  return (
    <div className="flex-1 flex flex-col h-[790px]">
      <div className="flex items-center justify-between p-4">
        <div />
        <div className="flex items-center">
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
            <div
              key={index}
              className={`flex ${
                message.role === "user" ? "justify-end" : "justify-start"
              }`}
            >
              <div
                className={`max-w-[80%] rounded-lg p-3 ${
                  message.role === "user"
                    ? "bg-primary text-primary-foreground"
                    : "bg-muted"
                }`}
              >
                <p className="text-sm">{message.content}</p>
                <p className="text-xs mt-1 opacity-70">
                  {message.timestamp.toLocaleTimeString([], {
                    hour: "2-digit",
                    minute: "2-digit",
                  })}
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
          <Button
            size="icon"
            onClick={handleSendMessage}
            disabled={!inputMessage.trim()}
          >
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
  );
};

export default ChartsConsultants;