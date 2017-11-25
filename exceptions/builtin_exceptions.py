# https://docs.python.org/2/library/exceptions.html

# AttributeError
class MyClass:
	def __init__(self):
		pass

x = MyClass()
x.my_method()


# ImportError
import my_awesome_module


# KeyError
my_dict = {'x': 5, 'y': 10}
print(my_dict['z'])


# RuntimeError
# Generic error unassociated with other types


# TypeError
int([]) # wrong argument type


# ValueError
int('a') # string is a valid type but incorrect value


# IOError
open('my_file', 'r') # FileNotFoundError, a more specific IOError