# import tkinter module
import os
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox, filedialog
import matplotlib.pyplot as plt
import pandas as pd
import xlrd
import numpy as np

master = Tk()
master.title("Base")


def open():
    global my_image
    global pp
    master.filename = filedialog.askopenfilename(title="Select a file",
                                                 filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
    pp = master.filename
    # het filename from location
    pp_filename = os.path.basename(pp)
    # populate e1 with file location
    e1.insert(0, pp_filename)

    return

def open_x():
    global ppx
    master.filename = filedialog.askopenfilename(title="Select a file",
                                                 filetypes=(("xls files", "*.xls"), ("all files", "*.*")))
    ppx = master.filename
    # het filename from location
    ppx_filename = os.path.basename(ppx)
    # populate e1 with file location
    e2.insert(0, ppx_filename)

    return


def process():
    # os.system('python z_data.py ' + pp)
    df = pd.read_csv(pp)
    hist_plot = df['z'].hist(bins=100)
    hist_plot.set_title('X height Histo')
    hist_plot.set_xlabel('Z height (um)')
    hist_plot.set_ylabel('Counts')
    hist_plot.plot()
    plt.show()

def processx():
    book = xlrd.open_workbook(ppx)
    sheet = book.sheet_by_index(0)
    total_rows = sheet.nrows
    total_columns = sheet.ncols
    colz1 = []
    colz2 = []
    for row in range(sheet.nrows):
        colz1.append(sheet.cell_value(row, 3))
    for row in range(sheet.nrows):
        colz2.append(sheet.cell_value(row, 9))

    new_colz1 = [x for x in colz1 if isinstance(x, float)]
    new_colz2 = [x for x in colz2 if isinstance(x, float)]
    len_new_colz1 = len(colz1)
    len_new_colz2 = len(colz2)
    even_indexes_colz1 = range(0, len_new_colz1, 2)
    even_indexes_colz2 = range(0, len_new_colz2, 2)
    actual_colz1 = [e for i, e in enumerate(new_colz1) if i in even_indexes_colz1]
    actual_colz2 = [e for i, e in enumerate(new_colz2) if i in even_indexes_colz2]
    tot_actual_z = [None] * (len(actual_colz1) + len(actual_colz2))
    tot_actual_z[::2] = actual_colz1
    tot_actual_z[1::2] = actual_colz2
    average_z = []
    for i in range(len(tot_actual_z), 4, 5):
        average_z.append(np.mean(tot_actual_z[i:(i + 5)]))
    plt.figure(1)
    plt.plot(average_z)
    plt.xlabel('Asic position')
    plt.ylabel('Height in mm')
    plt.title('Asic pad height')
    plt.show()

# this will create a label widget
l1 = Label(master, text="CSV File path")
l2 = Label(master, text="XLS File path")

# grid method to arrange labels in respective
# rows and columns as specified
l1.grid(row=0, column=0, sticky=W, pady=2)
l2.grid(row=2, column=0, sticky=W, pady=2)

# entry widgets, used to take entry from user
e1 = Entry(master)
e2 = Entry(master)

# this will arrange entry widgets
e1.grid(row=0, column=1, pady=2)
e2.grid(row=2, column=1, pady=2)

# adding image (remember image should be PNG and not JPG)
img = PhotoImage(file=r"logo.png")
img1 = img.subsample(1, 1)

# setting image with the help of label
Label(master, image=img1).grid(row=0, column=2,
                               columnspan=2, rowspan=2, padx=5, pady=5)

# button widget
b1 = Button(master, text="Choose CSV File", command=open)
b2 = Button(master, text="Process", command=process)
b4 = Button(master, text="Choose XLS File", command=open_x)
b5 = Button(master, text="Process", command=processx)

b3 = Button(master, text="Quit", command=quit)


def home(self):
    btn = QPushButton('quit', self)
    btn.clicked.connect(QCoreApplication.instance().quit)
    btn.resize(100, 100)
    btn.move(100, 100)
    self.show()


# arranging button widgets
b1.grid(row=1, column=0, sticky=E)
b2.grid(row=1, column=1, sticky=W)
b3.grid(row=2, column=3, sticky=E)
b4.grid(row=3, column=0, sticky=E)
b5.grid(row=3, column=1, sticky=W)


mainloop()
