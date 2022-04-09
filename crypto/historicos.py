from django.http import JsonResponse
from django.shortcuts import render







def dados(cripto, Client, client):
  
    candlesticks = client.get_historical_klines(str(cripto), Client.KLINE_INTERVAL_5MINUTE, '1 Jan, 2021',)

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

  

    return JsonResponse(processend_clanlesticks, safe=False)