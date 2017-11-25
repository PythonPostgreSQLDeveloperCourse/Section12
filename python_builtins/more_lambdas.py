
class Currency:
	def __init__(self, code, exchange_to_usd):
		self.amount = 0.00
		self.code = code
		self.exchange_to_usd = exchange_to_usd

	def __repr__(self):
		return '<Currency {} {}>'.format(self.amount, self.code)

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


# Imagine getting Currency from an API
# requests.get('some endpoint').json()
def _get_currency_resource(resource, transform=(lambda x: x)):
	data = {'items': [
		{'code':'usd', 'amount_to_usd':1.00,},
		{'code':'gbp', 'amount_to_usd':1.21,},
		{'code':'eur', 'amount_to_usd':1.07,},
		{'code':'jpy', 'amount_to_usd':0.14}
	]}

	my_resource = data[resource]
	# return list(map(transform, my_resource))
	return [transform(x) for x in my_resource]


currencies = _get_currency_resource('items')
print currencies

currencies = _get_currency_resource('items', lambda x: x['code'].upper())
print currencies

def get_currency_codes():
	return _get_currency_resource('items', lambda x: x['code'].upper())

print(get_currency_codes())


def get_currencies():
	return _get_currency_resource('items',
		lambda x: Currency(code=x['code'].upper(),
						   exchange_to_usd=x['amount_to_usd']))

print(get_currencies())


def calculate_in_all_currencies(usd_amount):
	print('-- {} USD in all currencies --'.format(usd_amount))
	for currency in get_currencies():
		currency.set_amount(usd_amount)
		print('In {}: {:.2f}'.format(currency.code, currency.in_currency(usd_amount)))

print(calculate_in_all_currencies(1000))
