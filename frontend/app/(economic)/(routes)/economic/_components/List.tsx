



import React from 'react'

const List = () => {
  return (
    <div className="bg-white rounded-xl px-4 py-4 shadow-2xl  mt-10">
    <div>
      <div className="flex items-center justify-between">
        <h1 className="font-semibold py-6 px-2">Histórico de transações</h1>      
      </div>
      <div className="block w-full overflow-x-auto ">
        <table className="items-center w-full bg-transparent border-collapse">
          <thead>
                      <tr>
                        <th className="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left  border-gary-700">Nome</th>
                        <th className="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left  border-gary-700">População</th>
                        <th className="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left  border-gary-700">Região</th>
                        <th className="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left  border-gary-700">Area Km²</th>
                        <th className="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left  border-gary-700">Status</th>                         
                      </tr>
          </thead>
          <tbody>     
            <tr>
              <th className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4 text-left flex items-center">
                        <img src="https://demos.creative-tim.com/notus-js/assets/img/bootstrap.jpg" className="h-12 w-28 bg-white rounded border" alt="..."/>
                <span className="ml-3 font-bold ">categoria </span></th>
              <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-sm font-semibold whitespace-nowrap p-4">Inscrição</td>
              <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">
                <div className="flex flex-col">
                  <span className="text-md font-semibold">dta</span>                                     
                </div>
              </td>
              <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">R$ </td>
              <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">
                <div className="flex items-center">
                    <span className="bg-red-500 py-1 px-6 rounded-full text-white">status</span>      
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

export default List
