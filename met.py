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

mainloop()

