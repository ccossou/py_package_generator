import tkinter as tk
import logging
import os
import configobj

from . import version
from . import config

LOG = logging.getLogger(__name__)


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        homedir = os.path.expanduser("~")
        self.conf_file = os.path.join(homedir, ".{my_package}rc")

        if os.path.isfile(self.conf_file):
            self.parameters = config.get_config(self.conf_file)
        else:
            self.parameters = configobj.ConfigObj()
            self.parameters.filename = self.conf_file

        self.cancel_stack = []

        self.init_main_window()

    def init_main_window(self):
        self.master.title("{my_package} v{}".format(version.__version__))

        # Create menu
        self.menubar = tk.Menu(self.master)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.quit)

        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.editmenu = tk.Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Cancel", accelerator="Ctrl+Z", command=self.cancel_action,
                                  state=tk.DISABLED)
        self.editmenu.add_command(label="Redo", accelerator="Ctrl+Shift+Z", command=self.redo_action, state=tk.DISABLED)

        self.menubar.add_cascade(label="Edit", menu=self.editmenu)

        self.master.bind('<Control-z>', lambda event: self.cancel_action())
        self.master.bind('<Control-Shift-KeyPress-Z>', lambda event: self.redo_action())

        self.master.config(menu=self.menubar)

        w = tk.Label(self, text="Hello, world!")
        w.pack()

    def cancel_action(self):
        # TODO define what to add in the cancel stack
        self.cancel_stack.append(None)

        self.editmenu.entryconfigure('Redo', state=tk.ACTIVE)

        # TODO If cancel not possible anymore
        if False:
            self.editmenu.entryconfigure('Cancel', state=tk.DISABLED)

    def redo_action(self):
        if len(self.cancel_stack) != 0:
            self.editmenu.entryconfigure('Cancel', state=tk.ACTIVE)

            # TODO redo cancel
            current_cancel = self.cancel_stack.pop(-1)

            if len(self.cancel_stack) == 0:
                self.editmenu.entryconfigure('Redo', state=tk.DISABLED)
