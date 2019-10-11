# Part a
# A program that takes population and area of a country/Region 
# and outputs the population density

# Getting the user region
region = input('Enter Region/Country: ')

# Get the population of that region
region_population = int(input(f'What is the population of {region}: '))

# Get the area of the region
region_area = float(input(f'What is the area of {region}: '))

# Print out the population density
print(f'The population density of {region}  is {region_population/ region_area}')

# Part b
# A program that takes user inputs for sales on Monday to Friday
# and prints the total of the sales made in a week
monday_sales = float(input('Enter Monday Sales: '))
tuesday_sales = float(input('Enter Tuesday Sales: '))
wednesday_sales = float(input('Enter Wednesday Sales: '))
thursday_sales = float(input('Enter Thursday Sales: '))
friday_sales = float(input('Enter Friday Sales: '))

total_weekly_sales = (monday_sales+tuesday_sales+wednesday_sales+thursday_sales+friday_sales)

# Print the total weekly sales
print(f'Your Total weekly sales is: {total_weekly_sales}')

# Part c
# A program that outputs the string 'ity' from the dictionary
# d2 = {'k1': {'k2': 'University'}}

# Define the dictionary
d2 = {'k1': {'k2': 'University'}}

# printing the 'ity'
print(f"Printing {d2['k1']['k2'][-3:]} form {d2}")