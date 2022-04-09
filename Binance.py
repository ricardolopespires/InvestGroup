from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import json

api_key = "eiXlqiLwskSPqFuLgiShKAvXYN99xsi7k0gAMdELR1hu2e7Ah1DjZ9FRKcm7dzd5"
api_secret = "VIFRVdvXd9eoKbwNtBMdEmvwNo6YRx6faczObnsva0gX3vywEdO7APvqtfKY4nfz"


client = Client(api_key, api_secret)

candlesticks = client.get_historical_klines("NEOBTC", Client.KLINE_INTERVAL_1WEEK, "1 Jan, 2017")

processend_clanlesticks = []

for data in candlesticks:
    candlestick = {
        'time': data[0] / 1000,
	'open':data[1],
	'high':data[2],
	'low':data[3],
	'close':data[4]

        }
    processend_clanlesticks.append(candlestick)


print(json.dumps(processend_clanlesticks, indent=4, sort_keys=True))
