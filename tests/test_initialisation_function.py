import io
from display_tty.src.my_disp import TOML_CONF as DEFAULT_TOML, Logging
from display_tty.src.initialiser import initialise_logger
from display_tty.src.constants import SAVE_TO_FILE as DEFAULT_SAVE, FILE_NAME as DEFAULT_FILE
import logging


def test_initialise_logger_accepts_falsy_overrides() -> None:
    """
    @brief Ensure initialise_logger accepts falsy but meaningful overrides.
    @details Verifies that values such as False, 0, empty string and empty dict are
    accepted and override module defaults.
    """
    fd = io.StringIO()
    disp = initialise_logger(
        class_name="test_owner",
        debug=False,
        save_to_file=False,
        file_name="",
        file_descriptor=fd,
        success=0,
        error=0,
        log_warning_when_present=False,
        log_errors_when_present=False,
    )

    assert disp.toml_content == DEFAULT_TOML
    assert disp.save_to_file is False
    assert disp.file_name == ""
    assert disp.file_descriptor is fd
    assert disp.success == 0
    assert disp.error == 0
    assert disp.log_warning_when_present is False
    assert getattr(disp, "log_error_when_present") is False


def test_initialise_logger_defaults() -> None:
    """
    @brief Ensure initialise_logger uses module defaults when optional args are omitted.
    """
    disp = initialise_logger(
        class_name="owner_default"
    )

    # Defaults should be applied
    assert disp.toml_content == DEFAULT_TOML

    assert disp.save_to_file == DEFAULT_SAVE
    assert disp.file_name == DEFAULT_FILE
    assert disp.file_descriptor is None


def test_initialise_logger_toml_override() -> None:
    """
    @brief Ensure initialise_logger accepts a provided TOML dict and uses it.
    """
    toml_override = dict(DEFAULT_TOML)
    toml_override["TITLE_WALL_CHARACTER"] = "^"

    disp = initialise_logger(
        class_name="owner_toml",
        toml_content=toml_override
    )

    assert disp.toml_content["TITLE_WALL_CHARACTER"] == "^"
    # Ensure original default was not mutated
    assert DEFAULT_TOML["TITLE_WALL_CHARACTER"] == "#"


def test_initialise_logger_save_to_file_and_filename() -> None:
    """
    @brief Ensure save_to_file and file_name overrides are applied.
    """
    disp = initialise_logger(
        class_name="owner_file",
        save_to_file=True,
        file_name="my_output.txt",
    )

    assert disp.save_to_file is True
    assert disp.file_name == "my_output.txt"
    assert disp.file_descriptor is None


def test_initialise_logger_with_logging_instance() -> None:
    """
    @brief Ensure initialise_logger accepts a Logging instance for class_name.
    """
    logger_instance = Logging()
    disp = initialise_logger(
        class_name=logger_instance
    )

    # Disp will configure/replace the provided logger argument with a logging.Logger
    # instance for its internal use. Ensure the call accepted the object and produced
    # a proper logger instance.
    assert isinstance(disp.logger, logging.Logger)
