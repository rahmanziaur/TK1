import tkinter as tk
import threading
import time

# Initialize the main window
r = tk.Tk()
r.title('Counting Seconds')

# Create and pack the label to display the seconds
l = tk.Label(r, text='0')
l.pack()

# Variables to control the timer
running = False
seconds = 0

# Function to count seconds
def count_seconds():
    global seconds, running
    while running:
        time.sleep(1)
        seconds += 1
        l.config(text=str(seconds))

# Start button click event
def start_counting():
    global running, seconds
    if not running:
        running = True
        threading.Thread(target=count_seconds, daemon=True).start()

# Stop button click event
def stop_counting():
    global running
    running = False

# Reset button click event
def reset_counting():
    global running, seconds
    running = False  # Stop counting
    seconds = 0      # Reset the seconds to 0
    l.config(text='0')  # Update the label

# Create and pack the "Start" button
start_button = tk.Button(r, text='Start', width=20, command=start_counting)
start_button.pack()

# Create and pack the "Stop" button
stop_button = tk.Button(r, text='Stop', width=20, command=stop_counting)
stop_button.pack()

# Create and pack the "Reset" button
reset_button = tk.Button(r, text='Reset', width=20, command=reset_counting)
reset_button.pack()

# Run the main loop
r.mainloop()
