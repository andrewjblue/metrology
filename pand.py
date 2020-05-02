from tkinter import *
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt
root = Tk()
root.title("Plotting")
import pandas as pd

def graph():
    #house_prices =np.random.normal(200000, 25000, 5000)
    #plt.hist(house_prices, bins=50)
    df = pd.read_csv('metrology/tr.csv')
    hist_plot = df['z'].hist(bins =100)
    hist_plot.set_title('X height Histo')
    hist_plot.set_xlabel('Z height (um)')
    hist_plot.set_ylabel('Counts')
    hist_plot.plot()
    plt.show()

my_btn= Button(root, text = 'graph', command=graph)
my_btn.pack()


root.mainloop()