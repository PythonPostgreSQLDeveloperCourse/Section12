'''
Video differs from this file's content in that Python 3 is being used

Helpful links:

	https://rhettinger.wordpress.com/2011/05/26/super-considered-super/
	http://code.activestate.com/recipes/577721-how-to-use-super-effectively-python-27-version/
'''

class Decimal(object):
	'''Decimal and number of places decimal is printed'''
	def __init__(self, number, places):
		self.number = number
		self.places = places

	def __repr__(self):
		return '%.{}f'.format(self.places) % self.number


class Currency(Decimal):
	''''''
	def __init__(self, symbol, number, places):
		super(Currency, self).__init__(number, places)
		self.symbol = symbol

	def __repr__(self):
		return '{}{}'.format(self.symbol, super(Currency, self).__repr__())

	def add_currency(self, currency):
		# exchange between currencies?
		pass


print(Decimal(15.6789, 3))
print(Currency('$', 15.6789, 3))
