import numpy as np
import xlrd
import matplotlib.pyplot as plt
import pylab

book = xlrd.open_workbook('h3_pre_glue01.xls')
sheet = book.sheet_by_index(0)

total_rows = sheet.nrows
total_columns = sheet.ncols
colz1=[]
colz2=[]


for row in range(sheet.nrows):
    colz1.append(sheet.cell_value(row,3))

for row in range(sheet.nrows):
    colz2.append(sheet.cell_value(row,9))


new_colz1=[x for x in colz1 if isinstance(x, float)]
new_colz2=[x for x in colz2 if isinstance(x, float)]
len_new_colz1 = len(colz1)
len_new_colz2 = len(colz2)
even_indexes_colz1 = range(0,len_new_colz1,2)
even_indexes_colz2 = range(0,len_new_colz2,2)
actual_colz1 = [e for i, e in enumerate(new_colz1) if i in even_indexes_colz1]
actual_colz2 = [e for i, e in enumerate(new_colz2) if i in even_indexes_colz2]
tot_actual_z = [None]*(len(actual_colz1)+len(actual_colz2))
tot_actual_z[::2] = actual_colz1
tot_actual_z[1::2] = actual_colz2
average_z=[]
for i in range(4,len(tot_actual_z),5):
    average_z.append(np.mean(tot_actual_z[i:(i+5)]))
plt.figure(1)
plt.plot(average_z)
plt.xlabel('Asic position')
plt.ylabel('Height in mm')
plt.title('Asic pad height')


#Save the Asic number and the average z in two columns into a text file
 
datafile_path = "z_height.txt"
datafile_id = open(datafile_path, 'w+')
#here you open the ascii file
 
asic_number= np.arange(10)
xarray = np.array(asic_number)
yarray = np.array(average_z)

#here is your data, in two numpy arrays
data = np.array([xarray, yarray])
data = data.T

#print data
#here you transpose your data, so to have it in two columns
  
np.savetxt(datafile_id, data, fmt=['%d','%0.4f'])
#here the ascii file is populated. 
 
datafile_id.close()
#close the file

plt.show()