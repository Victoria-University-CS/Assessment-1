# A program to split a given string
# Given String
new_str = "The cow jumped over the moon."

# Split by space
space_split = new_str.split()
print(f'Splitting by space gives: {space_split}')

# Split by a specified character 'o'
char_split = new_str.split('o')
print(f'Splitting by \'o\' gives: {char_split}')

# A program to determine the number of days
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# Get month from user input
# User input should be an integer
month = int(input('Enter Month: '))

# Printing the days in the month
print(f'There are {days_in_month[month-1]} days in month {month}')

# Changing the value of days of a given month
# And testing it
days_in_month[1] = 29
print(f'There are {days_in_month[1]} days in month 2')