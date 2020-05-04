import pandas as pd
from pylab import *
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

df = pd.read_csv('tr.csv')
x =df['x']
y =df['y']
z =df['z']

# make up data.
npts = 200
# define grid.
xi = np.linspace(95, 100, 100)	# 100 x grid points
yi = np.linspace(19, 21, 200)	# 200 y grid points

# mlab.griddata accepts the xi and yi 1d arrays above with different lengths.
# scipy's griddata requires a full grid array. This is created with the mgrid function.
xi, yi = np.mgrid[95:199:100j, 19:21:200j]
# grid the data.
# points = np.vstack((x,y)).T
zi = griddata((x,y), z, (xi, yi), method='cubic')
# contour the gridded data, plotting dots at the nonuniform data points.
CS = plt.contour(xi, yi, zi, 15, linewidths=0.5, colors='k')
CS = plt.contourf(xi, yi, zi, 15)
plt.colorbar()  # draw colorbar
# plot data points.
# plt.scatter(x, y, marker='o', s=5, zorder=10)
plt.xlim(95, 199)
plt.ylim(19, 21)
plt.title('griddata test (%d points)' % npts)
plt.show()