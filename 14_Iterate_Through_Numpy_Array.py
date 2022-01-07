import numpy as np
from numpy.lib.function_base import i0

height = np.array([12.3, 34.4, 34.3, 23.33, 23])
weight = np.array([334.3, 324.55, 444.55, 344.4, 344.9])

val = np.array([height, weight])

for i in np.nditer(val):
    print(i)

# O/P :-
# 12.3
# 34.4
# 34.3
# 23.33
# 23.0
# 334.3
# 324.55
# 444.55
# 344.4
# 344.9

# OR
 
for i in val.flat:  # OR you can use flat to loop over the each and every element 
    print(i)
