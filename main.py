import requests
from stock_price_entry import Stock_price_entry
from secret_constants import USERNAME, PASSWORD

response = requests.get('https://api.intrinio.com/prices?ticker=TPX', auth=(USERNAME, PASSWORD))
if response.status_code != 200:
    print('rest call failed')


stock_price_entries = []
for index_day in response.json()['data']:
	stock_price_entries.append(Stock_price_entry(index_day['date'], index_day['high'], index_day['low'], index_day['open'], index_day['close'], index_day['volume']))

print(stock_price_entries[0].get_entry_date())