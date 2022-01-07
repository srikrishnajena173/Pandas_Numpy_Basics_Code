# NOTE : Shortcut to use the block comments in VS Code is Ctrl + K and then press Ctrl + C

# In this file all the below commands are written in the Jupyter NoteBook
# We are loading the CSV File in Jupyter Notebook using pandas methods

import pandas
import os
os.listdir() # To check the list of dirctores in Jupyter Folder (C:\Users\KRISHNA\AppData\Roaming\jupyter)

# O/P :
#  ['.ipynb_checkpoints',
#  'FirstJupyterScript.ipynb',
#  'LoadCSVData.ipynb',
#  'nbconvert',
#  'nbsignatures.db',
#  'notebook_secret',
#  'runtime'] 

# Below command to read the dataframe from csv file
dataframe1 = pandas.read_csv("pandacsvfile.csv")
dataframe1
# O/P: 
#   ID	Address	City	State
# 0	1	LAN1	city1	state1
# 1	2	LAN2	city2	state2
# 2	3	LAN3	city3	state3
