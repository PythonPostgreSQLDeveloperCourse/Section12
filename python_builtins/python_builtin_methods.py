class Currency:
	def __init__(self, code, exchange_to_usd):
		self.amount = 0.00
		self.code = code
		self.exchange_to_usd = exchange_to_usd

	def __eq__(self, other):
		'''equal operator'''
		return self.to_usd() == other.to_usd()

	def __gt__(self, other):
		'''greater than operator'''
		return self.to_usd() > other.to_usd()

	def __lt__(self, other):
		'''greater than operator'''
		return self.to_usd() < other.to_usd()
	
	def __le__(self, other):
		'''less than/equal to operator'''
		return self.to_usd() <= other.to_usd()
	
	def __ge__(self, other):
		'''greater than/equal to operator'''
		return self.to_usd() >= other.to_usd()

	def set_amount(self, amount):
		self.amount = amount

	def in_currency(self, amount):
		return amount / self.exchange_to_usd

	def to_usd(self, amount=None):
		to_convert = amount or self.amount
		return to_convert * self.exchange_to_usd


pounds = Currency('GBP', 1.21)
print(pounds.in_currency(1000))
print(pounds.to_usd(1000))
euros = Currency('EUR', 1.07)

pounds.set_amount(1000)
euros.set_amount(1000)
# could be more direct
print(pounds.to_usd() > euros.to_usd())
print(pounds > euros)