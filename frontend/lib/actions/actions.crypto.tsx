import axios from "axios"; // Corrigido 'import' removendo espaço extra
import { parseStringify } from "../utils";
import { CryptoAsset } from "@/types/types";



import { AxiosResponse } from 'axios';

// Interface para tipar os dados retornados pela API
interface CryptoAsset {
  id: string;
  symbol: string;
  name: string;
  current_price: number;
  market_cap: number;
  total_volume: number;
  price_change_percentage_24h: number;
  [key: string]: any; // Para permitir outras propriedades dinâmicas
}

// Função para obter a lista de ativos de criptomoedas
export const getAssetCryptos = async (): Promise<CryptoAsset[] | string> => {
  try {
    const allCryptos: CryptoAsset[] = [];
    const coinsPerPage = 250; // Máximo de moedas por página permitido pela API do CoinGecko
    const totalCoinsDesired = 1000; // Quantidade mínima de moedas desejada
    const totalPages = Math.ceil(totalCoinsDesired / coinsPerPage); // Calcula o número de páginas necessárias

    // Loop para buscar múltiplas páginas até atingir o mínimo de 500 coins
    for (let page = 1; page <= totalPages; page++) {
      const res: AxiosResponse<CryptoAsset[]> = await axios.get(
        'https://api.coingecko.com/api/v3/coins/markets',
        {
          params: {
            vs_currency: 'usd', // Moeda para conversão (USD)
            order: 'market_cap_desc', // Ordena por capitalização de mercado
            per_page: coinsPerPage, // Define o número de moedas por página
            page, // Página atual
            sparkline: false, // Desativa dados de sparkline para reduzir o tamanho da resposta
          },
          headers: {
            // Adiciona cabeçalho para evitar bloqueios por limite de requisições (caso necessário)
            'Accept': 'application/json',
          },
          timeout: 10000, // Define um timeout de 10 segundos para evitar travamentos
        }
      );

      // Adiciona os dados retornados ao array principal
      allCryptos.push(...res.data);

      // Verifica se já atingiu o número mínimo de coins desejado
      if (allCryptos.length >= totalCoinsDesired) {
        break;
      }
    }

    // Garante que apenas os primeiros 500 coins sejam retornados, caso tenha mais
    return allCryptos.slice(0, totalCoinsDesired);
  } catch (error) {
    // Tratamento detalhado de erros
    if (axios.isAxiosError(error)) {
      // Erros específicos do Axios (ex.: problemas de rede, timeout, etc.)
      return `Erro ao buscar dados da API: ${error.message}`;
    } else if (error instanceof Error) {
      // Outros erros genéricos
      return `Erro inesperado: ${error.message}`;
    } else {
      // Erros desconhecidos
      return 'Erro desconhecido ao buscar dados da API';
    }
  }
};

// Exemplo de uso (opcional, para testes)
const fetchCryptos = async () => {
  const result = await getAssetCryptos();
  if (typeof result === 'string') {
    console.error(result); // Exibe mensagem de erro, se houver
  } else {
    console.log(`Total de criptomoedas obtidas: ${result.length}`);
    console.log('Primeiras 5 criptomoedas:', result.slice(0, 5));
  }
};

// fetchCryptos(); // Descomente para testar


export const getAssetCrypto = async (id: string): Promise<CryptoAsset | string> => {
  try {
    const res: AxiosResponse<CryptoAsset> = await axios.get(
      `https://api.coingecko.com/api/v3/coins/${id}`);

      if(res.status === 200){
        res.data
      }else{
        return parseStringify({"status":400, "message": "Error "})
      }

    }catch (error) {
      return parseStringify({"status":400, "message": "Error "})
    } 
};