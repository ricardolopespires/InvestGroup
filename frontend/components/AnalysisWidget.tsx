import { useEffect, useRef } from "react";

const AnalysisWidget = ({ asset }) => {
  const containerRef = useRef(null);

  useEffect(() => {
    if (!containerRef.current) return;

    // Remover script existente antes de adicionar um novo
    containerRef.current.innerHTML = "";

    const script = document.createElement("script");
    script.type = "text/javascript";
    script.async = true;
    script.src = "https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js";
    script.textContent = JSON.stringify({
      interval: "1D",
      width: "100%",
      isTransparent: false,
      height: 450,
      symbol: asset , // Usa o ativo fornecido ou um padrão
      showIntervalTabs: true,
      displayMode: "single",
      locale: "en",
      colorTheme: "light",
    });

    containerRef.current.appendChild(script);
  }, [asset]); // Adicionando asset como dependência para atualizar dinamicamente

  return (
    <div className="tradingview-widget-container" ref={containerRef}>
      <div className="tradingview-widget-container__widget"></div>
      <div className="tradingview-widget-copyright">
        <a href="https://www.tradingview.com/" rel="noopener nofollow" target="_blank">
          <span className="blue-text">Track all markets on TradingView</span>
        </a>
      </div>
    </div>
  );
};

export default AnalysisWidget;
