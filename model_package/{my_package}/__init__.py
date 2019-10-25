import logging
logging.getLogger("{my_package}").addHandler(logging.NullHandler())

from .version import __version__

from . import utils
