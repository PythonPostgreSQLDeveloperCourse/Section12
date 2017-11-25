'''
number = input('Enter a number: ')

try:
	print(int(number) * 2)
except LookupError:
	print('LookupError? This should never happen...')
except ValueError:
	print('You did not enter a base-10 number! Try again.')

print('Hello')
'''


import requests
from simplejson import JSONDecodeError


r = requests.post('http://text-processing.com/api/sentiment', data={'text': 'hello world'})
try:
	label = r.json()['label']
except JSONDecodeError:
	print('JSON response could not be decoded')
except KeyError:
	print('Got JSON response with no key "label"')
else:
	print(label)
