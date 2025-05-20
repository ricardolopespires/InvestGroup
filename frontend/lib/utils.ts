import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}


export const parseStringify = (value: any) => JSON.parse(JSON.stringify(value));



export function transformData(inputData: InputData[]): OutputData[] {
  return inputData.map(item => ({
      open: item.open,
      high: item.high,
      low: item.low,
      close: item.close,
      time: parseInt(item.time) // Convertendo string para número
  }));
}


export function timeDifferences(dateStr: string): string {
  const inputDate = new Date(dateStr);
  const now = new Date();

  const diffMs = now.getTime() - inputDate.getTime();
  const diffHours = diffMs / (1000 * 60 * 60);
  const diffDays = Math.floor(diffHours / 24);

  if (diffDays >= 1) {
    return `${diffDays} dias`;
  } else {
    return `${Math.floor(diffHours)} hora(s)`;
  }
}


export function formatDayAndMonth(createdAt: string): string {
  const date = new Date(createdAt);

  const day = date.getDate();
  const month = date.toLocaleString('pt-BR', { month: 'long' }) // "April"
  const year = date.getFullYear();

  return `${day} ${month} ${year}`;
}

; // Saída: "15 April"



// Formatter for BRL currency
export const formatBRL = (value: number): string =>
  // new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(value);

  new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(value);

// Formatter for percentage
export const formatPercentage = (value: number): string =>
  new Intl.NumberFormat('pt-BR', { style: 'percent', minimumFractionDigits: 2 }).format(value / 100);

// Formatter for minutes to min:ss
export const formatMinutes = (minutes: number): string => {
  if (isNaN(minutes) || minutes === 0) return '0min0s';
  const mins = Math.floor(minutes);
  const secs = Math.round((minutes - mins) * 60);
  return `${mins}min${secs}s`;
};

// Formatter for numbers
export const formatNumber = (value: number): string =>
  new Intl.NumberFormat('pt-BR').format(value);

export function formatNumbers(obj: any): any {
  // Itera sobre as chaves do objeto
  for (const key in obj) {
    if (typeof obj[key] === 'number') {
      // Arredonda os números para 2 casas decimais
      obj[key] = parseFloat(obj[key].toFixed(2));
    } else if (typeof obj[key] === 'object') {
      // Se o valor for um objeto, chama a função recursivamente
      formatNumbers(obj[key]);
    }
  }
  return obj;
}



export function toCapitalizer(frase: string): string {
  return frase
    .split(' ')
    .map(palavra => palavra.charAt(0).toUpperCase() + palavra.slice(1).toLowerCase())
    .join(' ');
}

export function paragraph(texto: string | undefined): string {
  if (!texto || typeof texto !== 'string') {
    throw new Error("O parâmetro 'texto' deve ser uma string válida.");
  }

  const palavras = texto.split(/\s+/);
  const blocos: string[] = [];

  for (let i = 0; i < palavras.length; i += 400) {
    const bloco = palavras.slice(i, i + 400).join(' ');
    blocos.push(bloco);
  }

  return blocos.join('\n\n'); // Dupla quebra de linha = "espaço para baixo"
}



export function calculate24HourProgress(startDate: string): number {
    // Converter a string da data para um objeto Date
    const start = new Date(startDate);
    const now = new Date();
    
    // Validar se a data é válida
    if (isNaN(start.getTime())) {
        throw new Error("Data de início inválida");
    }
    
    // Calcular a diferença em milissegundos
    const diffInMs = now.getTime() - start.getTime();
    
    // Converter 24 horas para milissegundos (24 * 60 * 60 * 1000 = 86,400,000)
    const twentyFourHoursInMs = 24 * 60 * 60 * 1000;
    
    // Calcular a porcentagem
    let percentage = (diffInMs / twentyFourHoursInMs) * 100;
    
    // Garantir que a porcentagem esteja entre 0 e 100
    percentage = Math.max(0, Math.min(100, percentage));
    
    // Arredondar para 2 casas decimais
    return Number(percentage.toFixed(2));
}


export function countdown24Hours(startDate: string): { hours: number; minutes: number; seconds: number; percentageRemaining: number } {
    // Converter a string da data para um objeto Date
    const start = new Date(startDate);
    const now = new Date();
    
    // Validar se a data é válida
    if (isNaN(start.getTime())) {
        throw new Error("Data de início inválida");
    }
    
    // Calcular o fim das 24 horas a partir da data inicial
    const end = new Date(start.getTime() + 24 * 60 * 60 * 1000);
    
    // Calcular a diferença em milissegundos
    let diffInMs = end.getTime() - now.getTime();
    
    // Se o tempo restante for negativo, retornar zeros
    if (diffInMs <= 0) {
        return { hours: 0, minutes: 0, seconds: 0, percentageRemaining: 0 };
    }
    
    // Calcular horas, minutos e segundos restantes
    const hours = Math.floor(diffInMs / (1000 * 60 * 60));
    diffInMs %= 1000 * 60 * 60;
    const minutes = Math.floor(diffInMs / (1000 * 60));
    diffInMs %= 1000 * 60;
    const seconds = Math.floor(diffInMs / 1000);
    
    // Calcular a porcentagem restante
    const twentyFourHoursInMs = 24 * 60 * 60 * 1000;
    const percentageRemaining = Number(((diffInMs / twentyFourHoursInMs) * 100).toFixed(2));
    
    return { hours, minutes, seconds, percentageRemaining };
}



export function descripton(texto: string, limite: number): string {
  if (texto.length <= limite) {
    return texto;  // Se o texto já for menor que o limite, retorna ele mesmo
  }

  return texto.slice(0, limite) + '...';  // Se o texto for maior que o limite, corta e adiciona "..."
}