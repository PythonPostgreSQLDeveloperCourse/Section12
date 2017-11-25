'''
Hiding of the inner-workings of the class
when showing the inner-workings is not necessary
'''
import oauth2
import constants
import urlparse


class TwitterConsoleLogin(object):
	'''Code copied from twitter_utils and composed into a class'''
	def __init__(self, consumer_key, consumer_secret):
		# create a consumer (allow Twitter to id the app)
		# Encapsulated variable
		self.__consumer = oauth2.Consumer(constants.CONSUMER_KEY, constants.CONSUMER_SECRET)

	def perform_twitter_login(self):
		'''
		We are mainly interested in getting the access_token from this object so
		simplify that process down in this method
		'''
		request_token = self.__get_request_token()
		verifier = self.__get_oauth_verifier(request_token)
		return self.__get_access_token(request_token, verifier)

	'''Encaplusated methods'''

	def __get_request_token(self):
		client = oauth2.Client(self.__consumer)

		response, content = client.request(constants.REQUEST_TOKEN_URL, 'POST')
		if response.status != 200:
			print('An error occurred requesting token from Twitter')

		# parse query string parameter
		return dict(urlparse.parse_qsl(content))

	def __get_oauth_verifier_url(self, request_token):
		return '{}?oauth_token={}'.format(constants.AUTHORIZATION_URL, request_token['oauth_token'])

	def __get_oauth_verifier(self, request_token):
		'''ask user to input the pin they recieve after granting access to the app'''
		print('Go to the following site in a browser:')
		print(self.__get_oauth_verifier_url())

		# ask user to input the pin they recieve after granting access to the app
		return input('Paste pin code you recieved here: ').strip()

	def __get_access_token(self, request_token, oauth_verifier):
		token = oauth2.Token(request_token['oauth_token'],
			request_token['oauth_token_secret'])
		token.set_verifier(oauth_verifier)

		client = oauth2.Client(self.__consumer, token)

		response, content = client.request(constants.ACCESS_TOKEN_URL, 'POST')
		if response.status != 200:
			print('An error occurred requesting token from Twitter')

		return dict(urlparse.parse_qsl(content))


twitter_login = TwitterConsoleLogin('my_key', 'my_secret')
twitter_login.perform_twitter_login()