import requests
from stock_price_entry import Stock_price_entry
from stock_price_batcher import Stock_price_batcher
from secret_constants import USERNAME, PASSWORD
import numpy as np
import tensorflow as tf
import math


def main():
	data = get_data_from_api()
	stock_price_entries = get_stock_price_entries_from_json(data)

	stock_price_batcher = Stock_price_batcher(stock_price_entries)
	training_entry_batch, training_result_batch = stock_price_batcher.get_training_entry_and_result_batch()
	testing_entry_batch, testing_result_batch = stock_price_batcher.get_testing_entry_and_result_batch()
	print(len(training_entry_batch))
	print(len(testing_entry_batch))
	print(training_entry_batch[98], training_result_batch[98])

	#tf.app.run()
	#get stock price entry batch of values
	#WILL ALLOWING IT TO SEE THE NEXT DAY THROW IT OFF???

def get_stock_price_entries_from_json(data):
	stock_price_entries = []
	for i in range(len(data[:-1])):
		stock_price_entries.append(Stock_price_entry(data[i]['date'], data[i]['high'], data[i]['low'], data[i]['open'], data[i]['close'], data[i]['volume'], data[i+1]))
	return stock_price_entries


def get_data_from_api():
	PAGE_SIZE = 100
	response = requests.get('https://api.intrinio.com/prices?ticker=TPX', auth=(USERNAME, PASSWORD))
	if response.status_code != 200:
		print('rest call failed')
	data = response.json()['data'][::-1]
	total_pages = response.json()['total_pages']
	print(total_pages)
	for i in range(1, 3): #total_pages):
		url = 'https://api.intrinio.com/prices?ticker=TPX&page_number=' + str(i)
		response = requests.get(url, auth=(USERNAME, PASSWORD))
		if response.status_code != 200:
			print('rest call failed')
		data = data + response.json()['data'][::-1]
	return data


if __name__ == "__main__":
	main()