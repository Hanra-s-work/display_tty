##
# EPITECH PROJECT, 2024
# display_tty
# File description:
# my_disp.py
##

"""
@file my_disp.py
@brief The file in charge of managing the beautified output on the terminal.
"""

import sys
import time
import inspect

from typing import List, Dict, Union

import logging
import colorlog

# Check if the script is being run directly or imported
if __name__ == "__main__":
    from colours import LoggerColours
    from constants import ERR, SUCCESS, OUT_TTY, OUT_STRING, OUT_FILE, OUT_DEFAULT, KEY_OUTPUT_MODE, KEY_PRETTIFY_OUTPUT, KEY_PRETTIFY_OUTPUT_IN_BLOCKS, KEY_ANIMATION_DELAY, KEY_ANIMATION_DELAY_BLOCKY, TOML_CONF, FORBIDDEN_NUMBER_LOG_LEVELS_CORRESPONDANCE, FORBIDDEN_NUMBER_LOG_LEVELS
    from log_level_tracker import LogLevelTracker
else:
    from .colours import LoggerColours
    from .constants import ERR, SUCCESS, OUT_TTY, OUT_STRING, OUT_FILE, OUT_DEFAULT, KEY_OUTPUT_MODE, KEY_PRETTIFY_OUTPUT, KEY_PRETTIFY_OUTPUT_IN_BLOCKS, KEY_ANIMATION_DELAY, KEY_ANIMATION_DELAY_BLOCKY, TOML_CONF, FORBIDDEN_NUMBER_LOG_LEVELS_CORRESPONDANCE, FORBIDDEN_NUMBER_LOG_LEVELS
    from .log_level_tracker import LogLevelTracker


class Logging:
    """
    @class Logging
    @brief Represents a placeholder for the logging library. This is not a functioning class.
    """

    def __init__(self) -> None:
        pass


