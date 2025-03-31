##
# EPITECH PROJECT, 2024
# display_tty
# File description:
# log_level_tracker.py
##

"""
@file log_level_tracker.py
@brief Provides the LogLevelTracker class to manage and track logging levels in the logging library.
@details This module allows adding custom logging levels, retrieving levels by name or value, 
and injecting the LogLevelTracker class into the logging library for extended functionality.
"""

from typing import Union, Dict
import logging


class LogLevelTracker:
    """
    @class LogLevelTracker
    @brief Class in charge of tracking the logging levels of the logger library.
    """

    def __init__(self, bypass_check: bool = False):
        """
        @brief Constructor for the LogLevelTracker class.
        @param bypass_check If True, bypasses the injection of the class into the logging library.
        """
        self.levels: Dict = {
            "DEBUG": logging.DEBUG,
            "INFO": logging.INFO,
            "WARN": logging.WARN,
            "ERROR": logging.ERROR,
            "CRITICAL": logging.CRITICAL,
        }
        if not bypass_check:
            self.inject_class()
            return

    class Levels:
        """
        @class Levels
        @brief Class used to patch the small error in the logging library regarding the NOTSET level.
        """

        CRITICAL = logging.CRITICAL
        CRIT = CRITICAL
        FATAL = CRITICAL
        ERROR = logging.ERROR
        WARNING = logging.WARNING
        WARN = WARNING
        INFO = logging.INFO
        DEBUG = logging.DEBUG
        NOTSET = 1
        __all__ = [
            CRITICAL,
            CRIT,
            FATAL,
            ERROR,
            WARNING,
            WARN,
            INFO,
            DEBUG,
            NOTSET,
        ]

    def add_level(self, level_name: str, level: int) -> bool:
        """
        @brief Adds a new logging level.
        @param level_name The name of the new logging level.
        @param level The integer value of the new logging level.
        @return True if the level was added successfully, False if the level already exists.
        """
        if level_name in self.levels:
            return False
        self.levels[level_name] = level
        return True

    def get_level(self, level_name: str) -> Union[int, None]:
        """
        @brief Retrieves the logging level for a given level name.
        @param level_name The name of the logging level.
        @return The integer value of the logging level, or None if the level name does not exist.
        """
        return self.levels.get(level_name, None)

    def get_level_name(self, level: int) -> Union[str, None]:
        """
        @brief Retrieves the logging level name for a given level value.
        @param level The integer value of the logging level.
        @return The name of the logging level, or None if the level value does not exist.
        """
        for key, value in self.levels.items():
            if value == level:
                return key
        return None

    def check_presence(self) -> bool:
        """
        @brief Checks if this class is already present in the logging library.
        @return True if the class is present, False otherwise.
        """
        root_logger = logging.getLogger()
        if not hasattr(root_logger, "log_level_tracker"):
            return False
        return True

    def inject_class(self) -> bool:
        """
        @brief Injects this class into the logging library if it is not already present.
        @return True if the class was successfully injected, False otherwise.
        """
        if not self.check_presence():
            root_logger = logging.getLogger()
            root_logger.log_level_tracker = self
            logging.log_level_tracker = self
            return True
        return False
