"""
File in charge linking of the disp file ot the module so that it could be imported as a module
"""
from .constants import ERR, ERROR, SUCCESS, OUT_TTY, OUT_STRING, OUT_FILE, OUT_DEFAULT, KEY_OUTPUT_MODE, KEY_PRETTIFY_OUTPUT, KEY_PRETTIFY_OUTPUT_IN_BLOCKS, KEY_ANIMATION_DELAY, KEY_ANIMATION_DELAY_BLOCKY, TOML_CONF, FORBIDDEN_NUMBER_LOG_LEVELS_CORRESPONDANCE, FORBIDDEN_NUMBER_LOG_LEVELS
from .my_disp import Disp
from .colours import LoggerColours

SAVE_TO_FILE = False
FILE_NAME = "run_results.txt"
FILE_DESCRIPTOR = None


IDISP = Disp(
    TOML_CONF,
    SAVE_TO_FILE,
    FILE_NAME,
)

IDISPLAY = IDISP
IDISPTTY = IDISP
IDTTY = IDISP


OSTRING = OUT_STRING
ODEFAULT = OUT_DEFAULT
OFILE = OUT_FILE
OTTY = OUT_TTY

KOUTPUT_MODE = KEY_OUTPUT_MODE
KPRETTIFY_OUTPUT = KEY_PRETTIFY_OUTPUT
KANIMATION_DELAY = KEY_ANIMATION_DELAY
KANIMATION_DELAY_BLOCKY = KEY_ANIMATION_DELAY_BLOCKY
KPRETTIFY_OUTPUT_IN_BLOCKS = KEY_PRETTIFY_OUTPUT_IN_BLOCKS


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
