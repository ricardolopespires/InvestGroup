"use client"

import Logout from "@/app/auth/Logout/page";



const page = () => {
    return (
        <div className="w-full h-full flex flex-col items-center justify-center">
            <header className="w-full h-20 flex items-center shadow-md justify-between">
                <div className="container flex items-center w-full gap-4">
                    <img src="/images/logo.png" alt="Logo-white" className="h-12 ml-4" />
                                  
                </div>
                <div className="text-2xl mr-9">
                    <Logout/>  
                </div>                 
            </header>
            <h1 className="text-4xl  text-center mt-16 mb-10">Análise do situação Financeira do Investidor</h1>
            <div className=" container flex flex-col mt-16 mb-10">
                <p className="text-xl flex items-center gap-2 font-bold">
                    <span>1</span>
                    <span>-</span>
                    <span>Qual é o seu principal objetivo ao investir?</span>
                </p>
                <div className="flex flex-col gap-4 mt-10 wifull justify-center ">
                    <button className="border border-blue-900 text-blue-900 text-xl hover:bg-blue-950 hover:text-white p-4 rounded-lg">
                    Preservar o capital e evitar perdas
                    </button>
                    <button className="border border-blue-900 text-blue-900 text-xl hover:bg-blue-950 hover:text-white p-4 rounded-lg">
                    Gerar renda extra com baixo risco
                    </button>
                    <button className="border border-blue-900 text-blue-900 text-xl hover:bg-blue-950 hover:text-white p-4 rounded-lg">
                    Equilibrar crescimento e segurança
                    </button>
                    <button className="border border-blue-900 text-blue-900 text-xl hover:bg-blue-950 hover:text-white p-4 rounded-lg">
                    Maximizar o retorno a longo prazo
                    </button>
                    <button className="border border-blue-900 text-blue-900 text-xl hover:bg-blue-950 hover:text-white p-4 rounded-lg">
                    Buscar altos ganhos, mesmo com alto risco
                    </button>
                </div>                
            </div>           
        </div>
    );
}

export default page;