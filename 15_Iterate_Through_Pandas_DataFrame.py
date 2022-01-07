import pandas as pd


##################  This code will create the pandas dataframe  ######################
# Values 
carPerCapValue = [809, 731, 588, 18, 200, 70, 45]
countryValue = ['United States ', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
driverRightValue = [True, False, False, False, True, True, True]

# Code is to keep the dictionary data in sequence 
from collections import OrderedDict

orderValue = OrderedDict([('cars_per_cap', carPerCapValue), ('country', countryValue),('drives_right', driverRightValue)])

# Store the order data in dictionary varaible called my_dict
my_dict = {'cars_per_cap':carPerCapValue, 'country':countryValue, 'drives_right':driverRightValue}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict, index = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG'])

# OR you can replace the rows index value with the below code as well
# cars.index = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']

print(cars)

# O/P :- 
#      cars_per_cap         country  drives_right
# US            809  United States           True
# AUS           731       Australia         False
# JAP           588           Japan         False
# IN             18           India         False
# RU            200          Russia          True
# MOR            70         Morocco          True
# EG             45           Egypt          True
################################   END    #########################

# 1.
for i in cars:
    print(i)  # As this will only print the the columns name

# O/P :- 
# cars_per_cap
# country
# drives_right


# 2.
# So print the complete rows, we have write the for loop as below 
for lab, row in cars.iterrows():
    print(str(lab) +' = '+ str(row)) # so here it is returning the value each row by row as pandas series 

# O/P :- 
# US = cars_per_cap               809
# country         United States 
# drives_right              True
# Name: US, dtype: object
# AUS = cars_per_cap          731
# country         Australia
# drives_right        False
# Name: AUS, dtype: object
# JAP = cars_per_cap      588
# country         Japan
# drives_right    False
# Name: JAP, dtype: object
# IN = cars_per_cap       18
# country         India
# drives_right    False
# Name: IN, dtype: object
# RU = cars_per_cap       200
# country         Russia
# drives_right      True
# Name: RU, dtype: object
# MOR = cars_per_cap         70
# country         Morocco
# drives_right       True
# Name: MOR, dtype: object
# EG = cars_per_cap       45
# country         Egypt
# drives_right     True
# Name: EG, dtype: object

# 3. 
# or suppose you want to run filter more, like you want only the countries from the pandas dataframe
for l, r in cars.iterrows():
    print(str(l) +':'+ str(r['country']))

# O/P :- 
# US:United States 
# AUS:Australia
# JAP:Japan
# IN:India
# RU:Russia
# MOR:Morocco
# EG:Egypt

# 4. 
# The output should be in the form "country: cars_per_cap". 
# Make sure to print out this exact string (with the correct spacing).
for lab, row in cars.iterrows() :
    print(row['country'] +': '+ str(row['cars_per_cap']))

# O/P :- 
# United States : 809
# Australia: 731
# Japan: 588
# India: 18
# Russia: 200
# Morocco: 70
# Egypt: 45


# 5.
# Use a for loop to add a new column, named COUNTRY, 
# that contains a uppercase version of the country names in the "country" column. 
# Code for loop that adds COUNTRY column
for l , r in cars.iterrows():
    cars.loc[l, 'COUNTRY'] = r['country'].upper()
# Print
print(cars)

# O/P :-
#      cars_per_cap  ...         COUNTRY
# US            809  ...  UNITED STATES
# AUS           731  ...       AUSTRALIA
# JAP           588  ...           JAPAN
# IN             18  ...           INDIA
# RU            200  ...          RUSSIA
# MOR            70  ...         MOROCCO
# EG             45  ...           EGYPT

# 6.
# Now without for loop add a new column called lowercountry and store the lower case country value
cars['lowercountry'] = cars['country'].apply(str.lower)    
print(cars)

# O/P :-
#      cars_per_cap  ...    lowercountry
# US            809  ...  united states
# AUS           731  ...       australia
# JAP           588  ...           japan
# IN             18  ...           india
# RU            200  ...          russia
# MOR            70  ...         morocco
# EG             45  ...           egypt


# 7.
# Now suppose you want to create a new column called country_length and want to add the values of 
# country character length in that column
cars['country_length'] = cars['country'].apply(len)
print(cars)

# O/P :-
#      cars_per_cap  ... country_length
# US            809  ...             14
# AUS           731  ...              9
# JAP           588  ...              5
# IN             18  ...              5
# RU            200  ...              6
# MOR            70  ...              7
# EG             45  ...              5