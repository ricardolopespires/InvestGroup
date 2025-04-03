import { useEffect, useRef } from "react";

type FundamentalDataWidgetProps = {
  asset: string;
};

const FundamentalDataWidget: React.FC<FundamentalDataWidgetProps> = ({ asset }) => {
  const widgetRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!widgetRef.current) return;

    const script = document.createElement("script");
    script.type = "text/javascript";
    script.src = "https://s3.tradingview.com/external-embedding/embed-widget-financials.js";
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

    widgetRef.current.appendChild(script);

    return () => {
      if (widgetRef.current) {
        widgetRef.current.innerHTML = "";
      }
    };
  }, [asset]);

  return (
    <section id="mini-symbol-overview-widget" className="flex flex-col">
      <div className="tradingview-widget-container" ref={widgetRef}>
        <div className="tradingview-widget-container__widget"></div>
        <div className="tradingview-widget-copyright">
          <a
            href="https://www.tradingview.com/"
            rel="noopener nofollow"
            target="_blank"
          >
            TradingView
          </a>
        </div>
      </div>
    </section>
  );
};

export default FundamentalDataWidget;
