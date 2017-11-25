class A(object):
	def hi(self):
		print('Po-ta-to')

class B(object):
	def hi(self):
		print('Po-tah-to')

	def another(self):
		print('In class B')

class C(A, B):
	pass


c = C()
c.hi()
c.another()