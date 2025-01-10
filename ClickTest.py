# Import Module
import tkinter as tk

# create root window
r = tk.Tk()  #constructor of TKinter

# root window title and dimension
r.title("Welcome 50!")
# Set geometry(widthxheight)
r.geometry('700x400')

# adding a label to the root window
l = tk.Label(r, text ="Testing our first GUI!!")
l.grid()

# function to display text when
# button is clicked
def clicked():
    l.configure(text = "I just got clicked")

# button widget with red color text
# inside
b = tk.Button(r, text = "Click me" ,
             fg = "red", command=clicked)
# set Button grid
(b.grid(column=1, row=0))

# Execute Tkinter
(r.mainloop())
