from tkinter import *
from tkinter import messagebox
from datetime import datetime
import webbrowser
import tkinter as tk
from tkinter import ttk
import os
# variables

# find time
now = datetime.now()

# window options
window = Tk()
window.title("Beluga V0.6")
window.configure(width=500, height=500)
window.configure(bg='lightblue')

# name


# display time
def st():
    messagebox.showinfo("Time", now.strftime("%H:%M:%S"))
B1 = Button(window, text = "Time", command = st)
B1.configure(bg='lightblue')
B1.grid(column=1, row=1)

# display date
def sd():
    messagebox.showinfo("Date", now.strftime("%Y-%m-%d"))
B2 = Button(window, text = "Date", command = sd)
B2.configure(bg='lightblue')
B2.grid(column=1, row=2)

# Web Sweeper
def NF():
    NF = Tk()
    text2 = Entry(NF)
    text2.pack()
    text2.focus_set()
    
    def recall():
        webbrowser.open(text2.get())
    B7 = Button(NF, text = "Search", width = 10, command = recall)
    B7.pack()
    
    mainloop()
B5 = Button(window, text = "Web Sweeper", command = NF)
B5.configure(bg='lightblue')
B5.grid(column=1, row=3)

# Project:Mango
def Mango():
    os.system("python Mango.py")
    exit()
B6 = Button(window, text = "Project:Mango",command = Mango)
B6.grid(column=2, row=2)
# App Manager


# Shutdown
def end():
    exit()
B4 = Button(window, text = "End Session",command = end)
B4.grid(column=1, row=4)


# Misc


window.mainloop()


