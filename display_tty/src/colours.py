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
# FILE: colours.py
# CREATION DATE: 06-11-2025
# LAST Modified: 12:31:22 06-11-2025
# DESCRIPTION: 
# A module that allows you to display text with a few boilers (i.e. put your text in a square for titles). It also allows to log to the terminal by wrapping around the logging library.
# /STOP
# COPYRIGHT: (c) Henry Letellier
# PURPOSE: File in charge of containing the class that will track logger colours that can be used by the class.
# // AR
# +==== END display_tty =================+
"""


from typing import Union


class LoggerColours:
    """
    @class LoggerColours
    @brief Class in charge of containing the colour names and id's that correspond to the allowed colours for the logger library.
    """

    # Colour constants
    BLUE = 0  # @brief Colour code for blue.
    RED = 1  # @brief Colour code for red.
    CYAN = 2  # @brief Colour code for cyan.
    BLACK = 3  # @brief Colour code for black.
    GREEN = 4  # @brief Colour code for green.
    WHITE = 5  # @brief Colour code for white.
    YELLOW = 6  # @brief Colour code for yellow.
    PURPLE = 7  # @brief Colour code for purple.
    LIGHT_RED = 8  # @brief Colour code for light red.
    LIGHT_BLUE = 9  # @brief Colour code for light blue.
    LIGHT_CYAN = 10  # @brief Colour code for light cyan.
    LIGHT_WHITE = 11  # @brief Colour code for light white.
    LIGHT_BLACK = 12  # @brief Colour code for light black.
    LIGHT_GREEN = 13  # @brief Colour code for light green.
    LIGHT_YELLOW = 14  # @brief Colour code for light yellow.
    LIGHT_PURPLE = 15  # @brief Colour code for light purple.
    BOLD_BLUE = 16  # @brief Colour code for bold blue.
    BOLD_RED = 17  # @brief Colour code for bold red.
    BOLD_CYAN = 18  # @brief Colour code for bold cyan.
    BOLD_BLACK = 19  # @brief Colour code for bold black.
    BOLD_GREEN = 20  # @brief Colour code for bold green.
    BOLD_WHITE = 21  # @brief Colour code for bold white.
    BOLD_YELLOW = 22  # @brief Colour code for bold yellow.
    BOLD_PURPLE = 23  # @brief Colour code for bold purple.
    BOLD_LIGHT_RED = 24  # @brief Colour code for bold light red.
    BOLD_LIGHT_BLUE = 25  # @brief Colour code for bold light blue.
    BOLD_LIGHT_CYAN = 26  # @brief Colour code for bold light cyan.
    BOLD_LIGHT_WHITE = 27  # @brief Colour code for bold light white.
    BOLD_LIGHT_BLACK = 28  # @brief Colour code for bold light black.
    BOLD_LIGHT_GREEN = 29  # @brief Colour code for bold light green.
    BOLD_LIGHT_YELLOW = 30  # @brief Colour code for bold light yellow.
    BOLD_LIGHT_PURPLE = 31  # @brief Colour code for bold light purple.
    THIN_BLUE = 32  # @brief Colour code for thin blue.
    THIN_RED = 33  # @brief Colour code for thin red.
    THIN_CYAN = 34  # @brief Colour code for thin cyan.
    THIN_BLACK = 35  # @brief Colour code for thin black.
    THIN_GREEN = 36  # @brief Colour code for thin green.
    THIN_WHITE = 37  # @brief Colour code for thin white.
    THIN_YELLOW = 38  # @brief Colour code for thin yellow.
    THIN_PURPLE = 39  # @brief Colour code for thin purple.
    THIN_LIGHT_RED = 40  # @brief Colour code for thin light red.
    THIN_LIGHT_BLUE = 41  # @brief Colour code for thin light blue.
    THIN_LIGHT_CYAN = 42  # @brief Colour code for thin light cyan.
    THIN_LIGHT_WHITE = 43  # @brief Colour code for thin light white.
    THIN_LIGHT_BLACK = 44  # @brief Colour code for thin light black.
    THIN_LIGHT_GREEN = 45  # @brief Colour code for thin light green.
    THIN_LIGHT_YELLOW = 46  # @brief Colour code for thin light yellow.
    THIN_LIGHT_PURPLE = 47  # @brief Colour code for thin light purple.

    @staticmethod
    def get_colour_string(colour_class, colour_code: int) -> str:
        """
        @brief Function in charge of returning the name of the colour to use.
        @param colour_class The class containing the colour definitions.
        @param colour_code The integer code of the colour.
        @return The name of the colour as a string, or an empty string if the code is invalid.
        """
        if isinstance(colour_code, int) is False or colour_code < 0:
            return ""
        for i in dir(colour_class):
            if colour_code == getattr(colour_class, i):
                return str(i).lower()
        return ""

    @staticmethod
    def get_colour_code(colour_class, colour_name: str) -> Union[int, None]:
        """
        @brief Function in charge of returning the code of the colour to use.
        @param colour_class The class containing the colour definitions.
        @param colour_name The name of the colour as a string.
        @return The integer code of the colour, or None if the name is invalid.
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
        """
        @brief Function in charge of checking if the colour is present in the list of allowed colours.
        @param colour_class The class containing the colour definitions.
        @param colour_name The name of the colour as a string.
        @return True if the colour is present, False otherwise.
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
        """
        @brief Function in charge of returning the list of all the colours.
        @param colour_class The class containing the colour definitions.
        @return A list of all the colour names as strings.
        """
        colours = []
        for i in dir(colour_class):
            if not i.startswith("__") and not callable(getattr(colour_class, i)):
                continue
            colours.append(i)
        return colours
