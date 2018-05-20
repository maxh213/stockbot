import cat
import random

class Stock_price_entry:

	def __init__(self, entry_date, high_value, low_value, open_value, close_value, volume):
		self.entry_date = entry_date
		self.high_value = high_value
		self.low_value = low_value
		self.open_value = open_value
		self.close_value = close_value
		self.volume = volume
		
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

