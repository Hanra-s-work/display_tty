""" 
# +==== BEGIN display_tty =================+
# LOGO: 
# ..@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# .@...........................#@
# @############################.@
# @...........................@.@
# @..#######################..@.@
# @.#########################.@.@
# @.##>_#####################.@.@
# @.#########################.@.@
# @.#########################.@.@
# @.#########################.@.@
# @.#########################.@.@
# @..#######################..@.@
# @...........................@.@
# @..+----+______________.....@.@
# @..+....+______________+....@.@
# @..+----+...................@.@
# @...........................@.#
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.
# /STOP
# PROJECT: display_tty
# FILE: __init__.py
# CREATION DATE: 06-11-2025
# LAST Modified: 13:8:51 06-11-2025
# DESCRIPTION: 
# A module that allows you to display text with a few boilers (i.e. put your text in a square for titles). It also allows to log to the terminal by wrapping around the logging library.
# @file __init__.py
# @brief This file links the disp file to the module, enabling it to be imported as a module.
# /STOP
# COPYRIGHT: (c) Henry Letellier
# PURPOSE: File in charge of containing the imports to easily use the internal elements from the module.
# // AR
# +==== END display_tty =================+
"""

from .my_disp import Disp
from .initialiser import initialise_logger
from .aliases import init, initialise
from .aliases import OSTRING, ODEFAULT, OFILE, OTTY
from .aliases import KOUTPUT_MODE, KPRETTIFY_OUTPUT, KANIMATION_DELAY, KANIMATION_DELAY_BLOCKY, KPRETTIFY_OUTPUT_IN_BLOCKS
from .colours import LoggerColours
from .instances import IDISP, IDISPLAY, IDISPTTY, IDTTY
from .constants import TOML_CONF
from .constants import ERR, ERROR, SUCCESS
from .constants import SAVE_TO_FILE, FILE_NAME, FILE_DESCRIPTOR
from .constants import OUT_TTY, OUT_STRING, OUT_FILE, OUT_DEFAULT
from .constants import FORBIDDEN_NUMBER_LOG_LEVELS_CORRESPONDANCE, FORBIDDEN_NUMBER_LOG_LEVELS
from .constants import KEY_OUTPUT_MODE, KEY_PRETTIFY_OUTPUT, KEY_PRETTIFY_OUTPUT_IN_BLOCKS, KEY_ANIMATION_DELAY, KEY_ANIMATION_DELAY_BLOCKY

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
