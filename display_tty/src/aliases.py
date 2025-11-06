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
# FILE: aliases.py
# CREATION DATE: 06-11-2025
# LAST Modified: 13:6:20 06-11-2025
# DESCRIPTION: 
# A module that allows you to display text with a few boilers (i.e. put your text in a square for titles). It also allows to log to the terminal by wrapping around the logging library.
# /STOP
# COPYRIGHT: (c) Henry Letellier
# PURPOSE: File in charge of containing shorter names of the variables to ease the call.
# // AR
# +==== END display_tty =================+
"""
from typing import Dict, Any, Optional, Union

from .my_disp import Logging

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


def initialise(
        class_name: Union[Logging, str],
        debug: bool = False,
        *,
        toml_content: Optional[Dict[str, Any]] = None,
        save_to_file: Optional[bool] = None,
        file_name: Optional[str] = None,
        file_descriptor: Optional[Any] = None,
        success: Optional[int] = None,
        error: Optional[int] = None,
        log_warning_when_present: Optional[bool] = None,
        log_errors_when_present: Optional[bool] = None):
    """Alias for initialise_logger kept for API compatibility.

    Original documentation:
    @brief Initialise and return a configured Disp instance for a given class or module.

    This factory function creates and returns a configured `Disp` instance (the library's
    display/logger wrapper) using defaults from `TOML_CONF`, `SAVE_TO_FILE` and `FILE_NAME`
    unless overridden by the provided keyword arguments. The `class_name` may be a
    `Logging`-compatible object (an object exposing logging-like methods) or a simple string
    used as a label for the logger.

    @param class_name Union[Logging, str]
        The logging owner (class instance or name) to attach to the returned `Disp` instance.
    @param debug bool, optional
        If True the returned `Disp` instance will run in debug mode (enable debug-level output).
        Defaults to False.
    @param toml_content Optional[Dict[str, Any]]
        Optional override for TOML configuration content (defaults to module-level TOML_CONF).
    @param save_to_file Optional[bool]
        Optional override to enable saving output to a file (defaults to module-level SAVE_TO_FILE).
    @param file_name Optional[str]
        Optional override for the file name used when saving to file (defaults to FILE_NAME).
    @param file_descriptor Optional[Any]
        Optional open file-like object to use for output (will be passed to `Disp`).
    @param success Optional[int]
        Optional custom success return code for the `Disp` instance.
    @param error Optional[int]
        Optional custom error return code for the `Disp` instance.
    @param log_warning_when_present Optional[bool]
        Optional flag to control whether warnings are logged when present.
    @param log_errors_when_present Optional[bool]
        Optional flag to control whether errors are logged when present.

    @return Disp
        A configured `Disp` instance ready to use.

    @note
        - Optional arguments are only applied when provided (truthy) except `save_to_file` which is explicitly converted to bool when passed.
        - Use `file_descriptor` to reuse an open file handle instead of letting `Disp` open its own file.
        - This function updates only configuration passed to `Disp` and does not change library global constants.
    """
    return initialise_logger(
        class_name=class_name,
        debug=debug,
        toml_content=toml_content,
        save_to_file=save_to_file,
        file_name=file_name,
        file_descriptor=file_descriptor,
        success=success,
        error=error,
        log_warning_when_present=log_warning_when_present,
        log_errors_when_present=log_errors_when_present
    )


# short alias
def init(
        class_name: Union[Logging, str],
        debug: bool = False,
        *,
        toml_content: Optional[Dict[str, Any]] = None,
        save_to_file: Optional[bool] = None,
        file_name: Optional[str] = None,
        file_descriptor: Optional[Any] = None,
        success: Optional[int] = None,
        error: Optional[int] = None,
        log_warning_when_present: Optional[bool] = None,
        log_errors_when_present: Optional[bool] = None):
    """Short alias for `initialise` (and therefore `initialise_logger`).

    Original documentation:
    @brief Initialise and return a configured Disp instance for a given class or module.

    This factory function creates and returns a configured `Disp` instance (the library's
    display/logger wrapper) using defaults from `TOML_CONF`, `SAVE_TO_FILE` and `FILE_NAME`
    unless overridden by the provided keyword arguments. The `class_name` may be a
    `Logging`-compatible object (an object exposing logging-like methods) or a simple string
    used as a label for the logger.

    @param class_name Union[Logging, str]
        The logging owner (class instance or name) to attach to the returned `Disp` instance.
    @param debug bool, optional
        If True the returned `Disp` instance will run in debug mode (enable debug-level output).
        Defaults to False.
    @param toml_content Optional[Dict[str, Any]]
        Optional override for TOML configuration content (defaults to module-level TOML_CONF).
    @param save_to_file Optional[bool]
        Optional override to enable saving output to a file (defaults to module-level SAVE_TO_FILE).
    @param file_name Optional[str]
        Optional override for the file name used when saving to file (defaults to FILE_NAME).
    @param file_descriptor Optional[Any]
        Optional open file-like object to use for output (will be passed to `Disp`).
    @param success Optional[int]
        Optional custom success return code for the `Disp` instance.
    @param error Optional[int]
        Optional custom error return code for the `Disp` instance.
    @param log_warning_when_present Optional[bool]
        Optional flag to control whether warnings are logged when present.
    @param log_errors_when_present Optional[bool]
        Optional flag to control whether errors are logged when present.

    @return Disp
        A configured `Disp` instance ready to use.

    @note
        - Optional arguments are only applied when provided (truthy) except `save_to_file` which is explicitly converted to bool when passed.
        - Use `file_descriptor` to reuse an open file handle instead of letting `Disp` open its own file.
        - This function updates only configuration passed to `Disp` and does not change library global constants.
    """
    return initialise(
        class_name=class_name,
        debug=debug,
        toml_content=toml_content,
        save_to_file=save_to_file,
        file_name=file_name,
        file_descriptor=file_descriptor,
        success=success,
        error=error,
        log_warning_when_present=log_warning_when_present,
        log_errors_when_present=log_errors_when_present
    )
