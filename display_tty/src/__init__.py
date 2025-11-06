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

from .constants import \
    ERR, ERROR, SUCCESS, \
    OUT_TTY, OUT_STRING, OUT_FILE, OUT_DEFAULT, \
    KEY_OUTPUT_MODE, KEY_PRETTIFY_OUTPUT, KEY_PRETTIFY_OUTPUT_IN_BLOCKS, KEY_ANIMATION_DELAY, KEY_ANIMATION_DELAY_BLOCKY, \
    TOML_CONF, \
    FORBIDDEN_NUMBER_LOG_LEVELS_CORRESPONDANCE, FORBIDDEN_NUMBER_LOG_LEVELS, \
    SAVE_TO_FILE, FILE_NAME, FILE_DESCRIPTOR
from .aliases import \
    OSTRING, ODEFAULT, OFILE, OTTY, \
    KOUTPUT_MODE, KPRETTIFY_OUTPUT, KANIMATION_DELAY, KANIMATION_DELAY_BLOCKY, KPRETTIFY_OUTPUT_IN_BLOCKS, \
    initialise, init
from .instances import IDISP, IDISPLAY, IDISPTTY, IDTTY
from .my_disp import Disp
from .colours import LoggerColours
from .initialiser import initialise_logger

TMP = None  # linter bypass for a false positive of statement has no effect

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
    # |- Constructor functions for ease of initialisation
    "init",
    "initialise",
    "initialise_logger",
]
