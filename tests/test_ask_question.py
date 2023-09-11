# tests/test_ask_question.py
import unittest.mock
from sys import stderr
from disp import IDISP


def print_debug(string: str = "") -> None:
    """ Print debug messages """
    debug = False
    if debug is True:
        print(f"DEBUG: {string}", file=stderr)


def test_is_empty() -> None:
    """ Test if the input string is empty """
    aqi = IDISP()
    response = aqi.is_empty("")
    print_debug(f"response = {response}")
    response2 = aqi.is_empty("\t")
    print_debug(f"response2 = {response2}")
    response3 = aqi.is_empty("   ")
    print_debug(f"response3 = {response3}")
    response4 = aqi.is_empty("Hello")
    print_debug(f"response4 = {response4}")
    assert response is True
    assert response2 is False
    assert response3 is False
    assert response4 is False


def test_is_version() -> None:
    """ Test if the version tester is working """
    aqi = AskQuestion()
    response = aqi.is_version("1.0.0")
    print_debug(f"response = {response}")
    response2 = aqi.is_version("1.a.0")
    print_debug(f"response2 = {response2}")
    assert response is True
    assert response2 is False


def test_contains_illegal_characters() -> None:
    """ Test if the illegal characters tester is working """
    aqi = AskQuestion()
    illegal_chars = "#@$"
    response = aqi.contains_illegal_characters("Hello", illegal_chars)
    print_debug(f"response = {response}")
    response2 = aqi.contains_illegal_characters("H#llo", illegal_chars)
    print_debug(f"response2 = {response2}")
    assert response is False
    assert response2 is True


def test_remove_char_overflow() -> None:
    """ Test if the character overflow remover is working """
    aqi = AskQuestion()
    response = aqi.remove_char_overflow("Hello", "l", 1, False)
    print_debug(f"response = {response}")
    response2 = aqi.remove_char_overflow("Hello", "l", 2, False)
    print_debug(f"response2 = {response2}")
    assert response == "Helo"
    assert response2 == "Hello"


def test_clean_number() -> None:
    """ Test if the number cleaner is working """
    aqi = AskQuestion()
    response = aqi.clean_number("1,000.99")
    print_debug(f"response = {response}")
    response2 = aqi.clean_number("1.234.567,89")
    print_debug(f"response2 = {response2}")
    assert response == "1.00099"
    assert response2 == "1.23456789"


@unittest.mock.patch('builtins.input', side_effect=["1.23"])
# Simulate user input for "1.23" when asked for a float
def test_ask_question_valid_input(mock_input) -> None:
    """Test asking question with valid inputs."""
    aqi = AskQuestion()
    response = aqi.ask_question("Enter a float: ", "float")
    print_debug(f"response = {response}")
    assert response == 1.23


def test_ask_question_invalid_input() -> None:
    """Test asking question with invalid inputs."""
    aqi = AskQuestion()
    response = aqi.test_input("abc ", "int")
    print_debug(f"response = {response}")
    response2 = aqi.usr_answer
    print_debug(f"response2 = {response2}")
    assert response is False
    assert response2 == ""


@unittest.mock.patch('builtins.input', side_effect=["y"])
# Simulate user input for "y" when asked for a bool
def test_ask_question_bool_input(mock_input):
    """Test asking boolean questions and answering them correctly."""
    aqi = AskQuestion()
    response = aqi.ask_question("Yes or No? ", "bool")
    print_debug(f"response = {response}")
    assert response is True


@unittest.mock.patch('builtins.input', side_effect=["1.0.0"])
# Simulate user input for "1.0.0" when asked for a version
def test_ask_question_version_input(mock_input):
    """Test asking version questions and answering them correctly."""
    aqi = AskQuestion()
    response = aqi.ask_question("Enter a version: ", "version")
    print_debug(f"response = {response}")
    assert response == "1.0.0"


def test_ask_question_empty_input():
    """Test asking empty string as input to ask_question function."""
    aqi = AskQuestion()
    response = aqi.test_input("", "str")
    print_debug(f"response = {response}")
    response2 = aqi.usr_answer
    print_debug(f"response2 = {response2}")
    assert response is False
    assert response2 == ""


