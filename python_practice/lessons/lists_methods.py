list1 = [1, 2, 3, 4, 5, 5, 6, 5]
list2 = ['banana', 'apples', 'mangos', 'oranges']

# list1.extend(list2) 
# .extend combines the list/varibale it's called on with the argument/list it's passed in 

# print(list1)
# Returns a now combined list of list1 with list2, and ordered that way too

# list2.append('cherry')
# .append(arg) adds the passed in argument to the end of the array it's called on (list2) 

# print(len(list2))
# len(arg) returns the length/number of index positions/elements within the argument being passed in (list2)  

# list2.insert(1, 'pineapples')
# print(list2) 
# .insert takes the arguments of an index position, and what we want inserted into that speciofic index position 

# list2.remove('apples')
# .remove takes the argument of what you want to remove from the list variable it's being called on 

# list1.clear()
# print(list1)
# .clear clears the contents of the list variable it's called on 

# print(list2.index('oranges'))
# .index returns the index position of the argument passed-in  

# print(list1.count(5))
# .count returns the number of instances the passed-in argument occurs within the list/argument the method is called on 

# list1.sort()
# list2.sort()
# print(list1)
# print(list2)
# .sort() returns the list/variable it's called on in either alphabetical or numerical order- ascending as the default  

# list1.reverse()
# list2.reverse()
# print(list1)
# print(list2)
# .reverse() returns the list/variable it's called on in reverse alphabetical or numerical order 

# list3 = list2.copy()
# print(list2)
# print(list3)
# .copy() does exactly that, it makes a copy of the variable/list it's being called on 

# list2.pop()
# print(list2)
# list1.pop(5)
# print(list1)
# .pop() returns the list/variable it's called on but removes the last element of the array. .pop also can take in a variable 
# of which index position to remove 

# del list2[1]
# print(list2)
# del = delete. You can also specify an index position, or delete the entire list. Delete vs clear: clear just deletes the contents 
# of the variable, where delete (when called on a variable) is deleting the variable and it's contents 