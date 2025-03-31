##
# EPITECH PROJECT, 2024
# display_tty
# File description:
# __main__.py
##

"""
@file __main__.py
@brief Entry point for the display_tty library when run as a script.
@details This script initializes the Disp class with a TOML configuration and runs a test method to validate its functionality. The output is not saved to a file by default.
"""

try:
    from src import Disp, TOML_CONF
except ImportError:
    from display_tty import Disp, TOML_CONF


if __name__ == "__main__":
    DI = Disp(
        toml_content=TOML_CONF,
        save_to_file=False,
        file_name="test_run.tmp",
        file_descriptor=None
    )
    DI.test_the_class()
