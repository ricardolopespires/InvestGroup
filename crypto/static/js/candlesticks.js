



var chart = LightweightCharts.createChart(document.getElementById('chart'), {	
	layout: {
		backgroundColor: '#ffffff',
		textColor: 'rgba(0, 0, 0, 0.9)',
	},
	grid: {
		vertLines: {
			color: 'rgba(255, 255, 255, 0.5)',
		},
		horzLines: {
			color: 'rgba(255, 255, 255, 0.5)',
		},
	},
	crosshair: {
		mode: LightweightCharts.CrosshairMode.Normal,
	},
	rightPriceScale: {
		borderColor: 'rgba(197, 203, 206, 0.8)',
	},
	timeScale: {
		borderColor: 'rgba(197, 203, 206, 0.8)',
	},
});

//Tulind Functions
const {
	sma_inc,} = require('./indicators');

var candleSeries = chart.addCandlestickSeries({
  upColor: '#33cc33',
  downColor: '#ff0000',
  borderDownColor: '#ff0000',
  borderUpColor: '#33cc33',
  wickDownColor: '#ff0000',
  wickUpColor: '#33cc33',
});

fetch('http://localhost:8000/crypto/trading/automatico/history/')
	
	.then((r) => r.json())
	.then((response) => {		
		candleSeries.setData(response);
	})

var binanceSocket = new WebSocket('wss://stream.binance.com:9443/ws/cakeusdt@kline_5m')
binanceSocket.onmessage = function (event){
	var message = JSON.parse(event.data);
	var candlestick = message.k;

	candleSeries.update({
		time: candlestick.t / 1000,
		open: candlestick.o,
		high: candlestick.h,
		low: candlestick.l,
		close: candlestick.c,
	})

	var order = candleSeries.chart().createOrderLine({
    setText: "Buy Line",
    setLineLength : 3, 
    setLineStyle: 0, 
    setQuantity: "221.235 USDT",

	})

	order.setPrice(6);

	var markers = [{ time: candleSeries[candleSeries.length - 48].time, position: 'aboveBar', color: '#f68410', shape: 'circle', text: 'D' }];
	for (var i = 0; i < datesForMarkers.length; i++) {
		if (i !== indexOfMinPrice) {
			markers.push({ time: datesForMarkers[i].time, position: 'aboveBar', color: '#e91e63', shape: 'arrowDown', text: 'Sell @ ' + Math.floor(datesForMarkers[i].high + 2) });
		} else {
			markers.push({ time: datesForMarkers[i].time, position: 'belowBar', color: '#2196F3', shape: 'arrowUp', text: 'Buy @ ' + Math.floor(datesForMarkers[i].low - 2) });
		}
	}
	candleSeries.setMarkers(markers);

}






