import { useState } from 'react'
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Select } from "@/components/ui/select"




import React from 'react'

const Boleta = () => {
    const [price, setPrice] = useState('102.000')
    const [stopOrder, setStopOrder] = useState('150')
    const [quantity, setQuantity] = useState('1')
  
    return (
      <div className="w-full h-[784px] bg-[#151928] text-white p-4 s">
        <div className="flex justify-between items-center mb-4">
          <h2 className="text-lg font-bold">Simulador 70361</h2>
          <span className="text-gray-400">🔒</span>
        </div>
        
        <div className="space-y-2 mb-4">
          <div className="flex justify-between">
            <label>Estrat.</label>
            <Select>
              <option>&lt;Nenhuma&gt;</option>
            </Select>
          </div>
          <div className="flex justify-between items-center">
            <label>Preço</label>
            <Input 
              type="number" 
              value={price} 
              onChange={(e) => setPrice(e.target.value)}
              className="w-24 bg-gray-700"
            />
          </div>
          <div className="flex justify-between items-center">
            <label>Stop Of.</label>
            <Input 
              type="number" 
              value={stopOrder} 
              onChange={(e) => setStopOrder(e.target.value)}
              className="w-24 bg-gray-700"
            />
          </div>
          <div className="flex justify-between items-center">
            <label>Qtd</label>
            <Input 
              type="number" 
              value={quantity} 
              onChange={(e) => setQuantity(e.target.value)}
              className="w-24 bg-gray-700"
            />
          </div>
        </div>
        
        <div className="grid grid-cols-3 gap-2 mb-4">
          {[1, 2, 3].map((num) => (
            <Button key={num} variant="outline" className="bg-gray-700">
              {num}
            </Button>
          ))}
        </div>
        
        <div className="flex justify-between items-center mb-4">
          <label>Total</label>
          <span className="font-bold">R$ 20.400,00</span>
        </div>
        
        <div className="grid grid-cols-2 gap-2 mb-4">
          <Button className="bg-yellow-500 text-black">C Limite</Button>
          <Button className="bg-green-500">V Stop</Button>
          <Button className="bg-yellow-500 text-black">C Mercado</Button>
          <Button className="bg-green-500">V Mercado</Button>
        </div>
        
        <div className="space-y-2">
          <Button variant="outline" className="w-full bg-gray-700">Cancel Ord.</Button>
          <Button variant="outline" className="w-full bg-gray-700">Inverter</Button>
          <Button variant="outline" className="w-full bg-gray-700">Zerar</Button>
          <Button className="w-full bg-red-500">Cancelar ordens + Zerar</Button>
        </div>
        
        <div className="mt-4">
          <h3 className="font-bold mb-2">Resultado</h3>
          <div className="flex justify-between">
            <span>Res. Aberto</span>
            <span>0,00</span>
          </div>
          <div className="flex justify-between">
            <span>Res. do Dia</span>
            <span className="text-green-500">R$ 6,50</span>
          </div>
          <div className="flex justify-between">
            <span>Médio</span>
            <span>R$ 0,00</span>
          </div>
        </div>
      </div>
    )
  }

export default Boleta