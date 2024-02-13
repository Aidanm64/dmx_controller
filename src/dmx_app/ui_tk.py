from tkinter import *
from tkinter import ttk

from dmx_app.service import DMXService
from PyDMXControl.controllers import 


class SpotlightView:

    def __init__(self):

class App:

    def __init__(self, window=Tk(), dmx_service=DMXService()):
        self.window = window
        self.dmx_service = dmx_service

        self.window.title("DMX App")
        self.window.geometry("400x300+10+10")


    def start(self):
        self.window.mainloop()



def run():
    dmx_service = DMXService(dmx=)
    app = App()
