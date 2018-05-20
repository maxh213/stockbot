
class Stock_price_entry:

	def __init__(self, entry_date, high_value, low_value, open_value, close_value, volume, next_day_stock_price_entry):
		self.entry_date = entry_date
		self.high_value = high_value
		self.low_value = low_value
		self.open_value = open_value
		self.close_value = close_value
		self.volume = volume
		self.next_day_stock_price_entry = next_day_stock_price_entry
		
	def get_entry_date(self):
		return self.entry_date

	def get_high_value(self):
		return self.high_value

	def get_low_value(self):
		return self.low_value

	def get_close_value(self):
		return self.close_value

	def get_open_value(self):
		return self.open_value

	def get_volume(self):
		return self.volume

	def get_result_of_next_day(self):
		if self.next_day_stock_price_entry['open'] < self.next_day_stock_price_entry['close']:
			return 1
		else:
			return -1

	def get_data_for_batch(self):
		return [[self.high_value, self.low_value, self.open_value, self.close_value, self.volume], [self.get_result_of_next_day()]]

