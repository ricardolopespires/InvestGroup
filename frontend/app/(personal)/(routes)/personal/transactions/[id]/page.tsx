"use client"
import { FaWallet, FaChild,FaCreditCard, FaDollarSign, FaBarcode, FaHandHoldingUsd,FaRegCreditCard, FaCashRegister, FaCar, FaPlaystation     } from "react-icons/fa";
import { useRouter, usePathname, useSearchParams } from 'next/navigation'
import Menu from "../../components/menu";
import React from 'react'


const page = () => {

    const router = useRouter();
    const pathname = usePathname()
    const searchParams = useSearchParams()

    const url = `${pathname}?${searchParams}`

  return(
    
    <div className='absolute inset-x-0 top-[140px] h-full px-20'>
    <div className='flex flex-col '>
    <div className="flex items-center space-x-1">
    <div className="text-3xl text-yellow-500 mr-2"><FaWallet /></div>
    <h1 className='text-2xl text-white'>Finanças pessoais</h1>
    </div>
    <p className='text-gray-500 '>Tomar decisões financeiras começa com  a administração do seu próprio dinheiro.</p>
    </div>
    <Menu/>
    <div className=" mx-auto py-16 bg-white mt-10 rounded-xl shadow-2xl bottom-10">
  <article className="overflow-hidden">
   <div className="bg-[white] rounded-b-md">
    <div className="p-9">
     <div className="space-y-6 text-slate-700">
      <img className="object-cover h-12" src="/images/logo.png" />

      <p className="text-xl font-extrabold tracking-tight uppercase font-body">
       Unwrapped.design
      </p>
     </div>
    </div>
    <div className="p-9">
     <div className="flex w-full">
      <div className="grid grid-cols-4 gap-12">
       <div className="text-sm font-light text-slate-500">
        <p className="text-sm font-normal text-slate-700">
         Invoice Detail:
        </p>
        <p>Unwrapped</p>
        <p>Fake Street 123</p>
        <p>San Javier</p>
        <p>CA 1234</p>
       </div>
       <div className="text-sm font-light text-slate-500">
        <p className="text-sm font-normal text-slate-700">Billed To</p>
        <p>The Boring Company</p>
        <p>Tesla Street 007</p>
        <p>Frisco</p>
        <p>CA 0000</p>
       </div>
       <div className="text-sm font-light text-slate-500">
        <p className="text-sm font-normal text-slate-700">Invoice Number</p>
        <p>000000</p>

        <p className="mt-2 text-sm font-normal text-slate-700">
         Date of Issue
        </p>
        <p>00.00.00</p>
       </div>
       <div className="text-sm font-light text-slate-500">
        <p className="text-sm font-normal text-slate-700">Terms</p>
        <p>0 Days</p>

        <p className="mt-2 text-sm font-normal text-slate-700">Due</p>
        <p>00.00.00</p>
       </div>
      </div>
     </div>
    </div>

    <div className="p-9">
     <div className="flex flex-col mx-0 mt-8">
      <table className="min-w-full divide-y divide-slate-500">
       <thead>
        <tr>
         <th scope="col" className="py-3.5 pl-4 pr-3 text-left text-sm font-normal text-slate-700 sm:pl-6 md:pl-0">
          Description
         </th>
         <th scope="col" className="hidden py-3.5 px-3 text-right text-sm font-normal text-slate-700 sm:table-cell">
          Quantity
         </th>
         <th scope="col" className="hidden py-3.5 px-3 text-right text-sm font-normal text-slate-700 sm:table-cell">
          Rate
         </th>
         <th scope="col" className="py-3.5 pl-3 pr-4 text-right text-sm font-normal text-slate-700 sm:pr-6 md:pr-0">
          Amount
         </th>
        </tr>
       </thead>
       <tbody>
        <tr className="border-b border-slate-200">
         <td className="py-4 pl-4 pr-3 text-sm sm:pl-6 md:pl-0">
          <div className="font-medium text-slate-700">Tesla Truck</div>
          <div className="mt-0.5 text-slate-500 sm:hidden">
           1 unit at $0.00
          </div>
         </td>
         <td className="hidden px-3 py-4 text-sm text-right text-slate-500 sm:table-cell">
          48
         </td>
         <td className="hidden px-3 py-4 text-sm text-right text-slate-500 sm:table-cell">
          $0.00
         </td>
         <td className="py-4 pl-3 pr-4 text-sm text-right text-slate-500 sm:pr-6 md:pr-0">
          $0.00
         </td>
        </tr>
        <tr className="border-b border-slate-200">
         <td className="py-4 pl-4 pr-3 text-sm sm:pl-6 md:pl-0">
          <div className="font-medium text-slate-700">
           Tesla Charging Station
          </div>
          <div className="mt-0.5 text-slate-500 sm:hidden">
           1 unit at $75.00
          </div>
         </td>
         <td className="hidden px-3 py-4 text-sm text-right text-slate-500 sm:table-cell">
          4
         </td>
         <td className="hidden px-3 py-4 text-sm text-right text-slate-500 sm:table-cell">
          $0.00
         </td>
         <td className="py-4 pl-3 pr-4 text-sm text-right text-slate-500 sm:pr-6 md:pr-0">
          $0.00
         </td>
        </tr>

      
       </tbody>
       <tfoot>
        <tr>
         <th scope="row" colspan="3" className="hidden pt-6 pl-6 pr-3 text-sm font-light text-right text-slate-500 sm:table-cell md:pl-0">
          Subtotal
         </th>
         <th scope="row" className="pt-6 pl-4 pr-3 text-sm font-light text-left text-slate-500 sm:hidden">
          Subtotal
         </th>
         <td className="pt-6 pl-3 pr-4 text-sm text-right text-slate-500 sm:pr-6 md:pr-0">
          $0.00
         </td>
        </tr>
        <tr>
         <th scope="row" colspan="3" className="hidden pt-6 pl-6 pr-3 text-sm font-light text-right text-slate-500 sm:table-cell md:pl-0">
          Discount
         </th>
         <th scope="row" className="pt-6 pl-4 pr-3 text-sm font-light text-left text-slate-500 sm:hidden">
          Discount
         </th>
         <td className="pt-6 pl-3 pr-4 text-sm text-right text-slate-500 sm:pr-6 md:pr-0">
          $0.00
         </td>
        </tr>
        <tr>
         <th scope="row" colspan="3" className="hidden pt-4 pl-6 pr-3 text-sm font-light text-right text-slate-500 sm:table-cell md:pl-0">
          Tax
         </th>
         <th scope="row" className="pt-4 pl-4 pr-3 text-sm font-light text-left text-slate-500 sm:hidden">
          Tax
         </th>
         <td className="pt-4 pl-3 pr-4 text-sm text-right text-slate-500 sm:pr-6 md:pr-0">
          $0.00
         </td>
        </tr>
        <tr>
         <th scope="row" colspan="3" className="hidden pt-4 pl-6 pr-3 text-sm font-normal text-right text-slate-700 sm:table-cell md:pl-0">
          Total
         </th>
         <th scope="row" className="pt-4 pl-4 pr-3 text-sm font-normal text-left text-slate-700 sm:hidden">
          Total
         </th>
         <td className="pt-4 pl-3 pr-4 text-sm font-normal text-right text-slate-700 sm:pr-6 md:pr-0">
          $0.00
         </td>
        </tr>
       </tfoot>
      </table>
     </div>
    </div>

    <div className="mt-48 p-9">
     <div className="border-t pt-9 border-slate-200">
      <div className="text-sm font-light text-slate-700">
       <p>
       As condições de pagamento são de 14 dias. Esteja ciente de que,
       de acordo com a Lei 0000 de Pagamento Atrasado de Dívidas Não Embrulhadas,
       os freelancers têm direito a reivindicar uma taxa de atraso de 00,00 em caso de
       não pagamento de dívidas após esse período, momento em que uma nova fatura será 
       apresentada com o acréscimo desta taxa. Se o pagamento da fatura revisada não for
       recebido dentro de mais 14 dias, serão cobrados juros adicionais na conta vencida e 
       uma taxa legal de 8% mais a base do Banco da Inglaterra de 0,5%, totalizando 8,5%. 
       As partes não podem contratar fora das disposições da lei..
       </p>
      </div>
     </div>
    </div>
   </div>
  </article>
 </div>
    </div>
    
    )
}

export default page