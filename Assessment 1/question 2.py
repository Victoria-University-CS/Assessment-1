# Part a
# Defining a dictionary called population
# providing information on the world's largest cities
# with the key as the city name and value as the population in millions of people
population = {
    "Shanghai": 17.8,
    "Instabul": 13.3,
    "Karachi": 13.0,
    "Mumbai": 12.5
}
# print dictionary keys and the dictionary created
print(f'The dictionary keys are: {population.keys()}.\nThe dictionary is: {population}')



# Part b
# A program for the gas elements that requires
elements = {
    'hydrogen':{'number': 1, 'weight': 1.00794, 'symbol': 'H'},
    'helium':{'number': 2, 'weight': 4.002602, 'symbol': 'He'}
}

# Adding Oxygen gas and printing the weight of a hellium gas

elements['oxygen'] = {'number': 8, 'weight': 15.999, 'symbol': 'O'},

# Print elements to verify
print(f'All elements are: {elements}')

# Printing the weight of Helium
print(f"The weight of Helium is: {elements['helium']['weight']}")