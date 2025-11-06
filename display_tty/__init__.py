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
# LAST Modified: 13:48:5 06-11-2025
# DESCRIPTION: 
# A module that allows you to display text with a few boilers (i.e. put your text in a square for titles). It also allows to log to the terminal by wrapping around the logging library.
# @file __init__.py
# @brief This file initializes the `display_tty` library, making its components accessible for external use.
# 
# This module serves as the entry point for the `display_tty` library. It imports and rebinds various classes, constants, 
# and configurations from the `src` submodule, allowing users to easily access and utilize them in their programs.
# 
# The file also defines aliases for certain classes and constants to provide flexibility in naming conventions. 
# Additionally, it exposes a comprehensive list of public symbols via the `__all__` variable, ensuring proper encapsulation 
# and controlled access to the library's components.
# 
# @details
# - Rebinds the `Disp` class to multiple aliases for convenience.
# - Provides a set of predefined color constants for logging purposes.
# - Exposes configuration keys and default settings for output modes and animations.
# - Includes constants for logging statuses and forbidden log levels.
# 
# @note This file is automatically imported when the `display_tty` library is used in another Python program.
# 
# @see src/Disp
# @see src/LoggerColours
# /STOP
# COPYRIGHT: (c) Henry Letellier
# PURPOSE: File in charge of allowing the module to be easily imported into other programs.
# // AR
# +==== END display_tty =================+
"""

from .src import Disp
from .src import LoggerColours
from .src import init, initialise, initialise_logger
from .src import TOML_CONF
from .src import ERR, ERROR, SUCCESS
from .src import OSTRING, ODEFAULT, OFILE, OTTY
from .src import IDISP, IDISPLAY, IDISPTTY, IDTTY
from .src import SAVE_TO_FILE, FILE_NAME, FILE_DESCRIPTOR
from .src import OUT_TTY, OUT_STRING, OUT_FILE, OUT_DEFAULT
from .src import FORBIDDEN_NUMBER_LOG_LEVELS_CORRESPONDANCE, FORBIDDEN_NUMBER_LOG_LEVELS
from .src import KEY_OUTPUT_MODE, KEY_PRETTIFY_OUTPUT, KEY_PRETTIFY_OUTPUT_IN_BLOCKS, KEY_ANIMATION_DELAY, KEY_ANIMATION_DELAY_BLOCKY
from .src import KOUTPUT_MODE, KPRETTIFY_OUTPUT, KANIMATION_DELAY, KANIMATION_DELAY_BLOCKY, KPRETTIFY_OUTPUT_IN_BLOCKS


# class rebinds
# @var Display
# Alias for the Disp class, used for display operations.
Display = Disp

# @var DispTTY
# Another alias for the Disp class, emphasizing TTY usage.
DispTTY = Disp

# @var DisplayTTY
# Alias for Disp class, highlighting its use for TTY displays.
DisplayTTY = Disp

# Colour class rebinds
# @var DisplayLoggerColours Alias for LoggerColours, used for logging color management.
DisplayLoggerColours = LoggerColours
LC = LoggerColours  # @var LC Short alias for LoggerColours.
DLC = LoggerColours  # @var DLC Another short alias for LoggerColours.

# Colour rebind, for those who wish to use variable names
# @var LOG_BLUE Predefined color constant for blue.
LOG_BLUE = LoggerColours.BLUE
LOG_RED = LoggerColours.RED  # @var LOG_RED Predefined color constant for red.
# @var LOG_CYAN Predefined color constant for cyan.
LOG_CYAN = LoggerColours.CYAN
# @var LOG_BLACK Predefined color constant for black.
LOG_BLACK = LoggerColours.BLACK
# @var LOG_GREEN Predefined color constant for green.
LOG_GREEN = LoggerColours.GREEN
# @var LOG_WHITE Predefined color constant for white.
LOG_WHITE = LoggerColours.WHITE
# @var LOG_YELLOW Predefined color constant for yellow.
LOG_YELLOW = LoggerColours.YELLOW
# @var LOG_PURPLE Predefined color constant for purple.
LOG_PURPLE = LoggerColours.PURPLE
# @var LOG_LIGHT_RED Predefined color constant for light red.
LOG_LIGHT_RED = LoggerColours.LIGHT_RED
# @var LOG_LIGHT_BLUE Predefined color constant for light blue.
LOG_LIGHT_BLUE = LoggerColours.LIGHT_BLUE
# @var LOG_LIGHT_CYAN Predefined color constant for light cyan.
LOG_LIGHT_CYAN = LoggerColours.LIGHT_CYAN
# @var LOG_LIGHT_WHITE Predefined color constant for light white.
LOG_LIGHT_WHITE = LoggerColours.LIGHT_WHITE
# @var LOG_LIGHT_BLACK Predefined color constant for light black.
LOG_LIGHT_BLACK = LoggerColours.LIGHT_BLACK
# @var LOG_LIGHT_GREEN Predefined color constant for light green.
LOG_LIGHT_GREEN = LoggerColours.LIGHT_GREEN
# @var LOG_LIGHT_YELLOW Predefined color constant for light yellow.
LOG_LIGHT_YELLOW = LoggerColours.LIGHT_YELLOW
# @var LOG_LIGHT_PURPLE Predefined color constant for light purple.
LOG_LIGHT_PURPLE = LoggerColours.LIGHT_PURPLE

__all__ = [
    # Class
    # |- Colour tracking
    "LoggerColours",  # @var LoggerColours Class for managing logging colors.
    # @var DisplayLoggerColours Alias for LoggerColours.
    "DisplayLoggerColours",
    "LC",  # @var LC Short alias for LoggerColours.
    "DLC",  # @var DLC Another short alias for LoggerColours.
    # |- Non-initialised instances
    "Disp",  # @var Disp Main display class.
    # \-Initialised instances
    "IDISP",  # @var IDISP Pre-initialized instance of Disp.
    # @var IDISPLAY Pre-initialized instance of Disp for display purposes.
    "IDISPLAY",
    # @var IDISPTTY Pre-initialized instance of Disp for TTY display.
    "IDISPTTY",
    "IDTTY",  # @var IDTTY Pre-initialized instance of Disp for TTY operations.
    # Constants
    # |- Statuses
    "ERR",  # @var ERR Constant representing an error status.
    "ERROR",  # @var ERROR Alias for ERR.
    "SUCCESS",  # @var SUCCESS Constant representing a success status.
    # |- Output modes
    # | |- full names
    "OUT_TTY",  # @var OUT_TTY Constant for TTY output mode.
    "OUT_FILE",  # @var OUT_FILE Constant for file output mode.
    "OUT_STRING",  # @var OUT_STRING Constant for string output mode.
    "OUT_DEFAULT",  # @var OUT_DEFAULT Constant for default output mode.
    # | \- short names
    "OTTY",  # @var OTTY Short alias for OUT_TTY.
    "OFILE",  # @var OFILE Short alias for OUT_FILE.
    "OSTRING",  # @var OSTRING Short alias for OUT_STRING.
    "ODEFAULT",  # @var ODEFAULT Short alias for OUT_DEFAULT.
    # |- Configuration
    "TOML_CONF",  # @var TOML_CONF Configuration file in TOML format.
    # |- setting names
    # | |- full names
    # @var KEY_OUTPUT_MODE Key for output mode configuration.
    "KEY_OUTPUT_MODE",
    # @var KEY_PRETTIFY_OUTPUT Key for prettifying output.
    "KEY_PRETTIFY_OUTPUT",
    # @var KEY_PRETTIFY_OUTPUT_IN_BLOCKS Key for block-based prettified output.
    "KEY_PRETTIFY_OUTPUT_IN_BLOCKS",
    # @var KEY_ANIMATION_DELAY Key for animation delay configuration.
    "KEY_ANIMATION_DELAY",
    # @var KEY_ANIMATION_DELAY_BLOCKY Key for blocky animation delay configuration.
    "KEY_ANIMATION_DELAY_BLOCKY",
    # | \- short names
    "KOUTPUT_MODE",  # @var KOUTPUT_MODE Short alias for KEY_OUTPUT_MODE.
    # @var KPRETTIFY_OUTPUT Short alias for KEY_PRETTIFY_OUTPUT.
    "KPRETTIFY_OUTPUT",
    # @var KANIMATION_DELAY Short alias for KEY_ANIMATION_DELAY.
    "KANIMATION_DELAY",
    # @var KANIMATION_DELAY_BLOCKY Short alias for KEY_ANIMATION_DELAY_BLOCKY.
    "KANIMATION_DELAY_BLOCKY",
    # @var KPRETTIFY_OUTPUT_IN_BLOCKS Short alias for KEY_PRETTIFY_OUTPUT_IN_BLOCKS.
    "KPRETTIFY_OUTPUT_IN_BLOCKS",
    # |- default settings presets values
    # | |- Output to file
    # @var SAVE_TO_FILE Constant for enabling saving output to a file.
    "SAVE_TO_FILE",
    # | |- File name
    "FILE_NAME",  # @var FILE_NAME Default file name for saving output.
    # | |- File descriptor
    "FILE_DESCRIPTOR",  # @var FILE_DESCRIPTOR File descriptor for output file.
    # |- Logging level exceptions
    # @var FORBIDDEN_NUMBER_LOG_LEVELS_CORRESPONDANCE Mapping of forbidden log levels.
    "FORBIDDEN_NUMBER_LOG_LEVELS_CORRESPONDANCE",
    # @var FORBIDDEN_NUMBER_LOG_LEVELS List of forbidden log levels.
    "FORBIDDEN_NUMBER_LOG_LEVELS",
    # \- Logging available colours
    "LOG_BLUE",  # @var LOG_BLUE Predefined color constant for blue.
    "LOG_RED",  # @var LOG_RED Predefined color constant for red.
    "LOG_CYAN",  # @var LOG_CYAN Predefined color constant for cyan.
    "LOG_BLACK",  # @var LOG_BLACK Predefined color constant for black.
    "LOG_GREEN",  # @var LOG_GREEN Predefined color constant for green.
    "LOG_WHITE",  # @var LOG_WHITE Predefined color constant for white.
    "LOG_YELLOW",  # @var LOG_YELLOW Predefined color constant for yellow.
    "LOG_PURPLE",  # @var LOG_PURPLE Predefined color constant for purple.
    # @var LOG_LIGHT_RED Predefined color constant for light red.
    "LOG_LIGHT_RED",
    # @var LOG_LIGHT_BLUE Predefined color constant for light blue.
    "LOG_LIGHT_BLUE",
    # @var LOG_LIGHT_CYAN Predefined color constant for light cyan.
    "LOG_LIGHT_CYAN",
    # @var LOG_LIGHT_WHITE Predefined color constant for light white.
    "LOG_LIGHT_WHITE",
    # @var LOG_LIGHT_BLACK Predefined color constant for light black.
    "LOG_LIGHT_BLACK",
    # @var LOG_LIGHT_GREEN Predefined color constant for light green.
    "LOG_LIGHT_GREEN",
    # @var LOG_LIGHT_YELLOW Predefined color constant for light yellow.
    "LOG_LIGHT_YELLOW",
    # @var LOG_LIGHT_PURPLE Predefined color constant for light purple.
    "LOG_LIGHT_PURPLE",
    "init",
    "initialise",
    "initialise_logger"
]
