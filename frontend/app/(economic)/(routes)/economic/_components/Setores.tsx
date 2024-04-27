



import React from 'react'

const Setores = () => {
  return (
    <div className="grid grid-cols-2 gap-4 w-full h-full">
        <div className='flex w-full h-full px-9 text-sm italic items-center'>
            <p>os principais setores econômicos de um país podem variar dependendo de sua estrutura econômica e desenvolvimento. No entanto, aqui estão alguns setores comuns que tendem a ser significativos em muitos países</p>
        </div>
        <div className='flex flex-col items-center w-full h-full mt-4 text-sm space-y-2'>
            <div className='flex items-center justify-between w-full gap-2'>
                <div className="w-1/4 flex items-center justify-start font-semibold">Comércio</div>
                <div className="w-3/4 bg-gray-200 rounded-full flex items-center h-2">
                    <div className='h-full w-[15%] bg-yellow-500 rounded-full'></div>
                </div>
                <div className="w-1/6 flex items-center justify-start font-semibold">15%</div>
            </div>
            <div className='flex items-center justify-between w-full gap-2'>
                <div className="w-1/4 flex items-center justify-start font-semibold">Indústria</div>
                <div className="w-3/4 bg-gray-200 rounded-full flex items-center h-2">
                    <div className='h-full w-[23%] bg-yellow-500 rounded-full'></div>
                </div>
                <div className="w-1/6 flex items-center justify-start font-semibold">23%</div>
            </div>
            <div className='flex items-center justify-between w-full gap-2'>
                <div className="w-1/4 flex items-center justify-start font-semibold">Serviços</div>
                <div className="w-3/4 bg-gray-200 rounded-full flex items-center h-2">
                    <div className='h-full w-[43%] bg-yellow-500 rounded-full'></div>
                </div>
                <div className="w-1/6 flex items-center justify-start font-semibold">43%</div>
            </div>
            <div className='flex items-center justify-between w-full gap-2'>
                <div className="w-1/4 flex items-center justify-start font-semibold">Tecnologia</div>
                <div className="w-3/4 bg-gray-200 rounded-full flex items-center h-2">
                    <div className='h-full w-[7%] bg-yellow-500 rounded-full'></div>
                </div>
                <div className="w-1/6 flex items-center justify-start font-semibold">7%</div>
            </div>
            <div className='flex items-center justify-between w-full gap-2'>
                <div className="w-1/4 flex items-center justify-start font-semibold">Energia</div>
                <div className="w-3/4 bg-gray-200 rounded-full flex items-center h-2">
                    <div className='h-full w-[3%] bg-yellow-500 rounded-full'></div>
                </div>
                <div className="w-1/6 flex items-center justify-start font-semibold">3%</div>
            </div>
            <div className='flex items-center justify-between w-full gap-2'>
                <div className="w-1/4 flex items-center justify-start font-semibold">Finanças</div>
                <div className="w-3/4 bg-gray-200 rounded-full flex items-center h-2">
                    <div className='h-full w-[23%] bg-yellow-500 rounded-full'></div>
                </div>
                <div className="w-1/6 flex items-center justify-start font-semibold">23%</div>
            </div>
            <div className='flex items-center justify-between w-full gap-2'>
                <div className="w-1/4 flex items-center justify-start font-semibold">Manufatura</div>
                <div className="w-3/4 bg-gray-200 rounded-full flex items-center h-2">
                    <div className='h-full w-[17%] bg-yellow-500 rounded-full'></div>
                </div>
                <div className="w-1/6 flex items-center justify-start font-semibold">17%</div>
            </div>
            <div className='flex items-center justify-between w-full gap-2'>
                <div className="w-1/4 flex items-center justify-start font-semibold">Construção</div>
                <div className="w-3/4 bg-gray-200 rounded-full flex items-center h-2">
                    <div className='h-full w-[40%] bg-yellow-500 rounded-full'></div>
                </div>
                <div className="w-1/6 flex items-center justify-start font-semibold">40%</div>
            </div>
            <div className='flex items-center justify-between w-full gap-2'>
                <div className="w-1/4 flex items-center justify-start font-semibold">Educação</div>
                <div className="w-3/4 bg-gray-200 rounded-full flex items-center h-2">
                    <div className='h-full w-[5%] bg-yellow-500 rounded-full'></div>
                </div>
                <div className="w-1/6 flex items-center justify-start font-semibold">5%</div>
            </div>        
        </div>
    </div>
  )
}

export default Setores
