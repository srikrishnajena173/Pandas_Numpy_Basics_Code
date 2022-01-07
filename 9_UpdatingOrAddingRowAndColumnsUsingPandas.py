# In this file all the below commands are written in the Jupyter NoteBook

# So here in this doc we will see how to add and update the rows and columns of DataFrame
import pandas

dataF = pandas.read_csv("pandasplaintextforaddingnewcumnsandrowsindataframe.txt")
dataF

# O/P :
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

# Now we are addning the new column in the DataFrame
dataF["Continent"] = ["Continet1"]

# So now this will fail with the below error message 
# *******ValueError: Length of values (1) does not match length of index (9)***********

# So now lets see what is the index of the DataFrame
len(dataF.index)

# O/P :- 9

# So if you see the above error, we are trying to add 1 value, however, the index is 9. So we need to add
#  total 9 value for the "Continent" column

dataF["Continent"] = dataF.shape[0]*["Continent"]
dataF

# O/P :

# Address	City	State	Postcode Country Continent
# 0	LAN1	city1	state1	post1	cont1	Continent
# 1	LAN2	city2	state2	post2	cont2	Continent
# 2	LAN3	city3	state3	post3	cont3	Continent
# 3	LAN4	city4	state4	post4	cont4	Continent
# 4	LAN5	city5	state5	post5	cont5	Continent
# 5	LAN6	city6	state6	post6	cont6	Continent
# 6	LAN7	city7	state7	post7	cont7	Continent
# 7	LAN8	city8	state8	post8	cont8	Continent
# 8	LAN9	city9	state9	post9	cont9	Continent

# One more example of adding the columns values
li = []
length = len(dataF.index)
for i in range(length):
    li.append(f"Continent{i}")
    
dataF["Continentsample"] = dataF.shape[0]*[li] 
dataF

# O/P :
# Address	City	State	Postcode Country Continent	Continentsample
# 0	LAN1	city1	state1	post1	cont1	Continent	[Continent0, Continent1, Continent2, Continent...
# 1	LAN2	city2	state2	post2	cont2	Continent	[Continent0, Continent1, Continent2, Continent...
# 2	LAN3	city3	state3	post3	cont3	Continent	[Continent0, Continent1, Continent2, Continent...
# 3	LAN4	city4	state4	post4	cont4	Continent	[Continent0, Continent1, Continent2, Continent...
# 4	LAN5	city5	state5	post5	cont5	Continent	[Continent0, Continent1, Continent2, Continent...
# 5	LAN6	city6	state6	post6	cont6	Continent	[Continent0, Continent1, Continent2, Continent...
# 6	LAN7	city7	state7	post7	cont7	Continent	[Continent0, Continent1, Continent2, Continent...
# 7	LAN8	city8	state8	post8	cont8	Continent	[Continent0, Continent1, Continent2, Continent...
# 8	LAN9	city9	state9	post9	cont9	Continent	[Continent0, Continent1, Continent2, Continent...


# Example of updating the data, so here we concatenating the Country column value, sepreated with the comma(,)
# and a String value called "America"
dataF["Continent"] = dataF["Country"] + "," + "America"
dataF

# O/P :

# Address	City	State	Postcode Country	Continent	Continentsample
# 0	LAN1	city1	state1	post1	cont1	cont1,America	[Continent0, Continent1, Continent2, Continent...
# 1	LAN2	city2	state2	post2	cont2	cont2,America	[Continent0, Continent1, Continent2, Continent...
# 2	LAN3	city3	state3	post3	cont3	cont3,America	[Continent0, Continent1, Continent2, Continent...
# 3	LAN4	city4	state4	post4	cont4	cont4,America	[Continent0, Continent1, Continent2, Continent...
# 4	LAN5	city5	state5	post5	cont5	cont5,America	[Continent0, Continent1, Continent2, Continent...
# 5	LAN6	city6	state6	post6	cont6	cont6,America	[Continent0, Continent1, Continent2, Continent...
# 6	LAN7	city7	state7	post7	cont7	cont7,America	[Continent0, Continent1, Continent2, Continent...
# 7	LAN8	city8	state8	post8	cont8	cont8,America	[Continent0, Continent1, Continent2, Continent...
# 8	LAN9	city9	state9	post9	cont9	cont9,America	[Continent0, Continent1, Continent2, Continent...



