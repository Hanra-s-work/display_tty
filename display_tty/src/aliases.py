from .constants import OUT_TTY, OUT_STRING, OUT_FILE, OUT_DEFAULT, KEY_OUTPUT_MODE, KEY_PRETTIFY_OUTPUT, KEY_PRETTIFY_OUTPUT_IN_BLOCKS, KEY_ANIMATION_DELAY, KEY_ANIMATION_DELAY_BLOCKY

from .initialiser import initialise_logger

TMP = None  # linter bypass for a false positive of statement has no effect


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

# Initialiser function
initialiser = initialise_logger
init = initialise_logger
