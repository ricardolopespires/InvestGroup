import React, { useEffect, useRef } from "react";

const CompanyProfileWidget = ({ asset }: { asset: string }) => {
  const widgetRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!asset) return; // Evita erros se asset for indefinido

    const script = document.createElement("script");
    script.type = "text/javascript";
    script.src =
      "https://s3.tradingview.com/external-embedding/embed-widget-symbol-profile.js";
    script.async = true;
    script.innerHTML = JSON.stringify({
      symbol: asset,
      width: "100%",
      height: 550,
      locale: "br",
      dateRange: "12M",
      colorTheme: "light",
      isTransparent: false,
      autosize: false,
      largeChartUrl: "",
    });

    if (widgetRef.current) {
      widgetRef.current.innerHTML = ""; // Limpa antes de adicionar o novo script
      widgetRef.current.appendChild(script);
    }

    return () => {
      if (widgetRef.current) {
        widgetRef.current.innerHTML = ""; // Remove apenas o script para evitar problemas
      }
    };
  }, [asset]); // Dependência adicionada

  return (
    <section id="mini-symbol-overview-widget" className="flex flex-col">
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
  );
};

export default CompanyProfileWidget;
