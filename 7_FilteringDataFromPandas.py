# In this file all the below commands are written in the Jupyter NoteBook
# In this doc we will exploring how to slice the index and read some particular data from DataFrame

# 2 Way to extract the data :
# 1. (loc[] )Label based indexing (Column Label is column of the table and Index Label is row of the table)
# 2. (iloc[] )Position based indexing

# 1. So here we will be starting the Label based indexing (i.e loc[] )

# IMPORTANT NOTE : Whenever you are filtering or deleteing DataFrame using the column string or index value, 
# always create the column for that DataFrame


import pandas

# Use the escape sequnce
dataF = pandas.read_csv("C:\\Users\\Sri\Documents\\jupyter\\pandasplaintextfilterdatascenario.txt")
print(dataF)

# O/P :- 

#   Address	City	State   Postcode Country
# 0	LAN1	city1	state1	post1	cont1
# 1	LAN2	city2	state2	post2	cont2
# 2	LAN3	city3	state3	post3	cont3
# 3	LAN4	city4	state4	post4	cont4
# 4	LAN5	city5	state5	post5	cont5
# 5	LAN6	city6	state6	post6	cont6
# 6	LAN7	city7	state7	post7	cont7
# 7	LAN8	city8	state8	post8	cont8
# 8	LAN9	city9	state9	post9	cont9

# Example 1:
print(dataF.loc[:,"City"])

# O/P :-
# 0    city1
# 1    city2
# 2    city3
# 3    city4
# 4    city5
# 5    city6
# 6    city7
# 7    city8
# 8    city9
# Name: City, dtype: object

# Example 2:
print(dataF.loc[:,"City":"Country"])

# O/P :-
#   City	State	Postcode	Country
# 0	city1	state1	post1	cont1
# 1	city2	state2	post2	cont2
# 2	city3	state3	post3	cont3
# 3	city4	state4	post4	cont4
# 4	city5	state5	post5	cont5
# 5	city6	state6	post6	cont6
# 6	city7	state7	post7	cont7
# 7	city8	state8	post8	cont8
# 8	city9	state9	post9	cont9

# Example 3
df = dataF.loc[8:,"Postcode"]
print(df)

# O/P :-
# 8    post9
# Name: Postcode, dtype: object

# Example 4 , store the data in list 
li = list(dataF.loc[:, "State"])
print(li)

# O/P :- 
# ['state1', 'state2', 'state3', 'state4', 'state5', 'state6', 'state7', 'state8', 'state9']


# =====================================================================================================================

# 2. Now let explore some examples of position based indexing (i.e. iloc[])

# Example 1
print(dataF.iloc[1:3,1:3]) # so here it will filter the 1st and 2nd row with 1st and 2nd column

# O/P :-
#   City	State
# 1	city2	state2
# 2	city3	state3

# Example 2
print(dataF.iloc[3, 2:4]) # so here it will filter 3rd row of 2nd and 4th column value

# O/P :-
# State       state4
# Postcode     post4
# Name: 3, dtype: object

# =========================================================================================

# More examples of filtering the data from dataFrames , lets explore this 
# Example of adding a dict in a pandas DataFrame
# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country':names, 'drives_right':dr, 'cars_per_cap':cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)
print(cars)

# O/P :- 
#          country  drives_right  cars_per_cap
# 0  United States          True           809
# 1      Australia         False           731
# 2          Japan         False           588
# 3          India         False            18
# 4         Russia          True           200
# 5        Morocco          True            70
# 6          Egypt          True            45


# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars.loc[:,"country":"drives_right"])

# O/P :- 
# 0    United States
# 1        Australia
# 2            Japan
# 3            India
# 4           Russia
# 5          Morocco
# 6            Egypt
# Name: country, dtype: object
#          country
# 0  United States
# 1      Australia
# 2          Japan
# 3          India
# 4         Russia
# 5        Morocco
# 6          Egypt
#          country  drives_right
# 0  United States          True
# 1      Australia         False
# 2          Japan         False
# 3          India         False
# 4         Russia          True
# 5        Morocco          True
# 6          Egypt          True


# Print out first 3 observations
print(cars.iloc[0:3])

# Print out fourth, fifth and sixth observation
print(cars.iloc[3:6])

# O/P :- 
#          country  drives_right  cars_per_cap
# 0  United States          True           809
# 1      Australia         False           731
# 2          Japan         False           588
#    country  drives_right  cars_per_cap
# 3    India         False            18
# 4   Russia          True           200
# 5  Morocco          True            70


# Print out observation for Japan
print(cars.iloc[2])

# Print out observations for Australia and Egypt i.e. the dataFrame of the data inbetween Australia and Egypt
print(cars.iloc[[1,6]])

# O/P :- 
# country         Japan
# drives_right    False
# cars_per_cap      588
# Name: 2, dtype: object
#      country  drives_right  cars_per_cap
# 1  Australia         False           731
# 6      Egypt          True            45

# Print out drives_right column as Series
print(cars.iloc[:, 2])

# Print out drives_right column as DataFrame
print(cars[['drives_right']])

# Print out cars_per_cap and drives_right as DataFrame
print(cars[['cars_per_cap','drives_right']])

# O/P :-
# 0    809
# 1    731
# 2    588
# 3     18
# 4    200
# 5     70
# 6     45
# Name: cars_per_cap, dtype: int64
#    drives_right
# 0          True
# 1         False
# 2         False
# 3         False
# 4          True
# 5          True
# 6          True
#    cars_per_cap  drives_right
# 0           809          True
# 1           731         False
# 2           588         False
# 3            18         False
# 4           200          True
# 5            70          True
# 6            45          True


# ================================================================================================
# One More Example 

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


# Import cars data
import pandas as pd

# Extract drives_right column as Series and store as dr
dr = cars['drives_right']
print(dr)

# Use dr, a boolean Series, to subset the cars DataFrame. Store the resulting selection in selF for false and selT for True.

selT = cars[dr == True]
selF = cars[dr == False]

# Print sel
print(selT)
print(selF)

# Even you can use the above code in one liner code as well 
selOneT = cars[cars['drives_right'] == True]
selOneF = cars[cars['drives_right'] == False]
print(selOneT)
print(selOneF)


# O/P :- 
# US      True
# AUS    False
# JAP    False
# IN     False
# RU      True
# MOR     True
# EG      True
# Name: drives_right, dtype: bool
#      cars_per_cap         country  drives_right
# US            809  United States           True
# RU            200          Russia          True
# MOR            70         Morocco          True
# EG             45           Egypt          True
#      cars_per_cap    country  drives_right
# AUS           731  Australia         False
# JAP           588      Japan         False
# IN             18      India         False
#      cars_per_cap         country  drives_right
# US            809  United States           True
# RU            200          Russia          True
# MOR            70         Morocco          True
# EG             45           Egypt          True
#      cars_per_cap    country  drives_right
# AUS           731  Australia         False
# JAP           588      Japan         False
# IN             18      India         False

# Create car_maniac: observations that have a cars_per_cap grater than 500
car_maniac = cars[cars['cars_per_cap'] > 500]

# Print car_maniac
print(car_maniac)

# O/P :- 
#      cars_per_cap         country  drives_right
# US            809  United States           True
# AUS           731       Australia         False
# JAP           588           Japan         False

import numpy as np
# Create medium: observations with cars_per_cap between 100 and 500  and its a oneliner code 
medium = cars[np.logical_and(cars['cars_per_cap'] > 100, cars['cars_per_cap'] < 500)]

# Print medium
print(medium)

# O/P :- 
#     cars_per_cap country  drives_right
# RU           200  Russia          True