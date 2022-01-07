# Below is the code to compare the numpy array 
# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
print(my_house >= 18)

# my_house less than your_house
print(my_house < your_house)

# O/P :- 
# [ True  True False False] , so this will compare the data 1 by 1 value with 18
# [False  True  True False] , so this will compare the data 0th index of 'my_house' is smaller than 0th index of your_house, likewise it will compare the values

