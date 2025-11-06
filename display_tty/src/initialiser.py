from typing import Dict, Any, Optional, Union
from .constants import TOML_CONF, SAVE_TO_FILE, FILE_NAME
from .my_disp import Disp, Logging


def initialise_logger(
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
        log_errors_when_present: Optional[bool] = None
) -> Disp:
    """
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
    _toml_content = TOML_CONF
    _save_to_file = SAVE_TO_FILE
    _file_name = FILE_NAME
    _optional_arg: Dict[str, Any] = {}
    if toml_content is not None:
        _toml_content = toml_content
    if save_to_file is not None:
        _save_to_file = bool(save_to_file)
    if file_name is not None:
        _file_name = file_name
    if file_descriptor is not None:
        _optional_arg["file_descriptor"] = file_descriptor
    if success is not None:
        _optional_arg["success"] = success
    if error is not None:
        _optional_arg["error"] = error
    if log_warning_when_present is not None:
        _optional_arg["log_warning_when_present"] = log_warning_when_present
    if log_errors_when_present is not None:
        _optional_arg["log_errors_when_present"] = log_errors_when_present
    return Disp(
        toml_content=_toml_content,
        save_to_file=_save_to_file,
        file_name=_file_name,
        debug=debug,
        logger=class_name,
        **_optional_arg
    )
