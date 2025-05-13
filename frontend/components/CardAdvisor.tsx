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
  } from "lucide-react";
  import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
  import { Badge } from "@/components/ui/badge";
  import { Switch } from "@/components/ui/switch";
  import React, { useEffect, useState } from 'react';
  import { getLevelAdvisors } from "@/lib/actions/actions.advisors";
  
  const CardAdvisor = ({ agent }) => {
    const [activeAgent, setActiveAgent] = useState(agent?.id || "agent_1");
    const [level, setLevel] = useState({});
    const [riskTolerance, setRiskTolerance] = useState(30);
  
    useEffect(() => {
      const fetchData = async () => {
        try {
          const res = await getLevelAdvisors({ AdvisorId: agent.id });
          setLevel(res[0] || {});
        } catch (error) {
          console.error("Error fetching advisor level:", error);
        }
      };
      if (agent?.id) {
        fetchData();
      }
    }, [agent]);
  
    const handleAgentToggle = (id, active) => {
      // In a real app, this would update the agent status
    };
  
    const handleRiskToleranceChange = (value) => {
      setRiskTolerance(value[0]);
    };
  
    const saveAgentSettings = () => {
      // In a real app, this would save the agent settings
    };
  
    if (!agent) {
      return null; // Or a fallback UI
    }
  
    return (
      <a href={`/investments/advisor/${agent.id}`}>
        <Card
          className={`cursor-pointer hover:border-blue-600 transition-colors h-[200px] `}
          onClick={() => setActiveAgent(agent.id)}
        >
          <CardContent className="p-4">
            <div className="space-y-4">
              <div className="flex items-center justify-between">
                <div className="flex items-center space-x-2">
                  <div className="bg-blue-950 p-2 rounded-sm">
                    <Bot className="h-6 w-6 text-white" />
                  </div>
                  <h3 className="font-medium">{agent.name}</h3>
                </div>
                <Switch
                  checked={agent.active}
                  onCheckedChange={(checked) => handleAgentToggle(agent.id, checked)}
                />
              </div>
  
              <p className="text-sm text-muted-foreground">{agent.description}</p>
  
              <div className="flex flex-wrap gap-2">
                {agent.preferredAssets?.map((asset) => (
                  <Badge key={asset} variant="outline">
                    {asset.charAt(0).toUpperCase() + asset.slice(1)}
                  </Badge>
                ))}
              </div>
  
              <div className="flex items-center justify-between text-sm">
                <div>
                  <span className="text-muted-foreground">Monthly: </span>
                  <span className={agent.performance?.monthly >= 0 ? "text-green-500" : "text-red-500"}>
                    {agent.performance?.monthly >= 0 ? "+" : ""}
                    {agent.performance?.monthly ?? 0}%
                  </span>
                </div>
                <div>
                  <span className="text-muted-foreground">All-time: </span>
                  <span className={agent.performance?.allTime >= 0 ? "text-green-500" : "text-red-500"}>
                    {agent.performance?.allTime >= 0 ? "+" : ""}
                    {agent.performance?.allTime ?? 0}%
                  </span>
                </div>
              </div>
            </div>
          </CardContent>
        </Card>
      </a>
    );
  };
  
  export default CardAdvisor;