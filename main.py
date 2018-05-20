import requests
from stock_price_entry import Stock_price_entry
from stock_price_entry_batcher import Stock_price_entry_batcher
from secret_constants import USERNAME, PASSWORD
import numpy as np
import tensorflow as tf


def main():
	response = get_response_from_api()
	stock_price_entries = get_stock_price_entries_from_json(response)
	stock_price_entry_batcher = Stock_price_entry_batcher(stock_price_entries)
	training_entry_batch, training_result_batch = stock_price_entry_batcher.get_training_entry_and_result_batch()
	testing_entry_batch, testing_result_batch = stock_price_entry_batcher.get_testing_entry_and_result_batch()
	print(training_entry_batch[1], training_result_batch[0])

	#tf.app.run()
	#get stock price entry batch of values

def get_stock_price_entries_from_json(response):
	stock_price_entries = []
	for index_day, next_index_day in grouped(response.json()['data'], 2):
		stock_price_entries.append(Stock_price_entry(index_day['date'], index_day['high'], index_day['low'], index_day['open'], index_day['close'], index_day['volume'], next_index_day))
		return stock_price_entries


def get_response_from_api():
	response = requests.get('https://api.intrinio.com/prices?ticker=TPX', auth=(USERNAME, PASSWORD))
	if response.status_code != 200:
		print('rest call failed')
	return response

def grouped(iterable, n):
    "s -> (s0,s1,s2,...sn-1), (sn,sn+1,sn+2,...s2n-1), (s2n,s2n+1,s2n+2,...s3n-1), ..."
    return izip(*[iter(iterable)]*n)



if __name__ == "__main__":
	main()