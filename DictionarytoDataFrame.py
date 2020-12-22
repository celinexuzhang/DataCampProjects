# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {
    'country': names,
    'drives_right': dr,
    'cars_per_cap': cpc}

cars = pd.DataFrame(my_dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)
# convert dataframe to csv
cars_csv = pd.DataFrame.to_csv(cars,encoding='utf-8', index=False)
# Print out cars
print(cars_csv)

# Import the cars.csv data: cars
#cars = pd.read_csv(cars_csv)
# Fix import by including index_col
#cars = pd.read_csv('cars.csv',index_col = 0)

