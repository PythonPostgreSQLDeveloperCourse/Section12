'''
print(10/2)
print(10/0)
'''
number = 10
divisor = 2


def divide_secure(number, divisor):
	if divisor == 0:
		# so something to communicate what went wrong
		raise ValueError('The divisor is zero')
	return number/divisor


# better way?
def divide_secure(number, divisor):
	assert divisor != 0, 'Divisor is zero'
	return number/divisor

