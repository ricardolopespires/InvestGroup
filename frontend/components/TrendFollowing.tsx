import {
    Card,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle,
  } from "@/components/ui/card";
  import {
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
  } from "@/components/ui/table";
  import { getTrendFollowingStocks } from "@/lib/actions/actions.stock";
import { cn, timeDifferences } from "@/lib/utils";
  import React, { useEffect, useState } from "react";
import { symbol } from "zod";
  
  interface TrendSignal {
    timeFrame: string;
    time: string;
    price: number;
    signal: string;
  }
  
  interface TrendFollowingProps {
    symbol: string;
    UserId: string;

  }


  const TrendFollowing: React.FC<TrendFollowingProps> = ({ symbol, UserId }) => {
    const [signal, setSignal] = useState<TrendSignal[]>([]);
    const [loading, setLoading] = useState<boolean>(true);
    const [error, setError] = useState<string | null>(null);
  
    useEffect(() => {
      const fetchData = async () => {
        try {
        
          const res = await getTrendFollowingStocks({
            symbol: symbol,
            UserId: UserId,
          });        
  
          setSignal(res.signals);
          setError(null);
        } catch (err) {
          setError(err instanceof Error ? err.message : "Erro ao buscar dados.");
        } finally {
          setLoading(false);
        }
      };
  
      fetchData();
    }, [symbol, UserId]); // `user` não precisa estar na lista de dependências, pois vem do localStorage
  
    if (loading) {
      return (
        <Card className="w-full">
          <CardHeader>
            <CardTitle>Seguindo Tendências</CardTitle>
            <CardDescription>Carregando dados...</CardDescription>
          </CardHeader>
        </Card>
      );
    }
  
    if (error) {
      return (
        <Card className="w-full">
          <CardHeader>
            <CardTitle>Seguindo Tendências</CardTitle>
            <CardDescription>Erro: {error}</CardDescription>
          </CardHeader>
        </Card>
      );
    }
  
    return (
      <Card className="w-full">
        <CardHeader>
          <CardTitle>Seguindo Tendências</CardTitle>
          <CardDescription>
            Como grandes traders ganham milhões em mercados em alta ou em baixa.
          </CardDescription>
        </CardHeader>
        <CardContent>
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>TimeFrame</TableHead>
                <TableHead>Tempo</TableHead>
                <TableHead>Preço</TableHead>
                <TableHead>Signal</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {signal?.length > 0 ? (
                signal?.map((item, index) => (
                  <TableRow key={index}>
                    <TableCell className="font-medium">
                      {item.timeframe}
                    </TableCell>
                    <TableCell>{timeDifferences(item.time)}</TableCell>
                    <TableCell>{item.price.toFixed(2)}</TableCell>
                    <TableCell>
                        <div className={cn("h-5 w-16 rounded-sm flex items-center justify-center text-white", item.signal === "buy" ? "bg-green-500" : "bg-red-500")}>
                            {item.signal.toUpperCase()}
                        </div>
                    </TableCell>
                  </TableRow>
                ))
              ) : (
                <TableRow>
                  <TableCell colSpan={4} className="text-center">
                    Nenhum dado disponível.
                  </TableCell>
                </TableRow>
              )}
            </TableBody>
          </Table>
        </CardContent>
      </Card>
    );
  };
  
  export default TrendFollowing;