# In this file all the below commands are written in the Jupyter NoteBook
# Now in this doc we will see how to delete a rows and columns from DataFrame using pandas functions

# IMPORTANT NOTE : Whenever you are filtering or deleteing DataFrame using the column string or index value, 
# always create the column for that DataFrame

import pandas

# So this is our DataFrame 
dataF = pandas.read_csv("deleterowsandcolumnsscenarios.txt")
dataF


dataF.columns = ["Address", "City", "State", "Postcode", "Country"]
dataF

# O/P -
# 	Address	City	State	Postcode	Country
# 0	LAN1	city1	state1	post1	cont1
# 1	LAN2	city2	state2	post2	cont2
# 2	LAN3	city3	state3	post3	cont3
# 3	LAN4	city4	state4	post4	cont4
# 4	LAN5	city5	state5	post5	cont5
# 5	LAN6	city6	state6	post6	cont6
# 6	LAN7	city7	state7	post7	cont7
# 7	LAN8	city8	state8	post8	cont8
# 8	LAN9	city9	state9	post9	cont9

# Example 1
df1 = dataF.drop("City", 1) # so , here it is deleting the City row completely
print(df1)

# O/P :
#   Address	State	Postcode	Country
# 0	LAN1	state1	post1	cont1
# 1	LAN2	state2	post2	cont2
# 2	LAN3	state3	post3	cont3
# 3	LAN4	state4	post4	cont4
# 4	LAN5	state5	post5	cont5
# 5	LAN6	state6	post6	cont6
# 6	LAN7	state7	post7	cont7
# 7	LAN8	state8	post8	cont8
# 8	LAN9	state9	post9	cont9

# Example 2 
df2 = dataF.drop(2) # so , here it delete till 2nd index row
print(df2)

# O/P - 
#   Address	City	State	Postcode	Country
# 0	LAN1	city1	state1	post1	cont1
# 1	LAN2	city2	state2	post2	cont2
# 3	LAN4	city4	state4	post4	cont4
# 4	LAN5	city5	state5	post5	cont5
# 5	LAN6	city6	state6	post6	cont6
# 6	LAN7	city7	state7	post7	cont7
# 7	LAN8	city8	state8	post8	cont8
# 8	LAN9	city9	state9	post9	cont9

# Example 3
df3 = dataF.drop(dataF.index[0:5],0) # so, here it deleting all the rows from 0th index till 5th index
print(df3)

# O/P :
# 	Address	City	State	Postcode	Country
# 5	LAN6	city6	state6	post6	cont6
# 6	LAN7	city7	state7	post7	cont7
# 7	LAN8	city8	state8	post8	cont8
# 8	LAN9	city9	state9	post9	cont9


# IMPORTANT NOTE : Whenever you are filtering or deleteing DataFrame using the column string or index value, 
# always create the column for that DataFrame

# Example 4 :- 
dataF.drop(dataF.columns[0:3],1) # so here the it is deleting the columns from 0th index to 2nd index

# O/P
#   Postcode	Country
# 0	post2	cont2
# 1	post3	cont3
# 2	post4	cont4
# 3	post5	cont5
# 4	post6	cont6
# 5	post7	cont7
# 6	post8	cont8
# 7	post9	cont9


dataF.index # gives you the information on the index length

# O/P :
# RangeIndex(start=0, stop=8, step=1)

dataF.columns # gives you columns info 

# O/P :
#Index(['Address', 'City', 'State', 'Postcode', 'Country'], dtype='object')