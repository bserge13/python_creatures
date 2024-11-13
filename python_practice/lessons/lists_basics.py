countries = ['United Kingdom', 'Sri Lanka', 'USA', 'Canada', 'Ireland']
# print(countries) Will print the entrie list within & including the square bracket [ ]. 

# print(countries[1][0]) Python recognizes list index positioning- this will print the letter 'S' from Sri Lnaka. 

# print(countries[1:]) The colon will print everything from index position 1 through to the end, including the [ ]. 

# print(countries[1:3]) The colon also allows you to specify which index position in the list to stop at. Will only print 
# Sri Lanka and USA. 

# print(countries[1][0:3]) This syntax will call on index position 1 of the list and then ONLY print out letters UP TO BUT NOT including 
# index position 3. EX: 0:3 will ONLY print 'Sri' here. [0:3] means [0] is where we start, [3] is where we stop, but does not
# get printed.   

# countries[2] = 'United States'
# countries[0] = 'Kenya'
# The above changes the values in the specified index positions 

# print(countries[-2]) 
# Negative index positions start from the end. The return here will be 'Canada' 

# print(len(countries))
# len(list variable) returns how many values are in the list. Equivalent would be .length or .count 

# print(type(countries)) will print the data type of what the passed-in variable holds. Return- <class 'list'> 

var = [1, True, 'False', 4.20] 
print(len(var))
# Return will be 4 
print(type(var[1]))
# Will return the data type at the specified index position of the passed in variable). Will return <class 'bool'>

lists = list(('Nigeria', 'Kenya', 42, False))
# Another option to create a list without using [ ]. Purpose is to pass in values and using list(()) to do the construction. 
print(lists)
# list constructor requires double parenthesis: list(()) 