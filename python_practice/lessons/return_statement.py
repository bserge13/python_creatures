def add_numbers(num1, num2):
    return num1 + num2  
    # anything after the 'return' statement will not be returned; return is the end of the road for printing  


num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
# turning the input into an integer is required in order to do math. Otherwise return will just be a combination of the two 
# inputs as if it were a string 
print(add_numbers(num1, num2))