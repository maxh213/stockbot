from stock_price_entry import Stock_price_entry

class Stock_price_batcher:

	def __init__(self, stock_price_entries):
		self.TRAINING_BATCH_SIZE = 3200
		self.TESTING_BATCH_SIZE = 420
		self.stock_price_entries = stock_price_entries
		self.training_entry_batch, self.training_result_batch = get_entry_and_result_batch(stock_price_entries[:self.TRAINING_BATCH_SIZE])
		self.testing_entry_batch, self.testing_result_batch = get_entry_and_result_batch(stock_price_entries[-self.TESTING_BATCH_SIZE:])

	def get_entry_and_result_batch(self, stock_price_entries):
		entry_batch = []
		result_batch = []
		for stock_price_entry in stock_price_entries:
			stock_price_entry_data = stock_price_entry.get_data_for_batch()
			entry_batch.append(stock_price_entry_data[0])
			result_batch.append(stock_price_entry_data[1])
		return entry_batch, result_batch

	def get_training_entry_and_result_batch(self):
		return self.training_entry_batch, self.training_result_batch

	def get_testing_entry_and_result_batch(self):
		return self.testing_entry_batch, self.testing_result_batch




		