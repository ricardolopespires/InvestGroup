







import React from 'react'

const Transaction = () => {
  return (
    <div className=" h-screen">
        <div className='bg-white rounded-xl p-4 h-[60%] shadow-2xl border border-gray-100 w-full'>
            <h1 className="font-semibold py-6 px-2">Histórico de transações</h1>
            <div className="block w-full overflow-x-auto ">
                    <table className="items-center w-full bg-transparent border-collapse">
                      <thead>
                        <tr>
                          <th className="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left  border-gary-700">Nome</th>
                          <th className="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left  border-gary-700">Tipo</th>
                          <th className="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left  border-gary-700">Data</th>
                          <th className="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left  border-gary-700">Valor</th>
                          <th className="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left  border-gary-700">Status</th>                         
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                        <th className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4 text-left flex items-center">
                          <img src="https://demos.creative-tim.com/notus-js/assets/img/bootstrap.jpg" className="h-12 w-12 bg-white rounded-full border" alt="..."/>
                          <span className="ml-3 font-bold "> Argon Design System </span></th>
                        <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-sm font-semibold whitespace-nowrap p-4">Inscrição</td>
                        <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">
                          <div className="flex flex-col">
                            <span className="text-md font-semibold">Oct 20,2022</span>
                            <span className="ml-2">10:40 PM</span>
                          </div>
                        </td>
                          <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">$2,500 USD</td>
                            <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"><div className="flex items-center">
                            <span className="bg-orange-500 py-1 px-6 rounded-full text-white">pendente</span>
                              </div>
                            </td>                          
                          </tr>   
                      </tbody>    
                    </table>
            </div>
        </div>
    </div>
  )
}

export default Transaction
