import tkinter as tk

r = tk.Tk()
r.title('Counting Seconds')
l = tk.Label(r, text='Counting Seconds')
l.pack()

def clicked():
    l.configure(text='I got clicked!')

button = tk.Button(r, text='Submit', width=75, command=clicked)
button.pack()


r.mainloop()