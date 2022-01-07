import pandas as pd
import numpy as np
# And suppose you want to iterate through irregularly nested lists inside list also.
def traverse(o, tree_types=(list, tuple)):
    if isinstance(o, tree_types):
        for value in o:
            for subvalue in traverse(value, tree_types):
                yield subvalue
    else:
        yield o


data = [(1,1,(1,1,(1,"1"))),(1,1,1),(1,),1,(1,(2,("1",)))]
# Here calling the function 
for value in traverse(data):
    print (value)