class Disp:
    """
    @class Disp
    @brief The class in charge of displaying messages with various styles and animations.

    @details This class provides methods to display messages in different formats, log messages, and manage output configurations.
    """

    def __init__(self, toml_content: Dict[str, any], save_to_file: bool = False, file_name: str = "text_output_run.txt", file_descriptor: any = None, debug: bool = False, logger: Union[Logging, str, None] = None, success: int = SUCCESS, error: int = ERR, log_warning_when_present: bool = True, log_errors_when_present: bool = True) -> None:
        """
        @brief Constructor for the Disp class.

        @param toml_content Dictionary containing configuration values.
        @param save_to_file Boolean indicating whether to save output to a file.
        @param file_name Name of the file to save output to.
        @param file_descriptor File descriptor for the output file.
        @param debug Boolean indicating whether debug mode is enabled.
        @param logger Logger instance or name to use for logging.
        @param success Integer representing the success status code.
        @param error Integer representing the error status code.
        @param log_warning_when_present Boolean indicating whether to log warnings when they arise in one of the function calls.
        @param log_errors_when_present Boolean indicating whether to log errors when they arise in one of the function calls.
        """
        self.__version__ = "1.0.0"
        self.toml_content = toml_content
        self.background_colour_key = 'background_colour'
        self.author = "(c) Created by Henry Letellier"
        self.nb_chr = 40
        self.debug = debug
        self.error = error
        self.success = success
        self.nb_side_walls = 2
        self.log_error_when_present = log_errors_when_present
        self.log_warning_when_present = log_warning_when_present
        self.log_level_tracker = LogLevelTracker()
        self.max_whitespace = self.nb_chr - self.nb_side_walls
        self.title_wall_chr = self.toml_content["TITLE_WALL_CHARACTER"]
        self.sub_title_wall_chr = self.toml_content["SUB_TITLE_WALL_CHARACTER"]
        self.sub_sub_title_wall_chr = self.toml_content["SUB_SUB_TITLE_WALL_CHARACTER"]
        self.message_char = self.toml_content["MESSAGE_CHARACTER"]
        self.message_error_char = self.toml_content["MESSAGE_ERROR_CHARACTER"]
        self.message_success_char = self.toml_content["MESSAGE_SUCCESS_CHARACTER"]
        self.message_inform_char = self.toml_content["MESSAGE_INFORM_CHARACTER"]
        self.message_warning_char = self.toml_content["MESSAGE_WARNING_CHARACTER"]
        self.message_question_char = self.toml_content["MESSAGE_QUESTION_CHARACTER"]
        if self.toml_content[KEY_PRETTIFY_OUTPUT_IN_BLOCKS] is True:
            self.message_animation_delay = self.toml_content[KEY_ANIMATION_DELAY_BLOCKY]
        else:
            self.message_animation_delay = self.toml_content[KEY_ANIMATION_DELAY]
        self.tree_node_char = self.toml_content["TREE_NODE_CHAR"]
        self.tree_node_end_char = self.toml_content["TREE_NODE_END_CHAR"]
        self.tree_line_seperator_char = self.toml_content["TREE_LINE_SEPERATOR_CHAR"]
        self.tree_column_seperator_char = self.toml_content["TREE_COLUMN_SEPERATOR_CHAR"]
        self.file_name = file_name
        self.save_to_file = save_to_file
        if self.toml_content[KEY_OUTPUT_MODE] == OUT_FILE:
            self.save_to_file = True
        self.file_descriptor = file_descriptor
        self.generated_content = ""
        if self.toml_content[KEY_OUTPUT_MODE] not in (OUT_FILE, OUT_STRING, OUT_TTY, OUT_DEFAULT):
            msg = f"Invalid output mode. Must be one of '{OUT_FILE}', "
            msg += f"'{OUT_STRING}', '{OUT_TTY}', '{OUT_DEFAULT}'"
            raise ValueError(msg)
        if self.toml_content[KEY_OUTPUT_MODE] == OUT_FILE:
            self._open_file()
        self._setup_logger(logger)

    def _setup_logger(self, logger: Union[Logging, str, None]) -> None:
        """
        @brief Setup the logger for the class.

        @param logger The logger to use. If None, a default logger will be used.
        """
        # ---- Logging data ----
        if callable(logger) and hasattr(logger, "debug"):
            self.logger = logger
        else:
            if isinstance(logger, str) is True:
                self.logger = logging.getLogger(logger)
            else:
                self.logger = logging.getLogger(self.__class__.__name__)
            if not self.logger.hasHandlers():
                handler = colorlog.StreamHandler()
                format_string = '[%(asctime)s] %(log_color)s%('
                format_string += self.background_colour_key
                format_string += '_log_color)s%(levelname)s%(reset)s %(name)s: \'%(message)s\''
                formatter = colorlog.ColoredFormatter(
                    fmt=format_string,
                    datefmt=None,
                    reset=True,
                    style='%',
                    log_colors={
                        'DEBUG':    'cyan',
                        'INFO':     'green',
                        'WARNING':  'yellow',
                        'ERROR':    'red',
                        'CRITICAL': 'bold_red'
                    },
                    secondary_log_colors={
                        self.background_colour_key: {
                            'DEBUG': 'bg_black',
                            'INFO': 'bg_black',
                            'WARNING': 'bg_black',
                            'ERROR': 'bg_black',
                            'CRITICAL': 'bg_black',
                        }
                    },
                )
                handler.setFormatter(formatter)
                self.logger.addHandler(handler)
            # This is what controls the importance of the log that will be allowed to be displayed, the higher the number, the more important the log is.
            self.update_logger_level(1)
        node = LogLevelTracker()
        if node.check_presence() is False:
            node.inject_class()

    def _create_function(self, name, func_code):
        # Create a namespace for the function
        namespace = {}

        # Execute the code that defines the function
        exec(func_code, globals(), namespace)

        # Extract the function from namespace
        func = namespace[name]
        return func

    def _add_function_to_instance(self, func_dest: object, func_name: str, func_code: str) -> None:
        """
        @brief Add a dynamically created function to an instance.

        @param func_dest The destination object to add the function to.
        @param func_name Name of the function.
        @param func_code Code of the function.
        """
        function_instance = self._create_function(func_name, func_code)
        setattr(func_dest, func_name, function_instance)

    def update_disp_debug(self, debug: bool) -> None:
        """
        @brief Update the debug mode.

        @param debug Boolean indicating whether debug mode is enabled.
        """
        self.debug = debug

    def update_logger_level(self, level: Union[int, LogLevelTracker.Levels] = LogLevelTracker.Levels.NOTSET) -> None:
        """
        @brief Update the logger level.

        @param level The log importance level. Defaults to NOTSET.

        @return The status code of the operation.
        """
        _func_name = inspect.currentframe().f_code.co_name

        if isinstance(level, str):
            level = level.upper()
            if hasattr(logging, "LogLevelTracker"):
                level = logging.LogLevelTracker.get_level(level)
        if isinstance(level, int) is False or level not in LogLevelTracker.Levels.__all__:
            level = LogLevelTracker.Levels.NOTSET
            if self.log_warning_when_present is True:
                self.log_warning(
                    f"The level is not valid, defaulting to {level}",
                    _func_name
                )
        self.logger.setLevel(level)

    def _check_the_logging_instance(self, logger_instance: logging.Logger = None) -> logging.Logger:
        """
        @brief Check if the logger instance is valid.

        @param logger_instance The logger instance to validate.
        @return A valid logger instance.
        """
        # Get the parent function name if present
        _func_name = inspect.currentframe()
        if _func_name.f_back is not None:
            _func_name = _func_name.f_back.f_code.co_name
        else:
            _func_name = _func_name.f_code.co_name

        # Checking the logger instance
        if logger_instance is None or not isinstance(logger_instance, logging.Logger):
            if self.log_warning_when_present is True:
                self.log_warning(
                    "No logger instance provided, using the default logger",
                    _func_name
                )
            logger_instance = self.logger
        return logger_instance

    def _check_colour_data(self, colour: Union[str, int], logger_instance: logging.Logger = None) -> Union[int, str]:
        """
        @brief Check if the provided colour data is valid.

        @param colour The colour to validate.
        @param logger_instance The logger instance to use for logging errors.
        @return The validated colour or an error code.
        """
        _func_name = inspect.currentframe()
        if _func_name.f_back is not None:
            _func_name = _func_name.f_back.f_code.co_name
        else:
            _func_name = _func_name.f_code.co_name

        # Checking if the colour exists
        if isinstance(colour, int):
            colour = LoggerColours.get_colour_string(LoggerColours, colour)
        if LoggerColours.check_if_colour_present(LoggerColours, colour) is False:
            if self.log_error_when_present is True:
                self.log_error(
                    "The provided colour is not valid",
                    _func_name
                )
            return self.error
        return colour

    def _check_level_data(self, level_name: Union[str, int], logger_instance: logging.Logger = None) -> Union[int, str]:
        """
        @brief Check if the provided level data is valid.

        @param level_name The level name or number to validate.
        @param logger_instance The logger instance to use for logging errors.
        @return The validated level name or an error code.
        """
        _func_name = inspect.currentframe()
        if _func_name.f_back is not None:
            _func_name = _func_name.f_back.f_code.co_name
        else:
            _func_name = _func_name.f_code.co_name

        # Check if there are any handlers in use.
        if len(logger_instance.handlers) == 0:
            if self.log_error_when_present is True:
                self.log_error(
                    'No handlers are present in this logging instance',
                    _func_name
                )
            return self.error

        # Checking for the presence of the logging level in the logger instance
        if isinstance(level_name, str):
            name_string = level_name.upper()
        elif isinstance(level_name, int):
            name_string = logging.getLevelName(level_name)
        else:
            if self.log_error_when_present is True:
                self.log_error(
                    "The level name must be a string or an integer",
                    _func_name
                )
            return self.error
        return name_string

    def _get_colour_formatter(self, logger_instance: logging.Logger = None) -> Union[None, colorlog.ColoredFormatter]:
        """
        @brief Get the colour formatter from the logger instance.

        @param logger_instance The logger instance to retrieve the formatter from.
        @return The colour formatter or an error code.
        """
        _func_name = inspect.currentframe()
        if _func_name.f_back is not None:
            _func_name = _func_name.f_back.f_code.co_name
        else:
            _func_name = _func_name.f_code.co_name

        # iterate through the handlers to find the colour handler
        colour_handler = None
        for i in logger_instance.handlers:
            if isinstance(i, colorlog.StreamHandler):
                colour_handler = i
                break
        if not colour_handler:
            if self.log_error_when_present is True:
                self.log_error(
                    'No colour handler is present in this logging instance',
                    _func_name
                )
            return self.error

        # Check if the colour is a string or an integer
        if hasattr(colour_handler, "formatter") is False:
            if self.log_error_when_present is True:
                self.log_error(
                    'The colour handler has no formatter',
                    _func_name
                )
            return self.error
        colour_formatter: colorlog.ColoredFormatter = colour_handler.formatter
        if isinstance(colour_formatter, colorlog.ColoredFormatter) is False:
            if self.log_error_when_present is True:
                self.log_error(
                    'The formatter is not a ColoredFormatter',
                    _func_name
                )
            return self.error
        if hasattr(colour_formatter, "log_colors") is False:
            if self.log_error_when_present is True:
                self.log_error(
                    'The formatter has no log_colors',
                    _func_name
                )
            return self.error
        return colour_formatter

    def update_logging_colour_text(self, colour: Union[str, int], level_name: Union[str, int], logger_instance: logging.Logger = None) -> int:
        """
        @brief Update or insert a logging colour for the text of the specified level.

        @param colour The colour to use (string or number).
        @param level_name The level name or number.
        @param logger_instance The logger instance to update.
        @return The status code of the operation.
        """
        _func_name = inspect.currentframe().f_code.co_name
        # Checking the logger instance
        logger_instance = self._check_the_logging_instance(logger_instance)

        name_string = self._check_level_data(
            level_name,
            logger_instance
        )
        if name_string == self.error:
            if self.log_error_when_present is True:
                self.log_error(
                    f"The level name {level_name} is not valid",
                    _func_name
                )
            return self.error

        name_string = name_string.upper()

        # Checking if the colour exists
        colour_input = colour
        colour = self._check_colour_data(
            colour,
            logger_instance
        )
        if colour == self.error:
            if self.log_error_when_present is True:
                self.log_error(
                    f"The colour {colour_input} is not valid",
                    _func_name
                )
            return self.error

        internal_log_colors = self._get_colour_formatter(logger_instance)
        if internal_log_colors == self.error or internal_log_colors is None:
            if self.log_error_when_present is True:
                self.log_error(
                    'The colour logging library is not valid',
                    _func_name
                )
            return self.error
        lib_log_colors = internal_log_colors.log_colors
        if isinstance(lib_log_colors, dict) is False:
            if self.log_error_when_present is True:
                self.log_error(
                    'The log_colors is not a dictionary',
                    _func_name
                )
            return self.error
        for i in lib_log_colors:
            if i.upper() == name_string:
                lib_log_colors[i] = colour
                return self.success
        lib_log_colors[name_string.upper()] = colour
        return self.success

    def update_logging_colour_background(self, colour: Union[str, int], level_name: Union[str, int], logger_instance: logging.Logger = None) -> int:
        """
        @brief Update or insert a logging colour for the background of the specified level.

        @param colour The colour to use (string or number).
        @param level_name The level name or number.
        @param logger_instance The logger instance to update.
        @return The status code of the operation.
        """
        _func_name = inspect.currentframe().f_code.co_name
        # Checking the logger instance
        logger_instance = self._check_the_logging_instance(logger_instance)

        name_string = self._check_level_data(
            level_name,
            logger_instance
        )
        if name_string == self.error:
            if self.log_error_when_present is True:
                self.log_error(
                    f"The level name {level_name} is not valid",
                    _func_name
                )
            return self.error
        name_string = name_string.upper()

        # Checking if the colour exists
        colour_input = colour
        colour = self._check_colour_data(
            colour,
            logger_instance
        )
        if colour == self.error:
            if self.log_error_when_present is True:
                self.log_error(
                    f"The colour {colour_input} is not valid",
                    _func_name
                )
            return self.error

        # Checking if the colour is a background colour
        if colour.startswith("bg_") is False:
            colour = "bg_" + colour

        secondary_log_colors = self._get_colour_formatter(logger_instance)
        if secondary_log_colors == self.error:
            if self.log_error_when_present is True:
                self.log_error(
                    'The secondary_log_colors is not valid',
                    _func_name
                )
            return self.error
        secondary_log_colors = secondary_log_colors.secondary_log_colors
        if isinstance(secondary_log_colors, dict) is False:
            if self.log_error_when_present is True:
                self.log_error(
                    'The secondary_log_colors is not a dictionary',
                    _func_name
                )
            return self.error

        # Add the level and colour to the secondary log colours
        if hasattr(secondary_log_colors, self.background_colour_key) is False:
            secondary_log_colors[self.background_colour_key] = {
                name_string.upper(): colour
            }
            return self.success
        for i in secondary_log_colors[self.background_colour_key]:
            if i.upper() == name_string:
                secondary_log_colors[self.background_colour_key][i.upper(
                )] = colour
                return self.success
        secondary_log_colors[
            self.background_colour_key
        ][name_string.upper()] = colour
        return self.success

    def add_custom_level(self, level: int, name: str, colour_text: Union[int, str] = "", colour_bg: Union[int, str] = "") -> int:
        """
        @brief Add a custom level to the logger.

        @param level The integer value of the custom level.
        @param name The name of the custom level.
        @param colour_text The text colour for the custom level.
        @param colour_bg The background colour for the custom level.
        @return The status code of the operation.
        """
        _func_name = inspect.currentframe().f_code.co_name
        logger = self._check_the_logging_instance(self.logger)
        # Check if the level is already taken
        if level in FORBIDDEN_NUMBER_LOG_LEVELS:
            if self.log_error_when_present is True:
                self.log_error(
                    f"The provided level  is forbidden because already taken '{level}'",
                    _func_name
                )
            return self.error
        if name in FORBIDDEN_NUMBER_LOG_LEVELS_CORRESPONDANCE:
            if self.log_error_when_present is True:
                self.log_error(
                    f"The provided name is forbidden because already taken '{name}'",
                    _func_name
                )
            return self.error
        # Add the level to the logger
        logging.addLevelName(level, name.upper())
        if hasattr(logging.getLogger(), "log_level_tracker") is False:
            if self.log_warning_when_present is True:
                self.log_warning(
                    "The log level tracker is not present, adding",
                    _func_name
                )
            logging.getLogger().log_level_tracker = self.log_level_tracker
        else:
            self.log_level_tracker = logging.getLogger().log_level_tracker
        if logging.getLogger().log_level_tracker.add_level(name, level) is False:
            if self.log_error_when_present is True:
                self.log_warning(
                    "The level could not be added to the log level tracker",
                    _func_name
                )
            return self.error
        # Check the colours
        if colour_text != "" or colour_text < 0:
            colour_text_status = self.update_logging_colour_text(
                colour_text,
                level,
                logger
            )
            if colour_text_status == self.error:
                if self.log_error_when_present is True:
                    self.log_warning(
                        "The colour for the text could not be set",
                        _func_name
                    )
        if colour_bg != "" or colour_bg < 0:
            colour_bg_status = self.update_logging_colour_background(
                colour_bg,
                level,
                logger
            )
            if colour_bg_status == self.error:
                if self.log_error_when_present is True:
                    self.log_warning(
                        "The colour for the background could not be set",
                        _func_name
                    )

        # generate the function name
        func_name = name.lower()
