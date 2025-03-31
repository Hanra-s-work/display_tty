##
# EPITECH PROJECT, 2024
# display_tty
# File description:
# log_level_tracker.py
##

from typing import Union, Dict
import logging


class LogLevelTracker:
    """
    Class in charge of tracking the logging levels of the logger library.
    """

    def __init__(self, bypass_check: bool = False):
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
        This is a class that will be used to patch the small error in the logging library regarding the notset level.
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
        Method in charge of adding a new logging level.
        """
        if level_name in self.levels:
            return False
        self.levels[level_name] = level
        return True

    def get_level(self, level_name: str) -> Union[int, None]:
        """
        Method in charge of getting the logging level of a given level name.
        """
        return self.levels.get(level_name, None)

    def get_level_name(self, level: int) -> Union[str, None]:
        """
        Method in charge of getting the logging level name of a given level.
        """
        for key, value in self.levels.items():
            if value == level:
                return key
        return None

    def check_presence(self) -> bool:
        """
        Method in charge of checking this class is present in the logging library or not.
        """
        root_logger = logging.getLogger()
        if not hasattr(root_logger, "log_level_tracker"):
            return False
        return True

    def inject_class(self) -> bool:
        """
        Method in charge of injecting this class in the logging library.
        """
        if not self.check_presence():
            root_logger = logging.getLogger()
            root_logger.log_level_tracker = self
            logging.log_level_tracker = self
            return True
        return False
