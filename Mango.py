from tkinter import *
from tkinter import messagebox
from datetime import datetime
import webbrowser
import tkinter as tk
from tkinter import ttk

import os
from user import *


# Change bg color


# Window
window = Tk()
window.title("Mango V0")
window.configure(width=500, height=500, bg = "lightblue")
#Retun
def beluga():
    os.system('python beluga.py')
    exit()
B1 = Button(window, text = "Home",command = beluga)
B1.pack()

#setup
def setup():
    messagebox.showinfo("Mission Complete","Done")
    # issue setup must get fixed
B2 = Button(window, text = "Launch Setup",command = setup)
B2.pack()

window.mainloop()
