from coinmarketcapapi import CoinMarketCapAPI, CoinMarketCapAPIError
import json

cmc = CoinMarketCapAPI('c773e9aa-0c9a-4420-8896-be97e954e7d9')


try:
    r = cmc.cryptocurrency_categories()
except CoinMarketCapAPIError as e:
    r = e.rep

#print(repr(r.error))
#print(repr(r.status))
#print(repr(r.data[1]))
print(json.dumps(repr(r.data), indent=4, sort_keys=True))



