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
