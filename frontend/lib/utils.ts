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