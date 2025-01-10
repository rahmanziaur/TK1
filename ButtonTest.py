import tkinter as tk

r = tk.Tk()
r.title('Counting Seconds')
button = tk.Button(r, text='Submit', width=75, command=r.destroy)
button.pack()
r.mainloop()