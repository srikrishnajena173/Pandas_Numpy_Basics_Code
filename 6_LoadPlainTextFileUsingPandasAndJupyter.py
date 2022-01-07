# In this file all the below commands are written in the Jupyter NoteBook
# We are loading the plain text File in Jupyter Notebook using pandas methods


import pandas

# 1. Below example to read a txt file which is seperated by comma (,)
dataFrame3 = pandas.read_csv("pandaplaintextfile.txt")
dataFrame3
# O/P :- 
#  ID	Address	City	State
# 0	1	LAN1	city1	state1
# 1	2	LAN2	city2	state2
# 2	3	LAN3	city3	state3

# pandas.read_csv? , command to see the signature of the read_csv function

# 2. Below example to read a text file which is seperated by semi-colon (;)
dataFrame5 = pandas.read_csv("pandasplaintextfilewithsemicolounseperator.txt",sep=";")
dataFrame5
# So, by deafult the read_csv create the table if the data seperate the comma (,).
# But if anything is aprat from the comma and we using any other seprator then we have call sep=":" or sep";"


# 3. Below is the example to read a text file which dont have any header in the column
dataFrame6 = pandas.read_csv("pandasplaintextwithoutheader.txt",header=None)
dataFrame6

# O/P :
#   0	  1	      2	      3
# 0	1	LAN1	city1	state1
# 1	2	LAN2	city2	state2
# 2	3	LAN3	city3	state3

# 4. Below is the example of adding the headers in the dataFrame
dataFrame6.columns = ["ID", "Street", "City", "State"]
dataFrame6

#   ID	Street	City	State
# 0	1	LAN1	city1	state1
# 1	2	LAN2	city2	state2
# 2	3	LAN3	city3	state3

# 5. Below is the example of adding a new index in the dataFrame
dataFrame7 = dataFrame6.set_index("ID")
dataFrame7

#	 Street	City	State
# ID			             # So here be careful as the set_index() create a new dataFrame, its not update/modify the dataFrame
# 1	 LAN1	city1	state1
# 2	 LAN2	city2	state2
# 3	 LAN3	city3	state3


# 6. Suppose you want to store the dataFrame6 index changes in dataFrame7 variable
# Then you can use the below example
dataFrame6.set_index("ID", inplace=True)
dataFrame6 # So here the dataFrame6 modified permanetly

# O/P :-
#    Street	City	State
# ID			
# 1	 LAN1	city1	state1
# 2	 LAN2	city2	state2
# 3	 LAN3	city3	state3


dataFrame6.set_index("Street", inplace=True)
dataFrame6

# 	    City	State
# Street		
# LAN1	city1	state1
# LAN2	city2	state2
# LAN3	city3	state3, so here what is did is deleted the ID Column and add the Street, even drop the existing Street Column

# Suppose you dont want to drop the Column
dataFrame6.set_index("City", inplace=True, drop=False) # So, here it won't delete the address column
dataFrame6

# 	    City	State
# City		
# city1	city1	state1
# city2	city2	state2
# city3	city3	state3
