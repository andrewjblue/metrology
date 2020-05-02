from tkinter import *  # todo finish the imports
from PIL import Image, ImageTk
from tkinter import messagebox, filedialog
import sys
import os
import csv
import matplotlib.pyplot as plt
import numpy



root = Tk()
root.title("Base")
my_img1 = ImageTk.PhotoImage(Image.open("logo.png"))

my_label=Label(image=my_img1)
my_label.grid(row=0, columnspan=3)

def open():
     global my_image
     global pp
     root.filename = filedialog.askopenfilename(initialdir="/Users/andrewjblue/PycharmProjects/giraffe3/metrology", title="Select a file", filetypes=(("csv files", "*.csv"),("all files", "*.*")))
     pp = root.filename
     pp_label = Label(root, text=pp)
     pp_label.grid(row=4, column=0, columnspan=2, padx=20, pady=(10, 0))

def process():
    os.system('python z_data.py ' + pp)

def json():
     return

f_name_label_editor = Label(root, text="Metrology File")
f_name_label_editor.grid(row=3, column=0, pady=(10, 0))
choose_btn=Button(root, text="Choose", command=open)
choose_btn.grid(row=3, column=1, pady=(10, 0))

process_btn=Button(root, text="Process", command=process)
process_btn.grid(row=5, column=0, pady=(10, 0))

json_btn=Button(root, text="Save to JSON", command=json)
json_btn.grid(row=5, column=1, pady=(10, 0))

quit_btn=Button(root, text="Quit", command=quit)
quit_btn.grid(row=6, column=1, pady=(10, 0))


# creating main tkinter window/toplevel
master = Tk()
master.title("Base")


# # this will create a label widget
# l1 = Label(master, text="CSV File path")
# l2 = Label(master, text="Width")
#
# # grid method to arrange labels in respective
# # rows and columns as specified
# l1.grid(row=0, column=0, sticky=W, pady=2)
# #l2.grid(row=1, column=0, sticky=W, pady=2)
#
# # entry widgets, used to take entry from user
# e1 = Entry(master)
# e2 = Entry(master)
#
# # this will arrange entry widgets
# e1.grid(row=0, column=1, pady=2)
# #e2.grid(row=1, column=1, pady=2)



# adding image (remember image should be PNG and not JPG)
img = PhotoImage(file=r"logo.png")
img1 = img.subsample(1, 1)

# setting image with the help of label
Label(master, image=img1).grid(row=0, column=2,columnspan=2, rowspan=2, padx=5, pady=5)

# button widget
b1 = Button(master, text="Choose File")
b2 = Button(master, text="Process")

# arranging button widgets
b1.grid(row=2, column=0, sticky=E)
b2.grid(row=2, column=1, sticky=E)



mainloop()

