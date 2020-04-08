import tkinter
import threading
from tkinter import *
from PC.start import Start
from PC.stop import Stop
from PC.Network.tcp_recieve import TCP_Recieve


class GUI:

    def __init__(self):
        self.start_thread = None
        self.stop_thread = None
        self.start_server_thread = None

        self.main_window = tkinter.Tk()
        self.main_window.title("Remote LIDAR")
        self.main_window.minsize(250, 100)

        # initialize buttons
        button_start = tkinter.Button(self.main_window, text="Start Scan", command=self.start)
        button_stop = tkinter.Button(self.main_window, text="Stop", command=self.stop)
        button_start_server = tkinter.Button(self.main_window, text="Start Server", command=self.start_server)

        button_start.config(height=1, width=15)
        button_stop.config(height=1, width=15)
        button_start_server.config(height=1, width=15)

        button_stop.pack(side=BOTTOM)
        button_start.pack(side=BOTTOM)
        button_start_server.pack(side=BOTTOM)

    def start(self):
        print('Starting Scan')
        self.start_thread = threading.Thread(target=Start.start)
        self.start_thread.start()

    def stop(self):
        print("Stopping Scan")
        self.stop_thread = threading.Thread(target=Stop.stop)
        self.stop_thread.start()

    def start_server(self):
        print("Starting Server")
        self.start_server_thread = threading.Thread(target=TCP_Recieve.get_file)
        self.start_server_thread.start()


gui = GUI()
# TCP_Recieve.get_file()
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
