##
# EPITECH PROJECT, 2024
# display_tty
# File description:
# __init__.py
##

"""
@file __init__.py
@brief This file links the disp file to the module, enabling it to be imported as a module.
"""

from .constants import ERR, ERROR, SUCCESS, OUT_TTY, OUT_STRING, OUT_FILE, OUT_DEFAULT, KEY_OUTPUT_MODE, KEY_PRETTIFY_OUTPUT, KEY_PRETTIFY_OUTPUT_IN_BLOCKS, KEY_ANIMATION_DELAY, KEY_ANIMATION_DELAY_BLOCKY, TOML_CONF, FORBIDDEN_NUMBER_LOG_LEVELS_CORRESPONDANCE, FORBIDDEN_NUMBER_LOG_LEVELS
from .my_disp import Disp
from .colours import LoggerColours

# Constants
"""
@var SAVE_TO_FILE
@brief Boolean flag to indicate whether to save output to a file.
"""
SAVE_TO_FILE = False

"""
@var FILE_NAME
@brief Name of the file where results will be saved if SAVE_TO_FILE is True.
"""
FILE_NAME = "run_results.txt"

"""
@var FILE_DESCRIPTOR
@brief File descriptor for the output file.
"""
FILE_DESCRIPTOR = None

# Instances
"""
@var IDISP
@brief Initialised instance of the Disp class with default configuration.
"""
IDISP = Disp(
    TOML_CONF,
    SAVE_TO_FILE,
    FILE_NAME,
)

"""
@var IDISPLAY
@brief Alias for IDISP.
"""
IDISPLAY = IDISP

"""
@var IDISPTTY
@brief Alias for IDISP.
"""
IDISPTTY = IDISP

"""
@var IDTTY
@brief Alias for IDISP.
"""
IDTTY = IDISP

# Output Modes
"""
@var OSTRING
@brief Alias for OUT_STRING constant.
"""
OSTRING = OUT_STRING

"""
@var ODEFAULT
@brief Alias for OUT_DEFAULT constant.
"""
ODEFAULT = OUT_DEFAULT

"""
@var OFILE
@brief Alias for OUT_FILE constant.
"""
OFILE = OUT_FILE

"""
@var OTTY
@brief Alias for OUT_TTY constant.
"""
OTTY = OUT_TTY

# Configuration Keys
"""
@var KOUTPUT_MODE
@brief Alias for KEY_OUTPUT_MODE constant.
"""
KOUTPUT_MODE = KEY_OUTPUT_MODE

"""
@var KPRETTIFY_OUTPUT
@brief Alias for KEY_PRETTIFY_OUTPUT constant.
"""
KPRETTIFY_OUTPUT = KEY_PRETTIFY_OUTPUT

"""
@var KANIMATION_DELAY
@brief Alias for KEY_ANIMATION_DELAY constant.
"""
KANIMATION_DELAY = KEY_ANIMATION_DELAY

"""
@var KANIMATION_DELAY_BLOCKY
@brief Alias for KEY_ANIMATION_DELAY_BLOCKY constant.
"""
KANIMATION_DELAY_BLOCKY = KEY_ANIMATION_DELAY_BLOCKY

"""
@var KPRETTIFY_OUTPUT_IN_BLOCKS
@brief Alias for KEY_PRETTIFY_OUTPUT_IN_BLOCKS constant.
"""
KPRETTIFY_OUTPUT_IN_BLOCKS = KEY_PRETTIFY_OUTPUT_IN_BLOCKS

# Module Exports
"""
@var __all__
@brief List of all public symbols exported by this module.
"""
__all__ = [
    # Class
    # |- Colour tracking
    "LoggerColours",
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
]
