##
# EPITECH PROJECT, 2024
# display_tty
# File description:
# colours.py
##

from typing import Union


class LoggerColours:
    """
    Class in charge of containing the colour names and id's that correspond to the allowed colours for the logger library.
    """
    BLUE = 0
    RED = 1
    CYAN = 2
    BLACK = 3
    GREEN = 4
    WHITE = 5
    YELLOW = 6
    PURPLE = 7
    LIGHT_RED = 8
    LIGHT_BLUE = 9
    LIGHT_CYAN = 10
    LIGHT_WHITE = 11
    LIGHT_BLACK = 12
    LIGHT_GREEN = 13
    LIGHT_YELLOW = 14
    LIGHT_PURPLE = 15
    BOLD_BLUE = 16
    BOLD_RED = 17
    BOLD_CYAN = 18
    BOLD_BLACK = 19
    BOLD_GREEN = 20
    BOLD_WHITE = 21
    BOLD_YELLOW = 22
    BOLD_PURPLE = 23
    BOLD_LIGHT_RED = 24
    BOLD_LIGHT_BLUE = 25
    BOLD_LIGHT_CYAN = 26
    BOLD_LIGHT_WHITE = 27
    BOLD_LIGHT_BLACK = 28
    BOLD_LIGHT_GREEN = 29
    BOLD_LIGHT_YELLOW = 30
    BOLD_LIGHT_PURPLE = 31
    THIN_BLUE = 32
    THIN_RED = 33
    THIN_CYAN = 34
    THIN_BLACK = 35
    THIN_GREEN = 36
    THIN_WHITE = 37
    THIN_YELLOW = 38
    THIN_PURPLE = 39
    THIN_LIGHT_RED = 40
    THIN_LIGHT_BLUE = 41
    THIN_LIGHT_CYAN = 42
    THIN_LIGHT_WHITE = 43
    THIN_LIGHT_BLACK = 44
    THIN_LIGHT_GREEN = 45
    THIN_LIGHT_YELLOW = 46
    THIN_LIGHT_PURPLE = 47

    @staticmethod
    def get_colour_string(colour_class, colour_code: int) -> str:
        """_summary_
            Function in charge of returning the name of the colour to use.

        Args:
            colour_class (_type_): _description_
            colour_code (int): _description_

        Returns:
            str: _description_
        """
        if isinstance(colour_code, int) is False or colour_code < 0:
            return ""
        for i in dir(colour_class):
            if colour_code == getattr(colour_class, i):
                return str(i).lower()
        return ""

    @staticmethod
    def get_colour_code(colour_class, colour_name: str) -> Union[int, None]:
        """_summary_
            Function in charge of returning the code of the colour to use.

        Args:
            colour_class (_type_): _description_
            colour_name (str): _description_

        Returns:
            Union[int, None]: _description_
        """
        if not isinstance(colour_name, str) or not colour_name or len(colour_name) == 0:
            return None
        for i in dir(colour_class):
            if callable(getattr(colour_class, i)):
                continue
            if colour_name == i.lower():
                return getattr(colour_class, i)
        return None

    @staticmethod
    def check_if_colour_present(colour_class, colour_name: str) -> bool:
        """_summary_
            Function in charge of checking if the colour is present in the list of allowed colours.

        Args:
            colour_class (_type_): _description_
            colour_name (str): _description_

        Returns:
            bool: _description_
        """
        if not isinstance(colour_name, str) or not colour_name or len(colour_name) == 0:
            return None
        colour_name_lower = colour_name.lower()
        for i in dir(colour_class):
            if callable(getattr(colour_class, i)):
                continue
            if colour_name_lower == i.lower():
                return True
        return False

    @staticmethod
    def get_all_colours(colour_class) -> list:
        """_summary_
            Function in charge of returning the list of all the colours.

        Args:
            colour_class (_type_): _description_

        Returns:
            list: _description_
        """
        return [i for i in dir(colour_class) if not i.startswith("__") and not callable(getattr(colour_class, i))]
