import tkinter
import threading
from tkinter import *
from PC.start import Start
from PC.stop import Stop


class GUI():

    def __init__(self):
        self.start_thread = None
        self.stop_thread = None

        self.main_window = tkinter.Tk()
        self.main_window.title("Remote LIDAR")
        self.main_window.minsize(250, 100)

        # initialize buttons
        button_start = tkinter.Button(self.main_window, text="Start", command=self.start)
        button_stop = tkinter.Button(self.main_window, text="Stop", command=self.stop)

        button_start.config(height=1, width=15)
        button_stop.config(height=1, width=15)

        button_stop.pack(side=BOTTOM)
        button_start.pack(side=BOTTOM)

    def start(self):
        self.start_thread = threading.Thread(target=Start.start)
        self.start_thread.start()

    def stop(self):
        self.stop_thread = threading.Thread(target=Stop.stop)
        self.stop_thread.start()


gui = GUI()
gui.main_window.mainloop()

# # initialize main window
# main_window = tkinter.Tk()
# main_window.title("Remote LIDAR")
# main_window.minsize(250, 100)
#
# # initialize buttons
# button_start = tkinter.Button(main_window, text="Start", command=Start.start)
# button_stop = tkinter.Button(main_window, text="Stop")
#
# button_start.config(height=1, width=15)
# button_stop.config(height=1, width=15)
#
# button_stop.pack(side=BOTTOM)
# button_start.pack(side=BOTTOM)
#
# main_window.mainloop()
