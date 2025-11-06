##
# EPITECH PROJECT, 2024
# display_tty
# File description:
# test_colours.py
##

"""
@file test_colours.py
@brief Unit tests for the LoggerColours utilities.
"""

from display_tty.src.colours import LoggerColours


def test_get_colour_string_valid() -> None:
    """Return the expected lowercase name for a valid colour code."""
    name = LoggerColours.get_colour_string(LoggerColours, LoggerColours.BLUE)
    assert name == "blue"


def test_get_colour_string_invalid() -> None:
    """Return empty string for invalid / negative codes."""
    assert LoggerColours.get_colour_string(LoggerColours, -1) == ""
    assert LoggerColours.get_colour_string(LoggerColours, 9999) == ""


def test_get_colour_code_valid_and_invalid() -> None:
    """Return code for valid name, None for invalid input."""
    assert LoggerColours.get_colour_code(
        LoggerColours, "blue") == LoggerColours.BLUE
    assert LoggerColours.get_colour_code(LoggerColours, "nonexistent") is None
    assert LoggerColours.get_colour_code(LoggerColours, "") is None
    assert LoggerColours.get_colour_code(LoggerColours, 123) is None


def test_check_if_colour_present() -> None:
    """check_if_colour_present returns True for valid name, False for unknown, and None for invalid input type."""
    assert LoggerColours.check_if_colour_present(LoggerColours, "blue") is True
    assert LoggerColours.check_if_colour_present(
        LoggerColours, "doesnotexist") is False
    # behaviour in implementation: returns None for invalid (non-empty string required)
    assert LoggerColours.check_if_colour_present(LoggerColours, "") is None
    assert LoggerColours.check_if_colour_present(LoggerColours, 123) is None


def test_get_all_colours_contains_callables_and_dunders() -> None:
    """The implementation currently returns a list containing callable names and dunder names.
    Verify that known callable (method) names are present in the list.
    """
    all_items = LoggerColours.get_all_colours(LoggerColours)
    # It should at least contain method names such as 'get_colour_string'
    assert "get_colour_string" in all_items
    assert "get_colour_code" in all_items
    assert "check_if_colour_present" in all_items
    assert "get_all_colours" in all_items
