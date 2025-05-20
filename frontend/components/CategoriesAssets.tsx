"use client"

import { useState } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { Check } from 'lucide-react'
import { Badge } from './ui/badge'

const cuisines = [
    {
      "id": 1,
      "name": "Ações"
    },
    {
      "id": 2,
      "name":"Commodities",
    },
    {
      "id": 3,
      "name":"Moedas"
    },
    {
      "id": 4,
      "name":"Indices"
    },
    {
      "id": 5,
      "name":"CriptoMoedas"
    },
]

const CategoriesAssets = ({ items }) => {
    const [selected, setSelected] = useState<string[]>([])

    const toggleCuisine = (item: string) => {
        setSelected((prev) =>
            prev.includes(item)
                ? prev.filter((c) => c !== item) // Remove o item se já estiver selecionado
                : [...prev, item] // Adiciona o item à lista se não estiver selecionado
        )
    }

    return (
        <div className="mt-10">
            <h3 className="font-medium mb-3">Ativos do {items.name}</h3>
            <div className="flex flex-wrap gap-2 text-xs">
                {items.asset?.map((item, i) => (
                    <button
                        key={i}
                        className={`flex items-center justify-center gap-2 py-1 px-2 rounded-full ${selected.includes(item) ? 'bg-green-500 text-white ' : 'border'}`} // Aplica estilo diferente se o item estiver selecionado
                        onClick={() => toggleCuisine(item)}
                    >
                        <span>{item}</span>
                        {selected.includes(item) && <Check size={16} />}
                    </button>
                ))}
            </div>
        </div>
    )
}

export default CategoriesAssets
