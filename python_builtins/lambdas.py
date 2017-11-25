'''
def l(x):
	return x > 5
'''
l = lambda x: x > 5
print(l(10))

def alter(values, check):
	return [val for val in values if check(val)]

my_list = [1, 2, 3, 4, 5]
another_list = alter(my_list, lambda x: x != 5)
print(another_list)

# more computationally expensive
def check_not_five(x):
	return x != 5

another_list = alter(my_list, check_not_five)

print(another_list)


## Part 2 - Filter

def alter(values, check):
	return list(filter(check, values))

my_list = [1, 2, 3, 4, 5]

another_list = alter(my_list, lambda x: x != 5)
print another_list


def remove_numbers(value):
	return alter(value, lambda x: x not in [str(n) for n in range(10)])

my_list = [1, 2, 3, 4, 5]
another_list = alter('hell5o', remove_numbers)
print another_list


def skip_letter(value, letter):
	return alter(value, lambda x: str(x) != letter)

print(skip_letter('hello', 'e'))