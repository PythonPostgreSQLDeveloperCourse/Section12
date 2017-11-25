class Leg(object):
	pass

class Back(object):
	pass

class Chair(object):
	'''Compose a class out of other classes'''
	def __init__(self, num_legs):
		self.legs = [Leg() for leg in range(num_legs)]
		self.back = Back()

	def __repr__(self):
		return 'I have {} legs and one back.'.format(len(self.legs))


print(Chair(4))