#         # Generate the function for the logger
#         function_code = f"""
# def {func_name}(self, message: str):
#     self.logger.log({level}, message)
# """
#         self._add_function_to_instance(
#             logger,
#             func_name,
#             function_code
#         )
        # Generate the function for the display class
        func_disp_name = f"disp_print_{func_name}"
        function_disp_code = f"""
def {func_disp_name}(self, string: str = "", func_name: Union[str, None] = None) -> None:
    if isinstance(func_name, str) is False or func_name is None:
        _func_name = inspect.currentframe()
        if _func_name.f_back is not None:
            func_name = _func_name.f_back.f_code.co_name
        else:
            func_name = _func_name.f_code.co_name
    self.log_custom_level({level}, string, func_name)
"""
        self._add_function_to_instance(
            self,
            func_disp_name,
            function_disp_code
        )
        # Generate the shorthand name for the display class
        func_log_name = f"log_{func_name}"
        function_disp_short_code = f"""
def {func_log_name}(self, string: str = "", func_name: Union[str, None] = None) -> None:
    if isinstance(func_name, str) is False or func_name is None:
        _func_name = inspect.currentframe()
        if _func_name.f_back is not None:
            _func_name = _func_name.f_back.f_code.co_name
        else:
            _func_name = _func_name.f_code.co_name
    self.log_custom_level({level}, string, _func_name)
"""
        self._add_function_to_instance(
            self,
            func_log_name,
            function_disp_short_code
        )
        return self.success

    def disp_print_custom_level(self, level: Union[int, str], string: str, func_name: Union[str, None] = None) -> None:
        """
        @brief Print a message with a custom level.

        @param level The custom level to use.
        @param string The message to print.
        @param func_name The name of the calling function.
        """
        if isinstance(func_name, str) is False or func_name is None:
            _func_name = inspect.currentframe()
            if _func_name.f_back is not None:
                func_name = _func_name.f_back.f_code.co_name
            else:
                func_name = _func_name.f_code.co_name
        if isinstance(level, str):
            log_level_tracker: LogLevelTracker = logging.getLogger().log_level_tracker
            level = log_level_tracker.get_level(level)
            if level is None:
                self.logger.error(
                    "The provided level is not valid"
                )
                return
        if self.logger.isEnabledFor(level):
            self.logger.log(level, "(%s) %s", func_name, string)

    def disp_print_debug(self, string: str = "", func_name: Union[str, None] = None) -> None:
        """
        @brief Print a debug message (using logger).

        @param string The message to print.
        @param func_name The name of the calling function.
        """
        if isinstance(func_name, str) is False or func_name is None:
            _func_name = inspect.currentframe()
            if _func_name.f_back is not None:
                func_name = _func_name.f_back.f_code.co_name
            else:
                func_name = _func_name.f_code.co_name
        if self.debug is True:
            self.logger.debug("(%s) %s", func_name, string)

    def disp_print_info(self, string: str = "", func_name: Union[str, None] = None) -> None:
        """
        @brief Print an information message (using logger).

        @param string The message to print.
        @param func_name The name of the calling function.
        """
        if isinstance(func_name, str) is False or func_name is None:
            _func_name = inspect.currentframe()
            if _func_name.f_back is not None:
                func_name = _func_name.f_back.f_code.co_name
            else:
                func_name = _func_name.f_code.co_name
        self.logger.info("(%s) %s", func_name, string)

    def disp_print_warning(self, string: str = "", func_name: Union[str, None] = None) -> None:
        """
        @brief Print a warning message (using logger).

        @param string The message to print.
        @param func_name The name of the calling function.
        """
        if isinstance(func_name, str) is False or func_name is None:
            _func_name = inspect.currentframe()
            if _func_name.f_back is not None:
                func_name = _func_name.f_back.f_code.co_name
            else:
                func_name = _func_name.f_code.co_name
        self.logger.warning("(%s) %s", func_name, string)

    def disp_print_error(self, string: str = "", func_name: Union[str, None] = None) -> None:
        """
        @brief Print an error message (using logger).

        @param string The message to print.
        @param func_name The name of the calling function.
        """
        if isinstance(func_name, str) is False or func_name is None:
            _func_name = inspect.currentframe()
            if _func_name.f_back is not None:
                func_name = _func_name.f_back.f_code.co_name
            else:
                func_name = _func_name.f_code.co_name
        self.logger.error("(%s) %s", func_name, string)

    def disp_print_critical(self, string: str = "", func_name: Union[str, None] = None) -> None:
        """
        @brief Print a critical message (using logger).

        @param string The message to print.
        @param func_name The name of the calling function.
        """
        if isinstance(func_name, str) is False or func_name is None:
            _func_name = inspect.currentframe()
            if _func_name.f_back is not None:
                func_name = _func_name.f_back.f_code.co_name
            else:
                func_name = _func_name.f_code.co_name
        self.logger.critical("(%s) %s", func_name, string)

    def log_custom_level(self, level: Union[int, str], string: str, func_name: Union[str, None] = None) -> None:
        """
        @brief Log a message with a custom level.

        @param level The custom level to use.
        @param string The message to log.
        @param func_name The name of the calling function.
        """
        if isinstance(func_name, str) is False or func_name is None:
            _func_name = inspect.currentframe()
            if _func_name.f_back is not None:
                func_name = _func_name.f_back.f_code.co_name
            else:
                func_name = _func_name.f_code.co_name
        self.disp_print_custom_level(level, string, func_name)

    def log_debug(self, string: str = "", func_name: Union[str, None] = None) -> None:
        """
        @brief Log a debug message.

        @param string The message to log.
        @param func_name The name of the calling function.
        """
        if isinstance(func_name, str) is False or func_name is None:
            _func_name = inspect.currentframe()
            if _func_name.f_back is not None:
                func_name = _func_name.f_back.f_code.co_name
            else:
                func_name = _func_name.f_code.co_name
        self.disp_print_debug(string, func_name)

    def log_info(self, string: str = "", func_name: Union[str, None] = None) -> None:
        """
        @brief Log an info message.

        @param string The message to log.
        @param func_name The name of the calling function.
        """
        if isinstance(func_name, str) is False or func_name is None:
            _func_name = inspect.currentframe()
            if _func_name.f_back is not None:
                func_name = _func_name.f_back.f_code.co_name
            else:
                func_name = _func_name.f_code.co_name
        self.disp_print_info(string, func_name)

    def log_warning(self, string: str = "", func_name: Union[str, None] = None) -> None:
        """
        @brief Log a warning message.

        @param string The message to log.
        @param func_name The name of the calling function.
        """
        if isinstance(func_name, str) is False or func_name is None:
            _func_name = inspect.currentframe()
            if _func_name.f_back is not None:
                func_name = _func_name.f_back.f_code.co_name
            else:
                func_name = _func_name.f_code.co_name
        self.disp_print_warning(string, func_name)

    def log_error(self, string: str = "", func_name: Union[str, None] = None) -> None:
        """
        @brief Log an error message.

        @param string The message to log.
        @param func_name The name of the calling function.
        """
        if isinstance(func_name, str) is False or func_name is None:
            _func_name = inspect.currentframe()
            if _func_name.f_back is not None:
                func_name = _func_name.f_back.f_code.co_name
            else:
                func_name = _func_name.f_code.co_name
        self.disp_print_error(string, func_name)

    def log_critical(self, string: str = "", func_name: Union[str, None] = None) -> None:
        """
        @brief Log a critical message.

        @param string The message to log.
        @param func_name The name of the calling function.
        """
        if isinstance(func_name, str) is False or func_name is None:
            _func_name = inspect.currentframe()
            if _func_name.f_back is not None:
                func_name = _func_name.f_back.f_code.co_name
            else:
                func_name = _func_name.f_code.co_name
        self.disp_print_critical(string, func_name)

    def close_file(self) -> None:
        """
        @brief Close the log file if it was opened.
        """
        if self.toml_content[KEY_OUTPUT_MODE] != OUT_FILE:
            if self.log_warning_when_present is True:
                self.log_warning(
                    "The file was not opened, no need to close it",
                    inspect.currentframe().f_code.co_name
                )
            return
        if self.file_descriptor is not None:
            self.file_descriptor.close()

    def get_generated_content(self) -> str:
        """
        @brief Return the generated string.

        @return The generated content.
        """
        data = self.generated_content
        self.generated_content = ""
        return data

    def _calculate_required_spaces(self, string_length: int) -> str:
        """
        @brief Generate the required amount of spaces for the padding of the shape.

        @param string_length The length of the provided string.
        @return The number of spaces required for the padding.
        """
        if string_length >= self.max_whitespace:
            white_spaces = " "
        else:
            calculated_length = int(
                (self.max_whitespace - string_length)/2
            )
            if calculated_length % 2 == 1 and calculated_length != 0:
                calculated_length += 1
            white_spaces = self.create_string(
                calculated_length,
                " "
            )
        return white_spaces

    def _open_file(self) -> None:
        """
        @brief Open the file if required and add the current date and time.
        """
        if self.save_to_file is True and self.file_descriptor is None:
            self.file_descriptor = open(
                self.file_name,
                "a",
                encoding="utf-8",
                newline="\n"
            )
        if self.file_descriptor is not None:
            self.append_run_date()

    def _is_safe(self, content: any) -> bool:
        """
        @brief Check if an item is safe to write or not.

        @param content The item to check.
        @return True if the item is safe to write, False otherwise.
        """
        if isinstance(content, (str, int, float, tuple, complex, bytes, bytearray, memoryview)) is False:
            return False
        return True

    def create_string(self, length, character) -> str:
        """
        @brief Create a string based on a character and a length.

        @param length The length of the string.
        @param character The character to use.
        @return The created string.
        """
        line = [character for i in range(0, length)]
        string = "".join(line)
        return string

    def display_animation(self, message: str = "Hello World!", delay: float = 0.02) -> None:
        """
        @brief Print the message letter by letter while applying a provided delay.

        @param message The message to display.
        @param delay The delay between each letter.
        """
        if " " in message and self.toml_content[KEY_PRETTIFY_OUTPUT] is True and self.toml_content[KEY_PRETTIFY_OUTPUT_IN_BLOCKS] is True:
            for letter in message.split(" "):
                sys.stdout.write(letter)
                sys.stdout.flush()
                sys.stdout.write(" ")
                time.sleep(delay)
        elif self.toml_content[KEY_PRETTIFY_OUTPUT] is True:
            for letter in message:
                sys.stdout.write(letter)
                sys.stdout.flush()
                time.sleep(delay)
        else:
            sys.stdout.write(message)
        print()

    def animate_message(self, message: str = "Hello World!", delay: float = 0.02) -> None:
        """
        @brief Display or dump (to file) a message.

        @param message The message to display or dump.
        @param delay The delay between each letter.
        """
        if self._is_safe(message) is False:
            message = f"{message}"
        if self.save_to_file is True and self.file_descriptor is not None:
            self.file_descriptor.write(f"{message}\n")
        elif self.toml_content[KEY_OUTPUT_MODE] == OUT_STRING:
            self.generated_content = f"{message}\n"
        else:
            self.display_animation(message, delay)

    def disp_message_box(self, msg: str, char: str = "#") -> None:
        """
        @brief Display a message in a box.

        @param msg The message to display.
        @param char The character to use for the box.

        @note The text is displayed in the center of the box, it is just difficult to show that in a function comment.\n
        @note This is a sample box (characters and dimensions depend on the provided configuration):\n
        @example #############################\n
        @example #        Sample text        #\n
        @example #############################
        """

        box_wall = self.create_string(self.nb_chr, char)

        title_content = ""
        if "\n" in msg:
            lines = msg.split("\n")
            for i in lines:
                string_length = len(i)
                white_spaces = self._calculate_required_spaces(string_length)
                title_content += char
                title_content += white_spaces
                title_content += i
                if string_length % 2 == 1 and string_length != 0:
                    white_spaces = white_spaces[:-1]
                title_content += white_spaces
                title_content += char
                title_content += '\n'
        else:
            string_length = len(msg)
            white_spaces = self._calculate_required_spaces(string_length)
            box_wall = self.create_string(self.nb_chr, char)
            title_content += char
            title_content += white_spaces
            title_content += msg
            if string_length % 2 == 1 and string_length != 0:
                white_spaces = white_spaces[:-1]
            title_content += white_spaces
            title_content += char
            title_content += "\n"

        generated_content = f"{box_wall}\n"
        generated_content += f"{title_content}"
        generated_content += f"{box_wall}"
        self.animate_message(
            f"{generated_content}",
            self.message_animation_delay
        )

    def disp_round_message_box(self, msg: str = "Sample text") -> None:
        """
        @brief Display a message in a rounded box.

        @param msg The message to display.

        @note The text is displayed in the center of the box, it is just difficult to show that in a function comment.\n
        @note This is a sample box (characters and dimensions depend on the provided configuration):\n
        @example ╔══════════════════════╗\n
        @example ║      Sample text     ║\n
        @example ╚══════════════════════╝\n
        """

        offset_reset = 2

        # Generate the top line
        top_wall = ""
        if 'ROUND_BOX_CORNER_LEFT' in self.toml_content:
            top_wall += self.toml_content['ROUND_BOX_CORNER_LEFT']
        else:
            if self.log_warning_when_present is True:
                self.log_warning(
                    "The top left corner is not defined, using the default one",
                    inspect.currentframe().f_code.co_name
                )
            top_wall += "╔"
        if 'ROUND_BOX_HORIZONTAL' in self.toml_content:
            top_wall += self.create_string(
                self.nb_chr - offset_reset,
                self.toml_content['ROUND_BOX_HORIZONTAL']
            )
        else:
            if self.log_warning_when_present is True:
                self.log_warning(
                    "The horizontal line is not defined, using the default one",
                    inspect.currentframe().f_code.co_name
                )
            top_wall += self.create_string(
                self.nb_chr-offset_reset,
                "═"
            )
        if 'ROUND_BOX_CORNER_RIGHT' in self.toml_content:
            top_wall += self.toml_content['ROUND_BOX_CORNER_RIGHT']
        else:
            if self.log_warning_when_present is True:
                self.log_warning(
                    "The top right corner is not defined, using the default one",
                    inspect.currentframe().f_code.co_name
                )
            top_wall += "╗"

        # Generate the bottom line
        bottom_wall = ""
        if 'ROUND_BOX_CORNER_BOTTOM_LEFT' in self.toml_content:
            bottom_wall += self.toml_content['ROUND_BOX_CORNER_BOTTOM_LEFT']
        else:
            if self.log_warning_when_present is True:
                self.log_warning(
                    "The bottom left corner is not defined, using the default one",
                    inspect.currentframe().f_code.co_name
                )
            bottom_wall += "╚"

        if 'ROUND_BOX_HORIZONTAL' in self.toml_content:
            bottom_wall += self.create_string(
                self.nb_chr-offset_reset,
                self.toml_content['ROUND_BOX_HORIZONTAL']
            )
        else:
            if self.log_warning_when_present is True:
                self.log_warning(
                    "The horizontal line is not defined, using the default one",
                    inspect.currentframe().f_code.co_name
                )
            bottom_wall += self.create_string(
                self.nb_chr-offset_reset,
                "═"
            )
        if 'ROUND_BOX_CORNER_BOTTOM_RIGHT' in self.toml_content:
            bottom_wall += self.toml_content['ROUND_BOX_CORNER_BOTTOM_RIGHT']
        else:
            if self.log_warning_when_present is True:
                self.log_warning(
                    "The bottom right corner is not defined, using the default one",
                    inspect.currentframe().f_code.co_name
                )
            bottom_wall += "╝"

        border_character = ""
        if 'ROUND_BOX_VERTICAL' in self.toml_content:
            border_character = self.toml_content['ROUND_BOX_VERTICAL']
        else:
            if self.log_warning_when_present is True:
                self.log_warning(
                    "The vertical line is not defined, using the default one",
                    inspect.currentframe().f_code.co_name
                )
            border_character = "║"

        center_content = ""
        if "\n" in msg:
            lines = msg.split("\n")
            for i in lines:
                string_length = len(i)
                white_spaces = self._calculate_required_spaces(string_length)
                center_content += border_character
                center_content += white_spaces
                center_content += i
                if string_length % 2 == 1 and string_length != 0:
                    white_spaces = white_spaces[:-1]
                center_content += white_spaces
                center_content += border_character
                center_content += '\n'
        else:
            string_length = len(msg)
            white_spaces = self._calculate_required_spaces(string_length)
            center_content += border_character
            center_content += white_spaces
            center_content += msg
            if string_length % 2 == 1 and string_length != 0:
                white_spaces = white_spaces[:-1]
            center_content += white_spaces
            center_content += border_character
            center_content += "\n"

        generated_content = f"{top_wall}\n"
        generated_content += f"{center_content}"
        generated_content += f"{bottom_wall}"
        self.animate_message(
            f"{generated_content}",
            self.message_animation_delay
        )

    def disp_diff_side_and_top_message_box(self, msg: str) -> None:
        """
        @brief Display a message in a box with different side and top characters.

        @param msg The message to display.

        @note The text is displayed in the center of the box, it is just difficult to show that in a function comment.\n
        @note This is a sample box (characters and dimensions depend on the provided configuration):\n
        @example _____________________________\n
        @example |        Sample text        |\n
        @example _____________________________
        """
        ceiling_boxes = ""
        if 'DIFF_BORDER_LINE_CHARACTER_BOX' in self.toml_content:
            ceiling_boxes = self.toml_content['DIFF_BORDER_LINE_CHARACTER_BOX']
        else:
            if self.log_warning_when_present is True:
                self.log_warning(
                    "The ceiling boxes are not defined, using the default one",
                    inspect.currentframe().f_code.co_name
                )
            ceiling_boxes = "-"

        border_character = ""
        if 'DIFF_SIDE_LINE_CHARACTER_BOX' in self.toml_content:
            border_character = self.toml_content['DIFF_SIDE_LINE_CHARACTER_BOX']
        else:
            if self.log_warning_when_present is True:
                self.log_warning(
                    "The border character is not defined, using the default one",
                    inspect.currentframe().f_code.co_name
                )
            border_character = "|"

        box_wall = self.create_string(self.nb_chr, ceiling_boxes)

        title_content = ""
        if "\n" in msg:
            lines = msg.split("\n")
            for i in lines:
                string_length = len(i)
                white_spaces = self._calculate_required_spaces(string_length)
                title_content += border_character
                title_content += white_spaces
                title_content += i
                if string_length % 2 == 1 and string_length != 0:
                    white_spaces = white_spaces[:-1]
                title_content += white_spaces
                title_content += border_character
                title_content += '\n'
        else:
            string_length = len(msg)
            white_spaces = self._calculate_required_spaces(string_length)
            title_content += border_character
            title_content += white_spaces
            title_content += msg
            if string_length % 2 == 1 and string_length != 0:
                white_spaces = white_spaces[:-1]
            title_content += white_spaces
            title_content += border_character
            title_content += "\n"

        generated_content = f"{box_wall}\n"
        generated_content += f"{title_content}"
        generated_content += f"{box_wall}"
        self.animate_message(
            f"{generated_content}",
            self.message_animation_delay
        )

    def disp_box_no_vertical(self, message: str, character: str = "@") -> None:
        """
        @brief Print a box format without internal vertical bars.

        @param message The message to display.
        @param character The character to use for the box.
        @note The text is displayed in the center of the box, it is just difficult to show that in a function comment.\n
        @note This is a sample box (characters and dimensions depend on the provided configuration):\n
        @example #############################\n
        @example          Sample text         \n
        @example #############################
        """
        if 'BOX_NO_VERTICAL' in self.toml_content:
            char = self.toml_content['BOX_NO_VERTICAL']
        else:
            if self.log_warning_when_present is True:
                self.log_warning(
                    "The box character is not defined, using the default one",
                    inspect.currentframe().f_code.co_name
                )
            char = character

        box_wall = self.create_string(self.nb_chr, char)

        title_content = ""
        if "\n" in message:
            lines = message.split("\n")
            for i in lines:
                string_length = len(i)
                white_spaces = self._calculate_required_spaces(string_length)
                title_content += white_spaces
                title_content += i
                if string_length % 2 == 1 and string_length != 0:
                    white_spaces = white_spaces[:-1]
                title_content += white_spaces
                title_content += '\n'
        else:
            string_length = len(message)
            white_spaces = self._calculate_required_spaces(string_length)
            title_content += white_spaces
            title_content += message
            if string_length % 2 == 1 and string_length != 0:
                white_spaces = white_spaces[:-1]
            title_content += white_spaces
            title_content += "\n"

        generated_content = f"{box_wall}\n"
        generated_content += f"{title_content}"
        generated_content += f"{box_wall}"
        self.animate_message(
            f"{generated_content}",
            self.message_animation_delay
        )

    def disp_vertical_message_box(self, msg: str, character: str = '') -> None:
        """
        @brief Display a message in a box with vertical bars.

        @param msg The message to display.
        @param character The character to use for the box.
        @note The text is displayed in the center of the box, it is just difficult to show that in a function comment.\n
        @note This is a sample box (characters and dimensions depend on the provided configuration):\n
        @example ###############\n
        @example #             #\n
        @example #             #\n
        @example #             #\n
        @example # Sample text #\n
        @example #             #\n
        @example #             #\n
        @example #             #\n
        @example ###############
        """

        if 'BOX_NO_VERTICAL' in self.toml_content:
            character = self.toml_content['BOX_NO_VERTICAL']
        elif character == '':
            if self.log_warning_when_present is True:
                self.log_warning(
                    "The box character is not defined, using the default one",
                    inspect.currentframe().f_code.co_name
                )
            character = "#"

        box_wall = self.create_string(self.nb_chr, character)

        title_content = ""
        if "\n" in msg:
            lines = msg.split("\n")
            for i in lines:
                string_length = len(i)
                white_spaces = self._calculate_required_spaces(string_length)
                title_content += character
                title_content += white_spaces
                title_content += i
                if string_length % 2 == 1 and string_length != 0:
                    white_spaces = white_spaces[:-1]
                title_content += white_spaces
                title_content += character
                title_content += "\n"
            msg = lines
        else:
            string_length = len(msg)
            white_spaces = self._calculate_required_spaces(string_length)
            title_content += character
            title_content += white_spaces
            title_content += msg
            if string_length % 2 == 1 and string_length != 0:
                white_spaces = white_spaces[:-1]
            title_content += white_spaces
            title_content += character
            title_content += "\n"

        inner_length = int(self.max_whitespace)
        inner_line = self.create_string(
            inner_length,
            " "
        )
        inner_line = f"{character}{inner_line}{character}"

        generated_content = f"{box_wall}\n"
        if "\n" in msg:
            max_height = (inner_length / 4) - len(msg)
            if max_height <= 2:
                max_height = 2
        else:
            max_height = 2
        i = 0
        while i < max_height:
            generated_content += f"{inner_line}\n"
            i += 1
        generated_content += f"{title_content}"
        i = 0
        while i < max_height:
            generated_content += f"{inner_line}\n"
            i += 1

        generated_content += f"{box_wall}"

        self.animate_message(
            f"{generated_content}",
            self.message_animation_delay
        )

    def box_vertical_no_horizontal(self, message: str, character: str = "") -> None:
        """
        @brief Print a box format without internal horizontal bars.

        @param message The message to display.
        @param character The character to use for the box.
        @note The text is displayed in the center of the box, it is just difficult to show that in a function comment.\n
        @note This is a sample box (characters and dimensions depend on the provided configuration):\n
        @example #                            #\n
        @example #                            #\n
        @example #                            #\n
        @example #                            #\n
        @example #                            #\n
        @example #       Sample text          #\n
        @example #                            #\n
        @example #                            #\n
        @example #                            #\n
        @example #                            #\n
        @example #                            #\n
        """
        if 'BOX_VERTICAL_NO_HORIZONTAL' in self.toml_content:
            character = self.toml_content['BOX_VERTICAL_NO_HORIZONTAL']
        elif character == '':
            if self.log_warning_when_present is True:
                self.log_warning(
                    "The box character is not defined, using the default one",
                    inspect.currentframe().f_code.co_name
                )
            character = "#"

        title_content = ""
        if "\n" in message:
            lines = message.split("\n")
            for i in lines:
                string_length = len(i)
                white_spaces = self._calculate_required_spaces(string_length)
                title_content += character
                title_content += white_spaces
                title_content += i
                if string_length % 2 == 1 and string_length != 0:
                    white_spaces = white_spaces[:-1]
                title_content += white_spaces
                title_content += character
                title_content += "\n"
            message = lines
        else:
            string_length = len(message)
            white_spaces = self._calculate_required_spaces(string_length)
            title_content += character
            title_content += white_spaces
            title_content += message
            if string_length % 2 == 1 and string_length != 0:
                white_spaces = white_spaces[:-1]
            title_content += white_spaces
            title_content += character
            title_content += "\n"
        inner_length = int(self.max_whitespace)
        if len(message) > self.max_whitespace:
            inner_length = self.max_whitespace
        inner_line = self.create_string(
            inner_length,
            " "
        )
        inner_line = f"{character}{inner_line}{character}"

        generated_content = ""
        if "\n" in message:
            max_height = (inner_length / 4) - len(message)
            if max_height <= 2:
                max_height = 2
        else:
            max_height = 2
        i = 0
        while i < max_height:
            generated_content += f"{inner_line}\n"
            i += 1
        generated_content += f"{title_content}"
        i = 0
        while i < max_height:
            if i+1 >= max_height:
                generated_content += f"{inner_line}"
            else:
                generated_content += f"{inner_line}\n"
            i += 1

        self.animate_message(
            f"{generated_content}",
            self.message_animation_delay
        )

    def title(self, title: str) -> None:
        """
        @brief Print a beautified title.

        @param title The title to display.
        """
        self.disp_message_box(title, self.title_wall_chr)

    def sub_title(self, sub_title: str) -> None:
        """
        @brief Print a beautified subtitle.

        @param sub_title The subtitle to display.
        """
        self.disp_message_box(sub_title, self.sub_title_wall_chr)

    def sub_sub_title(self, sub_sub_title: str) -> None:
        """
        @brief Print a beautified sub-subtitle.

        @param sub_sub_title The sub-subtitle to display.
        """
        self.disp_message_box(sub_sub_title, self.sub_sub_title_wall_chr)

    def message(self, message: Union[str, list]) -> None:
        """
        @brief Print a beautified message.

        @param message The message to display.
        @note This function displays the provided message using the 'MESSAGE_CHARACTER' key in the toml configuration\n
        @note Here is an example for the output (This is determined by the key repeated twice)\n
        @example @@ This is an example message @@
        """
        if isinstance(message, list) is True:
            for msg in message:
                m_msg = f"{self.message_char}{self.message_char} {msg} "
                m_msg += f"{self.message_char}{self.message_char}"
                self.animate_message(
                    m_msg,
                    self.message_animation_delay
                )
        else:
            msg = f"{self.message_char}{self.message_char} "
            msg += f" {message} {self.message_char}{self.message_char}"
            self.animate_message(
                msg,
                self.message_animation_delay
            )

    def error_message(self, message: Union[str, list]) -> None:
        """
        @brief Print a beautified error message.

        @param message The error message to display.
        @note This function displays the provided message using the 'MESSAGE_CHARACTER' key in the toml configuration\n
        @note Here is an example for the output (This is determined by the key repeated twice)\n
        @example ## This is an example message ##
        """
        if isinstance(message, list) is True:
            m_msg = f"{self.message_error_char}{self.message_error_char} Error: "
            m_msg += f"{self.message_error_char}{self.message_error_char}"
            for msg in message:
                m_msg = f"{self.message_error_char}{self.message_error_char} {msg} "
                m_msg += f"{self.message_error_char}{self.message_error_char}"
                self.animate_message(
                    m_msg,
                    self.message_animation_delay
                )
        else:
            msg = f"{self.message_error_char}{self.message_error_char} Error:"
            msg += f" {message} {self.message_error_char}{self.message_error_char}"
            self.animate_message(
                msg,
                self.message_animation_delay
            )

    def success_message(self, message: Union[str, list]) -> None:
        """
        @brief Print a beautified success message.

        @param message The success message to display.
        @note This function displays the provided message using the 'MESSAGE_CHARACTER' key in the toml configuration\n
        @note Here is an example for the output (This is determined by the key repeated twice)\n
        @example // This is an example message //
        """
        if isinstance(message, list) is True:
            m_msg = f"{self.message_success_char}{self.message_success_char} Success: "
            m_msg += f"{self.message_success_char}{self.message_success_char}"
            for msg in message:
                m_msg = f"{self.message_success_char}{self.message_success_char} {msg} "
                m_msg += f"{self.message_success_char}{self.message_success_char}"
                self.animate_message(
                    m_msg,
                    self.message_animation_delay
                )
        else:
            msg = f"{self.message_success_char}{self.message_success_char} Success:"
            msg += f" {message} {self.message_success_char}{self.message_success_char}"
            self.animate_message(
                msg,
                self.message_animation_delay
            )

    def warning_message(self, message: Union[str, list]) -> None:
        """
        @brief Print a beautified warning message.

        @param message The warning message to display.
        @note This function displays the provided message using the 'MESSAGE_CHARACTER' key in the toml configuration\n
        @note Here is an example for the output (This is determined by the key repeated twice)\n
        @example !! This is an example message !!
        """
        if isinstance(message, list) is True:
            m_msg = f"{self.message_warning_char}{self.message_warning_char} Warning: "
            m_msg += f"{self.message_warning_char}{self.message_warning_char}"
            for msg in message:
                m_msg = f"{self.message_warning_char}{self.message_warning_char} {msg} "
                m_msg += f"{self.message_warning_char}{self.message_warning_char}"
                self.animate_message(
                    m_msg,
                    self.message_animation_delay
                )
        else:
            msg = f"{self.message_warning_char}{self.message_warning_char} Warning:"
            msg += f" {message} {self.message_warning_char}{self.message_warning_char}"
            self.animate_message(
                msg,
                self.message_animation_delay
            )

    def question_message(self, message: Union[str, list]) -> None:
        """
        @brief Print a beautified question message.

        @param message The question message to display.
        @note This function displays the provided message using the 'MESSAGE_CHARACTER' key in the toml configuration\n
        @note Here is an example for the output (This is determined by the key repeated twice)\n
        @example ?? This is an example message ??
        """
        if isinstance(message, list) is True:
            m_msg = f"{self.message_question_char}{self.message_question_char} Question: "
            m_msg += f"{self.message_question_char}{self.message_question_char}"
            for msg in message:
                m_msg = f"{self.message_question_char}{self.message_question_char} {msg} "
                m_msg += f"{self.message_question_char}{self.message_question_char}"
                self.animate_message(
                    m_msg,
                    self.message_animation_delay
                )
        else:
            msg = f"{self.message_question_char}{self.message_question_char} Question:"
            msg += f" {message} {self.message_question_char}{self.message_question_char}"
            self.animate_message(
                msg,
                self.message_animation_delay
            )

    def inform_message(self, message: Union[str, List]) -> None:
        """
        @brief Print a beautified information message.

        @param message The information message to display.
        @note This function displays the provided message using the 'MESSAGE_CHARACTER' key in the toml configuration\n
        @note Here is an example for the output (This is determined by the key repeated twice)\n
        @example ii This is an example message ii
        """
        if isinstance(message, list) is True:
            for msg in message:
                m_msg = f"{self.message_inform_char}{self.message_inform_char} {msg} "
                m_msg += f"{self.message_inform_char}{self.message_inform_char}"
                self.animate_message(
                    m_msg,
                    self.message_animation_delay
                )
        else:
            msg = f"{self.message_inform_char}{self.message_inform_char} {message} "
            msg += f"{self.message_inform_char}{self.message_inform_char}"
            self.animate_message(
                msg,
                self.message_animation_delay
            )

    def _tree_node(self, line: str, offset: int, index: int, max_lenght: int) -> str:
        """
        @brief Display a line of the tree.

        @param line The line to display.
        @param offset The offset for the line.
        @param index The index of the line.
        @param max_lenght The maximum length of the tree.
        @return The processed line.
        @note The characters displayed in this tree function is managed by the following keys:\n
        @note     * TREE_NODE_CHAR\n
        @note     * TREE_NODE_END_CHAR\n
        @note     * TREE_LINE_SEPERATOR_CHAR\n
        @note     * TREE_COLUMN_SEPERATOR_CHAR\n
        @example     Here is an example generated by this function:\n
        @example     ├─── data1\n
        @example     └─── data2
        """
        processed_line = str()
        i = 0
        while i < offset:
            processed_line += f"{self.tree_column_seperator_char}   "
            i += 1
        if index is max_lenght:
            processed_line += f"{self.tree_node_end_char}{self.tree_line_seperator_char}"
            processed_line += f"{self.tree_line_seperator_char}{self.tree_line_seperator_char}"
        else:
            processed_line += f"{self.tree_node_char}{self.tree_line_seperator_char}"
            processed_line += f"{self.tree_line_seperator_char}{self.tree_line_seperator_char}"
        if self._is_safe(line) is False:
            line = f"{line}"
        processed_line += " "
        processed_line += line
        processed_line += '\n'
        return processed_line

    def tree(self, title: str, data: List[str], offset: int = 0) -> Union[str, None]:
        """
        @brief Print a list under the form of a beautified tree.

        @param title The title of the tree.
        @param data The data to display in the tree.
        @param offset The offset for the tree.
        @note The characters displayed in this tree function is managed by the following keys:\n
        @note     * TREE_NODE_CHAR\n
        @note     * TREE_NODE_END_CHAR\n
        @note     * TREE_LINE_SEPERATOR_CHAR\n
        @note     * TREE_COLUMN_SEPERATOR_CHAR\n
        @example     Here is an example generated by this function:\n
        @example     ├─── data1\n
        @example     └─── data2
        @return A stringified version of the tree if not set to be displayed.
        """
        generated_content = ""
        if offset == 0:
            generated_content += f"{title}\n"
        length = len(data) - 1

        for line in enumerate(data):
            if isinstance(data, list) and isinstance(line[1], (list, dict)):
                generated_content += self._tree_node(
                    "<list instance>",
                    offset,
                    line[0],
                    length
                )
                generated_content += self.tree(line[0], line[1], offset + 1)
                continue
            if isinstance(data, dict) and isinstance(data[line[1]], (list, dict)):
                generated_content += self._tree_node(
                    line[1],
                    offset,
                    line[0],
                    length
                )
                generated_content += self.tree(
                    line[0],
                    data[line[1]],
                    offset + 1
                )
                continue
            if isinstance(data, dict) and isinstance(data[line[1]], dict) is False:
                generated_content += self._tree_node(
                    f"{line[1]}: {data[line[1]]}",
                    offset,
                    line[0],
                    length
                )
            else:
                generated_content += self._tree_node(
                    line[1],
                    offset,
                    line[0],
                    length
                )
        if offset == 0:
            self.animate_message(
                f"{generated_content}",
                self.message_animation_delay
            )
        else:
            return generated_content

    def append_run_date(self) -> None:
        """
        @brief Add the date and time at which the program was launched.
        @note The text is displayed in the center of the box, it is just difficult to show that in a function comment.\n
        @note This is a sample box (characters and dimensions depend on the provided configuration):\n
        @example ########################################\n
        @example #    Run date: 07/06/2024 22:26:10     #\n
        @example ########################################
        """
        self.title(f"Run date: {time.strftime('%d/%m/%Y %H:%M:%S')} ")

    def test_the_class(self) -> None:
        """
        @brief Test function to ensure all implemented methods work as expected.
        """
        test_data = {
            "test_data1": "test_data1.1",
            "test_data2": "test_data2.1",
            "test_data3": [
                "test_data_list3.1",
                "test_data_list3.2",
                "test_data_list3.3",
                "test_data_list3.4",
                "test_data_list3.5"
            ],
            "test_data4": "test_data4.1",
            "test_data5": {
                "test_data5.1": "test_data5.1.1",
                "test_data5.2": "test_data5.2.1",
                "test_data5.3": "test_data5.3.1",
                "test_data5.4": "test_data5.4.1"
            },
            "test_data6": [
                {
                    "test_data6.1": "test_data6.1.1",
                    "test_data6.2": "test_data6.2.1"
                },
                [
                    "test_data_list6.3.1",
                    "test_data_list6.3.1",
                    "test_data_list6.3.1",
                    "test_data_list6.3.1"
                ]
            ],
            "test_data7": {
                "test_data7.1": {
                    "test_data7.1.1": "test_data7.1.1.1",
                    "test_data7.1.2": "test_data7.1.2.1"
                },
                "test_data7.2": [
                    "test_data7.2.1",
                    "test_data7.2.2",
                    "test_data7.2.3",
                    "test_data7.2.4",
                    "test_data7.2.5"
                ]
            }
        }
        self.append_run_date()
        self.animate_message("Test Message !", 0.01)
        self.question_message("Test Question message !")
        self.error_message("Test Error !")
        self.inform_message("Test Inform !")
        self.success_message("Test Success !")
        self.warning_message("Test Warning !")
        self.title("Test title")
        self.sub_title("Test sub title")
        self.sub_sub_title("Test sub sub title")
        self.disp_box_no_vertical('Test Box no vertical')
        self.disp_round_message_box("Test Disp round message box")
        self.disp_diff_side_and_top_message_box(
            "Test Disp diff side and top message box"
        )
        self.disp_vertical_message_box("Test Disp vertical message box")
        self.box_vertical_no_horizontal("Test Box vertical no horizontal")
        self.tree("Test data", test_data)
        prev_debug = self.debug
        self.debug = True
        self.disp_print_debug("This is a test for debug messages")
        self.debug = prev_debug
        self.disp_print_info("This is a test for info messages")
        self.disp_print_warning("This is a test for warning messages")
        self.disp_print_error("This is a test for error messages")
        self.disp_print_critical("This is a test for critical messages")
        self.log_custom_level(
            logging.WARNING, "This is a test warning for custom level messages"
        )
        custom_level_int = 2
        level_name = "DARLING"
        if self.add_custom_level(
            custom_level_int,
            level_name,
            "purple",
            LoggerColours.BLACK
        ) == self.error:
            self.log_error(
                f"The custom level '{level_name}' could not be added, please check the configuration"
            )
        else:
            self.log_custom_level(
                custom_level_int,
                f"This is a test for custom level message \"{logging.getLevelName(custom_level_int)}\""
            )
        custom_level_int = 196
        level_name = "Ikuno"
        if self.add_custom_level(
            custom_level_int,
            level_name,
            "cyan",
            LoggerColours.BLACK
        ) == self.error:
            self.log_error(
                f"The custom level '{level_name}' could not be added, please check the configuration"
            )
        else:
            self.log_custom_level(
                custom_level_int,
                f"This is a test for custom level message \"{logging.getLevelName(custom_level_int)}\""
            )
        self.close_file()


if __name__ == "__main__":
    DI = Disp(
        toml_content=TOML_CONF,
        save_to_file=False,
        file_name="test_run.tmp",
        file_descriptor=None,
        debug=False
    )
    DI.test_the_class()
