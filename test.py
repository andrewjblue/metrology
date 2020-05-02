# import tkinter module
import os
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox, filedialog


master = Tk()
master.title("Base")



def open():
    global my_image
    global pp
    master.filename = filedialog.askopenfilename(title="Select a file", filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
    pp = master.filename
    # het filename from location
    pp_filename = os.path.basename(pp)
    # populate e1 with file location
    e1.insert(0, pp_filename)

    return

def process():
    os.system('python z_data.py ' + pp)



# this will create a label widget
l1 = Label(master, text="CSV File path")

# grid method to arrange labels in respective
# rows and columns as specified
l1.grid(row=0, column=0, sticky=W, pady=2)

# entry widgets, used to take entry from user
e1 = Entry(master)

# this will arrange entry widgets
e1.grid(row=0, column=1, pady=2)



# adding image (remember image should be PNG and not JPG)
img = PhotoImage(file=r"logo.png")
img1 = img.subsample(1, 1)

# setting image with the help of label
Label(master, image=img1).grid(row=0, column=2,
                               columnspan=2, rowspan=2, padx=5, pady=5)

# button widget
b1 = Button(master, text="Choose File", command=open)
b2 = Button(master, text="Process", command=process)
b3 = Button(master, text="Quit", command=quit)


# arranging button widgets
b1.grid(row=1, column=0, sticky=E)
b2.grid(row=1, column=1, sticky=W)
b3.grid(row=2, column=3, sticky=E)



mainloop()
