


import React, { useEffect, useRef } from 'react'

const CountrieCurrency = ({currency}:{currency: string}) =>{
      // const asset = 'AAPL'; // Replace with the asset you want to display
      const widgetRef = useRef<HTMLDivElement>(null);


      console.log(currency)

    
      useEffect(() => {
        const script = document.createElement("script");
        script.type = "text/javascript";
        script.src = "https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js";
        script.async = true;
        script.innerHTML = JSON.stringify({
          symbol: `USD${currency}`,
          width: "100%",
          height: 219,
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
  return (
    <div className="relative w-full h-full">
            <section id="mini-symbol-overview-widget" className="flex flex-col"  >
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
    </div>
  )
}

export default CountrieCurrency