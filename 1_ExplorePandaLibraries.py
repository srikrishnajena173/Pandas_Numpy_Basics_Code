# NOTE :- Pandas is a high level data manipulation tool which is a wrapper of numpy
# (that means pandas is build on numpy)
# First we installed pandas in our system using the below command :
# pip3.8 install pandas
# Then we install the ipython using the below command :
# pip3.8 install ipython
# Which is good for data analysis and even better is jupeter notebook, its like a python shell
import pandas

# 1. So now in the below examples we will be creating some data using pandas library
# Suppose we are now storing the data in dataframe1 varaible
dataFrame1=pandas.DataFrame([[2, 4, 5],[20, 30, 40]])
print(dataFrame1)

# O/P :
#     0   1   2
# 0   2   4   5
# 1  20  30  40
# So in the above output is structured in a Mutli-Dimension format

# So here below is the type
# In [4]: type(dataFrame1)
# Out[4]: pandas.core.frame.DataFrame, so here the dataFrame1 is the object of pandas DataFrame

# With the below command you will get the functions associated with dataFrame1 or pandas.core.frame.DataFrame object
# In [5]: dir(dataFrame1)
# So, we will get multiple mathematical formual methods , lets find the mean of the dataFrame1
print(dataFrame1.mean())
# O/P :-
# 0    11.0
# 1    17.0
# 2    22.5, so here the output is the mean of each column

# In [6]: type(dataFrame1.mean())
# Out[6]: pandas.core.series.Series , so dataFrame1.mean() is object of pandas Series

# So suppose now we have to find the mean of all values in dataFrame
val=dataFrame1.mean()
print(val.mean())
# O/P :- 16.833333333333332


# 2. Example of creating your own column names
dataFrame2=pandas.DataFrame([[2, 4, 5],[20, 30, 40]], columns=["price","age","valeu"])
print(dataFrame2)

# O/P :-
#    price  age  valeu
# 0      2    4      5
# 1     20   30     40

print(dataFrame2.price)
# O/P :-
# 0     2
# 1    20, so here the output is the value of price column

# Now find the mean of the price column
print(dataFrame2.price.mean())
# O/P : 11.0

# 3. You can have row name as well
dataFrame3=pandas.DataFrame([[2, 4, 5],[20, 30, 40]], columns=["price","age","valeu"], index=["first","second"])
print(dataFrame3)

# O/P :-
#         price  age  valeu
# first       2    4      5
# second     20   30     40

# 4. You can create in the below way as well
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pandas.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)

# O/P :
#       calories  duration
# day1       420        50
# day2       380        40
# day3       390        45

print(df.loc["day2"])
# O/P
# calories    380
# duration     40

# Define a Dictonary in pandas Date Frame
dataFrame4 = pandas.DataFrame([{"Name":"Antony", "surenme":"josh"},{"Name":"jack"}])
print(dataFrame4)
# O/P :
#      Name   surenme
# 0  Antony    josh
# 1    jack     NaN

##########################################################################################################
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

# Print cars
print(cars)

# O/P :-
#    cars_per_cap        country  drives_right
# 0           809  United States          True
# 1           731      Australia         False
# 2           588          Japan         False
# 3            18          India         False
# 4           200         Russia          True
# 5            70        Morocco          True
# 6            45          Egypt          True

# Suppose now you want to add the row labels to the above dataframe
# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)

# O/P :- 
#            country  drives_right  cars_per_cap
# US   United States          True           809
# AUS      Australia         False           731
# JPN          Japan         False           588
# IN           India         False            18
# RU          Russia          True           200
# MOR        Morocco          True            70
# EG           Egypt          True            45

# Now suppose you want to get the column 
print(cars['country'])

# O/P :- 
# US     United States
# AUS        Australia
# JPN            Japan
# IN             India
# RU            Russia
# MOR          Morocco
# EG             Egypt
# Name: country, dtype: object

# Now suppose you want to check the type of the cars['country']
type(cars['country'])

# O/P :- pandas.core.series.Series
# which means the its return the series 

# Now suppose you want to return the data as dataFrame, then use [[]] double square barket
print(cars[['country']])

# O/P :- 
#            country
# US   United States
# AUS      Australia
# JPN          Japan
# IN           India
# RU          Russia
# MOR        Morocco
# EG           Egypt

type(cars[['country']])
# pandas.core.frame.DataFrame, which means the retun type is dataFrame

