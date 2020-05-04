import xlrd
import matplotlib.pyplot as plt
import pylab
import pandas as pd

import numpy as np
import xlrd
import matplotlib.pyplot as plt
import pylab

# from openpyxl.conftest import Workbook

# how to read an excell file with python
book = xlrd.open_workbook('h3_pre_glue01.xls')

# print number of sheets
# print book.nsheets

# print sheet names
# print book.sheet_names()

# get the first worksheet
# first_sheet = book.sheet_by_index(0)

# read a row
# print first_sheet.row_values(0)

# read a cell
# cell = first_sheet.cell(0,0)
# print cell
# print cell.value

# read a row slice
# print first_sheet.row_slice(rowx=0,start_colx=0,end_colx=2)

# Get the first booksheet
sheet = book.sheet_by_index(0)

# Number of rows
total_rows = sheet.nrows
total_columns = sheet.ncols
colz1 = []
colz2 = []

# reads the excell sheet in columns
for row in range(sheet.nrows):
    colz1.append(sheet.cell_value(row, 3))
    # print sheet.cell_value(row,3)

# reads the excell sheet in columns
for row in range(sheet.nrows):
    colz2.append(sheet.cell_value(row, 9))
    # print sheet.cell_value(row,9)

print
'The first column is: ', colz1
print
'The second column is: ', colz2

# Use List comprehensions to separate the float numbers from the rest of data
new_colz1 = [x for x in colz1 if isinstance(x, float)]
print
'Only the numerical values are: ', new_colz1
new_colz2 = [x for x in colz2 if isinstance(x, float)]
print
'Only the numerical values are: ', new_colz2

# We want only the actual values (refer to excell sheet) of the z column
# which correspond to the even indexes numbers from new_colz1
len_new_colz1 = len(colz1)
# print len_new_colz1
len_new_colz2 = len(colz2)
# print len_new_colz2
# Select only the even indexes
even_indexes_colz1 = range(0, len_new_colz1, 2)
print
even_indexes_colz1
# Select only the even indexes
even_indexes_colz2 = range(0, len_new_colz2, 2)
# print even_indexes_colz2

# Select only even indexes from the list
actual_colz1 = [e for i, e in enumerate(new_colz1) if i in even_indexes_colz1]
print(actual_colz1)

actual_colz2 = [e for i, e in enumerate(new_colz2) if i in even_indexes_colz2]
print(actual_colz2)

# How to concatenate the two lists so I have one with the first element from the
# first list the second is the first element of the second list etc.
tot_actual_z = [None] * (len(actual_colz1) + len(actual_colz2))
tot_actual_z[::2] = actual_colz1
tot_actual_z[1::2] = actual_colz2
print
tot_actual_z

# Finally we create a new list with the items in the previous list averaged each 5
average_z = []
for i in range(4, len(tot_actual_z), 5):
    average_z.append(np.mean(tot_actual_z[i:(i + 5)]))
print
average_z

# Plotting the data
plt.figure(1)
plt.plot(average_z)
plt.xlabel('Asic position')
plt.ylabel('Height in mm')
plt.title('Asic pad height')

# Save the Asic number and the average z in two columns into a text file

datafile_path = "z_height.txt"
datafile_id = open(datafile_path, 'w+')
# here you open the ascii file

asic_number = np.arange(10)
xarray = np.array(asic_number)
yarray = np.array(average_z)

# here is your data, in two numpy arrays
data = np.array([xarray, yarray])
data = data.T

# print data
# here you transpose your data, so to have it in two columns

np.savetxt(datafile_id, data, fmt=['%d', '%0.4f'])
# here the ascii file is populated.

datafile_id.close()
# close the file

plt.show()