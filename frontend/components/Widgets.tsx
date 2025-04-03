"use client";

import { useState, useRef, useEffect } from "react";

export default function TradingViewMiniSymbolOverview({asset}: {asset: string}) {
  // const asset = 'AAPL'; // Replace with the asset you want to display
  const widgetRef = useRef<HTMLDivElement>(null);
  const [showModal, setShowModal] = useState(false);
  const timeoutRef = useRef(null);

  useEffect(() => {
    const script = document.createElement("script");
    script.type = "text/javascript";
    script.src = "https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js";
    script.async = true;
    script.innerHTML = JSON.stringify({
      symbol: `${asset}`,
      width: 340,
      height: 160,
      locale: "br",
      dateRange: "12M",
      colorTheme: "light",
      isTransparent: false,
      autosize: false,
      largeChartUrl: "",
    });

    if (widgetRef.current) {
      widgetRef.current.appendChild(script);
    }

    return () => {
      if (widgetRef.current) {
        widgetRef.current.innerHTML = "";
      }
    };
  }, []);

   
    // Inicia um timer para esconder o modal após 2 segundos
    const startHideTimer = () => {
        clearTimeout(timeoutRef.current); // Reseta qualquer timer ativo
        timeoutRef.current = setTimeout(() => {
            setShowModal(false);
        }, 200);
    };

    // Mostra o modal e inicia o timer para fechar
    const handleMouseEnter = () => {
        setShowModal(true);
        startHideTimer();
    };

    // Cancela o timer ao sair
    const handleMouseLeave = () => {
        startHideTimer();
    };




  return (
    <div className="relative w-full h-full">
            <section id="mini-symbol-overview-widget" className="flex flex-col"  onMouseEnter={handleMouseEnter}
                    onMouseLeave={handleMouseLeave}>
                <div className="tradingview-widget-container" ref={widgetRef}>
                    <div className="tradingview-widget-container__widget"></div>
                    <div className="tradingview-widget-copyright">
                        <a
                            href="https://www.tradingview.com/"
                            rel="noopener nofollow"
                            target="_blank"
                        ></a>
                    </div>
                </div>             
            </section>

            {/* Modal */}
            {showModal && (
                <div
                    className="absolute inset-0 flex items-center justify-center bg-black bg-opacity-50 backdrop-blur-sm transition-opacity duration-300"
                    onMouseEnter={() => clearTimeout(timeoutRef.current)} // Cancela o timer ao entrar no modal
                    onMouseLeave={startHideTimer} // Reinicia o timer ao sair
                >
                    <a href={`/stock/market/${asset}`} className="w-60 text-center animate-fade-in">                      
                        <div className="text-sm bg-white p-4 rounded-md mt-2 flex items-center justify-center gap-2">
                           <span className="text-black text-xs">Mais informações</span>
                           <span className="text-amber-500">{asset}</span>.
                        </div>
                    </a>
                </div>
            )}
        </div>
  );
}
