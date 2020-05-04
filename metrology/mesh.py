import csv
import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('tr.csv')
X =df['x']
Y =df['y']
Z =df['z']



# Plot X,Y,Z
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(X, Y, Z, color='white', edgecolors='grey', alpha=0.5)
ax.scatter(X, Y, Z, c='red')
plt.show()