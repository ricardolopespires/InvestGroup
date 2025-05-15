import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { toCapitalizer } from "@/lib/utils"
import React, { useEffect, useState } from 'react'
import CardRecommendations from "./CardRecommendations"
import { getRecommendations } from "@/lib/actions/actions.agents"

const Recommendations = ({ asset }) => {
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const user = JSON.parse(localStorage.getItem('user'));

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const res = await getRecommendations({ userId: user?.email, asset });
        setRecommendations(res || []);
      } catch (err) {
        setError('Erro ao carregar recomendações');
      } finally {
        setLoading(false);
      }
    };

    if (user?.email && asset) {
      fetchData();
    } else {
      setLoading(false);
      setError('Usuário ou ativo não encontrado');
    }
  }, [asset, user]);

  return (
    <div className="flex-1 p-6">
      <section className="mb-10">
        <h1 className="text-3xl font-semibold mb-2">Recomendações de Investimento</h1>
        <p>
          Oportunidades de investimento em{' '}
          <strong className="text-blue-600">{toCapitalizer(asset)}</strong>{' '}
          com personalização com base em análises de mercado e perfis de risco.
        </p>

        {error ? (
          <div className="text-center text-red-600 py-8">
            {error}
          </div>
        ) : recommendations.length === 0 ? (
          <div className="text-center text-gray-600 py-8">
            Nenhuma recomendação disponível para {toCapitalizer(asset)} no momento.
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mb-6 mt-9">
            {recommendations?.map((item, i) => (
              <CardRecommendations
                key={i}
                asset={item.name || "AMZON"}
                symbol={item.symbol || "AMZN"}
                logo={item.img_url || "https://logospng.org/download/amazon/logo-amazon-4096.png"}
                timeToBuy={item.timeToBuy || "7:00:00"}
                price={item.price || "350,00"}
                timeframe={item.timeframe || "9%"}
                signal_time={item.signal_time || "00"}
                signal={item.signal || "sell"}
              />
            ))}
          </div>
        )}
      </section>
    </div>
  );
};

export default Recommendations;