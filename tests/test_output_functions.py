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
# FILE: test_output_functions.py
# CREATION DATE: 06-11-2025
# LAST Modified: 12:47:43 06-11-2025
# DESCRIPTION: 
# A module that allows you to display text with a few boilers (i.e. put your text in a square for titles). It also allows to log to the terminal by wrapping around the logging library.
# @file test_output_functions.py
# @brief Unit tests for the Disp class in the display_tty library.
# @details This file contains unit tests for various methods of the Disp class, including logging, message display, and custom level handling.
# /STOP
# COPYRIGHT: (c) Henry Letellier
# PURPOSE: Function in charge of testing the output functions of the display_tty library.
# // AR
# +==== END display_tty =================+
"""

import pytest
from display_tty.src.my_disp import Disp, TOML_CONF


@pytest.fixture
def disp_instance() -> Disp:
    """
    @brief Fixture to create an instance of the Disp class.
    @return An instance of the Disp class initialized with TOML_CONF.
    """
    return Disp(
        TOML_CONF
    )


def test_add_custom_level(disp_instance) -> None:
    """
    @brief Test the add_custom_level method of the Disp class.
    @details Verifies that a custom logging level can be added successfully.
    @param disp_instance The instance of the Disp class.
    """
    result = disp_instance.add_custom_level(25, "CUSTOM", "red", "black")
    assert result == 0  # Assuming 0 means success


def test_animate_message(disp_instance, capsys: pytest.CaptureFixture) -> None:
    """
    @brief Test the animate_message method of the Disp class.
    @details Verifies that the animate_message method outputs the correct message.
    @param disp_instance The instance of the Disp class.
    @param capsys Pytest fixture to capture stdout and stderr.
    """
    disp_instance.animate_message("Test", 0.01)
    captured = capsys.readouterr()
    assert "Test" in captured.out


def test_append_run_date(disp_instance, capsys: pytest.CaptureFixture) -> None:
    """
    @brief Test the append_run_date method of the Disp class.
    @details Verifies that the run date is appended to the output.
    @param disp_instance The instance of the Disp class.
    @param capsys Pytest fixture to capture stdout and stderr.
    """
    disp_instance.append_run_date()
    captured = capsys.readouterr()
    assert "Run date:" in captured.out


def test_box_vertical_no_horizontal(disp_instance, capsys: pytest.CaptureFixture) -> None:
    """
    @brief Test the box_vertical_no_horizontal method of the Disp class.
    @details Verifies that the method outputs the correct message in a vertical box.
    @param disp_instance The instance of the Disp class.
    @param capsys Pytest fixture to capture stdout and stderr.
    """
    disp_instance.box_vertical_no_horizontal("Test message", "#")
    captured = capsys.readouterr()
    assert "Test message" in captured.out


def test_create_string(disp_instance) -> None:
    """
    @brief Test the create_string method of the Disp class.
    @details Verifies that the method creates a string of the correct length and character.
    @param disp_instance The instance of the Disp class.
    """
    result = disp_instance.create_string(5, "*")
    assert result == "*****"


def test_disp_box_no_vertical(disp_instance, capsys: pytest.CaptureFixture) -> None:
    """
    @brief Test the disp_box_no_vertical method of the Disp class.
    @details Verifies that the method outputs the correct message in a horizontal box.
    @param disp_instance The instance of the Disp class.
    @param capsys Pytest fixture to capture stdout and stderr.
    """
    disp_instance.disp_box_no_vertical("Test", "*")
    captured = capsys.readouterr()
    assert "Test" in captured.out


def test_disp_diff_side_and_top_message_box(disp_instance, capsys: pytest.CaptureFixture) -> None:
    """
    @brief Test the disp_diff_side_and_top_message_box method of the Disp class.
    @details Verifies that the method outputs the correct message in a box with different side and top characters.
    @param disp_instance The instance of the Disp class.
    @param capsys Pytest fixture to capture stdout and stderr.
    """
    disp_instance.disp_diff_side_and_top_message_box("Test")
    captured = capsys.readouterr()
    assert "Test" in captured.out


def test_disp_message_box(disp_instance, capsys: pytest.CaptureFixture) -> None:
    """
    @brief Test the disp_message_box method of the Disp class.
    @details Verifies that the method outputs the correct message in a message box.
    @param disp_instance The instance of the Disp class.
    @param capsys Pytest fixture to capture stdout and stderr.
    """
    disp_instance.disp_message_box("Test", "#")
    captured = capsys.readouterr()
    assert "Test" in captured.out


def test_disp_print_critical(disp_instance, caplog: pytest.LogCaptureFixture) -> None:
    """
    @brief Test the disp_print_critical method of the Disp class.
    @details Verifies that a critical message is logged correctly.
    @param disp_instance The instance of the Disp class.
    @param caplog Pytest fixture to capture log messages.
    """
    with caplog.at_level("CRITICAL"):
        disp_instance.disp_print_critical("Critical error", "test_func")
    assert "Critical error" in caplog.text


def test_disp_print_debug(disp_instance, caplog: pytest.LogCaptureFixture) -> None:
    """
    @brief Test the disp_print_debug method of the Disp class.
    @details Verifies that a debug message is logged correctly when debugging is enabled.
    @param disp_instance The instance of the Disp class.
    @param caplog Pytest fixture to capture log messages.
    """
    disp_node: Disp = disp_instance
    disp_node.update_disp_debug(True)
    with caplog.at_level("DEBUG"):
        disp_node.disp_print_debug("Debug message", "test_func")
    assert "Debug message" in caplog.text


def test_disp_print_error(disp_instance, caplog: pytest.LogCaptureFixture) -> None:
    """
    @brief Test the disp_print_error method of the Disp class.
    @details Verifies that an error message is logged correctly.
    @param disp_instance The instance of the Disp class.
    @param caplog Pytest fixture to capture log messages.
    """
    with caplog.at_level("ERROR"):
        disp_instance.disp_print_error("Error message", "test_func")
    assert "Error message" in caplog.text


def test_disp_print_info(disp_instance, caplog: pytest.LogCaptureFixture) -> None:
    """
    @brief Test the disp_print_info method of the Disp class.
    @details Verifies that an info message is logged correctly.
    @param disp_instance The instance of the Disp class.
    @param caplog Pytest fixture to capture log messages.
    """
    with caplog.at_level("INFO"):
        disp_instance.disp_print_info("Info message", "test_func")
    assert "Info message" in caplog.text


def test_disp_print_warning(disp_instance, caplog: pytest.LogCaptureFixture) -> None:
    """
    @brief Test the disp_print_warning method of the Disp class.
    @details Verifies that a warning message is logged correctly.
    @param disp_instance The instance of the Disp class.
    @param caplog Pytest fixture to capture log messages.
    """
    with caplog.at_level("WARNING"):
        disp_instance.disp_print_warning("Warning message", "test_func")
    assert "Warning message" in caplog.text


def test_log_critical(disp_instance, caplog: pytest.LogCaptureFixture) -> None:
    """
    @brief Test the log_critical method of the Disp class.
    @details Verifies that a critical log message is logged correctly.
    @param disp_instance The instance of the Disp class.
    @param caplog Pytest fixture to capture log messages.
    """
    with caplog.at_level("CRITICAL"):
        disp_instance.log_critical("Critical log", "test_func")
    assert "Critical log" in caplog.text


def test_log_custom_level(disp_instance, caplog: pytest.LogCaptureFixture) -> None:
    """
    @brief Test the log_custom_level method of the Disp class.
    @details Verifies that a custom level log message is logged correctly.
    @param disp_instance The instance of the Disp class.
    @param caplog Pytest fixture to capture log messages.
    """
    disp_instance.add_custom_level(25, "CUSTOM", "red", "black")
    with caplog.at_level(25):
        disp_instance.log_custom_level(25, "Custom level log", "test_func")
    assert "Custom level log" in caplog.text


def test_log_debug(disp_instance, caplog: pytest.LogCaptureFixture) -> None:
    """
    @brief Test the log_debug method of the Disp class.
    @details Verifies that a debug log message is logged correctly when debugging is enabled.
    @param disp_instance The instance of the Disp class.
    @param caplog Pytest fixture to capture log messages.
    """
    disp_node = disp_instance
    disp_node.update_disp_debug(True)
    with caplog.at_level("DEBUG"):
        disp_node.log_debug("Debug message", "test_func")
    assert "Debug message" in caplog.text


def test_log_error(disp_instance, caplog: pytest.LogCaptureFixture) -> None:
    """
    @brief Test the log_error method of the Disp class.
    @details Verifies that an error log message is logged correctly.
    @param disp_instance The instance of the Disp class.
    @param caplog Pytest fixture to capture log messages.
    """
    with caplog.at_level("ERROR"):
        disp_instance.log_error("Error log", "test_func")
    assert "Error log" in caplog.text


def test_log_info(disp_instance, caplog: pytest.LogCaptureFixture) -> None:
    """
    @brief Test the log_info method of the Disp class.
    @details Verifies that an info log message is logged correctly.
    @param disp_instance The instance of the Disp class.
    @param caplog Pytest fixture to capture log messages.
    """
    with caplog.at_level("INFO"):
        disp_instance.log_info("Info log", "test_func")
    assert "Info log" in caplog.text


def test_log_warning(disp_instance, caplog: pytest.LogCaptureFixture) -> None:
    """
    @brief Test the log_warning method of the Disp class.
    @details Verifies that a warning log message is logged correctly.
    @param disp_instance The instance of the Disp class.
    @param caplog Pytest fixture to capture log messages.
    """
    with caplog.at_level("WARNING"):
        disp_instance.log_warning("Warning log", "test_func")
    assert "Warning log" in caplog.text


def test_update_logger_level(disp_instance) -> None:
    """
    @brief Test the update_logger_level method of the Disp class.
    @details Verifies that the logger level is updated correctly.
    @param disp_instance The instance of the Disp class.
    """
    result = disp_instance.update_logger_level(20)
    assert result is None


def test_tree(disp_instance, capsys: pytest.CaptureFixture) -> None:
    """
    @brief Test the tree method of the Disp class.
    @details Verifies that the tree method outputs the correct message.
    @param disp_instance The instance of the Disp class.
    @param capsys Pytest fixture to capture stdout and stderr.
    """
    disp_instance.tree("Test", ["data1", "data2"], 0)
    captured = capsys.readouterr()
    assert "Test\n" in captured.out
    assert "data1" in captured.out
    assert "data2" in captured.out
