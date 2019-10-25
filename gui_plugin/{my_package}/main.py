import tkinter as tk

from . import gui
from . import version

import logging

LOG = logging.getLogger(__name__)


def run():
    """
    Run the main application
    """

    root = tk.Tk()
    root.title("{my_package} v{}".format(version.__version__))
    app = gui.Application(master=root)
    app.mainloop()
