# import tkinter module
import os
from tkinter import *  # todo finish the imports
from tkinter import filedialog

import matplotlib.pyplot as plt
import pandas as pd

master = Tk()
master.title(async "Base")


def OPEN():
    global my_image
    global pp
    master.filename = filedialog.askopenfilename(title = "Select a file",
                                                 filetypes = (("csv files", "*.csv"), ("all files", "*.*")))
    pp = master.filename
    pp_filename = os.path.basename(pp)
    e1.insert(0, pp_filename)

    return

def process_h():
    df = pd.read_csv(pp)
    hist_plot = df['z'].hist(bins = (int(len(df) / 50)))
    hist_plot.set_title('Z height Histogram')
    hist_plot.set_xlabel('Z height (microns)')
    hist_plot.set_ylabel('Counts')
    hist_plot.plot()
    plt.show()

def process_d():
    df = pd.read_csv(pp)
    df['z'].plot(kind = 'density', figsize = (14, 6))
    plt.show()

def process_s():
    df = pd.read_csv(pp)
    X = df['x']
    Y = df['y']
    Z = df['z']
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    # ax.plot_surface(X, Y, Z, color='white', edgecolors='grey', alpha=0.5)
    ax.set_title('Surface Plot')
    ax.scatter(X, Y, Z, c = 'blue')
    plt.show()


# this will create a label widget
l1 = Label(master, text = "CSV File path")

# grid method to arrange labels in respective
# rows and columns as specified
l1.grid(row = 0, column = 0, sticky = W, pady = 2)

# entry widgets, used to take entry from user
e1 = Entry(master)

# this will arrange entry widgets
e1.grid(row = 0, column = 1, pady = 2)

# adding image (remember image should be PNG and not JPG)
img = PhotoImage(file = r"logo.png")
img1 = img.subsample(1, 1)

# setting image with the help of label
Label(master, image = img1).grid(row = 0, column = 2,
                                 columnspan = 2, rowspan = 2, padx = 5, pady = 5)

# button widget
b1 = Button(master, text = "Choose CSV File", command = OPEN)
b2 = Button(master, text = "Histogram", command = process_h)
b5 = Button(master, text = "Surface Plot", command = process_s)
b6 = Button(master, text = "Density Plot", command = process_d)
b3 = Button(master, text = "Quit", command = quit)

# arranging button widgets
b1.grid(row = 1, column = 0, columnspan = 3, sticky = W)
b2.grid(row = 2, column = 0, sticky = E)
b3.grid(row = 2, column = 3, sticky = E)
b5.grid(row = 2, column = 1, sticky = W)
b6.grid(row = 2, column = 3, sticky = W)

mainloop()
