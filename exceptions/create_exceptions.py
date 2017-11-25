'''Provide more information about the nature of the error just by subclassing exceptions'''

class MissingLabelError(KeyError):
	pass


class PageNotFound(LookupError):
	pass


class IncorrectPasswordError(ValueError):
	pass


class IncorrectUsernameError(ValueError):
	pass


class APIThrottleLimitError(RuntimeError):
	pass


# program... user enters wrong username
def login():
	raise IncorrectUsernameError


try:
	login()
except IncorrectUsernameError:
	print('Your username was incorrect. Have you forgotten it?')
except IncorrectPasswordError:
	# redirect to a password reset page
	print('Your password was incorrect. Have you forgotten it?')
