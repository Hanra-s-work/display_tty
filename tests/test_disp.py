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
# FILE: test_disp.py
# CREATION DATE: 06-11-2025
# LAST Modified: 12:44:46 06-11-2025
# DESCRIPTION: 
# A module that allows you to display text with a few boilers (i.e. put your text in a square for titles). It also allows to log to the terminal by wrapping around the logging library.
# @file test_disp.py
# @brief Unit tests for the display_tty library.
# @details This script contains unit tests for the IDISP class in the display_tty library. It verifies the functionality of various methods, including input validation and string creation.
# /STOP
# COPYRIGHT: (c) Henry Letellier
# PURPOSE: File in charge of testing the disp class.
# // AR
# +==== END display_tty =================+
"""

from sys import stderr
from display_tty import IDISP


def print_debug(string: str = "") -> None:
    """ Print debug messages """
    debug = False
    if debug is True:
        print(f"DEBUG: {string}", file=stderr)


def test_is_safe_list() -> None:
    """ Test if the input string is empty """
    test_input = ["e", "e"]
    response = IDISP._is_safe(test_input)
    assert response is False


def test_is_safe_dictionnary() -> None:
    """ Test if the input string is empty """
    test_input = {"e": "e", "r": "r"}
    response = IDISP._is_safe(test_input)
    assert response is False


def test_is_safe_string() -> None:
    """ Test if the input string is empty """
    test_input = "e"
    response = IDISP._is_safe(test_input)
    assert response is True


def test_is_safe_int() -> None:
    """ Test if the input string is empty """
    test_input = 0
    response = IDISP._is_safe(test_input)
    assert response is True


def test_is_safe_float() -> None:
    """ Test if the input string is empty """
    test_input = 0.01
    response = IDISP._is_safe(test_input)
    assert response is True


def test_is_safe_tuple() -> None:
    """ Test if the input string is empty """
    test_input = ("e", "e")
    response = IDISP._is_safe(test_input)
    assert response is True


def test_is_safe_complex() -> None:
    """ Test if the input string is empty """
    test_input = complex(2)
    response = IDISP._is_safe(test_input)
    assert response is True


def test_is_safe_bytes() -> None:
    """ Test if the input string is empty """
    test_input = bytes(b"e")
    response = IDISP._is_safe(test_input)
    assert response is True


def test_is_safe_bytearray() -> None:
    """ Test if the input string is empty """
    test_input = bytearray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    response = IDISP._is_safe(test_input)
    assert response is True


def test_is_safe_memoryview() -> None:
    """ Test if the input string is empty """
    test_input = memoryview(b"e")
    response = IDISP._is_safe(test_input)
    assert response is True


def test_string_creation() -> None:
    """ Test if the version tester is working """
    response = IDISP.create_string(20, "e")
    assert response == "eeeeeeeeeeeeeeeeeeee"
