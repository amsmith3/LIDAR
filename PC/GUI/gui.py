import tkinter
from tkinter import *

# initialize main window
main_window = tkinter.Tk()
main_window.title("Remote LIDAR")
main_window.minsize(250, 100)

# initialize buttons
button_start = tkinter.Button(main_window, text="Start")
button_stop = tkinter.Button(main_window, text="Stop")

button_start.config(height=1, width=15)
button_stop.config(height=1, width=15)

button_stop.pack(side=BOTTOM)
button_start.pack(side=BOTTOM)

main_window.mainloop()