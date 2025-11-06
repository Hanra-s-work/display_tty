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
# FILE: instances.py
# CREATION DATE: 06-11-2025
# LAST Modified: 12:26:43 06-11-2025
# DESCRIPTION: 
# A module that allows you to display text with a few boilers (i.e. put your text in a square for titles). It also allows to log to the terminal by wrapping around the logging library.
# /STOP
# COPYRIGHT: (c) Henry Letellier
# PURPOSE: File in charge of containing initialised instances that can be used on the go without the calling program having to initialise it themself.
# // AR
# +==== END display_tty =================+
"""

from .my_disp import Disp
from .constants import TOML_CONF, SAVE_TO_FILE, FILE_NAME

TMP = None  # linter bypass for a false positive of statement has no effect

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
