# WRITING/EDITING EXTERNAL FILES
# *Remember which method you're using when making the .open call

# count_file = open('lessons/file_reading_test.txt', 'w')
# count_file.write('Guam (updated now)')
# This will overwrite what ever is currently in the file and only contain what's passed in 

# count_file = open('lessons/file_reading_test.txt', 'a')
# count_file.write('\nMontana (updated now)')
# \n will add to the file on a new line IF specifying 'a' in the open call 


# .open methods:

# 'r' = read the file
# 'w' = write/edit the file
# 'a' = append to the ending the file
# 'r+' = read and write the file