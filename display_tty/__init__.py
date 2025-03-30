##
# EPITECH PROJECT, 2024
# display_tty
# File description:
# __init__.py
##

from .src import Disp
from .src import LoggerColours

from .src import TOML_CONF
from .src import ERR, ERROR, SUCCESS
from .src import OSTRING, ODEFAULT, OFILE, OTTY
from .src import IDISP, IDISPLAY, IDISPTTY, IDTTY
from .src import SAVE_TO_FILE, FILE_NAME, FILE_DESCRIPTOR
from .src import OUT_TTY, OUT_STRING, OUT_FILE, OUT_DEFAULT
from .src import FORBIDDEN_NUMBER_LOG_LEVELS_CORRESPONDANCE, FORBIDDEN_NUMBER_LOG_LEVELS
from .src import KOUTPUT_MODE, KPRETTIFY_OUTPUT, KANIMATION_DELAY, KANIMATION_DELAY_BLOCKY, KPRETTIFY_OUTPUT_IN_BLOCKS
from .src import KEY_OUTPUT_MODE, KEY_PRETTIFY_OUTPUT, KEY_PRETTIFY_OUTPUT_IN_BLOCKS, KEY_ANIMATION_DELAY, KEY_ANIMATION_DELAY_BLOCKY

# class rebinds
Display = Disp
DispTTY = Disp
DisplayTTY = Disp


# Colour class rebinds
DisplayLoggerColours = LoggerColours
LC = LoggerColours
DLC = LoggerColours

# Colour rebind, for those who wish to use variable names
LOG_BLUE = LoggerColours.BLUE
LOG_RED = LoggerColours.RED
LOG_CYAN = LoggerColours.CYAN
LOG_BLACK = LoggerColours.BLACK
LOG_GREEN = LoggerColours.GREEN
LOG_WHITE = LoggerColours.WHITE
LOG_YELLOW = LoggerColours.YELLOW
LOG_PURPLE = LoggerColours.PURPLE
LOG_LIGHT_RED = LoggerColours.LIGHT_RED
LOG_LIGHT_BLUE = LoggerColours.LIGHT_BLUE
LOG_LIGHT_CYAN = LoggerColours.LIGHT_CYAN
LOG_LIGHT_WHITE = LoggerColours.LIGHT_WHITE
LOG_LIGHT_BLACK = LoggerColours.LIGHT_BLACK
LOG_LIGHT_GREEN = LoggerColours.LIGHT_GREEN
LOG_LIGHT_YELLOW = LoggerColours.LIGHT_YELLOW
LOG_LIGHT_PURPLE = LoggerColours.LIGHT_PURPLE
ALLOWED_LOGGING_COLOURS = LoggerColours.ALLOWED_LOGGING_COLOURS

__all__ = [
    # Class
    # |- Colour tracking
    "LoggerColours",
    "DisplayLoggerColours",
    "LC",
    "DLC",
    # |- Non-initialised instances
    "Disp",
    # \-Initialised instances
    "IDISP",
    "IDISPLAY",
    "IDISPTTY",
    "IDTTY",
    # Constants
    # |- Statuses
    "ERR",
    "ERROR",
    "SUCCESS",
    # |- Output modes
    # | |- full names
    "OUT_TTY",
    "OUT_FILE",
    "OUT_STRING",
    "OUT_DEFAULT",
    # | \- short names
    "OTTY",
    "OFILE",
    "OSTRING",
    "ODEFAULT",
    # |- Configuration
    "TOML_CONF",
    # |- setting names
    # | |- full names
    "KEY_OUTPUT_MODE",
    "KEY_PRETTIFY_OUTPUT",
    "KEY_PRETTIFY_OUTPUT_IN_BLOCKS",
    "KEY_ANIMATION_DELAY",
    "KEY_ANIMATION_DELAY_BLOCKY",
    # | \- short names
    "KOUTPUT_MODE",
    "KPRETTIFY_OUTPUT",
    "KANIMATION_DELAY",
    "KANIMATION_DELAY_BLOCKY",
    "KPRETTIFY_OUTPUT_IN_BLOCKS",
    # |- default settings presets values
    # | |- Output to file
    "SAVE_TO_FILE",
    # | |- File name
    "FILE_NAME",
    # | |- File descriptor
    "FILE_DESCRIPTOR",
    # |- Logging level exceptions
    "FORBIDDEN_NUMBER_LOG_LEVELS_CORRESPONDANCE",
    "FORBIDDEN_NUMBER_LOG_LEVELS",
    # |- Logging available colours
    "LOG_BLUE",
    "LOG_RED",
    "LOG_CYAN",
    "LOG_BLACK",
    "LOG_GREEN",
    "LOG_WHITE",
    "LOG_YELLOW",
    "LOG_PURPLE",
    "LOG_LIGHT_RED",
    "LOG_LIGHT_BLUE",
    "LOG_LIGHT_CYAN",
    "LOG_LIGHT_WHITE",
    "LOG_LIGHT_BLACK",
    "LOG_LIGHT_GREEN",
    "LOG_LIGHT_YELLOW",
    "LOG_LIGHT_PURPLE",
    # \- Authorized logging colours
    "ALLOWED_LOGGING_COLOURS",
]
