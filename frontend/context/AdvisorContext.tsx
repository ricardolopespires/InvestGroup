// context/AdvisorContext.tsx
import { createContext, useState, useEffect, ReactNode } from 'react';
import axios from 'axios';

// Definindo tipos para o contexto
interface AdvisorContextType {
  operation: string | null;
  signal: string | null;
  interval: number;
  setInterval: (newInterval: number) => void;
  loading: boolean;
  error: string | null;
}

// Criando o contexto com valor inicial vazio
export const AdvisorContext = createContext<AdvisorContextType>({} as AdvisorContextType);

// Props do Provider
interface AdvisorProviderProps {
  children: ReactNode;
}

export const AdvisorProvider = ({ children }: AdvisorProviderProps) => {
  const [operation, setOperation] = useState<string | null>(null);
  const [signal, setSignal] = useState<string | null>(null);
  const [interval, setIntervalState] = useState<number>(() => {
    if (typeof window !== 'undefined') {
      const saved = localStorage.getItem('advisorInterval');
      return saved ? parseInt(saved, 10) : 5000;
    }
    return 5000;
  });
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  const setInterval = (newInterval: number) => {
    setIntervalState(newInterval);
    if (typeof window !== 'undefined') {
      localStorage.setItem('advisorInterval', newInterval.toString());
    }
  };

  const fetchData = async () => {
    setLoading(true);
    setError(null);
    try {
      const [operationRes, signalRes] = await Promise.all([
        axios.get<{ operation: string }>('http://localhost:8000/api/open-operations/'),
        axios.get<{ signal: string }>('http://localhost:8000/api/signals/'),
      ]);
      setOperation(operationRes.data.operation);
      setSignal(signalRes.data.signal);
    } catch (err) {
      setError('Não foi possível conectar à API');
      console.error('Erro ao buscar dados:', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
    const timer = setInterval(fetchData, interval);
    return () => clearInterval(timer);
  }, [interval]);

  return (
    <AdvisorContext.Provider value={{ operation, signal, interval, setInterval, loading, error }}>
      {children}
    </AdvisorContext.Provider>
  );
};