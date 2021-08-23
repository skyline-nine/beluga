from tkinter import *
from tkinter import messagebox
from datetime import datetime
import webbrowser
import tkinter as tk
from tkinter import ttk


# find time
now = datetime.now()

# window options
window = Tk()
window.title("Beluga V0.4")
window.configure(width=500, height=500)
window.configure(bg='lightblue')

# display time
def st():
    messagebox.showinfo("Time", now.strftime("%H:%M:%S"))
B1 = Button(window, text = "Time", command = st)
B1.grid(column=1, row=1)

# display date
def sd():
    messagebox.showinfo("Date", now.strftime("%Y-%m-%d"))
B2 = Button(window, text = "Date", command = sd)
B2.grid(column=1, row=2)

# Web Sweeper
def NF():
    headcrab = Tk()
    text2 = Entry(headcrab)
    text2.pack()
    
    text2.focus_set()
    
    def recall():
        webbrowser.open(text2.get())
    B6 = Button(headcrab, text = "Search", width = 10, command = recall)
    B6.pack()
    
    mainloop()

# Show Button
B5 = Button(window, text = "Web Sweeper", command = NF)
B5.grid(column=1, row=3)

# Misc

def end():
    exit()
B4 = Button(window, text = "End Session",command = end)
B4.grid(column=1, row=4)

# display os name and version
sysver = Label(window, text = "Beluga v 0.4")
sysver.grid(column=3, row=1)


window.mainloop()

