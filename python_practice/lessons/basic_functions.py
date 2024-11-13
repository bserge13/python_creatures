# print('My name is Blake, my age is', 31) 
# having 31 outside of the string and outside of quotes still prints out: 
# 'My name is Blake, my age is 31' (smart feature of python)

# variables 

# print('Blake is a bears')
# print('Blake is 31')
# print('Blake is from indiana') 

name = 'Blake'
age = 31 

# print(name) 

# print(name + ' is a bears fan')
# print(name + ' is 31')
# print(name + ' is from Indiana')

# python still uses concatination (joining variables) with the + followed by '' or ""  
# to concatinate an integer in python you MUST use a comma (,) to join rather than a plus sign (+) 
# CAN concatinate an integer AND string both with a comma (,)

# concatination syntax: IF ONLY string use plus sign (+), ELSIF concatinating string AND integer use comma (,)   

# print(name) 
# print(name + ' is', age)
# print(name, 'is', age)
# print(name + ' is a bears fan')


# print('Hi.\nHow are you?')
# \n is syntax for printing on a new line. 
# Thing to remember- mindful of your spaces within the string & after the new line (\n) or it will be printed too 

# print('Hi. It\'s me')
# to add special characters within a string you preceed the character with a backslash (\). The backslash (\) by itself will print just the backslash (\) 

# print(name.upper())
# print(name.lower())
# # .upper() & .lower() are like the ruby equivalent of .uppercase .lowercase 
# print(name.islower())
# .islower() & isupper() return boolean responses 

name2 = 'BLAKE'

# print(name2.lower().islower()) 
# .islower() returns a boolean 
# can daisy-chain functions together 

# print(len(name))
# returns length of string/variable passed-in 

# print(name.index('a'))
# returns the index position of a passed-in variable- IF two instances of same variable it returns the first index position it hits on the variable 

# print(name2.replace('KE', 'H'))
# replaces the first argument passed-in with the second argument