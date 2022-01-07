# Go to the pyhton terminal and write the below command to see the attributes of the data type  :-
# >>> dir(str)
# O/P :- 
# - ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
# '__getattribute__', '__getitem__', '__getnewargs__', 
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__',
# '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
# '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold',
# 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha',
# 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper',
# 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex',
# 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 
# 'upper', 'zfill']

# To know what attribute is for what purpose will get from the below python command
# >>> help(str.upper) 
# O/P :- 
# Help on method_descriptor:
# upper(self, /)
# Return a copy of the string converted to uppercase. 

# Like wise 

# >>> dir(list)
# >>> dir(int)
# >>> dir(float)

#=============================================================================================================

# Now to calculate the below avg in the list, lets see what are the attribute we can use to calculate the mean or median of the values

# NOTE :- If want to check the built-in python function like print(), type(), help(), exit() you can use the below python command 
# >>> dir(__builtins__) 

# To know what function is for what purpose will get from the below python command e.g.
# >>> help(__builtins__.StopAsyncIteration) 
# >>> help(__builtins__.min)
# Help on class StopAsyncIteration in module builtins:

from ConditionInPython import myVal


student_grade1= [10.2, 34.0, 30]

mysum = sum(student_grade1) # Sum is a inbuilt function to calculate the sum of the number
mysize = len(student_grade1) # len is a function Return the number of items in a container
meanValue = mysum / mysize
print("mean value is " + str(float(meanValue))) # concatination with string and float value and casting a float value to string

# A simple code to find the maximum value from a list using max() inbuilt function
student_grades2 = [9.1, 8.8, 7.5]
max_value = max(student_grades2)
print(max_value)


def myTemp(temp):
    if temp > 7:
       return "warm"
    else:
       return "cold"

print(myTemp(8))        
print(myTemp(6))       
print(myTemp(7))   

   
   