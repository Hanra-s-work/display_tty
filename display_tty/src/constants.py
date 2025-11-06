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
# FILE: constants.py
# CREATION DATE: 06-11-2025
# LAST Modified: 12:29:5 06-11-2025
# DESCRIPTION: 
# A module that allows you to display text with a few boilers (i.e. put your text in a square for titles). It also allows to log to the terminal by wrapping around the logging library.
# @file constants.py
# @brief This is the file in charge of containing the constants used in the display_tty library.
# @details This module defines constants and configuration settings used throughout the display_tty project. It includes error codes, output modes, animation delays,TOML configuration defaults, and forbidden log levels.
# /STOP
# COPYRIGHT: (c) Henry Letellier
# PURPOSE: File in charge of containing the constants of the program.
# // AR
# +==== END display_tty =================+
"""

# Error codes
ERR = 1  # General error code
ERROR = ERR  # Alias for ERR
SUCCESS = 0  # Success code

# Output modes
OUT_TTY = "tty"  # Output to terminal (TTY)
OUT_STRING = "string"  # Output as a string
OUT_FILE = "file"  # Output to a file
OUT_DEFAULT = ''  # Default output mode

# OUTPUT modes keys
KEY_OUTPUT_MODE = "OUTPUT_MODE"  # Key for selecting output mode
KEY_PRETTIFY_OUTPUT = "PRETTIFY_OUTPUT"  # Key for enabling prettified output
# Key for block-based prettified output
KEY_PRETTIFY_OUTPUT_IN_BLOCKS = "PRETTY_OUTPUT_IN_BLOCS"

# Animation delays
# Key for animation delay in messages
KEY_ANIMATION_DELAY = 'MESSAGE_ANIMATION_DELAY'
# Key for blocky animation delay
KEY_ANIMATION_DELAY_BLOCKY = 'MESSAGE_ANIMATION_DELAY_BLOCKY'

# TOML configuration defaults
TOML_CONF = {
    KEY_OUTPUT_MODE: OUT_TTY,  # Default output mode
    KEY_PRETTIFY_OUTPUT: True,  # Enable prettified output by default
    # Enable block-based prettified output by default
    KEY_PRETTIFY_OUTPUT_IN_BLOCKS: True,
    KEY_ANIMATION_DELAY: 0.01,  # Default animation delay
    KEY_ANIMATION_DELAY_BLOCKY: 0.01,  # Default blocky animation delay
    'MESSAGE_CHARACTER': '@',  # Default character for messages
    'MESSAGE_ERROR_CHARACTER': '#',  # Character for error messages
    'MESSAGE_INFORM_CHARACTER': 'i',  # Character for informational messages
    'MESSAGE_QUESTION_CHARACTER': '?',  # Character for question messages
    'MESSAGE_SUCCESS_CHARACTER': '/',  # Character for success messages
    'MESSAGE_WARNING_CHARACTER': '!',  # Character for warning messages
    'SUB_SUB_TITLE_WALL_CHARACTER': '*',  # Character for sub-sub-title walls
    'SUB_TITLE_WALL_CHARACTER': '@',  # Character for sub-title walls
    'TITLE_WALL_CHARACTER': '#',  # Character for title walls
    'TREE_COLUMN_SEPERATOR_CHAR': '│',  # Column separator for tree structures
    'TREE_LINE_SEPERATOR_CHAR': '─',  # Line separator for tree structures
    'TREE_NODE_CHAR': '├',  # Node character for tree structures
    'TREE_NODE_END_CHAR': '└',  # End node character for tree structures
    'BOX_NO_VERTICAL': '#',  # Box character without vertical lines
    'BOX_VERTICAL_NO_HORIZONTAL': '#',  # Box character without horizontal lines
    'ROUND_BOX_CORNER_LEFT': '╔',  # Top-left corner of a rounded box
    'ROUND_BOX_CORNER_RIGHT': '╗',  # Top-right corner of a rounded box
    'ROUND_BOX_CORNER_BOTTOM_LEFT': '╚',  # Bottom-left corner of a rounded box
    'ROUND_BOX_CORNER_BOTTOM_RIGHT': '╝',  # Bottom-right corner of a rounded box
    'ROUND_BOX_HORIZONTAL': '═',  # Horizontal line for rounded boxes
    'ROUND_BOX_VERTICAL': '║',  # Vertical line for rounded boxes
    'DIFF_BORDER_LINE_CHARACTER_BOX': '-',  # Border line character for diff boxes
    'DIFF_SIDE_LINE_CHARACTER_BOX': '|',  # Side line character for diff boxes
}

# Forbidden log levels
FORBIDDEN_NUMBER_LOG_LEVELS_CORRESPONDANCE = {
    "INFO": 20,  # Informational messages
    "WARN": 30,  # Warning messages
    "DEBUG": 10,  # Debugging messages
    "FATAL": 50,  # Fatal error messages
    "ERROR": 40,  # Error messages
    "NOTSET": 0,  # No specific log level
    "WARNING": 40,  # Alias for WARN
    "CRITICAL": 50  # Alias for FATAL
}

FORBIDDEN_NUMBER_LOG_LEVELS = list(
    FORBIDDEN_NUMBER_LOG_LEVELS_CORRESPONDANCE.values()
)  # List of forbidden log level numbers


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