# Example of how to add a new row and there is no direct method to add the rows in the DataFrame, 
# so we have work around to perform this action, that means the rows become columns and columns became rows
data_New = dataF.T # here T mean transpose the array dimension 
data_New
# O/P :
# 	        0	     1	    2	    3	    4	    5	    6	    7	   8
# Address	LAN1	LAN2	LAN3	LAN4	LAN5	LAN6	LAN7	LAN8	LAN9
# City	    city1	city2	city3	city4	city5	city6	city7	city8	city9
# State	    state1	state2	state3	state4	state5	state6	state7	state8	state9
# Postcode	post1	post2	post3	post4	post5	post6	post7	post8	post9
# Country	cont1	cont2	cont3	cont4	cont5	cont6	cont7	cont8	cont9
# Continent	cont1,America	cont2,America	cont3,America	cont4,America	cont5,America	cont6,America	cont7,America	cont8,America	cont9,America
# Continentsample	[Continent0, Continent1, Continent2, Continent...	[Continent0, Continent1, Continent2, Continent...	[Continent0, Continent1, Continent2, Continent...	[Continent0, Continent1, Continent2, Continent...	[Continent0, Continent1, Continent2, Continent...	[Continent0, Continent1, Continent2, Continent...	[Continent0, Continent1, Continent2, Continent...	[Continent0, Continent1, Continent2, Continent...	[Continent0, Continent1, Continent2, Continent...

# Now add the new data in new Column called MyAddress and the length of the new data should be same
# as the index of column which is 7.
data_New["MyAdress"] = ["MyAddress", "MyCity", "MyState", "MyPostcode", "MyCountry", "MyContinent", "MyContinentSample"]
data_New

# O/P 
# 	         0	     1	     2	    3	    4	    5	    6	    7	    8	   MyAdress
# Address	LAN1	LAN2	LAN3	LAN4	LAN5	LAN6	LAN7	LAN8	LAN9	MyAddress
# City	city1	city2	city3	city4	city5	city6	city7	city8	city9	MyCity
# State	state1	state2	state3	state4	state5	state6	state7	state8	state9	MyState
# Postcode	post1	post2	post3	post4	post5	post6	post7	post8	post9	MyPostcode
# Country	cont1	cont2	cont3	cont4	cont5	cont6	cont7	cont8	cont9	MyCountry
# Continent	cont1,America	cont2,America	cont3,America	cont4,America	cont5,America	cont6,America	cont7,America	cont8,America	cont9,America	MyContinent
# Continentsample	[Continent0, Continent1, Continent2, Continent...	[Continent0, Continent1, Continent2, Continent...	[Continent0, Continent1, Continent2, Continent...	[Continent0, Continent1, Continent2, Continent...	[Continent0, Continent1, Continent2, Continent...	[Continent0, Continent1, Continent2, Continent...	[Continent0, Continent1, Continent2, Continent...	[Continent0, Continent1, Continent2, Continent...	[Continent0, Continent1, Continent2, Continent...	My


# Now again convert the columns into rows and rows into columns using T  function (transpose)
dataF = data_New.T
dataF

# O/P 
# Address	City	State	Postcode	Country	Continent	Continentsample
# 0	LAN1	city1	state1	post1	cont1	cont1,America	[Continent0, Continent1, Continent2, Continent...
# 1	LAN2	city2	state2	post2	cont2	cont2,America	[Continent0, Continent1, Continent2, Continent...
# 2	LAN3	city3	state3	post3	cont3	cont3,America	[Continent0, Continent1, Continent2, Continent...
# 3	LAN4	city4	state4	post4	cont4	cont4,America	[Continent0, Continent1, Continent2, Continent...
# 4	LAN5	city5	state5	post5	cont5	cont5,America	[Continent0, Continent1, Continent2, Continent...
# 5	LAN6	city6	state6	post6	cont6	cont6,America	[Continent0, Continent1, Continent2, Continent...
# 6	LAN7	city7	state7	post7	cont7	cont7,America	[Continent0, Continent1, Continent2, Continent...
# 7	LAN8	city8	state8	post8	cont8	cont8,America	[Continent0, Continent1, Continent2, Continent...
# 8	LAN9	city9	state9	post9	cont9	cont9,America	[Continent0, Continent1, Continent2, Continent...
# MyAdress	MyAddress	MyCity	MyState	MyPostcode	MyCountry	MyContinent	MyContinentSample