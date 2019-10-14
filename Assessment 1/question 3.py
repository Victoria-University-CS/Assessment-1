# A program that takes the username 
# and maximum characters required in a permit

# Create a variable for the username
username = input('Enter username: ')

# Create a variable for the maximum number of chars
# that can fit the permit
max_permit_chars = int(input('Permit Charater Limit: '))

# Prints if the name fits or not
print(f'Does "{username}" fit?: {len(username) <= max_permit_chars}')

# Prints the string that is printed on the permit
print(f'"{username[0: max_permit_chars]}" from {username} can be printed to the permit')

# Converts the username to upper case and prints it
username_upper = username.upper()
print(f'{username} in upper case is "{username_upper}"')

# Prints the middle character
middle_char = int(len(username_upper)/2) # or middle_char = len(username)//2
print(f'Middle Character from {username_upper} is "{username_upper[middle_char-1]}"')

# Print between second and last character
print(f'Second to last chars in username is "{username[1:-1]}"')