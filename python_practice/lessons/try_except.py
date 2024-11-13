# Used for handling errors 

try:
    x = int(input('Enter an integer: '))
    print(x)
except: 
    print('Something went wrong... Please try again') 
    # this will be a default for any input or error
# except ValueError:
#     print('Value not an integer')
    # this will be specific to only value errors- wrong type of input from the user 
# else:
#     print('Nothing went wrong')
    # this will only run if the try: is successful and except: didn't get ran 
finally: 
    print('Try Except Finished')
    # this will be the last line of code ran regardless of whether the try: or ecept: were ran 


# try: is best case 
# except: is worst case/error handling 
# else: is a final line or return if try: runs but NOT except: 
# finally: is the last line or return regardless  
