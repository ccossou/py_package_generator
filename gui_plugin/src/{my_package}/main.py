import tkinter as tk

from . import gui
from . import utils

import logging

LOG = logging.getLogger(__name__)


def run():
    """
    Run the main application
    """

    utils.init_log()

    root = tk.Tk()
    app = gui.Application(master=root)

    app.mainloop()
