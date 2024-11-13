# EXTERNAL FILE READING

count_file = open('lessons/file_reading_test.txt', 'r')

# print(count_file.readline())
# Will return the first line
print(count_file.readlines())
# Will return all the lines, formatted: ['Ghana\n', 'Mexico\n', 'Spain\n', 'France ']
# print(count_file.readlines()[2])
# Will return based on index position

# for line in count_file.readlines():
#     print (line)

count_file.close

# .open methods: 

# 'r' = read the file
# 'w' = write/edit the file
# 'a' = append to the ending the file
# 'r+' = read and write the file