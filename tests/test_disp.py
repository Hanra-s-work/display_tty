# tests/test_ask_question.py
from sys import stderr
from disp import IDISP


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
