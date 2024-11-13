# tuples are immutable 

three_numbers = (1, 2, 3)
more_numbers = tuple((4, 5, 6))
strings = ('home', 'land', 'earth')
# three_numbers[1] = 23
# will raise error because can't reassign a tupples values
print(three_numbers)
print(strings)
print(len(three_numbers))
print(len(strings))
print(type(three_numbers))
print(type(strings))