# In this file all the below commands are written in the Jupyter NoteBook
# We are loading the Excel File in Jupyter Notebook using pandas methods

# Offcourse you need pandas to read the excel file in python, as well as you need the below dependencies also:
# pip3.8 install openpyxl
# pip3.8 install xlrd

import pandas

dataFrame2 = pandas.read_excel("pandaexcelfile.xlsx", sheet_name=0) # The excel sheet will consider as index
dataFrame2