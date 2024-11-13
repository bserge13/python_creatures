number = 42

# print(40)
# print(number) 
# print(20 + 22) 
# print(20 - 12.82) 
# print(20 * 10) 
# print(number / 2)
# print(20 / 6) 
# print(20 % 6) 
# When dividing / = float/decimal return and % = only the remainder of what's being divded 

number2 = str(number)

# print(number2)
# won't appear in terminal in quotes, but IS still a string 

# print('number is' + number) 
# this will error because number is an integer and cannot be concatinated without a comma (,) vs number2 is a varibale holding a string and CAN 
# concatinate with the plus sign (+) 
# print('number is ' + number2) 

# print(-5)
# print(abs(-5))
# built-in python function meaning 'absolute value', i.e. without the neagative sign 

# print(max(4, 7, 3, 9))
# max() will return the highest value of all numbers passed-in
# print(min(7, -3, 14, 13))
# min() will return the lowest value of all numbers passed-in
# print(round(40.2))
# round() will return the passed-in variable as a rounded number.
# Can specify to which decimal place to round to ex: (round(40.2, 3)) which would round to 3 decimal place   
# print(bin(number))
# will return the binary text of a passed-in variable, but MUST to be whole number 

from math import * 
# Here we imported ALL (import *) from (from math) the math python class the mathmatical functions python has to offer (which includes non-built-in functions like finding squareroot)
print(sqrt(number))
# returns the squareroot of the passed-in integer/variable 
