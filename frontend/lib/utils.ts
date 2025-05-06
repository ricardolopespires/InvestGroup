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