def test_ask_question_space_input():
    """Test asking empty string as input to ask_question function."""
    aqi = AskQuestion()
    response = aqi.test_input(" ", "str")
    print_debug(f"response = {response}")
    response2 = aqi.usr_answer
    print_debug(f"response2 = {response2}")
    assert response is False
    assert response2 == ""


def test_ask_question_tab_input():
    """Test asking empty string as input to ask_question function."""
    aqi = AskQuestion()
    response = aqi.test_input("\t", "str")
    print_debug(f"response = {response}")
    response2 = aqi.usr_answer
    print_debug(f"response2 = {response2}")
    assert response is False
    assert response2 == ""


def test_ask_question_tab_and_space_input():
    """Test asking empty string as input to ask_question function."""
    aqi = AskQuestion()
    response = aqi.test_input("\t ", "str")
    print_debug(f"response = {response}")
    response2 = aqi.usr_answer
    print_debug(f"response2 = {response2}")
    assert response is False
    assert response2 == ""


def test_ask_question_tab_and_space_mix_input():
    """Test asking empty string as input to ask_question function."""
    aqi = AskQuestion()
    response = aqi.test_input(
        "\t  \t\t\t  \t\t   \t\t  \t\t   \t\t \t\t",
        "str"
    )
    print_debug(f"response = {response}")
    response2 = aqi.usr_answer
    print_debug(f"response2 = {response2}")
    assert response is False
    assert response2 == ""


def test_ask_question_whitespace_input():
    """Test asking whitespace as input to ask_question function."""
    aqi = AskQuestion()
    # Simulate user input for whitespace
    response = aqi.test_input("            ", "str")
    print_debug(f"response = {response}")
    response2 = aqi.usr_answer
    print_debug(f"response2 = {response2}")
    assert response is False
    assert response2 == ""


def test_ask_question_tabs_input():
    """Test asking whitespace as input to ask_question function."""
    aqi = AskQuestion()
    # Simulate user input for tabs
    response = aqi.test_input("\t\t\t\t\t\t\t\t\t\t\t\t", "str")
    print_debug(f"response = {response}")
    response2 = aqi.usr_answer
    print_debug(f"response2 = {response2}")
    assert response is False
    assert response2 == ""


def test_ask_question_invalid_characters():
    """Test asking invalid characters as input to ask_question function."""
    aqi = AskQuestion()
    # Simulate user input for "!@#" when asked for alphanumeric
    response = aqi.test_input("!@#", "alnum")
    print_debug(f"response = {response}")
    response2 = aqi.usr_answer
    print_debug(f"response2 = {response2}")
    assert response is False
    assert response2 == ""


@unittest.mock.patch('builtins.input', side_effect=["42"])
# Simulate user input for "42" when asked for a uint
def test_ask_question_valid_uint(mock_input):
    """ Test asking valid uints (positive integers) in the range [0, 2^32-1]. """
    aqi = AskQuestion()
    response = aqi.ask_question("Enter a uint: ", "uint")
    print_debug(f"response = {response}")
    assert response == 42


def test_ask_question_invalid_uint():
    """Test asking invalid uints (negative integers) in the range [0, 2^32-1]."""
    aqi = AskQuestion()
    # Simulate user input for "-42" when asked for a uint
    response = aqi.test_input("-42", "uint")
    print_debug(f"response = {response}")
    response2 = aqi.usr_answer
    print_debug(f"response2 = {response2}")
    assert response is False
    assert response2 == ""


@unittest.mock.patch('builtins.input', side_effect=["3.14"])
# Simulate user input for "3.14" when asked for a ufloat
def test_ask_question_valid_ufloat(mok_input):
    """Test asking valid ufloats (positive floats) in the range [0, 2^32-1]."""
    aqi = AskQuestion()
    response = aqi.ask_question("Enter a ufloat: ", "ufloat")
    print_debug(f"response = {response}")
    assert response == 3.14


def test_ask_question_invalid_ufloat():
    """Test asking invalid ufloats (negative floats) in the range [0, 2^32-1]."""
    aqi = AskQuestion()
    # Simulate user input for "-3.14" when asked for a ufloat
    response = aqi.test_input("-3.14", "ufloat")
    print_debug(f"response = {response}")
    response2 = aqi.usr_answer
    print_debug(f"response2 = {response2}")
    assert response is False
    assert response2 == ""
