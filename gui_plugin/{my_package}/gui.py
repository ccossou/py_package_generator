import tkinter as tk
import logging

LOG = logging.getLogger(__name__)


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.__create_widgets()

    def __create_widgets(self):

        w = tk.Label(self, text="Hello, world!")
        w.pack()
