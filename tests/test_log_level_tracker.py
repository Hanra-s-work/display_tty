##
# EPITECH PROJECT, 2024
# display_tty
# File description:
# test_log_level_tracker.py
##

"""
@file test_log_level_tracker.py
@brief Unit tests for the LogLevelTracker class.
"""

import logging
from display_tty.src.log_level_tracker import LogLevelTracker


def test_add_and_get_level() -> None:
    """
    @brief Verify adding a custom level and retrieving it.
    @details Adds a level, ensures add_level returns True the first time and False
    the second time, and validates get_level for existing and missing names.
    """
    tracker = LogLevelTracker(bypass_check=True)
    added = tracker.add_level("CUSTOM", 1234)
    assert added is True
    # Adding again must return False
    added2 = tracker.add_level("CUSTOM", 1234)
    assert added2 is False
    # get_level returns the value
    assert tracker.get_level("CUSTOM") == 1234
    # get_level for unknown returns None
    assert tracker.get_level("UNKNOWN") is None


def test_get_level_name() -> None:
    """
    @brief Verify retrieval of level name by numeric value.
    @details Adds a level and checks get_level_name returns the corresponding name
    and returns None for unknown values.
    """
    tracker = LogLevelTracker(bypass_check=True)
    tracker.add_level("MYLVL", 4321)
    name = tracker.get_level_name(4321)
    assert name == "MYLVL"
    assert tracker.get_level_name(99999) is None


def test_inject_and_presence_clean_up() -> None:
    """
    @brief Test inject_class and check_presence behaviour.
    @details Ensures the tracker is attached to the root logger (or already present)
    and that repeated injection is idempotent. Cleans up any changes to avoid
    leaking state to other tests.
    """
    # Ensure inject_class attaches to the root logger and setting is idempotent
    tracker = LogLevelTracker(bypass_check=True)
    # clean any previous state
    root_logger = logging.getLogger()
    prev_attr = getattr(root_logger, "log_level_tracker", None)
    prev_global = getattr(logging, "log_level_tracker", None)

    try:
        tracker.inject_class()
        # If another test injected it before, inject_class may return False.
        # The important guarantees are that the class is present afterwards and
        # that calling inject_class again is idempotent (returns False).
        assert tracker.check_presence() is True
        # second inject returns False
        injected_second = tracker.inject_class()
        assert injected_second is False
    finally:
        # restore previous attributes to avoid leaking state to other tests
        if prev_attr is None:
            if hasattr(root_logger, "log_level_tracker"):
                delattr(root_logger, "log_level_tracker")
        else:
            root_logger.log_level_tracker = prev_attr

        if prev_global is None:
            if hasattr(logging, "log_level_tracker"):
                delattr(logging, "log_level_tracker")
        else:
            logging.log_level_tracker = prev_global
