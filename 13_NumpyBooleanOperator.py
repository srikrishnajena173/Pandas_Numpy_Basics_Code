# Boolean operator in numpy array 
# We have special functions for boolean operator 

# logical_and(x1, x2, /[, out, where, …]) Compute the truth value of x1 AND x2 element-wise.

# logical_or(x1, x2, /[, out, where, casting, …]) Compute the truth value of x1 OR x2 element-wise.

# logical_not(x, /[, out, where, casting, …]) Compute the truth value of NOT x element-wise.

# logical_xor(x1, x2, /[, out, where, …]) Compute the truth value of x1 XOR x2, element-wise.


# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5, my_house < 10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11, your_house < 11))