import Portifolio from "@/app/dashboard/_componentes/Portifolio"

const total = 594.2
const Rentavel = 434
const convertToPercent = (val, total) => {
  return ((val / total) * 100).toFixed(1)
}
export const data = {
  Portifolio: [
    {
      id: 'Renda Fixa',
      label: 'Renda Fixa',
      value: convertToPercent(228.8, total),
    },
    {
      id: 'Ações',
      label: 'Ações',
      value: convertToPercent(100.6, total),
    },
    {
      id: 'Fundos Imobiliarios',
      label: 'Fundos',
      value: convertToPercent(74.3, total),
    },
    {
      id: 'Crypto',
      label: 'Crypto',
      value: convertToPercent(74.4, total),
    },
    {
      id: 'Opções',
      label: 'Opções',
      value: convertToPercent(59.5, total),
    },
    {
      id: 'Cambio',
      label: 'Cambio',
      value: convertToPercent(56.6, total),
    },
  ],
  Semanal: [
    {
      id: 'Renda Fixa',
      label: 'Renda Fixa',
      value: convertToPercent(134, Rentavel),
    },
    {
      id: 'Ações',
      label: 'Ações',
      value: convertToPercent(97, Rentavel),
    },
    {
      id: 'Fundos Imobiliarios',
      label: 'Fundos',
      value: convertToPercent(60, Rentavel),
    },
    {
      id: 'Cripto',
      label: 'Cripto',
      value: convertToPercent(46, Rentavel),
    },
    {
      id: 'Opções',
      label: 'Opções',
      value: convertToPercent(60, Rentavel),
    },
    {
      id: 'Cambio',
      label: 'Cambio',
      value: convertToPercent(37, Rentavel),
    },
  ],
}



